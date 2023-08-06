[![PyPI](https://img.shields.io/pypi/v/poetry-lock-groups-plugin)](https://pypi.org/project/poetry-lock-groups-plugin/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-lock-groups-plugin)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/poetry-lock-groups-plugin)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/mit)

`poetry-lock-groups-plugin` is a lightweight plugin which enables Poetry's [dependency group](https://python-poetry.org/docs/managing-dependencies/#dependency-groups) options (`--with`, `--without`, `--only`) when executing the `lock` command.  Broadly, this plugin helps enable a solution pattern that developers may use when working with and releasing packages within a more complex Python monorepo environment that relies on path-based dependencies.


## Installation

Execute the following command:
```shell
poetry self add poetry-lock-groups-plugin
```

## Use Case

When working within a Python monorepo project structure with [local path dependencies](https://python-poetry.org/docs/dependency-specification/#path-dependencies), a frequently encountered challenge involves publishing these packages to a PyPI index in a way that can be easily utilized by downstream consumers.  Specifically, while editable path dependencies work well to support normal development activities, publishing a package with local path dependencies into a usable `sdist` or `wheel` archive typically involves replacing those path dependencies with references to packages that are resolvable within a PyPI repository.

In order to support this scenario, rather than maintaining two distinct versions of `pyproject.toml` (one with local path dependencies and the other with PyPI resolvable dependencies), developers may leverage dependency groups. Vanilla Poetry recognizes dependency groups only at the `install` phase - by advancing that recognition to the `lock` stage, we enable predictable, flexible patterns to support monorepo development.

## Example

Given the following `pyproject.toml` where `my-poetry-project` depends on `common-library` within the same monorepo project structure:
```toml
[tool.poetry]
name = "my-poetry-project"
version = "0.1.0.dev"
description = ""

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.plugins."poetry.application.plugin"]
lock-groups-plugin = "poetry_lock_groups.plugin:LockGroupsPlugin"

[tool.poetry.group.remote.dependencies]
common-library = "^1.2.6"

[tool.poetry.group.local.dependencies]
common-library = {path = "../../common-library/"}

[build-system]
requires = ["poetry-core>=1.2"]
build-backend = "poetry.core.masonry.api"
```

By running the following command:

```shell
poetry lock --with remote --without local
```

This will generate a `poetry.lock` file that includes the dependency definitions within the `remote` group, but without those in the `local` group.  Note that if we included both groups, or simply refrained from specifying group usages, we would see behavior 
identical to that in vanilla Poetry, which is, in this case, undefined. 

Developers will typically execute the following commands as a part of their development workflow while building/testing functionality:
```shell
poetry lock --with local --without remote
poetry install --with local --without remote
```
However, when performing releases, developers will execute the following to ensure that local path dependencies are removed from archives that are published to the configured PyPI repository:
```shell
poetry lock --with remote --without local
poetry install --with remote --without local
```

Consider using [Habushu](https://bitbucket.org/cpointe/habushu/) to codify and automate this workflow!

### Usage Considerations 

Note that the following sequence of commands may fail:
```shell
poetry lock --without local
poetry install --with local
```
This is because the `poetry install` command searches `poetry.lock` to install dependencies. By building the lock file without the `local` group, any dependencies that exist only within that group will have no known sources, rendering them unresolvable.

`poetry-lock-groups-plugin` **only** modifies lock operations initiated via the `lock` command.  It makes no attempt to modify behavior resulting from an implied lock, such as when running `poetry install` without having already created a lock file.

### Alternative Approaches

Instead of using dependency groups as described above to capture local path dependencies in a monorepo project, developers may consider using the [poetry-stickywheel-plugin](https://pypi.org/project/poetry-stickywheel-plugin/) or other similar approach to dynamically re-write `pyproject.toml` on archive deployment with local path dependency declarations appropriately replaced. 

## Releasing to PyPI

Releasing `poetry-lock-groups-plugin` leverages the `maven-release-plugin` to automate release preparation and delegates to the [habushu-maven-plugin](https://bitbucket.org/cpointe/habushu) to publish the package to PyPI during the `deploy` phase.  A [PyPI account](https://pypi.org/account/register/) with access to the [poetry-lock-groups-plugin](https://pypi.org/project/poetry-lock-groups-plugin/) project is required. PyPI account credentials should be specified in your `settings.xml` under the `<id>pypi</id>` `<server>` entry:

```xml
<settings>
  <servers>
    <server>
      <id>pypi</id>
      <username>pypi-username</username>
      <password>pypi-password</password>
    </server>
  </servers>
</settings>
```
