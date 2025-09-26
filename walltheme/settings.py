"""
Setting configuration
"""

import os
from pathlib import Path

__version__ = '0.1.7'

TEMPLATE_DIR = Path(os.path.expanduser('~/.config/walltheme/templates'))
CACHE_DIR = Path(os.path.expanduser('~/.cache/walltheme'))
