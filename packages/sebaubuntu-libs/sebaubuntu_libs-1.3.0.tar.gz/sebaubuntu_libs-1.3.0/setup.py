# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sebaubuntu_libs',
 'sebaubuntu_libs.libaik',
 'sebaubuntu_libs.libandroid',
 'sebaubuntu_libs.libandroid.fstab',
 'sebaubuntu_libs.libandroid.partitions',
 'sebaubuntu_libs.libandroid.props',
 'sebaubuntu_libs.libandroid.vintf',
 'sebaubuntu_libs.libexception',
 'sebaubuntu_libs.libgofile',
 'sebaubuntu_libs.libgofile.raw_api',
 'sebaubuntu_libs.liblocale',
 'sebaubuntu_libs.liblogging',
 'sebaubuntu_libs.libnekobin',
 'sebaubuntu_libs.libpath',
 'sebaubuntu_libs.libreorder',
 'sebaubuntu_libs.libsed',
 'sebaubuntu_libs.libstring',
 'sebaubuntu_libs.libtyping']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'sebaubuntu-libs',
    'version': '1.3.0',
    'description': "SebaUbuntu's shared libs",
    'long_description': '# sebaubuntu_libs\n\n[![PyPi version](https://img.shields.io/pypi/v/sebaubuntu_libs)](https://pypi.org/project/sebaubuntu_libs/)\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/383072c93d5b4fa293237d42360e2170)](https://www.codacy.com/gh/SebaUbuntu/sebaubuntu_libs/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SebaUbuntu/sebaubuntu_libs&amp;utm_campaign=Badge_Grade)\n\nA collection of code shared between my projects\n\n## Installation\n\n```sh\npip3 install sebaubuntu_libs\n```\n\n# License\n\n```\n#\n# Copyright (C) 2022 Sebastiano Barezzi\n#\n# SPDX-License-Identifier: Apache-2.0\n#\n```\n',
    'author': 'Sebastiano Barezzi',
    'author_email': 'barezzisebastiano@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sebaubuntu-python/sebaubuntu_libs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
