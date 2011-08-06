from functools import wraps

import sqlalchemy

from tables import metadata

class ExceptionDisplayMixin(object):
    def __unicode__(self):
        return u'%s: %s' % (self.__class__.__name__, self.message)

    def __str__(self):
        return unicode(self).encode('utf-8')

class ParameterError(ExceptionDisplayMixin, KeyError):
    pass

def required_params(*params):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            for param in params:
                if param not in kwargs:
                    raise ParameterError('%s is required for %s function' %
                                    (param, func.__name__))
            return func(*args, **kwargs)
        return wrapped
    return decorator

def create_tables(config):
    engine = create_engine(config['database'], echo=config.get('debug', False))
    metadata.create_all(engine)
