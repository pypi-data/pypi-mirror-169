## How to create a new python project with projen

1. run `pj new python --name=kaito_model` (`pj` is an alias for `npx projen`)
2. configure `.projenrc.py` by adding below

   ```python
    project = PythonProject(
        ...
        homepage="",
        license=None,
        project_type=ProjectType.LIB, # or ProjectType.APP if this is not a library
        pip=False,
        venv=False,
        setuptools=False,
        poetry=True,
        poetry_options={
            "repository": "https://github.com/MetaSearch-IO/KaitoModelPython.git",
        },
        deps=[
            "python@^3.9",
        ],
    )
   ```

   Note that python dependency is required by [poetry](https://python-poetry.org/docs/) and the version should be at least 3.7

3. increase the version in `.projenrc.py` if necessary.
4. setup the poetry environment by running `poetry env use <PATH_TO_PROJECT>/.env/bin/python3.9` (or your desired python version)
   1. see [poetry docs](https://python-poetry.org/docs/configuration#local-configuration) for the exact env path.
   2. you may also need to change the IDE interpreter to the same path, otherwise the IDE will not be able to find the dependencies.
5. run `pj build` to install dependencies and generate artifacts.
6. if not already, setup pypi main token by `poetry config pypi-token.pypi <main-token>`, find main token in [notion doc](https://www.notion.so/kaitoai/Use-Projen-to-manage-Python-project-ced223f610384a598c96c919fd94a69e)
7. run `pj publish` to upload a new version to [pypi](https://pypi.org/).

## How to adopt projen to an existing python project

1. run `pj new python`, the script will recognize your project name and create a `.projenrc.py` file.
2. delete the content inside the newly created `<project-name>` folder, move content from `src` (or other folder name with existing source files) to `<project-name>`, and delete the `src` folder. Move the test files to `<project-name>/tests` as well.
   1. you may want to change the `module_name` in `.projenrc.py`, note that only lowercase letters and underscores are allowed.
3. refer to [How to create a new python project with projen](#how-to-create-a-new-python-project-with-projen) step 2 till the end, configure the `.projenrc.py` file.
4. additionally, you need to base on the existing `setup.cfg` (or `requirements.txt`), add the dependencies to `.projenrc.py` file. Then delete the `setup.cfg` (or `requirements.txt`) file.


## How to automate the release process

1. create a project specific [pypi token](https://pypi.org/manage/account/) with `repo` scope, and add it to the github secrets as `PYPI_API_TOKEN`. Or ask your admin to do it for you.
2.

## Bonus

### How to enforce pre commit actions (for any language)

1. install [pre-commit](https://pre-commit.com) and add pre-commit to deps list.
2. create a pre-commit configuration file `.pre-commit-config.yaml` similar to below

   ```yaml
   # See https://pre-commit.com for more information
   # See https://pre-commit.com/hooks.html for more hooks
   repos:
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v3.2.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
           exclude: ^\.* # Most dot files managed by projen and are read only
         - id: check-yaml
         - id: check-added-large-files
   ```

3. run `pre-commit install`
4. (optional) run `pre-commit autoupdate` to update hooks to the latest version

### How to run github actions locally

1. install [act](https://github.com/nektos/act)
2. (optional) create an act environment variables fle `.actenv` with extra env variables, some examples could be

   ```bash
   GITHUB_TOKEN=<your-github-token>
   PYPI_API_TOKEN=<your-pypi-token>
   ```

   Note that act will try to load file `.env` as environment variables, but it will not work because `.env` now it's a virtual environment folder managed by projen. So we need to create a new file.

3. run `act --env-file .actenv` to run the github actions locally.
   1. the first time run `act` will let you choose default image, you should choose at least __Medium__ image.
   2. make an alias for this command for easier use `alias act='act --env-file .actenv'`

### TODO: Run `projen` as pre-commit hook to ensure the project is up to date

### TODO: Auto bump the version number
