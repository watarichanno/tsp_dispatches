"""Custom template filters."""


def nation(name):
    """Enclose nation name with [nation][/nation] tag.
    If provided value is a personnel info dict, use the nation value.

    Args:
        name (str|dict): Nation name or personnel info

    Returns:
        str: [nation]nation name[/nation]
    """

    if isinstance(name, dict) and 'nation' in name:
        name = name['nation']

    return '[nation]{}[/nation]'.format(name)


def region(name):
    """Enclose region name with [region][/region] tag.

    Args:
        name (str): Region name.

    Returns:
        str: [region]region name[/region]
    """

    return '[region]{}[/region]'.format(name)


def info(personnel, print_format='{nation} ({discord_handle})', print_format_no_discord='{nation}'):
    """Output information of a government official.

    Args:
        personnel (dict): Government official info defined in template variables
        print_format (str, optional): Output format. Defaults to '{nation} ({discord_handle})'.

    Returns:
        str: Formatted output
    """

    if 'discord_handle' not in personnel:
        return print_format_no_discord.format(nation=nation(personnel.get('nation', '')),
                                              name=personnel['name'])

    return print_format.format(nation=nation(personnel.get('nation', '')),
                               discord_handle=personnel.get('discord_handle'),
                               name=personnel['name'])


def gen_table_tags(input_list, column_num=5, start_tag='[nation]', end_tag='[/nation]'):
    """Generate table tags ([tr][td][/td][/tr]) for tables.
    E.g. [tr][td]nation1[/td][td]nation2[/td][/tr]

    Args:
        input_list (list): List.
        column_num (str, optional): Number of columns. Defaults to 5.
        start_tag (str, optional): Start tag to format a cell. Defaults to '[p][nation]'.
        end_tag (str, optional): End tag to format a cell. Defaults to '[/nation][/p].
    """

    result = ""

    for i in range(0, len(input_list), column_num):
        result += "[tr]"

        try:
            for j in range(i, i + column_num):
                result += "[td]{}{}{}[/td]".format(start_tag, input_list[j], end_tag)
        except(IndexError):
            pass

        result += "[/tr]"

    return result

