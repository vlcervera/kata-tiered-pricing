# Tiered pricing

This project contains the solution of two katas related:

[Tiered Pricing](./definitions/TIERED_PRICING.md) and 
[Graduated Tiered Pricing](./definitions/GRADUATED_TIERED_PRICING.md)

Graduated tiered pricing is an evolution of tiered pricing, so we can implement it in the same
project and offer the possibility to execute both scenarios.

Improvements:

Currently we have duplicated code in both pricing scenarios when we retrieve the correct tier for subscriptions. We can refactor it and search a common code for this part but maybe it has no sense for this point of the exercesise. 
Maybe if we are going to have another pricing scenario and it requires this code we can look to refactor it in a Tiers class that contains the tier pricing configuration and use it but for now we can have this part duplicated.

As consecuence of this duplication, we need to duplicate code in testing of both pricing scenarios to test the incorrect test cases in case of not have tier or have multiple tiers for susbcription 

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
