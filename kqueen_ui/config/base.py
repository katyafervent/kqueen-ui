class BaseConfig:
    DEBUG = False
    LOG_LEVEL = 'WARNING'
    LOG_CONFIG = 'kqueen_ui/utils/logger_config.yml'
    CACHE = {'CACHE_TYPE': 'simple'}
    PRELOADER = 'simple'

    # KQueen UI endpoints
    HOST = 'localhost'
    PORT = 8000
    PUBLIC_ENDPOINT = 'localhost:8000'

    # KQueen API
    KQUEEN_API_URL = 'http://localhost:5000/api/v1/'
    KQUEEN_AUTH_URL = 'http://localhost:5000/api/v1/auth'

    # Babel
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

    # Addons
    ENABLE_ADDONS = True

    # Registration
    ENABLE_PUBLIC_REGISTRATION = False
    KQUEEN_SERVICE_USER_USERNAME = 'admin'
    KQUEEN_SERVICE_USER_PASSWORD = 'default'

    # Mail
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_CONN_TIMEOUT = 30
    MAIL_USE_SSL = False
    MAIL_SSL_KEYFILE = None
    MAIL_SSL_CERTFILE = None
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = 'kqueen@mirantis.com'

    # Cluster statuses
    CLUSTER_ERROR_STATE = 'Error'
    CLUSTER_OK_STATE = 'OK'
    CLUSTER_PROVISIONING_STATE = 'Deploying'
    CLUSTER_DEPROVISIONING_STATE = 'Destroying'
    CLUSTER_RESIZING_STATE = 'Resizing'
    CLUSTER_UNKNOWN_STATE = 'Unknown'
    CLUSTER_TRANSIENT_STATES = [
        CLUSTER_PROVISIONING_STATE,
        CLUSTER_DEPROVISIONING_STATE,
        CLUSTER_RESIZING_STATE
    ]

    # Provisioner statuses
    PROVISIONER_ERROR_STATE = 'Error'
    PROVISIONER_OK_STATE = 'OK'
    PROVISIONER_UNKNOWN_STATE = 'Not Reachable'

    @classmethod
    def get(cls, name, default=None):
        """Emulate get method from dict"""

        if hasattr(cls, name):
            return getattr(cls, name)
        else:
            return default

    @classmethod
    def to_dict(cls):
        """Return dict of all uppercase attributes"""

        out = {}

        for att_name in dir(cls):
            if att_name.isupper():
                out[att_name] = getattr(cls, att_name)

        return out
