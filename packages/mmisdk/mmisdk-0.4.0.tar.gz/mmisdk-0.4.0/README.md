# MMI Custodian SDK (Beta)

Python library to create and submit Ethereum transactions to custodians connected with [MetaMask Institutional](https://metamask.io/institutions); the most trusted DeFi wallet and Web3 gateway for organizations.

> **BETA DISCLAIMER.** By using this library, you acknowledge the technology is still in Beta access and for internal testing purposes only. You are responsible for your use of the Beta access to Open Source SDK and ConsenSys is not responsible for any bugs, deficiencies or issues that may occur.

![Banner](https://image-server-xab.s3.eu-west-1.amazonaws.com/mmisdk-banner.png)

## Contents

-   [Usage](#usage)
    -   [Getting started](#getting-started)
    -   [Supported custodians](#supported-custodians)
-   [Developer documentation](#developer-documentation)
    -   [Requirements](#requirements)
    -   [Installing dependencies](#installing-dependencies)
    -   [Unit tests](#unit-tests)
    -   [Releasing automatically](#releasing-automatically)
    -   [Releasing manually](#releasing-manually)
        -   [Building](#building)
        -   [Publishing to PyPI](#publishing-to-pypi)
-   [Contributing](#contributing)
-   [Changelog](#changelog)

## Usage

Use this SDK to programmatically create Ethereum transactions, and submit them to custodians connected with MetaMask Institutional. Automate trading strategies on your wallets under custody, and still benefit from the institutional-grade security of your favorite qualified custodian and custody provider.

### Getting started

```bash
$ pip install mmisdk
```

```python
>>> from mmisdk import CustodianFactory

>>> factory = CustodianFactory()

>>> custodian = factory.create_for("qredo", "YOUR-TOKEN")

>>> transaction = custodian.create_transaction(qredo_tx_details, tx_params)
>>> custodian.get_transaction(transaction.id)
```

For a complete documentation on how to use the library, visit the page [MetaMask Institutional SDK](https://consensys.gitlab.io/codefi/products/mmi/mmi-sdk-py/sdk-python/), or check the [GitLab repository](https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/blob/main/docs/mkdocs/sdk-python.md).

### Supported custodians

| Custodian       | Supported | As of version | Factory name param  |
| --------------- | --------- | ------------- | ------------------- |
| Bitgo           | ✅        | `0.3.0`       | `"bitgo"`           |
| Bitgo Test      | ✅        | `0.3.0`       | `"bitgo-test"`      |
| Cactus          | ✅        | `0.2.0`       | `"cactus"`          |
| Cactus Dev      | ✅        | `0.2.0`       | `"cactus-dev"`      |
| Gnosis Safe     | ✅        | `0.4.0`       | `"gnosis-safe"`     |
| Gnosis Safe Dev | ✅        | `0.4.0`       | `"gnosis-safe-dev"` |
| Qredo           | ✅        | `0.2.0`       | `"qredo"`           |
| Qredo Dev       | ✅        | `0.1.0`       | `"qredo-dev"`       |
| Saturn          | ✅        | `0.4.0`       | `"saturn"`          |
| Saturn Dev      | ✅        | `0.4.0`       | `"saturn-dev"`      |
| All others      | ❌        |               |                     |

### Running the examples

You can also explore various usage examples in the directory [`./examples`](https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py/-/tree/main/examples).

To run them, first export your custodian's token in the expected environment variable, then run the example file. For instance:

```bash
$ export MMISDK_TOKEN_BITGO_TEST=xxxx
$ python examples/getting_a_transaction_bitgo.py
```

> Note: Each example file expects to find to token under a specific environment variable name, that depends on the custodian and the environment (dev/test/prod) you're addressing. Read each example's code to figure out the right variable.

## Developer documentation

The commands we list below use `python` and `pip`. Depending on your local setup, you might need to replace them by `python3` and `pip3`.

### Requirements

-   Python 3.7 or above

### Installing dependencies

To install `mmisdk`, along with the tools you need to develop and run tests, run the following:

```bash
$ pip install -e .[dev]
```

### Unit tests

Run all unit tests with your default Python version:

```bash
$ pytest src
# or
$ python3.8 -m pytest src # Testing against a specific Python version
```

### End to end tests

A good way to test the library is also to run the various examples scripts.

Copy the file `.env.sample` to `.env`, then replace the values whith your tokens

```bash
$ cp .env.sample .env
```

Then run all examples at once like so:

```bash
$ python e2e/run_examples.py
```

### Releasing automatically

To release a new version, follow these steps:

1. Make sur you're on branch `main`
2. This template provides a basic [bumpversion](https://pypi.org/project/bump2version) configuration. To bump the version, run:

    - `bumpversion patch` to increase version from `1.0.0` to `1.0.1`.
    - `bumpversion minor` to increase version from `1.0.0` to `1.1.0`.
    - `bumpversion major` to increase version from `1.0.0` to `2.0.0`.

    Use [Semantic Versioning 2.0.0](http://semver.org/) standard to bump versions.

3. Push the changes and the tags:

    ```bash
    git push --tags
    ```

### Releasing manually

#### Building

Before building dists make sure you got a clean build area:

```bash
rm -rf build
rm -rf src/*.egg-info
```

Note:

> Dirty `build` or `egg-info` dirs can cause problems: missing or stale files in the resulting dist or strange and confusing errors. Avoid having them around.

Then you should check that you got no packaging issues:

```bash
tox -e check
```

When checking with `tox -e check`, you might receive warnings from `isort` that imports are not properly ordered. To automatically sort your imports with `isort`, run the following:

```bash
pip install isort
isort .
```

To run a complete QA analysis, including unit tests again multiple Python versions, manifest check, and imports order check, run:

```bash
tox
```

And then you can build the `sdist`, and if possible, the `bdist_wheel` too:

```bash
python setup.py clean --all sdist bdist_wheel
```

#### Publishing to PyPI

To make a release of the project on PyPI, assuming you got some distributions in `dist/`, the most simple usage is:

```bash
twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip
```

In ZSH you can use this to upload everything in `dist/` that ain't a linux-specific wheel (you may need `setopt extended_glob`):

```bash
twine upload --skip-existing dist/*.(whl|gz|zip)~dist/*linux*.whl
```

## Contributing

See [CONTRIBUTING.rst](./CONTRIBUTING.rst).

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
