# Tiered pricing

This project contains the solution of two katas related:

[Tiered Pricing](./definitions/TIERED_PRICING.md) and 
[Graduated Tiered Pricing](./definitions/GRADUATED_TIERED_PRICING.md)

Graduated tiered pricing is an evolution of tiered pricing, so we can implement it in the same
project and offer the possibility to execute both scenarios.

Improvements:
- Duplicated code to check the tiers for susbcriptions and the management of exceptions
- Duplicated test for the code mentioned above
- Most probably we can refactor this part in a Tiers object that contains the tiers available and methods to get the tier for each subscription and manage the exceptions on it
## Python version

This project uses Python 3.9. You can use pyenv to configure your environment.

```
https://github.com/pyenv/pyenv#installation
```

## Install
You can install all dependencies required for this project using:
````shell
make install
````

## Run tiered pricing
You can run Tiered pricing application using:
```shell
make run-tiered
```
## Run graduated tiered pricing
You can run Graduated Tiered pricing application using:
```shell
make run-graduated
```

## Linter
You can apply linter and format tools using:
````shell
make lint
````

## Format
You can apply format tools isolated from linter in case of linter fails using:
````shell
make format
````

## Pre push
You can install pre-push hook :
````shell
make pre-push
````

## Test
You can run the test suite using:
````shell
make test
````
