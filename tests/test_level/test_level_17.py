import textwrap

from parameterized import parameterized

import exceptions
import hedy
from hedy_sourcemap import SourceRange
# from hedy_sourcemap import SourceRange
from tests.Tester import HedyTester, SkippedMapping  # , SkippedMapping


class TestsLevel17(HedyTester):
    level = 17

    def test_if_with_indent(self):
        code = textwrap.dedent("""\
    naam is 'Hedy'
    if naam is 'Hedy':
        print 'koekoek'""")
        expected = textwrap.dedent("""\
    naam = 'Hedy'
    if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
      print(f'''koekoek''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_if_with_equals_sign(self):
        code = textwrap.dedent("""\
    naam is 'Hedy'
    if naam == Hedy:
        print 'koekoek'""")

        expected = textwrap.dedent("""\
    naam = 'Hedy'
    if convert_numerals('Latin', naam) == convert_numerals('Latin', 'Hedy'):
      print(f'''koekoek''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_if_else(self):
        code = textwrap.dedent("""\
    antwoord is ask 'Hoeveel is 10 plus 10?'
    if antwoord is 20:
        print 'Goedzo!'
        print 'Het antwoord was inderdaad ' antwoord
    else:
        print 'Foutje'
        print 'Het antwoord moest zijn ' antwoord""")

        expected = textwrap.dedent("""\
    antwoord = input(f'''Hoeveel is 10 plus 10?''')
    try:
      antwoord = int(antwoord)
    except ValueError:
      try:
        antwoord = float(antwoord)
      except ValueError:
        pass
    if convert_numerals('Latin', antwoord) == convert_numerals('Latin', '20'):
      print(f'''Goedzo!''')
      print(f'''Het antwoord was inderdaad {antwoord}''')
    else:
      print(f'''Foutje''')
      print(f'''Het antwoord moest zijn {antwoord}''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_if_else_boolean(self):
        code = textwrap.dedent("""\
    computerc = 'PC'
    userc = 'Hedy'
    print 'Pilihan komputer: ' computerc
    if userc is computerc and userc is 'Hedy':
        print 'SERI'
    else:
        print 'Komputer'""")

        expected = textwrap.dedent("""\
    computerc = 'PC'
    userc = 'Hedy'
    print(f'''Pilihan komputer: {computerc}''')
    if convert_numerals('Latin', userc) == convert_numerals('Latin', computerc) and convert_numerals('Latin', userc) == convert_numerals('Latin', 'Hedy'):
      print(f'''SERI''')
    else:
      print(f'''Komputer''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_for_loop_arabic(self):
        code = textwrap.dedent("""\
    for دورة in range ١ to ٥:
        print دورة""")

        expected = textwrap.dedent("""\
    step = 1 if 1 < 5 else -1
    for دورة in range(1, 5 + step, step):
      print(f'''{دورة}''')
      time.sleep(0.1)""")

        self.single_level_tester(
            code=code,
            expected=expected,
            expected_commands=['for', 'print'])

    def test_if_elif_boolean(self):
        code = textwrap.dedent("""\
    computerc = 'PC'
    userc = 'Hedy'
    print 'Pilihan komputer: ' computerc
    if userc is computerc and userc is 'Hedy':
        print 'SERI'
    elif userc is 'PC' and userc is 'Hedy':
        print 'HARI'
    else:
        print 'Komputer'""")

        expected = textwrap.dedent("""\
    computerc = 'PC'
    userc = 'Hedy'
    print(f'''Pilihan komputer: {computerc}''')
    if convert_numerals('Latin', userc) == convert_numerals('Latin', computerc) and convert_numerals('Latin', userc) == convert_numerals('Latin', 'Hedy'):
      print(f'''SERI''')
    elif convert_numerals('Latin', userc) == convert_numerals('Latin', 'PC') and convert_numerals('Latin', userc) == convert_numerals('Latin', 'Hedy'):
      print(f'''HARI''')
    else:
      print(f'''Komputer''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_for_loop(self):
        code = textwrap.dedent("""\
    a is 2
    b is 3
    for a in range 2 to 4:
        a is a + 2
        b is b + 2""")
        expected = textwrap.dedent("""\
    a = 2
    b = 3
    step = 1 if 2 < 4 else -1
    for a in range(2, 4 + step, step):
      a = a + 2
      b = b + 2
      time.sleep(0.1)""")

        self.single_level_tester(code=code, expected=expected)

    def test_if__else(self):
        code = textwrap.dedent("""\
    a is 5
    if a is 1:
        a is 2
    else:
        a is 222""")
        expected = textwrap.dedent("""\
    a = 5
    if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
      a = 2
    else:
      a = 222""")
        self.single_level_tester(code=code, expected=expected)

    def test_forloop(self):
        code = textwrap.dedent("""\
    for i in range 1 to 10:
        print i
    print 'wie niet weg is is gezien'""")
        expected = textwrap.dedent("""\
    step = 1 if 1 < 10 else -1
    for i in range(1, 10 + step, step):
      print(f'''{i}''')
      time.sleep(0.1)
    print(f'''wie niet weg is is gezien''')""")

        self.single_level_tester(code=code, expected=expected)

    def test_allow_space_after_else_line(self):
        code = textwrap.dedent("""\
    a is 1
    if a is 1:
        print a
    else:
        print 'nee'""")

        expected = textwrap.dedent("""\
    a = 1
    if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
      print(f'''{a}''')
    else:
      print(f'''nee''')""")

        self.multi_level_tester(
            max_level=17,
            code=code,
            expected=expected,
            expected_commands=['is', 'if', 'print', 'print']
        )

    def test_while_undefined_var(self):
        code = textwrap.dedent("""\
      while antwoord != 25:
          print 'hoera'""")

        self.single_level_tester(
            code=code,
            exception=hedy.exceptions.UndefinedVarException
        )

    def test_allow_space_before_colon(self):

        code = textwrap.dedent("""\
    a is 1
    if a is 1  :
        print a
    else:
        print 'nee'""")

        expected = textwrap.dedent("""\
    a = 1
    if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
      print(f'''{a}''')
    else:
      print(f'''nee''')""")

        self.multi_level_tester(
            code=code,
            max_level=17,
            expected=expected
        )

    def test_if_under_else_in_for(self):
        # todo can me multitester with higher levels!
        code = textwrap.dedent("""\
    for i in range 0 to 10:
        antwoord is ask 'Wat is 5*5'
        if antwoord is 24:
            print 'Dat is fout!'
        else:
            print 'Dat is goed!'
        if antwoord is 25:
            i is 10""")

        expected = textwrap.dedent("""\
    step = 1 if 0 < 10 else -1
    for i in range(0, 10 + step, step):
      antwoord = input(f'''Wat is 5*5''')
      try:
        antwoord = int(antwoord)
      except ValueError:
        try:
          antwoord = float(antwoord)
        except ValueError:
          pass
      if convert_numerals('Latin', antwoord) == convert_numerals('Latin', '24'):
        print(f'''Dat is fout!''')
      else:
        print(f'''Dat is goed!''')
      if convert_numerals('Latin', antwoord) == convert_numerals('Latin', '25'):
        i = 10
      time.sleep(0.1)""")

        self.single_level_tester(code=code, expected=expected)

    def test_if_elif(self):
        code = textwrap.dedent("""\
      a is 5
      if a is 1:
          a is 2
      elif a is 2:
          a is 222""")
        expected = textwrap.dedent("""\
      a = 5
      if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
        a = 2
      elif convert_numerals('Latin', a) == convert_numerals('Latin', '2'):
        a = 222""")

        self.single_level_tester(code=code, expected=expected)

    def test_if_elif_french(self):
        code = textwrap.dedent("""\
      a est 5
      si a est 1:
          a est 2
      sinon si a est 2:
          a est 222""")
        expected = textwrap.dedent("""\
      a = 5
      if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
        a = 2
      elif convert_numerals('Latin', a) == convert_numerals('Latin', '2'):
        a = 222""")

        self.single_level_tester(code=code, expected=expected, lang='fr')

    def test_if_with_multiple_elifs(self):
        code = textwrap.dedent("""\
      a is 5
      if a is 1:
          a is 2
      elif a is 4:
          a is 3
      elif a is 2:
          a is 222""")
        expected = textwrap.dedent("""\
      a = 5
      if convert_numerals('Latin', a) == convert_numerals('Latin', '1'):
        a = 2
      elif convert_numerals('Latin', a) == convert_numerals('Latin', '4'):
        a = 3
      elif convert_numerals('Latin', a) == convert_numerals('Latin', '2'):
        a = 222""")

        self.single_level_tester(
            code=code, expected=expected, expected_commands=[
                'is', 'if', 'is', 'elif', 'is', 'elif', 'is'])

    def test_if_in_list_with_string_var_gives_type_error(self):
        code = textwrap.dedent("""\
        items is 'red'
        if 'red' in items:
            a is 1""")
        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_equality_with_lists(self):
        code = textwrap.dedent("""\
      m is [1, 2]
      n is [1, 2]
      if m is n:
          print 'JA!'""")

        expected = textwrap.dedent("""\
      m = [1, 2]
      n = [1, 2]
      if convert_numerals('Latin', m) == convert_numerals('Latin', n):
        print(f'''JA!''')""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            max_level=17
        )

    def test_equality_with_incompatible_types_gives_error(self):
        code = textwrap.dedent("""\
    a is 'test'
    b is 15
    if a is b:
      c is 1""")
        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 3,
            exception=hedy.exceptions.InvalidTypeCombinationException
        )

    @parameterized.expand(HedyTester.comparison_commands)
    def test_comparisons(self, comparison):
        code = textwrap.dedent(f"""\
      leeftijd is ask 'Hoe oud ben jij?'
      if leeftijd {comparison} 12:
          print 'Dan ben je jonger dan ik!'""")
        expected = textwrap.dedent(f"""\
      leeftijd = input(f'''Hoe oud ben jij?''')
      try:
        leeftijd = int(leeftijd)
      except ValueError:
        try:
          leeftijd = float(leeftijd)
        except ValueError:
          pass
      if convert_numerals('Latin', leeftijd){comparison}convert_numerals('Latin', 12):
        print(f'''Dan ben je jonger dan ik!''')""")

        self.single_level_tester(code=code, expected=expected)

    @parameterized.expand(HedyTester.number_comparison_commands)
    def test_smaller_with_string_gives_type_error(self, comparison):
        code = textwrap.dedent(f"""\
      a is 'text'
      if a {comparison} 12:
          b is 1""")

        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 2,
            exception=hedy.exceptions.InvalidArgumentTypeException
        )

    def test_not_equal_string_literal(self):
        code = textwrap.dedent(f"""\
    if 'quoted' != 'string':
      sleep""")
        expected = textwrap.dedent(f"""\
    if 'quoted'!='string':
      time.sleep(1)""")

        self.multi_level_tester(
            code=code,
            expected=expected
        )

    @parameterized.expand(["'text'", '1', '1.3', '[1, 2]'])
    def test_not_equal(self, arg):
        code = textwrap.dedent(f"""\
      a = {arg}
      b = {arg}
      if a != b:
          b = 1""")

        expected = textwrap.dedent(f"""\
      a = {arg}
      b = {arg}
      if convert_numerals('Latin', a)!=convert_numerals('Latin', b):
        b = 1""")

        self.multi_level_tester(
            code=code,
            expected=expected
        )

    @parameterized.expand([
        ("'text'", '1'),        # text and number
        ('[1, 2]', '1'),        # list and number
        ('[1, 2]', "'text'")])  # list and text
    def test_not_equal_with_diff_types_gives_error(self, left, right):
        code = textwrap.dedent(f"""\
        a = {left}
        b = {right}
        if a != b:
            b = 1""")

        self.multi_level_tester(
            code=code,
            extra_check_function=lambda c: c.exception.arguments['line_number'] == 3,
            exception=exceptions.InvalidTypeCombinationException
        )

    def test_if_pressed_with_turtlecolor(self):
        code = textwrap.dedent("""\
      if x is pressed:
          color red""")

        expected = HedyTester.dedent(f"""\
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
            {HedyTester.indent(
              HedyTester.turtle_color_command_transpiled('red'),
              12, True)
            }
            break
          # End of PyGame Event Handler""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            extra_check_function=self.is_turtle()
        )

    def test_if_no_colon_after_pressed_gives_parse_error(self):
        code = textwrap.dedent("""\
        if x is pressed
            print 'no colon!'""")

        self.single_level_tester(
            code=code,
            exception=hedy.exceptions.ParseException,
            extra_check_function=lambda c: c.exception.error_location[0] == 2 and c.exception.error_location[1] == 31
        )

    def test_if_button_is_pressed_print(self):
        code = textwrap.dedent("""\
        x = 'PRINT'
        x is button
        if PRINT is pressed:
            print 'The button got pressed!'""")

        expected = HedyTester.dedent(f"""\
        x = 'PRINT'
        create_button(x)
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
              print(f'''The button got pressed!''')
              break
            # End of PyGame Event Handler""")

        self.single_level_tester(code=code, expected=expected)

    def test_pressed_elif(self):
        code = textwrap.dedent("""\
        if a is pressed:
            print 'A'
        elif b is pressed:
            print 'B'
        else:
            print 'Other'""")

        expected = HedyTester.dedent(f"""\
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
              print(f'''A''')
              break
            # End of PyGame Event Handler
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'b':
              print(f'''B''')
              break
            # End of PyGame Event Handler    
            else:
              print(f'''Other''')
              break""")

        self.single_level_tester(code=code, expected=expected)

    def test_nested_functions(self):
        code = textwrap.dedent("""\
        define simple_function:
            define nested_function:
                print 1
        call simple_function""")

        expected = textwrap.dedent("""\
        pass
        simple_function()""")

        skipped_mappings = [
            SkippedMapping(SourceRange(1, 1, 3, 34), hedy.exceptions.NestedFunctionException),
        ]

        self.single_level_tester(
            code=code,
            expected=expected,
            skipped_mappings=skipped_mappings,
        )

    def test_source_map(self):
        code = textwrap.dedent("""\
        for i in range 1 to 10:
            print i
        print 'Ready or not, here I come!'""")

        excepted_code = textwrap.dedent("""\
        step = 1 if 1 < 10 else -1
        for i in range(1, 10 + step, step):
          print(f'''{i}''')
          time.sleep(0.1)
        print(f'''Ready or not, here I come!''')""")

        expected_source_map = {
            '1/5-1/6': '1/10-1/11',
            '2/11-2/12': '1/1-1/2',
            '2/5-2/12': '3/1-3/18',
            '1/1-2/21': '1/1-4/18',
            '3/1-3/35': '5/1-5/41',
            '1/1-3/36': '1/1-5/41'
        }

        self.single_level_tester(code, expected=excepted_code)
        self.source_map_tester(code=code, expected_source_map=expected_source_map)
