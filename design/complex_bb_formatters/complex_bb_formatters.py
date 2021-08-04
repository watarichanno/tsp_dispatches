"""Custom BBcode tags.
"""

import os
import sys
import re
import logging

import toml

from nsdu import BBCode

# Allow importing other modules
sys.path.append(os.path.dirname(__file__))

import utils
import law_config

DISPATCH_URL = 'https://www.nationstates.net/page=dispatch/id='

logger = logging.getLogger(__name__)


@BBCode.register('url')
class Url():
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_url(options['url'],
                            context['urls'],
                            context['dispatch_info'])
        return '[url={}][color=#ff9900]{}[/color][/url]'.format(url, value)


@BBCode.register('raw_url')
class RawUrl():
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_url(options['raw_url'],
                            context['urls'],
                            context['dispatch_info'])
        return '[url={}]{}[/url]'.format(url, value)


@BBCode.register('img')
class Img():
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_img_url(value, context['img_urls'])
        return '[img]{}[/img]'.format(url)


@BBCode.register('tt')
class Tt():
    def format(self, tag_name, value, options, parent, context):
        if 'tt' not in options:
            tt_opt = 5
        else:
            tt_opt = options['tt']
        return ('[tr][td={}][background-block=#1089e6][hr]'
                '[center][font=Avenir, Segoe UI, sans-serif][size=140]'
                '[color=#ffffff][b]{}[/b][/color][/size][/font][/center]'
                '[hr][/background-block][/td][/tr]').format(tt_opt, value)


@BBCode.register('td')
class Td():
    def format(self, tag_name, value, options, parent, context):
        if 'td' not in options:
            return ('[td][font=Avenir, Segoe UI, sans-serif][size=120]{}'
                    '[/size][/font][/td]').format(value)
        return ('[td={}][font=Avenir, Segoe UI, sans-serif][size=120]{}'
                '[/size][/font][/td]').format(options['td'], value)


@BBCode.register('tdr')
class TdRaw():
    def format(self, tag_name, value, options, parent, context):
        if 'td' not in options:
            return ('[td]{}[/td]').format(value)
        return ('[td={}]{}[/td]').format(options['td'], value)


@BBCode.register('th')
class Th():
    def format(self, tag_name, value, options, parent, context):
        if 'th' not in options:
            return ('[td][font=Avenir, Segoe UI, sans-serif][size=130]'
                    '[color=#109aed][b]{}[/b][/color][/size][/font][/td]').format(value)
        return ('[td={}][font=Avenir, Segoe UI, sans-serif][size=130]'
                '[color=#109aed][b]{}[/b][/color][/size][/font][/td]').format(options['th'], value)


@BBCode.register('ref')
class Ref():
    def format(self, tag_name, value, options, parent, context):
        if '[*]' in value:
            return ('[font=Avenir, Segoe UI, sans-serif][size=120][color=#109aed][b]References: [/b]'
                    '[/color][/size][/font][list]{}[/list]').format(value)
        else:
            return ('[font=Avenir, Segoe UI, sans-serif][size=120][color=#109aed][b]Reference: [/b]'
                    '[/color]{}[/size][/font]').format(value)


@BBCode.register('law')
class Law():
    def format(self, tag_name, value, options, parent, context):
        url = utils.get_law_url(value, context['dispatch_info'], law_config.DISPATCH_NAME_PREFIX,
                                law_config.CITATION_PATTERN, law_config.ARTICLE_FORMAT, law_config.SECTION_FORMAT)
        return '[url={}][color=#ff9900]{}[/color][/url]'.format(url, value)
