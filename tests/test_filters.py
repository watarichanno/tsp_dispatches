from tsp_dispatches.design import filters


class TestNation():
    def test_with_regular_string(self):
        assert filters.nation('test') == '[nation]test[/nation]'

    def test_with_dict_variable(self):
        assert filters.nation({'nation': 'cool'}) == '[nation]cool[/nation]'


class TestRegion():
    def test_default(self):
        assert filters.region('test') == '[region]test[/region]'

class TestInfo():
    def test_default_format_with_discord_handle(self):
        r = filters.info({'name': 'foo', 'nation': 'footopia', 'discord_handle': 'Foo#1234'})
        assert r == '[nation]footopia[/nation] (Foo#1234)'

    def test_default_format_with_no_discord_handle(self):
        r = filters.info({'name': 'foo', 'nation': 'footopia'})
        assert r == '[nation]footopia[/nation]'

    def test_custom_format_with_discord_handle(self):
        r = filters.info({'name': 'foo', 'nation': 'footopia', 'discord_handle': 'Foo#1234'},
                         print_format='{name} {nation} {discord_handle}',
                         print_format_no_discord='{name} {nation}')
        assert r == 'foo [nation]footopia[/nation] Foo#1234'

    def test_custom_format_with_no_discord_handle(self):
        r = filters.info({'name': 'foo', 'nation': 'footopia'},
                         print_format='{name} {nation} {discord_handle}',
                         print_format_no_discord='{name} {nation}')
        assert r == 'foo [nation]footopia[/nation]'


class TestGenList():
    def test_default(self):
        assert filters.gen_list(['a', 'b', 'c']) == 'a, b, c'

    def test_with_custom_delimiter(self):
        assert filters.gen_list(['a', 'b', 'c'], delimiter='. ') == 'a. b. c'

    def test_with_custom_tag(self):
        expected = '[n]a[/n], [n]b[/n], [n]c[/n]'
        assert filters.gen_list(['a', 'b', 'c'], start_tag='[n]', end_tag='[/n]') == expected


class TestGenPersonnelList():
    def test_default(self):
        personnel = [{'name': 'foo', 'nation': 'footopia', 'discord_handle': 'Foo#1234'},
                     {'name': 'bar', 'nation': 'bartopia', 'discord_handle': 'Bar#4321'}]
        expected = '[nation]footopia[/nation] (Foo#1234), [nation]bartopia[/nation] (Bar#4321)'
        assert filters.gen_personnel_list(personnel) == expected

    def test_with_custom_delimiter(self):
        personnel = [{'name': 'foo', 'nation': 'footopia', 'discord_handle': 'Foo#1234'},
                     {'name': 'bar', 'nation': 'bartopia', 'discord_handle': 'Bar#4321'}]
        expected = '[nation]footopia[/nation] (Foo#1234). [nation]bartopia[/nation] (Bar#4321)'
        assert filters.gen_personnel_list(personnel, delimiter='. ') == expected


class TestGenTableTags():
    def test_with_default_tag_and_column_num(self):
        expected = '[tr][td]1[/td][td]2[/td][td]3[/td][/tr]'
        assert filters.gen_table_tags(['1', '2', '3']) == expected

    def test_with_custom_tag_and_column_num(self):
        expected = '[tr][td][a]1[/a][/td][td][a]2[/a][/td][/tr][tr][td][a]3[/a][/td][/tr]'
        assert filters.gen_table_tags(['1', '2', '3'], column_num=2, start_tag='[a]', end_tag='[/a]') == expected


class TestGenTableTagsPersonnel():
    def test_default(self):
        personnel = [{'name': 'foo', 'nation': 'footopia', 'discord_handle': 'Foo#1234'},
                     {'name': 'bar', 'nation': 'bartopia', 'discord_handle': 'Bar#4321'}]
        expected = ('[tr][td][nation]footopia[/nation] (Foo#1234)[/td]'
                    '[td][nation]bartopia[/nation] (Bar#4321)[/td][/tr]')
        assert filters.gen_table_tags_personnel(personnel) == expected