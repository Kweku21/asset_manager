import logging

from source.contrib.utils import create_folders
from .base import *

logger = logging.getLogger('source')
logger.error("Current mode: %s" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *

create_folders(MEDIA_ROOT)
