# digit-dog-ceo-test

automated checks for https://dog.ceo/dog-api/documentation/breed

## Requirements

The following libs/tools versions have been in use:
- `Python 3.8.3`
- `pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip`

## How to run

Currently (locally on my MacOSX machine):
```
sudo python3 -m pip install pylint
sudo python3 -m pip install questions-three
sudo python3 src/skeleton_suite.py

# to run the linter, use:
sudo python3 -m pylint src/skeleton_suite.py

```

Notes: TODO - fix the "ugly" need for sudo. I'm having trouble with the python envs locally - I'll need to figure out a proper setup, but right now using sudo is the only way it works.

Ideally it should work with:

```
pip install pylint
pip install questions-three
python src/skeleton_suite.py
```

## How to run the whole suite of automated checks

To run all checks:
```
sudo python3 -m questions_three.ci.run_all src/test
```

To run all checks in parallel "threads":
```
sudo MAX_PARALLEL_SUITES=4 python3 -m questions_three.ci.run_all src/test
````

## Reports

Reports can be found in `reports/` after execution.

## Exercise approach and test notes

Gonna split up workflow in following fashion - 30 mins coming up with a working skeleton that will do a request to the API and check the response; 15 mins thinking of scenarios interesting to check across the whole API; remainder of the time coding away automated checks.

In the interest of time I'll be using the following library: [questions-three](https://github.com/CyberGRX/questions-three) it has a fair ammount of useful code so I can avoid a more direct approach which would take me a bit more time like for example the one described [here](https://medium.com/@peter.jp.xie/rest-api-testing-using-python-751022c364b8).

Also going to try and use some sort of linter, like [pylint](https://pylint.org/), to keep to code slightly structured.