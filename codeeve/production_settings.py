from codeeve.settings import *  # noqa
from codeeve.settings import DATABASES
# Parse database configuration from $DATABASE_URL
import dj_database_url

DEVELOPMENT_ENV = False

DATABASES['default'] = dj_database_url.config()
