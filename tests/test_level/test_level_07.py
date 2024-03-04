import textwrap

from parameterized import parameterized

import hedy
from hedy_sourcemap import SourceRange
from tests.Tester import HedyTester, SkippedMapping


class TestsLevel7(HedyTester):
    level = 7
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
    # repeat tests
    #
    def test_repeat_turtle(self):
        code = "repeat 3 times forward 100"

        expected = HedyTester.dedent(
            "for __i__ in range(int('3')):",
            (HedyTester.forward_transpiled(100, self.level), '  '))

        self.single_level_tester(code=code, expected=expected, extra_check_function=self.is_turtle())

    def test_repeat_print(self):
        code = "repeat 5 times print 'me wants a cookie!'"

        expected = textwrap.dedent("""\
        for __i__ in range(int('5')):
          print(f'me wants a cookie!')
          time.sleep(0.1)""")

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.single_level_tester(code=code, expected=expected, output=output)

    def test_repeat_print_variable(self):
        code = textwrap.dedent("""\
        n is 5
        repeat n times print 'me wants a cookie!'""")

        expected = HedyTester.dedent(
            "n = '5'",
            self.variable_type_check_transpiled('n', 'int'),
            "for __i__ in range(int(n)):",
            ("print(f'me wants a cookie!')", '  '),
            ("time.sleep(0.1)", '  ')
        )

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.single_level_tester(code=code, expected=expected, output=output)

    def test_repeat_print_undefined_variable_gives_error(self):
        code = "repeat n times print 'me wants a cookie!'"

        self.single_level_tester(code=code, exception=hedy.exceptions.UndefinedVarException)

    def test_missing_body(self):
        code = textwrap.dedent("""\
        prind skipping
        repeat 5 times""")

        expected = textwrap.dedent("""\
        pass
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(2, 1, 2, 15), hedy.exceptions.MissingInnerCommandException)
        ]

        self.multi_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
            max_level=8
        )

    @parameterized.expand(HedyTester.quotes)
    def test_print_without_opening_quote_gives_error(self, q):
        code = textwrap.dedent(f"""\
        print hedy 123{q}
        prind skipping""")

        expected = textwrap.dedent("""\
        pass
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 16), hedy.exceptions.UnquotedTextException),
            SkippedMapping(SourceRange(2, 1, 2, 15), hedy.exceptions.InvalidCommandException)
        ]

        self.multi_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
            max_level=17
        )

    @parameterized.expand(HedyTester.quotes)
    def test_print_without_closing_quote_gives_error(self, q):
        code = textwrap.dedent(f"""\
        prind skipping
        print {q}hedy 123""")

        expected = textwrap.dedent("""\
        pass
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(2, 1, 2, 16), hedy.exceptions.UnquotedTextException)
        ]

        self.multi_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
            max_level=17
        )

    def test_repeat_with_string_variable_gives_type_error(self):
        code = textwrap.dedent("""\
        n is 'test'
        repeat n times print 'n'""")

        self.single_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException)

    def test_repeat_with_list_variable_gives_type_error(self):
        code = textwrap.dedent("""\
        n is 1, 2, 3
        repeat n times print 'n'""")

        self.single_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException)

    def test_repeat_with_missing_print_gives_error(self):
        code = textwrap.dedent("""\
        repeat 3 print 'x'""")

        self.single_level_tester(
            code=code,
            exception=hedy.exceptions.IncompleteRepeatException
        )

    def test_repeat_with_missing_times_gives_error_skip(self):
        code = textwrap.dedent("""\
        x is 3
        repeat 3 print 'x'""")

        expected = textwrap.dedent("""\
        x = '3'
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(2, 1, 2, 19), hedy.exceptions.IncompleteRepeatException),
        ]

        self.single_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
        )

    def test_repeat_with_missing_print_gives_lonely_text_exc(self):
        code = textwrap.dedent("""\
        prind skipping
        repeat 3 times 'n'""")

        expected = textwrap.dedent("""\
        pass
        for __i__ in range(int('3')):
          pass
          time.sleep(0.1)""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(2, 16, 2, 19), hedy.exceptions.LonelyTextException)
        ]

        self.single_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
        )

    def test_repeat_with_missing_times_gives_error(self):
        code = textwrap.dedent("""\
        prind skipping
        repeat 3 print 'n'""")

        expected = textwrap.dedent("""\
        pass
        pass""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 1, 15), hedy.exceptions.InvalidCommandException),
            SkippedMapping(SourceRange(2, 1, 2, 19), hedy.exceptions.IncompleteRepeatException),
        ]

        self.single_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
        )

    def test_repeat_with_missing_times_gives_error_2(self):
        code = "repeat 5"

        self.multi_level_tester(
            code=code,
            max_level=8,
            exception=hedy.exceptions.IncompleteRepeatException
        )

    def test_repeat_ask(self):
        code = textwrap.dedent("""\
        n is ask 'How many times?'
        repeat n times print 'n'""")

        expected = HedyTester.dedent(
            "n = input(f'How many times?')",
            self.variable_type_check_transpiled('n', 'int'),
            "for __i__ in range(int(n)):",
            ("print(f'n')", '  '),
            ("time.sleep(0.1)", '  ')
        )

        self.single_level_tester(code=code, expected=expected)

    @parameterized.expand(['5', '𑁫', '५', '૫', '੫', '৫', '೫', '୫', '൫', '௫',
                           '౫', '၅', '༥', '᠕', '៥', '๕', '໕', '꧕', '٥', '۵'])
    def test_repeat_with_all_numerals(self, number):
        code = textwrap.dedent(f"repeat {number} times print 'me wants a cookie!'")

        expected = textwrap.dedent(f"""\
        for __i__ in range(int('{int(number)}')):
          print(f'me wants a cookie!')
          time.sleep(0.1)""")

        output = textwrap.dedent("""\
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!
        me wants a cookie!""")

        self.single_level_tester(code=code, expected=expected, output=output)

    def test_repeat_over_9_times(self):
        code = textwrap.dedent("""\
        repeat 10 times print 'me wants a cookie!'""")

        expected = textwrap.dedent("""\
        for __i__ in range(int('10')):
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

        self.single_level_tester(
            code=code,
            expected=expected,
            expected_commands=['repeat', 'print'],
            output=output)

    def test_repeat_with_variable_name_collision(self):
        code = textwrap.dedent("""\
        i is hallo!
        repeat 5 times print 'me wants a cookie!'
        print i""")

        expected = textwrap.dedent("""\
        i = 'hallo!'
        for __i__ in range(int('5')):
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

        self.single_level_tester(
            code=code,
            expected=expected,
            expected_commands=['is', 'repeat', 'print', 'print'],
            output=output)

    def test_repeat_if(self):
        code = textwrap.dedent("""\
        naam is Hedy
        if naam is Hedy repeat 3 times print 'Hallo Hedy!'""")

        expected = textwrap.dedent("""\
        naam = 'Hedy'
        if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
          for __i__ in range(int('3')):
            print(f'Hallo Hedy!')
            time.sleep(0.1)""")

        self.single_level_tester(
            code=code,
            expected=expected)

    def test_if_pressed_repeat(self):
        code = "if x is pressed repeat 5 times print 'doe het 5 keer!' else print 'iets anders'"

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
              for __i__ in range(int('5')):
                print(f'doe het 5 keer!')
                time.sleep(0.1)
              break
            else:
              print(f'iets anders')
              break
            # End of PyGame Event Handler""")

        self.single_level_tester(
            code=code,
            expected=expected)

    def test_if_pressed_multiple(self):
        code = textwrap.dedent("""\
            if x is pressed print 'doe het 1 keer!' else print 'iets anders'
            if y is pressed print 'doe het 1 keer!' else print 'iets anders'
            if z is pressed print 'doe het 1 keer!' else print 'iets anders'""")

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
              print(f'doe het 1 keer!')
              break
            else:
              print(f'iets anders')
              break
            # End of PyGame Event Handler
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
              print(f'doe het 1 keer!')
              break
            else:
              print(f'iets anders')
              break
            # End of PyGame Event Handler
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'z':
              print(f'doe het 1 keer!')
              break
            else:
              print(f'iets anders')
              break
            # End of PyGame Event Handler""")

        self.single_level_tester(
            code=code,
            expected=expected,
            translate=False)

    def test_repeat_if_pressed_multiple(self):
        code = textwrap.dedent("""\
            repeat 3 times if x is pressed forward 15 else forward -15
            repeat 3 times if y is pressed forward 15 else forward -15
            repeat 3 times if z is pressed forward 15 else forward -15""")

        expected = HedyTester.dedent("""\
        for __i__ in range(int('3')):
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
                __trtl = 15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              else:
                __trtl = -15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              # End of PyGame Event Handler
          time.sleep(0.1)
        for __i__ in range(int('3')):
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
                __trtl = 15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              else:
                __trtl = -15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              # End of PyGame Event Handler
          time.sleep(0.1)
        for __i__ in range(int('3')):
          pygame_end = False
          while not pygame_end:
            pygame.display.update()
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
              pygame_end = True
              pygame.quit()
              break
            if event.type == pygame.KEYDOWN:
              if event.unicode == 'z':
                __trtl = 15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              else:
                __trtl = -15
                try:
                  __trtl = int(__trtl)
                except ValueError:
                  raise Exception('catch_value_exception')
                t.forward(min(600, __trtl) if __trtl > 0 else max(-600, __trtl))
                time.sleep(0.1)
                break
              # End of PyGame Event Handler
          time.sleep(0.1)""")

        self.single_level_tester(
            code=code,
            expected=expected,
            translate=False)

    def test_repeat_if_multiple(self):
        code = textwrap.dedent("""\
            aan is ja
            repeat 3 times if aan is ja print 'Hedy is leuk!'
            repeat 3 times if aan is ja print 'Hedy is leuk!'""")

        expected = HedyTester.dedent("""\
        aan = 'ja'
        for __i__ in range(int('3')):
          if convert_numerals('Latin', aan) == convert_numerals('Latin', 'ja'):
            print(f'Hedy is leuk!')
          else:
            x__x__x__x = '5'
          time.sleep(0.1)
        for __i__ in range(int('3')):
          if convert_numerals('Latin', aan) == convert_numerals('Latin', 'ja'):
            print(f'Hedy is leuk!')
          time.sleep(0.1)""")

        output = textwrap.dedent("""\
        Hedy is leuk!
        Hedy is leuk!
        Hedy is leuk!
        Hedy is leuk!
        Hedy is leuk!
        Hedy is leuk!""")

        self.single_level_tester(
            code=code,
            expected=expected,
            output=output)

    def test_source_map(self):
        code = textwrap.dedent("""\
        print 'The prince kept calling for help'
        repeat 5 times print 'Help!'
        print 'Why is nobody helping me?'""")

        expected_code = textwrap.dedent("""\
        print(f'The prince kept calling for help')
        for __i__ in range(int('5')):
          print(f'Help!')
          time.sleep(0.1)
        print(f'Why is nobody helping me?')""")

        expected_source_map = {
            '1/1-1/41': '1/1-1/43',
            '2/16-2/29': '3/3-3/18',
            '2/1-2/29': '2/1-4/18',
            '3/1-3/34': '5/1-5/36',
            '1/1-3/35': '1/1-5/36'
        }

        self.single_level_tester(code, expected=expected_code)
        self.source_map_tester(code=code, expected_source_map=expected_source_map)

# music tests

    def test_play_repeat(self):
        code = textwrap.dedent("""\
            repeat 3 times play C4""")

        expected = textwrap.dedent("""\
            for __i__ in range(int('3')):
              if 'C4' not in notes_mapping.keys() and 'C4' not in notes_mapping.values():
                  raise Exception('catch_value_exception')
              play(notes_mapping.get(str('C4'), str('C4')))
              time.sleep(0.5)
              time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            translate=False,
            skip_faulty=False,
            unused_allowed=True,
            expected=expected,
            max_level=7
        )

    def test_play_repeat_random(self):
        code = textwrap.dedent("""\
            notes is C4, E4, D4, F4, G4
            repeat 3 times play notes at random""")

        expected = textwrap.dedent("""\
            notes = ['C4', 'E4', 'D4', 'F4', 'G4']
            for __i__ in range(int('3')):
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
            max_level=7
        )
