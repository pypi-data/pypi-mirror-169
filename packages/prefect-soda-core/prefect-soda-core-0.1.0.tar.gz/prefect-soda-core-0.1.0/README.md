# prefect-soda-core

## Welcome!

Prefect 2.0 collection for Soda Core

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-soda-core` with `pip`:

```bash
pip install prefect-soda-core
```

### Write and run a flow

```python
from prefect import flow
from prefect_soda_core.soda_configuration import SodaConfiguration
from prefect_soda_core.sodacl_check import SodaCLCheck
from prefect_soda_core.tasks import soda_scan_execute


@flow
def run_soda_scan():
    soda_configuration_block = SodaConfiguration(
        configuration_yaml_path="/path/to/config.yaml"
    )
    sodacl_check_block = SodaCLCheck(
        sodacl_yaml_path="/path/to/checks.yaml"
    )
    
    return soda_scan_execute(
        data_source_name="my_datasource",
        configuration=soda_configuration_block,
        checks=soda_check_block,
        variables={"var": "value"},
        verbose=True
    )

run_soda_scan()
```

## Resources

If you encounter any bugs while using `prefect-soda-core`, feel free to open an issue in the [prefect-soda-core](https://github.com/sodadata/prefect-soda-core) repository.

If you have any questions or issues while using `prefect-soda-core`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-soda-core` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/sodadata/prefect-soda-core.git

cd prefect-soda-core/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
