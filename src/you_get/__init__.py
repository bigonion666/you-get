#!/usr/bin/env python
# This file is Python 2 compliant.

import sys

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if sys.version_info[0] == 3:
    #from .extractor import Extractor, VideoExtractor
    #from .util import log

    from .__main__ import *

    #from .common import *
    #from .version import *
    #from .cli_wrapper import *
    #from .extractor import *
else:
    # Don't import anything.
    pass
