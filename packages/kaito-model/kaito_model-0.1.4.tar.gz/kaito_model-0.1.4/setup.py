# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kaito_model',
 'kaito_model.discord',
 'kaito_model.mapper',
 'kaito_model.pynamo',
 'kaito_model.pynamo.discord']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.0,<0.6.0', 'pynamodb>=5.2.1,<6.0.0']

setup_kwargs = {
    'name': 'kaito-model',
    'version': '0.1.4',
    'description': '',
    'long_description': '## How to create a new python project with projen\n\n1. run `pj new python --name=kaito_model` (`pj` is an alias for `npx projen`)\n2. configure `.projenrc.py` by adding below\n\n   ```python\n    project = PythonProject(\n        ...\n        homepage="",\n        license=None,\n        project_type=ProjectType.LIB, # or ProjectType.APP if this is not a library\n        pip=False,\n        venv=False,\n        setuptools=False,\n        poetry=True,\n        poetry_options={\n            "repository": "https://github.com/MetaSearch-IO/KaitoModelPython.git",\n        },\n        deps=[\n            "python@^3.9",\n        ],\n    )\n   ```\n\n   Note that python dependency is required by [poetry](https://python-poetry.org/docs/) and the version should be at least 3.7\n\n3. increase the version in `.projenrc.py` if necessary.\n4. setup the poetry environment by running `poetry env use <PATH_TO_PROJECT>/.env/bin/python3.9` (or your desired python version)\n   1. see [poetry docs](https://python-poetry.org/docs/configuration#local-configuration) for the exact env path.\n   2. you may also need to change the IDE interpreter to the same path, otherwise the IDE will not be able to find the dependencies.\n5. run `pj build` to install dependencies and generate artifacts.\n6. if not already, setup pypi main token by `poetry config pypi-token.pypi <main-token>`, find main token in [notion doc](https://www.notion.so/kaitoai/Use-Projen-to-manage-Python-project-ced223f610384a598c96c919fd94a69e)\n7. run `pj publish` to upload a new version to [pypi](https://pypi.org/).\n\n## How to adopt projen to an existing python project\n\n1. run `pj new python`, the script will recognize your project name and create a `.projenrc.py` file.\n2. delete the content inside the newly created `<project-name>` folder, move content from `src` (or other folder name with existing source files) to `<project-name>`, and delete the `src` folder. Move the test files to `<project-name>/tests` as well.\n   1. you may want to change the `module_name` in `.projenrc.py`, note that only lowercase letters and underscores are allowed.\n3. refer to [How to create a new python project with projen](#how-to-create-a-new-python-project-with-projen) step 2 till the end, configure the `.projenrc.py` file.\n4. additionally, you need to base on the existing `setup.cfg` (or `requirements.txt`), add the dependencies to `.projenrc.py` file. Then delete the `setup.cfg` (or `requirements.txt`) file.\n\n\n## How to automate the release process\n\n1. create a project specific [pypi token](https://pypi.org/manage/account/) with `repo` scope, and add it to the github secrets as `PYPI_API_TOKEN`. Or ask your admin to do it for you.\n2.\n\n## Bonus\n\n### How to enforce pre commit actions (for any language)\n\n1. install [pre-commit](https://pre-commit.com) and add pre-commit to deps list.\n2. create a pre-commit configuration file `.pre-commit-config.yaml` similar to below\n\n   ```yaml\n   # See https://pre-commit.com for more information\n   # See https://pre-commit.com/hooks.html for more hooks\n   repos:\n     - repo: https://github.com/pre-commit/pre-commit-hooks\n       rev: v3.2.0\n       hooks:\n         - id: trailing-whitespace\n         - id: end-of-file-fixer\n           exclude: ^\\.* # Most dot files managed by projen and are read only\n         - id: check-yaml\n         - id: check-added-large-files\n   ```\n\n3. run `pre-commit install`\n4. (optional) run `pre-commit autoupdate` to update hooks to the latest version\n\n### How to run github actions locally\n\n1. install [act](https://github.com/nektos/act)\n2. (optional) create an act environment variables fle `.actenv` with extra env variables, some examples could be\n\n   ```bash\n   GITHUB_TOKEN=<your-github-token>\n   PYPI_API_TOKEN=<your-pypi-token>\n   ```\n\n   Note that act will try to load file `.env` as environment variables, but it will not work because `.env` now it\'s a virtual environment folder managed by projen. So we need to create a new file.\n\n3. run `act --env-file .actenv` to run the github actions locally.\n   1. the first time run `act` will let you choose default image, you should choose at least __Medium__ image.\n   2. make an alias for this command for easier use `alias act=\'act --env-file .actenv\'`\n\n### TODO: Run `projen` as pre-commit hook to ensure the project is up to date\n\n### TODO: Auto bump the version number\n',
    'author': 'kaito-hao',
    'author_email': 'anya@kaito.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MetaSearch-IO/KaitoModelPython',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
