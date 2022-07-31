# test_bees

> How to run the project?

Given that you have the _python_ installed.

Have the geckodriver installed because UI tests will are run on Firefox.


```console
git clone git@github.com:ralphribeiro/test_bees.git
cd test_bees
```

```console
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
or with poetry

```console
poetry install && poetry shell
```

> To run tests

_From the project root directory_

- Integration: `tox -e integration`
- UI: `tox -e UI`
- To run all teste: `tox`


> Documents

.features files on tests/.../features contains all documentation of tests, as well as in the reports.


> Reports

Reports will be generated in the project root (configured in behave.ini) with the respective suffixes.


