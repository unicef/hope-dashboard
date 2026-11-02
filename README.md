# HOPE Dashboard


[![Test](https://github.com/unicef/hope-dashboard/actions/workflows/test.yml/badge.svg)](https://github.com/unicef/hope-dashboard/actions/workflows/test.yml)
[![Lint](https://github.com/unicef/hope-dashboard/actions/workflows/lint.yml/badge.svg)](https://github.com/unicef/hope-dashboard/actions/workflows/lint.yml)
[![codecov](https://codecov.io/github/unicef/hope-dashboard/graph/badge.svg?token=FBUB7HML5S)](https://codecov.io/github/unicef/hope-dashboard)
[![Documentation](https://github.com/unicef/hope-dashboard/actions/workflows/docs.yml/badge.svg)](https://unicef.github.io/hope-dashboard/)
[![Pypi](https://badge.fury.io/py/hope-dashboard.svg)](https://badge.fury.io/py/hope-dashboard)
[![Docker Pulls](https://img.shields.io/docker/pulls/unicef/hope-dashboard)](https://hub.docker.com/repository/docker/unicef/hope-dashboard/tags)


## Translations

You can contribute to the Portal translation at https://app.transifex.com/unicef-hope/hope-dashboard/dashboard/


## Contributing

### Requirements

- [uv](https://docs.astral.sh/uv/)
- [direnv](https://direnv.net/)

### Checkout and configure development environment

```shell

    git clone https://github.com/unicef/hope-dashboard.git
    cd hope-dashboard
    uv venv .venv
    uv sync

    ./manage.py env --develop > .envrc  # create initial development configuration
    direnv allow .  # enable enviroment
    createdb hope_dashboard  # create postgres database on localhost

```
