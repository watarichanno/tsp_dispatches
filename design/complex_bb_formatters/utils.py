"""Utility functions for some BBCode tags.
"""

import pathlib
import re
import logging

import toml


logger = logging.getLogger(__name__)


DISPATCH_URL = 'https://www.nationstates.net/page=dispatch/id='


def get_img_url(url, custom_vars_urls):
    if url in custom_vars_urls:
        r = custom_vars_urls[url]
    else:
        r = url

    return r


def get_url(url, custom_vars_urls, dispatches):
    """Get real URL from special URL if needed.

    Args:
        url (str): Input URL.
        custom_vars_urls (dict): URLs in custom vars file.
        dispatches (dict): Dispatch configurations.

    Returns:
        str: Real URL.
    """

    if url in custom_vars_urls:
        r = custom_vars_urls[url]
    elif url in dispatches:
        dispatch_id = dispatches[url]['ns_id']
        r = '{}{}'.format(DISPATCH_URL, dispatch_id)
    elif url.split('#')[0] in dispatches:
        url = url.split('#')
        dispatch_id = dispatches[url[0]]['ns_id']
        r = '{}{}#{}'.format(DISPATCH_URL, dispatch_id, url[1])
    else:
        r = url

    return r


def get_base_url(text, dispatch_info, dispatch_name_prefix):
    """Get base URL of law dispatch from law name.

    Args:
        text (str): Law name
        dispatch_info (dict): Dispatch info
        dispatch_name_prefix (str): Dispatch name prefix

    Returns:
        str: Base URL
    """

    name = text.lower()
    name = name.replace('the ', '', 1)

    name = name.replace(' ', '_')
    name = '{}{}'.format(dispatch_name_prefix, name)
    if name in dispatch_info:
        dispatch_id = dispatch_info[name]['ns_id']
        return '{}{}'.format(DISPATCH_URL, dispatch_id)

    logger.error('Law "%s" not found in dispatch config', name)
    return None


def get_law_url(text, dispatch_info, dispatch_name_prefix,
                citation_pattern, article_format, section_format):
    url = ""
    pattern = re.compile(citation_pattern)
    r = pattern.search(text)

    law = r.group('law')
    if law:
        base_url = get_base_url(law, dispatch_info, dispatch_name_prefix)
        if base_url:
            url += base_url

    article = r.group('art')
    section = r.group('sec')
    if article:
        url += '#'
        url += article_format.format(article)
    if section:
        url += section_format.format(section)

    return url