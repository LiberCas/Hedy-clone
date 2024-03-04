import textwrap

from parameterized import parameterized

import hedy
from hedy import Command
from hedy_sourcemap import SourceRange
from tests.Tester import HedyTester, SkippedMapping


class TestsLevel8(HedyTester):
    level = 8
    '''
    Tests should be ordered as follows:
     * commands in the order of hedy.py e.g. for level 1: ['print', 'ask', 'echo', 'turn', 'forward']
     * combined tests
     * markup tests
     * negative tests

    Naming conventions are like this:
     * single keyword positive tests are just keyword or keyword_special_case
     * multi keyword positive tests are keyword1_keywords_2
     * negative tests should be situation_gives_exception
    '''

    #
    # if command
    #

    def test_if_one_line(self):
        code = textwrap.dedent("""\
        prind skipping
        antwoord is 25
        if antwoord is 100 print 'goed zo' else print 'neenee'""")

        expected = textwrap.dedent("""\
        pass
        antwoord = '25'
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(3, 1, 3, 55), hedy.exceptions.WrongLevelException)
        ]

        # one line if's are no longer allowed
        self.multi_level_tester(
            code=code,
            max_level=11,
            expected=expected,
            skipped_mappings=skipped_mappings,
        )

    def test_if_no_indentation(self):
        code = textwrap.dedent("""\
        antwoord is ask Hoeveel is 10 keer tien?
        if antwoord is 100
        print 'goed zo'""")

        # gives the right exception for all levels even though it misses brackets
        # because the indent check happens before parsing
        self.multi_level_tester(code=code, exception=hedy.exceptions.NoIndentationException)

    def test_if_equality_with_is(self):
        code = textwrap.dedent("""\
        naam is Hedy
        if naam is Hedy
            print 'leuk'""")

        expected = textwrap.dedent("""\
        naam = 'Hedy'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
          print(f'leuk')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_with_equals_sign(self):
        code = textwrap.dedent("""\
        naam is Hedy
        if naam = Hedy
            print 'leuk'""")

        expected = textwrap.dedent("""\
        naam = 'Hedy'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
          print(f'leuk')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_trailing_space_linebreak_print(self):
        code = textwrap.dedent("""\
        naam is James
        if naam is trailing_space
            print 'shaken'""")

        expected = textwrap.dedent("""\
        naam = 'James'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'trailing_space'):
          print(f'shaken')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_unquoted_rhs_with_space(self):
        code = textwrap.dedent("""\
        naam is James
        if naam is James Bond
            print 'shaken'""")

        expected = textwrap.dedent("""\
        naam = 'James'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'James Bond'):
          print(f'shaken')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_unquoted_rhs_with_space_and_trailing_space_linebreak_print(self):
        code = textwrap.dedent("""\
        naam is James
        if naam is trailing space
            print 'shaken'""")

        expected = textwrap.dedent("""\
        naam = 'James'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'trailing space'):
          print(f'shaken')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    @parameterized.expand(HedyTester.quotes)
    def test_if_equality_quoted_rhs_with_space(self, q):
        code = textwrap.dedent(f"""\
        naam is James
        if naam is {q}James Bond{q}
            print {q}shaken{q}""")

        expected = textwrap.dedent(f"""\
        naam = 'James'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'James Bond'):
          print(f'shaken')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    @parameterized.expand(HedyTester.quotes)
    def test_if_equality_quoted_rhs_with_spaces(self, q):
        code = textwrap.dedent(f"""\
        naam is James
        if naam is {q}Bond James Bond{q}
            print 'shaken'""")

        expected = textwrap.dedent(f"""\
        naam = 'James'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Bond James Bond'):
          print(f'shaken')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_single_quoted_rhs_with_inner_double_quote(self):
        code = textwrap.dedent(f"""\
        answer is no
        if answer is 'He said "no"'
          print 'no'""")

        expected = textwrap.dedent(f"""\
        answer = 'no'
        if convert_numerals('Latin', answer) == convert_numerals('Latin', 'He said "no"'):
          print(f'no')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_double_quoted_rhs_with_inner_single_quote(self):
        code = textwrap.dedent(f"""\
        answer is no
        if answer is "He said 'no'"
          print 'no'""")

        expected = textwrap.dedent(f"""\
        answer = 'no'
        if convert_numerals('Latin', answer) == convert_numerals('Latin', 'He said \\'no\\''):
          print(f'no')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_2_vars_equality_print(self):
        code = textwrap.dedent("""\
        jouwkeuze is schaar
        computerkeuze is schaar
        if computerkeuze is jouwkeuze
            print 'gelijkspel!'""")

        expected = textwrap.dedent("""\
        jouwkeuze = 'schaar'
        computerkeuze = 'schaar'
        if convert_numerals('Latin', computerkeuze) == convert_numerals('Latin', jouwkeuze):
          print(f'gelijkspel!')""")

        self.multi_level_tester(max_level=11, code=code, expected=expected, output='gelijkspel!')

    def test_unquoted_print_in_body(self):
        code = textwrap.dedent("""\
        svar = ask 'Vad är 5 plus 5?'
        if svar is 10
            print 'Bra jobbat!
            print 'Svaret var faktiskt ' svar""")

        self.multi_level_tester(code=code,
                                skip_faulty=False,
                                exception=hedy.exceptions.UnquotedTextException,
                                max_level=16)

    def test_wrongly_quoted_print_in_body(self):
        code = textwrap.dedent("""\
        svar = ask 'Vad är 5 plus 5?'
        if svar is 10
            print 'Bra jobbat!"
            print 'Svaret var faktiskt ' svar""")

        self.multi_level_tester(code=code,
                                skip_faulty=False,
                                exception=hedy.exceptions.UnquotedTextException,
                                max_level=16)

    def test_if_in_list_print(self):
        code = textwrap.dedent("""\
        items is red, green
        selected is red
        if selected in items
            print 'found!'""")

        expected = textwrap.dedent("""\
        items = ['red', 'green']
        selected = 'red'
        if selected in items:
          print(f'found!')""")

        self.multi_level_tester(
            max_level=11,
            code=code,
            expected=expected,
            output='found!',
            expected_commands=['is', 'is', 'if', 'in', 'print']
        )

    def test_if_not_in_list_print(self):
        code = textwrap.dedent("""\
         letters is a, b, c
         if d not in letters
             print 'Not found'""")

        expected = textwrap.dedent("""\
         letters = ['a', 'b', 'c']
         if 'd' not in letters:
           print(f'Not found')""")

        self.multi_level_tester(
            max_level=11,
            code=code,
            expected=expected,
            output='Not found'
        )

    @parameterized.expand(HedyTester.in_not_in_list_commands)
    def test_if_not_in_and_in_list_with_string_var_gives_type_error(self, operator):
        code = textwrap.dedent(f"""\
        items is red
        if red {operator} items
          print 'found!'""")
        self.multi_level_tester(
            max_level=11,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    @parameterized.expand(HedyTester.in_not_in_list_commands)
    def test_if_not_in_and_in_list_with_input_gives_type_error(self, operator):
        code = textwrap.dedent(f"""\
            items is ask 'What are the items?'
            if red {operator} items
              print 'found!'""")
        self.multi_level_tester(
            max_level=11,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_if_equality_assign_calc(self):
        code = textwrap.dedent("""\
        cmp is 1
        test is 2
        acu is 0
        if test is cmp
            acu is acu + 1""")

        expected = textwrap.dedent("""\
        cmp = '1'
        test = '2'
        acu = '0'
        if convert_numerals('Latin', test) == convert_numerals('Latin', cmp):
          acu = int(acu) + int(1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_in_undefined_list_gives_error(self):
        code = textwrap.dedent("""\
        selected is 5
        if selected in items
            print 'found!'""")

        self.multi_level_tester(code=code, exception=hedy.exceptions.UndefinedVarException, max_level=16)

    def test_equality_promotes_int_to_string(self):
        code = textwrap.dedent("""\
        a is test
        b is 15
        if a is b
            b is 1""")

        expected = textwrap.dedent("""\
        a = 'test'
        b = '15'
        if convert_numerals('Latin', a) == convert_numerals('Latin', b):
          b = '1'""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_equality_with_lists_gives_error(self):
        code = textwrap.dedent("""\
        m is 1, 2
        n is 1, 2
        if m is n
          print 'success!'""")
        # FH Mar 2023: waarom is dit fout?
        self.multi_level_tester(
            max_level=11,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 3,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_if_in_list_with_string_var_gives_type_error(self):
        code = textwrap.dedent("""\
        items is red
        if red in items
            print 'found!'""")

        self.multi_level_tester(
            max_level=11,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_if_in_list_with_input_gives_type_error(self):
        code = textwrap.dedent("""\
        items is ask 'What are the items?'
        if red in items
            print 'found!'""")
        self.multi_level_tester(
            max_level=16,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_equality_with_list_gives_error(self):
        code = textwrap.dedent("""\
        color is 5, 6, 7
        if red is color
            print 'success!'""")

        self.multi_level_tester(
            max_level=11,
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_if_with_negative_number(self):
        code = textwrap.dedent("""\
        antwoord = -10
        if antwoord is -10
            print 'Nice'""")

        expected = textwrap.dedent("""\
        antwoord = '-10'
        if convert_numerals('Latin', antwoord) == convert_numerals('Latin', '-10'):
          print(f'Nice')""")

        self.multi_level_tester(code=code, expected=expected, output='Nice', max_level=11)

    #
    # if else tests
    #

    def test_if_else_no_indentation(self):
        code = textwrap.dedent("""\
        antwoord is ask Hoeveel is 10 keer tien?
        if antwoord is 100
        print 'goed zo'
        else
        print 'bah slecht'""")

        # gives the right exception for all levels even though it misses brackets
        # because the indent check happens before parsing
        self.multi_level_tester(code=code,
                                exception=hedy.exceptions.NoIndentationException)

    def test_if_equality_print_else_print(self):
        code = textwrap.dedent("""\
        naam is Hedy
        if naam is Hedy
            print 'leuk'
        else
            print 'minder leuk'""")

        expected = textwrap.dedent("""\
        naam = 'Hedy'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
          print(f'leuk')
        else:
          print(f'minder leuk')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_equality_assign_else_assign(self):
        code = textwrap.dedent("""\
        a is 5
        if a is 1
            x is 2
        else
            x is 222""")
        expected = textwrap.dedent("""\
        a = '5'
        if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
          x = '2'
        else:
          x = '222'""")

        self.multi_level_tester(code=code, expected=expected, max_level=11, unused_allowed=True)

    def test_if_else_followed_by_print(self):
        code = textwrap.dedent("""\
        kleur is geel
        if kleur is groen
            antwoord is ok
        else
            antwoord is stom
        print antwoord""")

        expected = textwrap.dedent("""\
        kleur = 'geel'
        if convert_numerals('Latin', kleur) == convert_numerals('Latin', 'groen'):
          antwoord = 'ok'
        else:
          antwoord = 'stom'
        print(f'{antwoord}')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_else_trailing_space_after_else(self):
        code = textwrap.dedent("""\
        a is 1
        if a is 1
            print a
        else
            print 'nee'""")

        expected = textwrap.dedent("""\
        a = '1'
        if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
          print(f'{a}')
        else:
          print(f'nee')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_list_assignment_else_print(self):
        code = textwrap.dedent("""\
        people is mom, dad, Emma, Sophie
        dishwasher is people at random
        if dishwasher is Sophie
            print 'too bad I have to do the dishes'
        else
            print 'luckily no dishes because' dishwasher 'is already washing up'""")

        expected = HedyTester.dedent(
            "people = ['mom', 'dad', 'Emma', 'Sophie']",
            HedyTester.list_access_transpiled('random.choice(people)'),
            """\
        dishwasher = random.choice(people)
        if convert_numerals('Latin', dishwasher) == convert_numerals('Latin', 'Sophie'):
          print(f'too bad I have to do the dishes')
        else:
          print(f'luckily no dishes because{dishwasher}is already washing up')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_print_line_with_spaces_works(self):
        code = "print 'hallo'\n      \nprint 'hallo'"
        expected = "print(f'hallo')\nprint(f'hallo')"
        expected_commands = [Command.print, Command.print]

        self.multi_level_tester(
            code=code,
            expected=expected,
            expected_commands=expected_commands,
            max_level=11)

    def test_if_empty_start_line_with_whitespace_else_print(self):
        code = "        \n"
        code += textwrap.dedent("""\
        if 1 is 2
            print 'nice!'
        else
            print 'pizza is better'""")

        expected = textwrap.dedent("""\
        if convert_numerals('Latin', '1') == convert_numerals('Latin', '2'):
          print(f'nice!')
        else:
          print(f'pizza is better')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11, translate=False)

    def test_if_empty_middle_line_with_whitespace_else_print(self):
        code = textwrap.dedent("""\
        if 1 is 2
            print 'nice!'""")
        code += "\n        \n"
        code += textwrap.dedent("""\
        else
            print 'pizza is better'""")

        expected = textwrap.dedent("""\
        if convert_numerals('Latin', '1') == convert_numerals('Latin', '2'):
          print(f'nice!')
        else:
          print(f'pizza is better')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_else_with_multiple_lines(self):
        code = textwrap.dedent("""\
        antwoord is ask 'Hoeveel is 10 plus 10?'
        if antwoord is 20
            print 'Goedzo!'
            print 'Het antwoord was inderdaad ' antwoord
        else
            print 'Foutje'
            print 'Het antwoord moest zijn ' antwoord""")

        expected = textwrap.dedent("""\
        antwoord = input(f'Hoeveel is 10 plus 10?')
        if convert_numerals('Latin', antwoord) == convert_numerals('Latin', '20'):
          print(f'Goedzo!')
          print(f'Het antwoord was inderdaad {antwoord}')
        else:
          print(f'Foutje')
          print(f'Het antwoord moest zijn {antwoord}')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    #
    # repeat command
    #
    def test_repeat_no_indentation(self):
        code = textwrap.dedent("""\
          repeat 3 times
          print 'hooray!'""")

        self.multi_level_tester(code=code, exception=hedy.exceptions.NoIndentationException)

    def test_repeat_repair_too_few_indents(self):
        code = textwrap.dedent("""\
        repeat 5 times
             print('repair')
          print('me')""")

        fixed_code = textwrap.dedent("""\
        repeat 5 times
             print('repair')
             print('me')""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.NoIndentationException,
            extra_check_function=(lambda x: x.exception.fixed_code == fixed_code)
        )

    def test_repeat_repair_too_many_indents(self):
        code = textwrap.dedent("""\
        repeat 5 times
          print('repair')
             print('me')""")
        fixed_code = textwrap.dedent("""\
        repeat 5 times
          print('repair')
          print('me')""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.IndentationException,
            extra_check_function=(lambda x: x.exception.fixed_code == fixed_code)
        )

    def test_unexpected_indent(self):
        code = textwrap.dedent("""\
        print('repair')
           print('me')""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.IndentationException
        )

    def test_repeat_turtle(self):
        code = textwrap.dedent("""\
            repeat 3 times
                forward 100""")

        expected = HedyTester.dedent(
            "for i in range(int('3')):",
            (HedyTester.forward_transpiled(100, self.level), '  '))

        self.multi_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_turtle(),
            max_level=11
        )

    def test_repeat_print(self):
        code = textwrap.dedent("""\
        repeat 5 times
            print 'koekoek'""")

        expected = textwrap.dedent("""\
        for i in range(int('5')):
          print(f'koekoek')
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_repeat_print_variable(self):
        code = textwrap.dedent("""\
        n is 5
        repeat n times
            print 'me wants a cookie!'""")

        expected = HedyTester.dedent(
            "n = '5'",
            self.variable_type_check_transpiled('n', 'int'),
            "for i in range(int(n)):",
            ("print(f'me wants a cookie!')", '  '),
            ("time.sleep(0.1)", '  ')
        )

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.multi_level_tester(code=code, expected=expected, output=output, max_level=11)

    def test_repeat_arabic(self):
        code = textwrap.dedent("""\
        repeat ٥ times
            print 'koekoek'""")

        expected = textwrap.dedent("""\
        for i in range(int('5')):
          print(f'koekoek')
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_repeat_with_arabic_variable_print(self):
        code = textwrap.dedent("""\
        n is ٥
        repeat n times
            print 'me wants a cookie!'""")

        expected = HedyTester.dedent(
            "n = '٥'",
            self.variable_type_check_transpiled('n', 'int'),
            "for i in range(int(n)):",
            ("print(f'me wants a cookie!')", '  '),
            ("time.sleep(0.1)", '  ')
        )

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.multi_level_tester(code=code, expected=expected, output=output, max_level=11)

    def test_repeat_with_non_latin_variable_print(self):
        code = textwrap.dedent("""\
        állatok is 5
        repeat állatok times
            print 'me wants a cookie!'""")

        expected = HedyTester.dedent(
            "állatok = '5'",
            self.variable_type_check_transpiled('állatok', 'int'),
            "for i in range(int(állatok)):",
            ("print(f'me wants a cookie!')", '  '),
            ("time.sleep(0.1)", '  ')
        )

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.multi_level_tester(code=code, expected=expected, output=output, max_level=11)

    def test_repeat_undefined_variable_gives_error(self):
        code = textwrap.dedent("""\
        repeat n times
            print 'me wants a cookie!'""")

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.UndefinedVarException,
            max_level=17)

    # issue 297
    def test_repeat_print_assign_addition(self):
        code = textwrap.dedent("""\
        count is 1
        repeat 12 times
            print count ' times 12 is ' count * 12
            count is count + 1""")

        expected = textwrap.dedent("""\
        count = '1'
        for i in range(int('12')):
          print(f'{count} times 12 is {int(count) * int(12)}')
          count = int(count) + int(1)
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_repeat_with_comment(self):
        code = textwrap.dedent("""\
        repeat 5 times #This should be ignored
            print 'koekoek'
            print 'koekoek'""")

        expected = textwrap.dedent("""\
        for i in range(int('5')):
          print(f'koekoek')
          print(f'koekoek')
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_repeat_with_string_variable_gives_type_error(self):
        code = textwrap.dedent("""\
        n is 'test'
        repeat n times
            print 'n'""")

        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException,
            max_level=17)

    def test_repeat_with_list_variable_gives_type_error(self):
        code = textwrap.dedent("""\
        n is 1, 2, 3
        repeat n times
            print 'n'""")

        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException,
            max_level=15)

    def test_repeat_deprecated_gives_deprecated_error(self):
        code = "repeat 5 times print 'In the next tab you can repeat multiple lines of code at once!'"

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.WrongLevelException,
            max_level=17)

    def test_repeat_ask(self):
        code = textwrap.dedent("""\
        n is ask 'How many times?'
        repeat n times
            print 'n'""")

        expected = HedyTester.dedent(
            "n = input(f'How many times?')",
            self.variable_type_check_transpiled('n', 'int'),
            'for i in range(int(n)):',
            ("print(f'n')", '  '),
            ('time.sleep(0.1)', '  ')
        )

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    @parameterized.expand(['5', '𑁫', '५', '૫', '੫', '৫', '೫', '୫', '൫', '௫',
                           '౫', '၅', '༥', '᠕', '៥', '๕', '໕', '꧕', '٥', '۵'])
    def test_repeat_with_all_numerals(self, number):
        code = textwrap.dedent(f"""\
        repeat {number} times
            print 'me wants a cookie!'""")

        expected = textwrap.dedent(f"""\
        for i in range(int('{int(number)}')):
          print(f'me wants a cookie!')
          time.sleep(0.1)""")

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.multi_level_tester(code=code, expected=expected, output=output, max_level=11)

    def test_repeat_over_9_times(self):
        code = textwrap.dedent("""\
        repeat 10 times
            print 'me wants a cookie!'""")

        expected = textwrap.dedent("""\
        for i in range(int('10')):
          print(f'me wants a cookie!')
          time.sleep(0.1)""")

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            expected_commands=['repeat', 'print'],
            output=output,
            max_level=11
        )

    def test_repeat_with_variable_name_collision(self):
        code = textwrap.dedent("""\
        i is hallo!
        repeat 5 times
            print 'me wants a cookie!'
        print i""")

        expected = textwrap.dedent("""\
        i = 'hallo!'
        for _i in range(int('5')):
          print(f'me wants a cookie!')
          time.sleep(0.1)
        print(f'{i}')""")

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        hallo!""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            expected_commands=['is', 'repeat', 'print', 'print'],
            output=output,
            max_level=11
        )

    def test_repeat_without_body_gives_error(self):
        code = "repeat 5 times"

        self.multi_level_tester(
            code=code,
            exception=hedy.exceptions.MissingInnerCommandException,
        )

    #
    # negative tests
    #

    # issue 902
    def test_repeat_if_gives_error(self):
        code = textwrap.dedent("""\
        print 'kassabon'
        prijs is 0
        repeat 7 times # TEST
            ingredient is ask 'wat wil je kopen?'
            if ingredient is appel
                prijs is prijs + 1
        print 'Dat is in totaal ' prijs ' euro.'""")

        self.single_level_tester(code=code, exception=hedy.exceptions.LockedLanguageFeatureException)

    def test_if_repeat_gives_error(self):
        code = textwrap.dedent("""\
        kleur is groen
        if kleur is groen
            repeat 3 times
                print 'mooi'""")

        self.single_level_tester(code=code, exception=hedy.exceptions.LockedLanguageFeatureException)

    #
    # if pressed tests
    #

    def test_if_pressed_x_print(self):
        code = textwrap.dedent("""\
        if x is pressed
            print 'it is a letter key'
        else
            print 'other key'""")
        expected = HedyTester.dedent("""\
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'x':
              print(f'it is a letter key')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other key')
              break""")
        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_double_if_pressed(self):
        code = textwrap.dedent("""\
        if x is pressed
          print 'first key'
        else
          print 'other key'
        if y is pressed
          print 'second key'
        else
          print 'other key'""")

        expected = HedyTester.dedent("""\
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'x':
              print(f'first key')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other key')
              break
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'y':
              print(f'second key')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other key')
              break""")

        self.maxDiff = None
        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_pressed_is_number_key_print(self):
        code = textwrap.dedent("""\
        if 1 is pressed
            print 'it is a number key'
        else
            print 'it is something else'""")

        expected = HedyTester.dedent("""\
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == '1':
              print(f'it is a number key')
              break
            # End of PyGame Event Handler    
            else:
              print(f'it is something else')
              break""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_pressed_command_in_between(self):
        code = textwrap.dedent("""\
        if a is pressed
          print 'A is pressed'
        else
          print 'other'
        print 'Press another button'
        if b is pressed
          print 'B is pressed'
        else
          print 'other'""")

        expected = textwrap.dedent("""\
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'a':
              print(f'A is pressed')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other')
              break
        print(f'Press another button')
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'b':
              print(f'B is pressed')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other')
              break""")

        self.maxDiff = None
        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_pressed_missing_else_gives_error(self):
        code = textwrap.dedent("""\
        prind skipping
        if x is pressed 
          print 'missing else!'""")

        expected = textwrap.dedent("""\
        pass
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(2, 1, 3, 33), hedy.exceptions.MissingElseForPressitException),
        ]

        self.multi_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
            max_level=14
        )

    def test_if_no_indent_after_pressed_and_else_gives_noindent_error(self):
        code = textwrap.dedent("""\
        if x is pressed
        print 'no indent!'
        else
        print 'no indent again!'""")

        # gives the right exception for all levels even though it misses brackets
        # because the indent check happens before parsing
        self.multi_level_tester(code=code, exception=hedy.exceptions.NoIndentationException)

    #
    # button tests
    #
    def test_if_button_is_pressed_print(self):
        code = textwrap.dedent("""\
        PRINT is button
        if PRINT is pressed 
          print 'The button got pressed!'
        else
          print 'other is pressed'""")

        expected = HedyTester.dedent(f"""\
        create_button('PRINT')
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.USEREVENT:
            if event.key == 'PRINT':
              print(f'The button got pressed!')
              break
            # End of PyGame Event Handler    
            else:
              print(f'other is pressed')
              break""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_button_is_pressed_make_button(self):
        code = textwrap.dedent("""\
        BUTTON1 is button
        if BUTTON1 is pressed 
          BUTTON2 is button
        else
          print 'something else'""")

        expected = HedyTester.dedent(f"""\
        create_button('BUTTON1')
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.USEREVENT:
            if event.key == 'BUTTON1':
              create_button('BUTTON2')
              break
            # End of PyGame Event Handler    
            else:
              print(f'something else')
              break""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_button_is_pressed_print_else_print(self):
        code = textwrap.dedent("""\
        PRINT is button
        PRINT2 is button
        if PRINT is pressed
            print 'The button got pressed!'
        else
            print 'oof :('""")

        expected = HedyTester.dedent(f"""\
        create_button('PRINT')
        create_button('PRINT2')
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.USEREVENT:
            if event.key == 'PRINT':
              print(f'The button got pressed!')
              break
            # End of PyGame Event Handler    
            else:
              print(f'oof :(')
              break""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_source_map(self):
        code = textwrap.dedent("""\
        print 'Welcome to Restaurant Chez Hedy!'
        people = ask 'How many people will be joining us today?'
        print 'Great!'
        repeat people times
            food = ask 'What would you like to order?'
            print food
        print 'Thank you for ordering!'
        print 'Enjoy your meal!'""")

        expected_code = HedyTester.dedent(
            "print(f'Welcome to Restaurant Chez Hedy!')",
            "people = input(f'How many people will be joining us today?')",
            "print(f'Great!')",
            self.variable_type_check_transpiled('people', 'int'),
            "for i in range(int(people)):",
            ("food = input(f'What would you like to order?')", '  '),
            ("print(f'{food}')", '  '),
            ("time.sleep(0.1)", '  '),
            "print(f'Thank you for ordering!')",
            "print(f'Enjoy your meal!')"
        )

        expected_source_map = {
            '1/1-1/41': '1/1-1/43',
            '2/1-2/7': '2/1-2/7',
            '2/1-2/57': '2/1-2/61',
            '3/1-3/15': '3/1-3/17',
            '4/8-4/14': '2/27-2/33',
            '5/5-5/9': '9/1-9/5',
            '5/5-5/47': '9/1-9/47',
            '6/11-6/15': '1/1-1/5',
            '6/5-6/15': '10/1-10/17',
            '4/1-6/24': '4/1-11/18',
            '7/1-7/32': '12/1-12/34',
            '8/1-8/25': '13/1-13/27',
            '1/1-8/26': '1/1-13/27',
        }

        self.single_level_tester(code, expected=expected_code)
        self.source_map_tester(code=code, expected_source_map=expected_source_map)

    def test_play_repeat_random(self):
        code = textwrap.dedent("""\
            repeat 10 times
                notes is C4, E4, D4, F4, G4
                note is notes at random
                print note
                play note""")

        expected = textwrap.dedent("""\
            for i in range(int('10')):
              notes = ['C4', 'E4', 'D4', 'F4', 'G4']
              try:
                random.choice(notes)
              except IndexError:
                raise Exception('catch_index_exception')
              note = random.choice(notes)
              print(f'{note}')
              chosen_note = str(note).upper()
              if chosen_note not in notes_mapping.keys() and chosen_note not in notes_mapping.values():
                  raise Exception('catch_value_exception')
              play(notes_mapping.get(chosen_note, chosen_note))
              time.sleep(0.5)
              time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            translate=False,
            skip_faulty=False,
            unused_allowed=True,
            expected=expected,
            max_level=11
        )

    def test_play_integers(self):
        code = textwrap.dedent("""\
        notes = 1, 2, 3

        repeat 10 times
            play notes at random""")

        expected = textwrap.dedent("""\
        notes = ['1', '2', '3']
        for i in range(int('10')):
          chosen_note = str(random.choice(notes)).upper()
          if chosen_note not in notes_mapping.keys() and chosen_note not in notes_mapping.values():
              raise Exception('catch_value_exception')
          play(notes_mapping.get(chosen_note, chosen_note))
          time.sleep(0.5)
          time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            translate=False,
            skip_faulty=False,
            unused_allowed=True,
            expected=expected,
            max_level=11
        )

    def test_play_repeat_with_calc(self):
        code = textwrap.dedent("""\
        note is 34
        repeat 3 times
            play note
            note is note + 1""")

        expected = textwrap.dedent("""\
        note = '34'
        for i in range(int('3')):
          chosen_note = str(note).upper()
          if chosen_note not in notes_mapping.keys() and chosen_note not in notes_mapping.values():
              raise Exception('catch_value_exception')
          play(notes_mapping.get(chosen_note, chosen_note))
          time.sleep(0.5)
          note = int(note) + int(1)
          time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            translate=False,
            skip_faulty=False,
            unused_allowed=True,
            expected=expected,
            max_level=11
        )
