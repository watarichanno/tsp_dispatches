"""Complex formatter config.
"""

DISPATCH_NAME_PREFIX = "laws/"
CITATION_PATTERN = (
    "(Section ((?P<sec>\d+), ))?(((\d+), )+)?(Article (?P<art>\w+) of )?(?P<law>.+)"
)
ARTICLE_FORMAT = "a{}"
SECTION_FORMAT = "_s{}"
