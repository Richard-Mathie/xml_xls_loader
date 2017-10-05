# Flask-Cache-Redis-Cluster
[![PyPI version](https://img.shields.io/pypi/v/_.svg)](https://pypi.python.org/pypi/_)
[![Travis CI](https://travis-ci.org/Richard-Mathie/_.svg?branch=master)](https://travis-ci.org/_/_)
[![Code Climate](https://codeclimate.com/repos/_/badges/_/gpa.svg)](https://codeclimate.com/repos/_/feed)
[![Test Coverage](https://codeclimate.com/repos/_/badges/_/coverage.svg)](https://codeclimate.com/repos/_/coverage)


## Usage

```python
from flask import Flask
from flask_caching import Cache
app = Flask(__name__)


class Config(object):

    CACHE_TYPE = 'flask_cache_redis_cluster.rediscluster'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_KEY_PREFIX = '<your prefix>'
    # ... other options


app.config.from_object(Config)
cache = Cache(app)
```

## Links
* []()
