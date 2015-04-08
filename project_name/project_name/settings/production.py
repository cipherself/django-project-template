from __future__ import absolute_import

from .base import *  # noqa

import os


from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
    raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_setting('SECRET_KEY')


#################### LOGGING ####################
# See: https://docs.djangoproject.com/en/dev/topics/logging/

# Send an email to the site admins on every HTTP 500 error when DEBUG=False.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
#################### END LOGGING ####################
