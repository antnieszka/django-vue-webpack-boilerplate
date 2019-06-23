from .base import *

DEBUG = False

WEBPACK_LOADER["DEFAULT"].update(
    {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "dist/",
        "STATS_FILE": os.path.join(FRONTEND_DIR, "webpack-stats-prod.json"),
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
)

