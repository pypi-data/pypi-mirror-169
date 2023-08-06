# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsw']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'daiquiri>=3.2.1,<4.0.0',
 'lxml>=4.9.1,<5.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'tabulate>=0.8.10,<0.9.0']

entry_points = \
{'console_scripts': ['tsw = tsw.main:cli']}

setup_kwargs = {
    'name': 'tsw',
    'version': '0.2.1',
    'description': 'A python library to interact with Tournament Software',
    'long_description': '# Tournament Software\n\nTournament Software python library\n\n![example workflow](https://github.com/userlerueda/utr/actions/workflows/on_push.yml/badge.svg?branch=main) ![GitHub](https://img.shields.io/github/license/userlerueda/tournamentsw) ![GitHub all releases](https://img.shields.io/github/downloads/userlerueda/tournamentsw/total)\n\n## Description\n\n## Installation\n\nTo install the latest version:\n\n```bash\npip install tsw\n```\n\nTo install the library from GitHub:\n\n```bash\npip install git+https://github.com/userlerueda/tournamentsw.git\n```\n\n## Usage Guide\n\n### Using via CLI\n\n#### Getting Events\n\n```bash\n$ tsw events B88B8B48-E97D-45EF-BCB5-D2B393B0EAC6\n+------+--------------------+---------+-----------+\n|   id | Name               |   Draws |   Entries |\n|------+--------------------+---------+-----------|\n|    7 | HASTA 14 AÑOS      |       1 |        18 |\n|    2 | INTERMEDIA MIXTO A |       1 |        32 |\n|    3 | INTERMEDIA MIXTO B |       1 |        22 |\n|    1 | PRIMERA            |       1 |        11 |\n|    4 | SEGUNDA MIXTO      |       1 |        32 |\n|    8 | TERCERA DAMAS      |       1 |        21 |\n|    5 | TERCERA MIXTO A    |       1 |        20 |\n|    6 | TERCERA MIXTO B    |       1 |        23 |\n+------+--------------------+---------+-----------+\n```\n\n#### Getting Draws for a Tournament\n\n```bash\n❯ tsw draws B88B8B48-E97D-45EF-BCB5-D2B393B0EAC6 7\n+------+---------------+--------+-------------+-----------------+---------------+\n|   id | Draw          |   Size | Type        | Qualification   |   Consolation |\n|------+---------------+--------+-------------+-----------------+---------------|\n|   11 | HASTA 14 AÑOS |     32 | Elimination | No              |           nan |\n+------+---------------+--------+-------------+-----------------+---------------+\n```\n\n#### Getting Matches for a Draw\n\n```bash\ntsw matches B88B8B48-E97D-45EF-BCB5-D2B393B0EAC6 11\n+-----------------------+------------------+--------------------+-----------------+--------------------+------------------------------+\n| Timestamp             | Winner Country   | Winner Name        | Loser Country   | Loser Name         | Score                        |\n|-----------------------+------------------+--------------------+-----------------+--------------------+------------------------------|\n| Sat 5/14/2022 2:00 PM | COL              | Gabriel Echeverri  | COL             | Rafael Sanint      | [[6, 1], [6, 0]]             |\n| Sat 5/14/2022 2:00 PM | COL              | Juan Martin Siegel | COL             | Emma Villa         | [[3, 6], [6, 2], [10, 7]]    |\n| Sun 5/15/2022 2:00 PM | COL              | Juan Marulanda     | COL             | Gabriel Echeverri  | [[4, 6], [6, 3], [10, 7]]    |\n| Sun 5/15/2022 2:00 PM | COL              | Matias Lopez       | COL             | Violeta Gonzalez   | [[6, 0], [6, 1]]             |\n| Sun 5/15/2022 2:00 PM | COL              | Manuel Orozco      | COL             | Samuel Escandon    | [[6, 3], [6, 1]]             |\n| Sun 5/15/2022 2:00 PM | COL              | Simon Scanzani Iza |                 |                    | [[6, 3], [6, 2]]             |\n| Sun 5/15/2022 4:00 PM | COL              | Pamela Duque       | COL             | Emiliano Fernandez | [[6, 4], [5, 7], [10, 8]]    |\n| Sun 5/15/2022 4:00 PM | COL              | Mariana Guerrero   | COL             | Pablo Rueda        | [[6, 3], [4, 6], [10, 6]]    |\n| Sun 5/15/2022 4:00 PM | COL              | Matias Castro      | COL             | Jacobo Castro      | [[6, 0], [6, 0]]             |\n| Sun 5/15/2022 4:00 PM | COL              | Pedro Gutierrez    | COL             | Juan Martin Siegel | [[3, 6], [6, 4], [10, 0]]    |\n| Sat 5/21/2022 2:00 PM | COL              | Juan Marulanda     | COL             | Matias Lopez       | [[6, 4], [6, 4]]             |\n| Sat 5/21/2022 2:00 PM | COL              | Manuel Orozco      | COL             | Simon Scanzani Iza | [[6, 1], [6, 3]]             |\n| Sat 5/21/2022 2:00 PM | COL              | Pamela Duque       | COL             | Mariana Guerrero   | [[6, 3], [6, 3]]             |\n| Sat 5/21/2022 2:00 PM | COL              | Pedro Gutierrez    | COL             | Matias Castro      | [[7, 5], [1, 6], [10, 6]]    |\n| Sun 5/22/2022 2:00 PM | COL              | Juan Marulanda     | COL             | Manuel Orozco      | [[7, 6, 3], [2, 6], [10, 3]] |\n| Sun 5/22/2022 2:00 PM | COL              | Pedro Gutierrez    | COL             | Pamela Duque       | [[6, 3], [6, 3]]             |\n| Sat 5/28/2022 3:00 PM | COL              | Juan Marulanda     | COL             | Pedro Gutierrez    | [[6, 3], [6, 3]]             |\n+-----------------------+------------------+--------------------+-----------------+--------------------+------------------------------+\n```\n\n### Using as a Library\n\n## Credits\n\n## License\n\nThis project is covered under the terms described in [LICENSE](LICENSE).\n\n## Contributing\n\nSee the [Contributing](CONTRIBUTING.md) if you want to contribute.\n\n## Changes\n\nSee the [Changelog](CHANGELOG.md) for a full list of changes.\n',
    'author': 'Luis Rueda',
    'author_email': 'userlerueda@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/userlerueda/utr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
