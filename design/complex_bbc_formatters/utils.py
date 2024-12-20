"""Utility functions for some BBCode tags.
"""

import re
import logging


logger = logging.getLogger(__name__)


DISPATCH_URL = "https://www.nationstates.net/page=dispatch/id="


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
        try:
            dispatch_id = dispatches[url].ns_id
            r = "{}{}".format(DISPATCH_URL, dispatch_id)
        except KeyError:
            logger.error('Id of dispatch "%s" not found.', url)
            r = url
    elif url.split("#")[0] in dispatches:
        url = url.split("#")
        dispatch_id = dispatches[url[0]].ns_id
        r = "{}{}#{}".format(DISPATCH_URL, dispatch_id, url[1])
    else:
        r = url

    return r

