# lt-pytest-project

## Running in a virtualenv without using Docker

Open Terminal.app and create the following environment variables using your LambdaTest credentials:

- LT_USERNAME=your_lambdatest_username
- LT_ACCESS_KEY=your_lambdatest_access_key

Create the virtual environment:
```virtualenv venv```

Activate the virtual environment:
```source venv/bin/activate```

Install the requirements:
```pip install -r requirements.txt```

Run tests in parallel:
```pytest -n 2 test_check_webpage_title.py```