# {{ cookiecutter.project_name }}

[![Continous Integration](https://github.com/cmnemoi/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/cmnemoi/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml)

{{ cookiecutter.project_description }}

# Installation

You need to have `curl` and [`uv`](https://docs.astral.sh/uv/getting-started/installation/) installed on your system.

Then run the following command : `curl -sSL https://raw.githubusercontent.com/cmnemoi/{{ cookiecutter.project_slug }}/main/clone-and-install | bash`

# Development

Run tests with `make test`.

# License

The source code of this repository is licensed under the [{{ cookiecutter.project_license }} License](LICENSE).