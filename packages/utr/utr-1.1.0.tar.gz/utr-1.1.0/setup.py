# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['utr', 'utr.cli', 'utr.cli.player', 'utr.cli.results', 'utr.cli.score']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'daiquiri>=3.2.1,<4.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tabulate>=0.8.10,<0.9.0']

entry_points = \
{'console_scripts': ['utr = utr.cli.cli:cli']}

setup_kwargs = {
    'name': 'utr',
    'version': '1.1.0',
    'description': 'A python library to interact with UTR API',
    'long_description': '# UTR\nUniversal Tennis Rating python library\n\n![example workflow](https://github.com/userlerueda/utr/actions/workflows/on_push.yml/badge.svg?branch=main) ![GitHub](https://img.shields.io/github/license/userlerueda/utr) ![GitHub all releases](https://img.shields.io/github/downloads/userlerueda/utr/total)\n\n## Description\n\n## Installation\n\nTo install the library from GitHub:\n\n```bash\npip install git+https://github.com/userlerueda/utr.git\n```\n\n## Usage Guide\n\n### Using via CLI\n\n#### Getting Player Information\n\n```bash\n$ utr player 909618\n{\n  "eventViewModel": null,\n  "id": "909618",\n  "firstName": "German Andres",\n  "lastName": "Castillo Contreras",\n  "gender": "M",\n  "city": "Bogot\\u00e1",\n  "state": "Bogota",\n  "hasYobOnly": false,\n  "singlesUtr": 0.0,\n  "singlesUtrDisplay": "0.xx",\n  "ratingStatusSingles": "Unrated",\n  "ratingProgressSingles": "0",\n  "ratingStatusImgageSingles": null,\n  "doublesUtr": 0.0,\n  "doublesUtrDisplay": "0.xx",\n  "ratingStatusDoubles": "Unrated",\n  "ratingProgressDoubles": "0",\n  "ratingStatusImgageDoubles": null,\n  "importSource": null,\n  "nationality": "COL",\n  "myUtrSingles": 0.0,\n  "myUtrSinglesDisplay": "0.xx",\n  "myUtrStatusSingles": "Unrated",\n  "myUtrDoubles": 0.0,\n  "myUtrDoublesDisplay": "0.xx",\n  "myUtrStatusDoubles": "Unrated",\n  "finalPbr": null,\n  "pbrRatingDisplay": null,\n  "memberId": 91765,\n  "utrRange": {\n    "minUtr": 5.25,\n    "maxUtr": 7.25,\n    "lastReliableRating": null,\n    "lastReliableRatingDate": null,\n    "minUtrDisplay": "5.xx",\n    "maxUtrDisplay": "7.xx",\n    "lastReliableRatingDisplay": "0.xx",\n    "pbrRange": null\n  },\n  "historicRatings": {\n    "historicSinglesRating": null,\n    "historicSinglesRatingReliability": null,\n    "historicSinglesRatingDate": null,\n    "historicDoublesRating": null,\n    "historicDoublesRatingReliability": null,\n    "historicDoublesRatingDate": null,\n    "historicSinglesRatingDisplay": "0.xx",\n    "historicDoublesRatingDisplay": "0.xx"\n  }\n}\n```\n\n#### Getting Results for a Club\n\n```bash\n$ utr results 12610\n+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+\n| event        | event_id   |   result_id | date                | winner                           |   winner_id | loser                          |   loser_id | sourceType   | excludeFromRating   | score            |\n|--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------|\n| Club Matches |            |    34601132 | 2022-09-24T21:00:00 | Pablo LEMUS                      |     2581102 | Jorge González                 |    3525582 | myutr        | False               | 6-2 6-2          |\n...\n...\n...\n| Club Matches |            |    34590366 | 2022-02-19T19:00:00 | Ana María Peláez                 |     3541392 | Pablo Rico                     |    3178932 | myutr        | False               | 2-6 6-2 10-7     |\n+--------------+------------+-------------+---------------------+----------------------------------+-------------+--------------------------------+------------+--------------+---------------------+------------------+\n```\n\n### Using as a Library\n\n## Credits\n\n## License\n\nThis project is covered under the terms described in [LICENSE](LICENSE).\n\n## Contributing\n\nSee the [Contributing](CONTRIBUTING.md) if you want to contribute.\n\n## Changes\n\nSee the [Changelog](CHANGELOG.md) for a full list of changes.\n',
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
