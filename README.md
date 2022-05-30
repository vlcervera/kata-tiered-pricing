# Tiered pricing

This project contains the result of two katas in the same code:

[Tiered Pricing](./definitions/TIERED_PRICING.md) and 
[Graduated Tiered Pricing](./definitions/GRADUATED_TIERED_PRICING.md)

Graduated tiered pricing is an evolution of tiered pricing, so we can implement it in the same
project and offer the possibility to execute both scenarios.

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

## Run
You can run Tiered pricing application using:
```shell
make run
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

## Test
You can run the test suite using:
````shell
make test
````
