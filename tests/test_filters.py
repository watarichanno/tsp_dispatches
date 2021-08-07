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


class TestGenTableList():
    def test_with_default_tag_and_column_num(self):
        expected = '[tr][td][nation]1[/nation][/td][td][nation]2[/nation][/td][td][nation]3[/nation][/td][/tr]'
        assert filters.gen_table_tags(['1', '2', '3']) == expected

    def test_with_custom_tag_and_column_num(self):
        expected = '[tr][td][a]1[/a][/td][td][a]2[/a][/td][/tr][tr][td][a]3[/a][/td][/tr]'
        assert filters.gen_table_tags(['1', '2', '3'], column_num=2, start_tag='[a]', end_tag='[/a]') == expected