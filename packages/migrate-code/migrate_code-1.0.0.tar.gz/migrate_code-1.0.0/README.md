# migrate-code

[![PyPI - Version](https://img.shields.io/pypi/v/migrate-code.svg)](https://pypi.org/project/migrate-code)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/migrate-code.svg)](https://pypi.org/project/migrate-code)

______________________________________________________________________

**Table of Contents**

- [migrate-code](#migrate-code)
  - [Links](#links)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
  - [License](#license)

## Links

- [GitLab](https://gitlab.com/bmares/migrate-code)
- [GitHub](https://github.com/maresb/migrate-code)

## Installation

```console
pip install migrate-code
```

## Quickstart

Migration stages will be converted into commits when the upgrade is applied. The `migration.py` file should define a `Migration` variable either called `m` or `migration`.

```file
# migration.py

from migrate_code import Migration, get_repo_root

m = Migration("Demonstrate basic usage")

@m.add_stage(1, "Create a new file")
def stage_1():
    (get_repo_root() / "new_file.txt").write_text("Hello world")


@m.add_stage(2, "Create another file")
def stage_2():
    (get_repo_root() / "another_file.txt").write_text("Hello another world")


@m.add_stage("1.1", "Modify the first file")
def stage_1_1():
    (get_repo_root() / "new_file.txt").write_text("Hello world, again")
```

Now it is easy to create and reset commits:

```console
$ git init
$ git add migration.py
$ git commit -m "Add migration.py"
$ migrate-code log
  ------- (2) Create another file
  ------- (1.1) Modify the first file
  ------- (1) Create a new file
$ migrate-code current
None
$ migrate-code upgrade
Running migration 1: Create a new file
Running migration 1.1: Modify the first file
Running migration 2: Create another file
$ git log --oneline
5041191 (HEAD -> master) Create another file
92012af Modify the first file
d4d0611 Create a new file
78438e2 Add migration.py
$ migrate-code log
* 5041191 (2) Create another file
  92012af (1.1) Modify the first file
  d4d0611 (1) Create a new file
$ migrate-code current
2
$ migrate-code reset
Resetting migration 2: Create another file
Resetting migration 1.1: Modify the first file
Resetting migration 1: Create a new file
$ git log --oneline
78438e2 (HEAD -> master) Add migration.py
$ migrate-code log
  ------- (2) Create another file
  ------- (1.1) Modify the first file
  ------- (1) Create a new file
$ migrate-code upgrade --stage 1.1
Running migration 1: Create a new file
Running migration 1.1: Modify the first file
$ git log --oneline
7b65210 (HEAD -> master) Modify the first file
a7c1027 Create a new file
78438e2 Add migration.py
$ migrate-code log
  ------- (2) Create another file
* 7b65210 (1.1) Modify the first file
  a7c1027 (1) Create a new file
```

## License

`migrate-code` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
