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
        print_format_no_discord (str, optional): Output format with no discord handle. Defaults to '{nation}'.

    Returns:
        str: Formatted output
    """

    if 'discord_handle' not in personnel:
        return print_format_no_discord.format(nation=nation(personnel.get('nation', '')),
                                              name=personnel['name'])

    return print_format.format(nation=nation(personnel.get('nation', '')),
                               discord_handle=personnel.get('discord_handle'),
                               name=personnel['name'])


def gen_list(input_list, delimiter=', ', start_tag='', end_tag=''):
    """Generate a text list with each item separated by a delimiter.
    E.g nation1, nation2, nation3

    Args:
        input_list (list): List.
        delimiter (str, optional): Delimiter. Defaults to ', '.
        start_tag (str, optional): Start tag to format an item. Defaults to ''.
        end_tag (str, optional): End tag to format an item. Defaults to ''.

    Returns:
        str: A text list.
    """

    result = delimiter.join(["{}{}{}".format(start_tag, item, end_tag) for item in input_list])
    return result


def gen_personnel_list(input_list, delimiter=', ',
                       print_format='{nation} ({discord_handle})',
                       print_format_no_discord='{nation}'):
    """Generate a text list for personnel.

    Args:
        input_list (list): Personnel list
        delimiter (str, optional): Delimiter. Defaults to ', '.
        print_format (str, optional): Output format. Defaults to '{nation} ({discord_handle})'.
        print_format_no_discord (str, optional): Output format with no discord handle. Defaults to '{nation}'.
    """

    result = delimiter.join([info(item, print_format, print_format_no_discord) for item in input_list])
    return result


def gen_table_tags(input_list, column_num=5, start_tag='', end_tag=''):
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


def gen_table_tags_personnel(input_list, column_num=5,
                             print_format='{nation} ({discord_handle})',
                             print_format_no_discord='{nation}'):
    """Generate table tags ([tr][td][/td][/tr]) for tables.
    E.g. [tr][td]nation1[/td][td]nation2[/td][/tr]

    Args:
        input_list (list): List.
        column_num (str, optional): Number of columns. Defaults to 5.
        start_tag (str, optional): Start tag to format a cell. Defaults to '[p][nation]'.
        end_tag (str, optional): End tag to format a cell. Defaults to '[/nation][/p].
    """

    result = ''

    for i in range(0, len(input_list), column_num):
        result += '[tr]'

        try:
            for j in range(i, i + column_num):
                result += '[td]{}[/td]'.format(info(input_list[j], print_format, print_format_no_discord))
        except(IndexError):
            pass

        result += '[/tr]'

    return result

