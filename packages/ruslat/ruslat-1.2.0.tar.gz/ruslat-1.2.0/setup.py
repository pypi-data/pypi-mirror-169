# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ruslat']

package_data = \
{'': ['*']}

install_requires = \
['regex>=2022.9.13,<2023.0.0']

entry_points = \
{'console_scripts': ['ruslat = ruslat.command_line:main']}

setup_kwargs = {
    'name': 'ruslat',
    'version': '1.2.0',
    'description': 'Transliterator for Russian Latin Alphabet',
    'long_description': '# Converter for Russian Latin Alphabet\n\n## Installation\n```pip install ruslat```\n\n## Usage\nUsing a function\n```python\n>>> import ruslat\n>>> ruslat.latinizator(\'Съешь же ещё этих мягких французских булок да выпей чаю.\')\n\'Sješ že jesčë etih miagkih francuzskih bulok da vypej čaju.\'\n```\nAs a command line tool (example for Windows)\n```\nC:\\Users\\user>ruslat test.txt\nSuccesfully latinized test.txt to lat_test.txt\n```\n\n## Known issues\n- Each word must be in lowercase, titlecase or uppercase. "Mixed case" like `ФсЕМ прИФФкИ в эТОм чЯТиКе` is not allowed, but `ПРИВЕТ` or `Чатик` works. For regular texts, it is enough.\n- Word \'Я\' (not letter, but word) is always being converted to \'Ja\', even if it\'s e.g. a title: `КАК Я ПРОВЕЛ ЛЕТО -> KAK Ja PROVEL LETO`.\n\n## License\nruslat is licensed under the MIT License. For the full text, check out `LICENSE`.',
    'author': 'Zeta Factorial',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZetaFactorial/ruslat',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
