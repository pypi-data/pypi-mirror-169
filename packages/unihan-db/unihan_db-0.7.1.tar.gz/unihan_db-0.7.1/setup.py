# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['unihan_db']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy', 'appdirs', 'unihan-etl>=0.18.1,<0.19.0']

setup_kwargs = {
    'name': 'unihan-db',
    'version': '0.7.1',
    'description': 'SQLAlchemy models for UNIHAN CJK database',
    'long_description': "# unihan-db &middot; [![Python Package](https://img.shields.io/pypi/v/unihan-db.svg)](https://pypi.org/project/unihan-db/) [![License](https://img.shields.io/github/license/cihai/unihan-db.svg)](https://github.com/cihai/unihan-db/blob/master/LICENSE) [![Code Coverage](https://codecov.io/gh/cihai/unihan-db/branch/master/graph/badge.svg)](https://codecov.io/gh/cihai/unihan-db)\n\nDatabase [SQLAlchemy](https://www.sqlalchemy.org/) models for\n[UNIHAN](http://www.unicode.org/charts/unihan.html). Part of the [cihai](https://cihai.git-pull.com)\nproject. Powered by [unihan-etl](https://unihan-etl.git-pull.com). See also:\n[libUnihan](http://libunihan.sourceforge.net/).\n\nBy default, unihan-db creates a SQLite database in an\n[XDG data directory](https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html). You\ncan specify a custom database destination by passing a database url into\n[get_session](http://unihan-db.git-pull.com/api.html#unihan_db.bootstrap.get_session).\n\n## Example usage\n\n```python\n#!/usr/bin/env python\nimport pprint\n\nfrom sqlalchemy.sql.expression import func\n\nfrom unihan_db import bootstrap\nfrom unihan_db.tables import Unhn\n\nsession = bootstrap.get_session()\n\nbootstrap.bootstrap_unihan(session)\n\nrandom_row = session.query(Unhn).order_by(\n    func.random()\n).limit(1).first()\n\npp = pprint.PrettyPrinter(indent=0)\n\npp.pprint(random_row.to_dict())\n```\n\nRun:\n\n    $ ./examples/01_bootstrap.py\n\nOutput:\n\n```python\n{'char': '鎷',\n'kCantonese': [{'char_id': '鎷', 'definition': 'maa5', 'id': 24035}],\n'kDefinition': [],\n'kHanYu': [{'char_id': '鎷',\n          'id': 24014,\n          'locations': [{'character': 5,\n                       'generic_indice_id': 24014,\n                       'generic_reading_id': None,\n                       'id': 42170,\n                       'page': 4237,\n                       'virtual': 0,\n                       'volume': 6}],\n          'type': 'kHanYu'}],\n'kHanyuPinyin': [{'char_id': '鎷',\n                'id': 18090,\n                'locations': [{'character': 5,\n                             'generic_indice_id': None,\n                             'generic_reading_id': 18090,\n                             'id': 42169,\n                             'page': 4237,\n                             'virtual': 0,\n                             'volume': 6}],\n                'readings': [{'generic_reading_id': 18090,\n                            'id': 26695,\n                            'reading': 'mǎ'}],\n                'type': 'kHanyuPinyin'}],\n'kMandarin': [{'char_id': '鎷', 'hans': 'mǎ', 'hant': 'mǎ', 'id': 23486}],\n'ucn': 'U+93B7'}\n```\n\n## Developing\n\n```console\n$ git clone https://github.com/cihai/unihan-etl.git\n```\n\n```console\n$ cd unihan-etl\n```\n\n[Bootstrap your environment and learn more about contributing](https://cihai.git-pull.com/contributing/). We use the same conventions / tools across all cihai projects: `pytest`, `sphinx`, `flake8`, `mypy`, `black`, `isort`, `tmuxp`, and file watcher helpers (e.g. `entr(1)`).\n\n## More information\n\n[![Docs](https://github.com/cihai/unihan-db/workflows/docs/badge.svg)](https://unihan-db.git-pull.com/)\n[![Build Status](https://github.com/cihai/unihan-db/workflows/tests/badge.svg)](https://github.com/cihai/unihan-db/actions?query=workflow%3A%22tests%22)\n",
    'author': 'Tony Narlock',
    'author_email': 'tony@git-pull.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://unihan-db.git-pull.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
