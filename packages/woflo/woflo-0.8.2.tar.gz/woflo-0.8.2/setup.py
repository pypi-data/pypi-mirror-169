# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['woflo', 'woflo.runners', 'woflo.task', 'woflo.util']

package_data = \
{'': ['*']}

install_requires = \
['multiprocess>=0.70.13,<0.71.0']

setup_kwargs = {
    'name': 'woflo',
    'version': '0.8.2',
    'description': 'Python local-first no-bloat task orchestration framework ',
    'long_description': '# woflo\n[![CI](https://github.com/petereon/woflo/actions/workflows/python-test.yml/badge.svg)](https://github.com/petereon/woflo/actions/workflows/python-test.yml)\n[![MyPy Lint](https://github.com/petereon/woflo/actions/workflows/python-lint.yml/badge.svg)](https://github.com/petereon/woflo/actions/workflows/python-lint.yml)\n[![codecov](https://codecov.io/gh/petereon/woflo/branch/master/graph/badge.svg?token=JDAVYDG3ST)](https://codecov.io/gh/petereon/woflo)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=petereon_woflo&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=petereon_woflo)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=petereon_woflo&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=petereon_woflo)\n![PyPI Downloads](https://img.shields.io/pypi/dm/woflo?color=g&label=%F0%9F%93%A5%20Downloads)\n\n## Overview\n\n**woflo** is a Python local-first no-bloat extensible task orchestration framework.\n\nOkay, that\'s a lot of buzz. So what is actually the point?\n\nMain goal is to abstract a lot of functionality related to Task orchestration and execution away while keeping the "API" clear and dead-simple.\n\nCurrently this includes:\n- retries\n- retry timeout\n- parallelism\n- logging\n\n## Installation\n\nTo download from PyPI use:\n\n```shell\npip install woflo\n```\n\nTo install from source:\n\n```shell\ngit clone https://github.com/petereon/woflo.git\ncd woflo\npoetry build\ncd dist\npip install ./woflo-<version>-py3-none-any.whl\n```\n\n## Examples\n\nIntended usage is by utilizing a decorator `@task`, consider a very simple example which would run 10 sleepy workers in parallel without blocking the main thread:\n\n```python\nimport time\nfrom woflo import task\n\n\n@task\ndef sleepy_worker():\n    time.sleep(5)\n    print(\'I am done\')\n\n\nfor _ in range(10):\n    sleepy_task_run = sleepy_worker()\n```\n\nYou can also include retries for tasks that might fail at times. Following would attempt to run the decorated function for 3 times in total with 5 second delay between attempts.\n\n```python\nfrom woflo import task\n\n\n@task(retries=2, retry_sleep_time=5)\ndef fetch_data_from_unstable_api():\n    ...\n```\n\nFurthermore, you can also provide a runner within a `@task` decorator. For example the `SequentialTaskRun` if prefer your tasks to run sequentially and like to wait around a computer a lot. For example:\n\n```python\nfrom woflo import task\nfrom woflo.runners import SequentialTaskRun\n\n\n@task(runner=SequentialTaskRun)\ndef sequential_sleepy_worker():\n    time.sleep(5)\n    print(\'I am done\')\n\n\nfor _ in range(10):\n    sleepy_task_run = sequential_sleepy_worker()\n```\n\nEach `TaskRun` should also expose a few methods that enable you to handle it:\n\n- `.get_result()` to fetch the return value of the finished task \n- `.wait()` to block main thread till the task finishes (irrelevant for `SequentialTaskRun` which will block until it finishes anyway)\n- `.stop()` to stop the task while its running (irrelevant for `SequentialTaskRun` which will block until it finishes anyway)\n- `.is_running()` to check if the task is still running (irrelevant for `SequentialTaskRun` which will block until it finishes anyway)\n\nLet us define an example task:\n\n```python\nimport time\nfrom woflo import task\n\n@task\ndef quick_nap(duration):\n    time.sleep(duration)\n    if duration < 10\n        raise Exception("Ouch oof")\n    else:\n        return \'Well rested\'\n```\n\nAfter you run it,\n\n```python\nnapping = quick_nap(10)\n```\n\nyou can check on it to monitor it\'s state and receive results,\n\n```python\nassert napping.is_running()\n\nnapping.wait()\nassert napping.get_result() == "Well rested"\n```\n\n## Task Runners\n\nIt is designed to be easily extended by developing a\xa0custom `Task` runners. Library itself currently exposes two such runners, `MultiprocessTaskRun` and `SequentialTaskRun`. \n\nAdditionally `woflo` makes available a\xa0`BaseTaskRun`, an interface against which custom runners can be developed.\n\nThe defualt task runner is `MultiprocessTaskRun`, which can run multiple tasks, or even multiple instances of the same task at the same time in parallel in separate Python process.\n\n### MultiprocessTaskRun\n\nThe defualt task runner, which can run multiple tasks, or even multiple instances of the same task at the same time in parallel in separate Python process.\n\nIt offers two modes of operation:\n- `ForkProcess`, which forks a main process and inherits all of its state. Forking is default on Darwin and Linux (it is not available on Windows)\n- `SpawnProcess`, which spawns a new process with same global state\n\nThis behavior can be configured by setting the `process_type`:\n\n```python\nfrom woflo.runners.multiprocess import SpawnProcess, MultiprocessTaskRun\n\nMultiprocessTaskRun.process_type = SpawnProcess\n\n@task(runner=MultiprocessTaskRun)\ndef sleepy_worker():\n    time.sleep(5)\n    print(\'I am done\')\n\n```\n\n## Roadmap\n\n- [x] ~~Setup GitHub Actions, SonarCloud monitoring and Codecov~~\n- [x] ~~Make a PyPI Package~~\n- [ ] Decide on final API and create a version 1.x.x\n- [ ] Implement a Dask runner\n- [ ] Implement a Thread runner\n- [ ] Implement an Async runner\n\n## Known issues\n\n- [x] ~~Processes potentially inherint a large in-memory state in MultiprocessTaskRun~~\n- [ ] `SpawnProcess` running into `OSError: [Errno 9] Bad file descriptor` on `macOS 12.6` when using `multiprocess.sharedctypes.Value` as reflected in [this issue](https://github.com/uqfoundation/multiprocess/issues/115)\n- [ ] Imports need some refactoring\n',
    'author': 'Peter Vyboch',
    'author_email': 'pvyboch1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/petereon/woflo',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.8,<4.0.0',
}


setup(**setup_kwargs)
