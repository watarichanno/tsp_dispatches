"""Custom BBcode tags.
"""

import logging
import os
import sys

from nsdu import BBCode, ComplexFormatter

# Allow importing other modules
sys.path.append(os.path.dirname(__file__))

import law_config
import utils

DISPATCH_URL = "https://www.nationstates.net/page=dispatch/id="

logger = logging.getLogger(__name__)


@BBCode.register("pre", render_embedded=False)
class Pre(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        return "[pre]{}[/pre]".format(value)


@BBCode.register("raw", render_embedded=False)
class Raw(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        return "[raw]{}[/raw]".format(value)


@BBCode.register("url")
class Url(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_url(options["url"], context["urls"], context["dispatch_info"])
        return "[url={}][url_content]{}[/url_content][/url]".format(url, value)


@BBCode.register("raw_url")
class RawUrl(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_url(
            options["raw_url"], context["urls"], context["dispatch_info"]
        )
        return "[url={}]{}[/url]".format(url, value)


@BBCode.register("img")
class Img(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_img_url(value, context["img_urls"])
        return "[img]{}[/img]".format(url)


@BBCode.register("tt")
class Tt(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        if "tt" not in options:
            tt_opt = 5
        else:
            tt_opt = options["tt"]
        return "[tr][td={}][tt_content]{}[/tt_content][/td][/tr]".format(tt_opt, value)


@BBCode.register("td")
class Td(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        if "td" not in options:
            return ("[td][td_content]{}[/td_content][/td]").format(value)
        return "[td={}][td_content]{}[/td_content][/td]".format(options["td"], value)


@BBCode.register("th")
class Th(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        if "th" not in options:
            return "[td][th_content]{}[/th_content][/td]".format(value)
        return "[td={}][th_content]{}[/th_content][/td]".format(options["th"], value)


@BBCode.register("*", render_embedded=True, newline_closes=True, same_tag_closes=True)
class ListElem(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        return "[*][*_content]{}[/*_content]".format(value)


@BBCode.register("law")
class Law(ComplexFormatter):
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_law_url(
            value,
            context["dispatch_info"],
            law_config.DISPATCH_NAME_PREFIX,
            law_config.CITATION_PATTERN,
            law_config.ARTICLE_FORMAT,
            law_config.SECTION_FORMAT,
        )
        return "[url={}][url_content]{}[/url_content][/url]".format(url, value)
