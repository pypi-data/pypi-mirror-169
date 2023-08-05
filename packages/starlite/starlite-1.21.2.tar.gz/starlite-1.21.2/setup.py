# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlite',
 'starlite.cache',
 'starlite.config',
 'starlite.connection',
 'starlite.exceptions',
 'starlite.handlers',
 'starlite.logging',
 'starlite.middleware',
 'starlite.middleware.compression',
 'starlite.openapi',
 'starlite.plugins',
 'starlite.routes',
 'starlite.template',
 'starlite.types',
 'starlite.utils']

package_data = \
{'': ['*']}

install_requires = \
['orjson',
 'pydantic',
 'pydantic-factories',
 'pydantic-openapi-schema',
 'pyyaml',
 'starlette',
 'starlite-multipart',
 'typing-extensions']

extras_require = \
{'brotli': ['brotli'],
 'cryptography': ['cryptography'],
 'full': ['brotli', 'cryptography', 'requests'],
 'testing': ['requests']}

setup_kwargs = {
    'name': 'starlite',
    'version': '1.21.2',
    'description': 'Light-weight and flexible ASGI API Framework',
    'long_description': '<!-- markdownlint-disable -->\n<img alt="Starlite logo" src="./docs/images/SVG/starlite-banner.svg" width="100%" height="auto">\n<!-- markdownlint-restore -->\n\n<div align="center">\n\n![PyPI - License](https://img.shields.io/pypi/l/starlite?color=blue)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/starlite)\n\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite&metric=coverage)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite)\n\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite)\n[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite)\n\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/starlite-api/starlite.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/starlite-api/starlite/context:python)\n[![Total alerts](https://img.shields.io/lgtm/alerts/g/starlite-api/starlite.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/starlite-api/starlite/alerts/)\n\n<!-- prettier-ignore-start -->\n<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->\n[![All Contributors](https://img.shields.io/badge/all_contributors-45-orange.svg?style=flat-square)](#contributors-)\n<!-- ALL-CONTRIBUTORS-BADGE:END -->\n<!-- prettier-ignore-end -->\n\n[![Discord](https://img.shields.io/discord/919193495116337154?color=blue&label=chat%20on%20discord&logo=discord)](https://discord.gg/X3FJqy8d2j)\n[![Matrix](https://img.shields.io/badge/%5Bm%5D%20chat%20on%20Matrix-bridged-blue)](https://matrix.to/#/#starlitespace:matrix.org)\n\n[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://itnext.io/introducing-starlite-3928adaa19ae)\n\n</div>\n\n# Starlite\n\nStarlite is a powerful, flexible and highly performant ASGI API framework built on top\nof [Starlette](https://github.com/encode/starlette)\nand [pydantic](https://github.com/samuelcolvin/pydantic).\n\nCheck out the [Starlite documentation 📚](https://starlite-api.github.io/starlite/)\n\n## Installation\n\n```shell\npip install starlite\n```\n\n## Core Features\n\n- Both functional and OOP python support\n- Class based controllers\n- Extended testing support\n- Builtin Validation and Parsing using Pydantic\n- Dataclass Support\n- Dependency Injection\n- Layered Middleware\n- Layered Parameter declaration\n- Route Guards based Authorization\n- Life Cycle Hooks\n- Plugin System\n- SQLAlchemy Support (via plugin)\n- Tortoise-ORM Support (via plugin)\n- Automatic OpenAPI 3.1 schema generation\n- Support for [Redoc](https://github.com/Redocly/redoc)\n- Support for [Swagger-UI](https://swagger.io/tools/swagger-ui/)\n- Support for [Stoplight Elements](https://github.com/stoplightio/elements)\n- Ultra-fast json serialization and deserialization using [orjson](https://github.com/ijl/orjson)\n\n## Example Applications\n\n- [starlite-pg-redis-docker](https://github.com/starlite-api/starlite-pg-redis-docker): In addition to Starlite, this\n  demonstrates a pattern of application modularity, SQLAlchemy 2.0 ORM, Redis cache connectivity, and more. Like all\n  Starlite projects, this application is open to contributions, big and small.\n- [starlite-hello-world](https://github.com/starlite-api/starlite-hello-world): A bare-minimum application setup. Great\n  for testing and POC work.\n\n## Relation to Starlette and FastAPI\n\nAlthough Starlite uses the Starlette ASGI toolkit, it does not simply extend Starlette, as FastAPI does. Starlite uses\nselective pieces of Starlette while implementing its own routing and parsing logic, the primary reason for this is to\nenforce a set of best practices and discourage misuse. This is done to promote simplicity and scalability - Starlite is\nsimple to use, easy to learn, and unlike both Starlette and FastAPI - it keeps complexity low when scaling.\n\n### Performant\n\nAdditionally, Starlite is very fast in comparison to other ASGI\nframeworks. In fact, the only framework that is faster\nin [our benchmarks](https://github.com/starlite-api/api-performance-tests) is _BlackSheep_, which is almost completely\nwritten in cython and does not work with pydantic out of the box as such:\n\n#### JSON Benchmarks\n\n<img alt="API JSON Benchmarks" src="https://github.com/starlite-api/api-performance-tests/raw/main/result-json.png">\n\n#### PlainText Benchmarks\n\n<img alt="API Plaintext Benchmarks" src="https://github.com/starlite-api/api-performance-tests/raw/main/result-plaintext.png">\n\nLegend:\n\n- a-: async, s-: sync\n- np: no params, pp: path param, qp: query param, mp: mixed params\n\nYou can see and run the benchmarks [here](https://github.com/starlite-api/api-performance-tests).\n\n### Class Based Controllers\n\nWhile supporting function based route handlers, Starlite also supports and promotes python OOP using class based\ncontrollers:\n\n```python title="my_app/controllers/user.py"\nfrom typing import List, Optional, NoReturn\n\nfrom pydantic import UUID4\nfrom starlite import Controller, Partial, get, post, put, patch, delete\nfrom datetime import datetime\n\nfrom my_app.models import User\n\n\nclass UserController(Controller):\n    path = "/users"\n\n    @post()\n    async def create_user(self, data: User) -> User:\n        ...\n\n    @get()\n    async def list_users(self) -> List[User]:\n        ...\n\n    @get(path="/{date:int}")\n    async def list_new_users(self, date: datetime) -> List[User]:\n        ...\n\n    @patch(path="/{user_id:uuid}")\n    async def partial_update_user(self, user_id: UUID4, data: Partial[User]) -> User:\n        ...\n\n    @put(path="/{user_id:uuid}")\n    async def update_user(self, user_id: UUID4, data: User) -> User:\n        ...\n\n    @get(path="/{user_name:str}")\n    async def get_user_by_name(self, user_name: str) -> Optional[User]:\n        ...\n\n    @get(path="/{user_id:uuid}")\n    async def get_user(self, user_id: UUID4) -> User:\n        ...\n\n    @delete(path="/{user_id:uuid}")\n    async def delete_user(self, user_id: UUID4) -> NoReturn:\n        ...\n```\n\n### ReDoc, Swagger-UI and Stoplight Elements API Documentation\n\nWhile running Starlite, you can view the generated OpenAPI documentation using a [ReDoc](https://redoc.ly/) site,\na [Swagger-UI](https://swagger.io/tools/swagger-ui/) as well as\na [Stoplight Elements](https://github.com/stoplightio/elements) site.\n\n### Data Parsing, Type Hints and Pydantic\n\nOne key difference between Starlite and Starlette/FastAPI is in parsing of form data and query parameters- Starlite\nsupports mixed form data and has faster and better query parameter parsing.\n\nStarlite is rigorously typed, and it enforces typing. For example, if you forget to type a return value for a route\nhandler, an exception will be raised. The reason for this is that Starlite uses typing data to generate OpenAPI specs,\nas well as to validate and parse data. Thus typing is absolutely essential to the framework.\n\nFurthermore, Starlite allows extending its support using plugins.\n\n### SQLAlchemy Support, Plugin System and DTOs\n\nStarlite has a plugin system that allows the user to extend serialization/deserialization, OpenAPI generation and other\nfeatures. It ships with a builtin plugin for SQL Alchemy, which allows the user to use SQLAlchemy declarative classes\n"natively", i.e. as type parameters that will be serialized/deserialized and to return them as values from route\nhandlers.\n\nStarlite also supports the programmatic creation of DTOs with a `DTOFactory` class, which also supports the use of\nplugins.\n\n### OpenAPI\n\nStarlite has custom logic to generate OpenAPI 3.1.0 schema, the latest version. The schema generated by Starlite is\nsignificantly more complete and more correct than those generated by FastAPI, and they include optional generation of\nexamples using the `pydantic-factories` library.\n\n### Dependency Injection\n\nStarlite has a simple but powerful DI system inspired by pytest. You can define named dependencies - sync or async - at\ndifferent levels of the application, and then selective use or overwrite them.\n\n### Middleware\n\nStarlite supports the Starlette Middleware system while simplifying it and offering builtin configuration of CORS and\nsome other middlewares.\n\n### Route Guards\n\nStarlite has an authorization mechanism called `guards`, which allows the user to define guard functions at different\nlevel of the application (app, router, controller etc.) and validate the request before hitting the route handler\nfunction.\n\n### Request Life Cycle Hooks\n\nStarlite supports request life cycle hooks, similarly to Flask - i.e. `before_request` and `after_request`\n\n## Contributing\n\nStarlite is open to contributions big and small. You can always [join our discord](https://discord.gg/X3FJqy8d2j) server\nor [join our Matrix](https://matrix.to/#/#starlitespace:matrix.org) space\nto discuss contributions and project maintenance. For guidelines on how to contribute, please\nsee [the contribution guide](CONTRIBUTING.md).\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tbody>\n    <tr>\n      <td align="center"><a href="https://www.linkedin.com/in/nhirschfeld/"><img src="https://avatars.githubusercontent.com/u/30733348?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Na\'aman Hirschfeld</b></sub></a><br /><a href="#maintenance-Goldziher" title="Maintenance">🚧</a> <a href="https://github.com/starlite-api/starlite/commits?author=Goldziher" title="Code">💻</a> <a href="https://github.com/starlite-api/starlite/commits?author=Goldziher" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/peterschutt"><img src="https://avatars.githubusercontent.com/u/20659309?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Peter Schutt</b></sub></a><br /><a href="#maintenance-peterschutt" title="Maintenance">🚧</a> <a href="https://github.com/starlite-api/starlite/commits?author=peterschutt" title="Code">💻</a> <a href="https://github.com/starlite-api/starlite/commits?author=peterschutt" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://ashwinvin.github.io"><img src="https://avatars.githubusercontent.com/u/38067089?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ashwin Vinod</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=ashwinvin" title="Code">💻</a> <a href="https://github.com/starlite-api/starlite/commits?author=ashwinvin" title="Documentation">📖</a></td>\n      <td align="center"><a href="http://www.damiankress.de"><img src="https://avatars.githubusercontent.com/u/28515387?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Damian</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=dkress59" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://remotepixel.ca"><img src="https://avatars.githubusercontent.com/u/10407788?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vincent Sarago</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=vincentsarago" title="Code">💻</a></td>\n      <td align="center"><a href="https://hotfix.guru"><img src="https://avatars.githubusercontent.com/u/5310116?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jonas Krüger Svensson</b></sub></a><br /><a href="#platform-JonasKs" title="Packaging/porting to new platform">📦</a></td>\n      <td align="center"><a href="https://github.com/sondrelg"><img src="https://avatars.githubusercontent.com/u/25310870?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sondre Lillebø Gundersen</b></sub></a><br /><a href="#platform-sondrelg" title="Packaging/porting to new platform">📦</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="https://github.com/vrslev"><img src="https://avatars.githubusercontent.com/u/75225148?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lev</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=vrslev" title="Code">💻</a> <a href="#ideas-vrslev" title="Ideas, Planning, & Feedback">🤔</a></td>\n      <td align="center"><a href="https://github.com/timwedde"><img src="https://avatars.githubusercontent.com/u/20231751?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tim Wedde</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=timwedde" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/tclasen"><img src="https://avatars.githubusercontent.com/u/11999013?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tory Clasen</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=tclasen" title="Code">💻</a></td>\n      <td align="center"><a href="http://t.me/Bobronium"><img src="https://avatars.githubusercontent.com/u/36469655?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Arseny Boykov</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Bobronium" title="Code">💻</a> <a href="#ideas-Bobronium" title="Ideas, Planning, & Feedback">🤔</a></td>\n      <td align="center"><a href="https://github.com/yudjinn"><img src="https://avatars.githubusercontent.com/u/7493084?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacob Rodgers</b></sub></a><br /><a href="#example-yudjinn" title="Examples">💡</a></td>\n      <td align="center"><a href="https://github.com/danesolberg"><img src="https://avatars.githubusercontent.com/u/25882507?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dane Solberg</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=danesolberg" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/madlad33"><img src="https://avatars.githubusercontent.com/u/54079440?v=4?s=100" width="100px;" alt=""/><br /><sub><b>madlad33</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=madlad33" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="http://matthewtyleraylward.com"><img src="https://avatars.githubusercontent.com/u/19205392?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthew Aylward </b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Butch78" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/Joko013"><img src="https://avatars.githubusercontent.com/u/30841710?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jan Klima</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Joko013" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/i404788"><img src="https://avatars.githubusercontent.com/u/50617709?v=4?s=100" width="100px;" alt=""/><br /><sub><b>C2D</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=i404788" title="Tests">⚠️</a></td>\n      <td align="center"><a href="https://github.com/to-ph"><img src="https://avatars.githubusercontent.com/u/84818322?v=4?s=100" width="100px;" alt=""/><br /><sub><b>to-ph</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=to-ph" title="Code">💻</a></td>\n      <td align="center"><a href="https://imbev.gitlab.io/site"><img src="https://avatars.githubusercontent.com/u/105524473?v=4?s=100" width="100px;" alt=""/><br /><sub><b>imbev</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=imbev" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://git.roboces.dev/catalin"><img src="https://avatars.githubusercontent.com/u/45485069?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cătălin</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=185504a9" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/Seon82"><img src="https://avatars.githubusercontent.com/u/46298009?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Seon82</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Seon82" title="Documentation">📖</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="https://github.com/slavugan"><img src="https://avatars.githubusercontent.com/u/8457612?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Slava</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=slavugan" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/Harry-Lees"><img src="https://avatars.githubusercontent.com/u/52263746?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Harry</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Harry-Lees" title="Code">💻</a> <a href="https://github.com/starlite-api/starlite/commits?author=Harry-Lees" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/cofin"><img src="https://avatars.githubusercontent.com/u/204685?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cody Fincher</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=cofin" title="Code">💻</a> <a href="https://github.com/starlite-api/starlite/commits?author=cofin" title="Documentation">📖</a> <a href="#maintenance-cofin" title="Maintenance">🚧</a></td>\n      <td align="center"><a href="https://www.patreon.com/cclauss"><img src="https://avatars.githubusercontent.com/u/3709715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christian Clauss</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=cclauss" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/josepdaniel"><img src="https://avatars.githubusercontent.com/u/36941460?v=4?s=100" width="100px;" alt=""/><br /><sub><b>josepdaniel</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=josepdaniel" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/devtud"><img src="https://avatars.githubusercontent.com/u/6808024?v=4?s=100" width="100px;" alt=""/><br /><sub><b>devtud</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/issues?q=author%3Adevtud" title="Bug reports">🐛</a></td>\n      <td align="center"><a href="https://github.com/nramos0"><img src="https://avatars.githubusercontent.com/u/35410160?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nicholas Ramos</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=nramos0" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="https://twitter.com/seladb"><img src="https://avatars.githubusercontent.com/u/9059541?v=4?s=100" width="100px;" alt=""/><br /><sub><b>seladb</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=seladb" title="Documentation">📖</a> <a href="https://github.com/starlite-api/starlite/commits?author=seladb" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/aedify-swi"><img src="https://avatars.githubusercontent.com/u/66629131?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Simon Wienhöfer</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=aedify-swi" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/mobiusxs"><img src="https://avatars.githubusercontent.com/u/57055149?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MobiusXS</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=mobiusxs" title="Code">💻</a></td>\n      <td align="center"><a href="http://aidansimard.dev"><img src="https://avatars.githubusercontent.com/u/73361895?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Aidan Simard</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Aidan-Simard" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/waweber"><img src="https://avatars.githubusercontent.com/u/714224?v=4?s=100" width="100px;" alt=""/><br /><sub><b>wweber</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=waweber" title="Code">💻</a></td>\n      <td align="center"><a href="http://scolvin.com"><img src="https://avatars.githubusercontent.com/u/4039449?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Samuel Colvin</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=samuelcolvin" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/toudi"><img src="https://avatars.githubusercontent.com/u/81148?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mateusz Mikołajczyk</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=toudi" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="https://github.com/Alex-CodeLab"><img src="https://avatars.githubusercontent.com/u/1678423?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alex </b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Alex-CodeLab" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/odiseo0"><img src="https://avatars.githubusercontent.com/u/87550035?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Odiseo</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=odiseo0" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/ingjavierpinilla"><img src="https://avatars.githubusercontent.com/u/36714646?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Javier  Pinilla</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=ingjavierpinilla" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/Chaoyingz"><img src="https://avatars.githubusercontent.com/u/32626585?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chaoying</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Chaoyingz" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://github.com/infohash"><img src="https://avatars.githubusercontent.com/u/46137868?v=4?s=100" width="100px;" alt=""/><br /><sub><b>infohash</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=infohash" title="Code">💻</a></td>\n      <td align="center"><a href="https://www.linkedin.com/in/john-ingles/"><img src="https://avatars.githubusercontent.com/u/35442886?v=4?s=100" width="100px;" alt=""/><br /><sub><b>John Ingles</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=john-ingles" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/h0rn3t"><img src="https://avatars.githubusercontent.com/u/1213719?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Eugene</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=h0rn3t" title="Tests">⚠️</a> <a href="https://github.com/starlite-api/starlite/commits?author=h0rn3t" title="Code">💻</a></td>\n    </tr>\n    <tr>\n      <td align="center"><a href="https://github.com/jonadaly"><img src="https://avatars.githubusercontent.com/u/26462826?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jon Daly</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=jonadaly" title="Documentation">📖</a></td>\n      <td align="center"><a href="https://harshallaheri.me/"><img src="https://avatars.githubusercontent.com/u/73422191?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Harshal Laheri</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=Harshal6927" title="Code">💻</a></td>\n      <td align="center"><a href="https://github.com/sorasful"><img src="https://avatars.githubusercontent.com/u/32820423?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Téva KRIEF</b></sub></a><br /><a href="https://github.com/starlite-api/starlite/commits?author=sorasful" title="Code">💻</a></td>\n    </tr>\n  </tbody>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.\nContributions of any kind welcome!\n',
    'author': "Na'aman Hirschfeld",
    'author_email': 'nhirschfeld@gmail.com',
    'maintainer': "Na'aman Hirschfeld",
    'maintainer_email': 'nhirschfeld@gmail.com',
    'url': 'https://github.com/starlite-api/starlite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
