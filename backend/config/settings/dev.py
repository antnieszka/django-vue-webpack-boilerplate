from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "n3@wsgyxr)65$+s%z=b7#@8460%t_t0&s*elevyu%h5w_0i9@@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ("127.0.0.1", "localhost")


WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(FRONTEND_DIR, "webpack-stats.json"),
        # "STATS_FILE": os.path.join(FRONTEND_DIR, "webpack-stats-prod.json"),  # left for testing purposes...
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}
