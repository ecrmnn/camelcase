# camelcase
> Convert to camelcase

[![Travis](https://img.shields.io/travis/ecrmnn/camelcase.svg?style=flat-square)](https://travis-ci.org/ecrmnn/camelcase'.svg?branch=master)
[![PyPI](https://img.shields.io/pypi/v/camel-case.svg?style=flat-square)](https://pypi.python.org/pypi/camel-case)
[![PyPI](https://img.shields.io/pypi/d/camel-case.svg?style=flat-square)](https://pypi.python.org/pypi/camel-case)
[![PyPI](https://img.shields.io/pypi/l/camel-case.svg?style=flat-square)](https://pypi.python.org/pypi/camel-case)

### Installation
```bash
pip install camel-case
```

### Usage
```python
from camelcase import camelcase


camelcase('foo-bar')
#=> fooBar

camelcase('FoO_BAR')
#=> fooBar

camelcase('__FOO__bar__')
#=> fooBar

camelcase('foo bar')
#=> fooBar

camelcase('foo   bar')
#=> fooBar

camelcase('blå_bær_sylte-tøy')
#=> blåBærSylteTøy

camelcase('blå', 'bær', 'sylte', 'tøy')
#=> blåBærSylteTøy

camelcase(['spam', 'eggs'])
#=> spamEggs
```

### Language support
Python 3.2 - 3.6 +

### License
MIT © [Daniel Eckermann](http://danieleckermann.com)