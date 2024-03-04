import os

import utils
from tests.Tester import HedyTester, Snippet
import exceptions
from parameterized import parameterized
import hedy
from website.yaml_file import YamlFile

# set this to True to revert broken snippets to their en counterpart automatically
# this is useful for large Weblate PRs that need to go through, this fixes broken snippets
fix_error = False
if os.getenv('fix_for_weblate'):
    fix_error = True

# Set the current directory to the root Hedy folder
os.chdir(os.path.join(os.getcwd(), __file__.replace(os.path.basename(__file__), '')))


def collect_snippets(path):
    Hedy_snippets = []
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.yaml')]
    for file in files:
        lang = file.split(".")[0]
        file = os.path.join(path, file)
        yaml = YamlFile.for_file(file)
        levels = yaml.get('levels')

        for level, content in levels.items():
            level_number = int(level)
            if level_number > hedy.HEDY_MAX_LEVEL:
                print('content above max level!')
            else:
                try:
                    for exercise_id, exercise in levels[level].items():
                        code = exercise.get('code')
                        snippet = Snippet(
                            filename=file,
                            level=level,
                            field_name=f"{exercise_id}",
                            code=code)
                        Hedy_snippets.append(snippet)
                except BaseException:
                    print(f'Problem reading commands yaml for {lang} level {level}')

    return Hedy_snippets


Hedy_snippets = [(s.name, s) for s in collect_snippets(path='../../content/parsons')]

level = 1
if level:
    Hedy_snippets = [(name, snippet) for (name, snippet) in Hedy_snippets if snippet.level == level]

Hedy_snippets = HedyTester.translate_keywords_in_snippets(Hedy_snippets)


class TestsParsonsPrograms(HedyTester):

    @parameterized.expand(Hedy_snippets, skip_on_empty=True)
    def test_parsons(self, name, snippet):
        if snippet is not None and len(snippet.code) > 0:
            try:
                self.single_level_tester(
                    code=snippet.code,
                    level=int(snippet.level),
                    lang=snippet.language,
                    unused_allowed=True,
                    translate=False,
                    skip_faulty=False
                )

            except hedy.exceptions.CodePlaceholdersPresentException:  # Code with blanks is allowed
                pass
            except OSError:
                return None  # programs with ask cannot be tested with output :(
            except exceptions.HedyException as E:
                if fix_error:
                    # Read English yaml file
                    original_yaml = YamlFile.for_file('../../content/parsons/en.yaml')
                    original_text = original_yaml['levels'][snippet.level][int(snippet.field_name)]

                    # Read broken yaml file
                    broken_yaml = utils.load_yaml_rt(snippet.filename)
                    broken_yaml['levels'][snippet.level][int(snippet.field_name)] = original_text

                    with open(snippet.filename, 'w') as file:
                        file.write(utils.dump_yaml_rt(broken_yaml))
                else:
                    self.output_test_error(E, snippet)
