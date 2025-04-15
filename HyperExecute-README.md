# Running Tests with HyperExecute

This guide explains how to run the pytest Selenium tests using LambdaTest's HyperExecute platform.

## Prerequisites

1. Install the HyperExecute CLI:
   ```
   # For macOS/Linux
   curl -O https://downloads.lambdatest.com/hyperexecute/darwin/hyperexecute
   chmod +x hyperexecute
   
   # For Windows
   curl -O https://downloads.lambdatest.com/hyperexecute/windows/hyperexecute.exe
   ```

2. Set up your LambdaTest credentials as environment variables:
   ```
   # For macOS/Linux
   export LT_USERNAME=your_lambdatest_username
   export LT_ACCESS_KEY=your_lambdatest_access_key
   
   # For Windows
   set LT_USERNAME=your_lambdatest_username
   set LT_ACCESS_KEY=your_lambdatest_access_key
   ```

## Running Tests

1. Navigate to the project directory:
   ```
   cd /path/to/lt-pytest-project
   ```

2. Run tests using the HyperExecute CLI:
   ```
   # For macOS/Linux
   ./hyperexecute --config hyperexecute.yaml
   
   # For Windows
   hyperexecute.exe --config hyperexecute.yaml
   ```

## HyperExecute YAML Configuration

The `hyperexecute.yaml` file contains the following key configurations:

- **runson**: Specifies the platform to run tests on (Windows)
- **concurrency**: Sets the number of parallel test executions (2)
- **testDiscovery**: Configures how tests are discovered
- **testRunnerCommand**: Defines how tests are executed
- **browserCapabilities**: Configures the browser settings for tests
- **uploadArtefacts**: Specifies which test artifacts to upload

## Benefits of HyperExecute

- **Faster Execution**: Tests run in parallel, reducing overall execution time
- **Smart Test Distribution**: Automatically splits tests for optimal execution
- **Detailed Reporting**: Comprehensive test reports with screenshots and videos
- **Secure Environment**: Encrypted test execution and secure cloud storage
- **Reduced Flakiness**: Retry mechanism for failed tests

## Troubleshooting

If you encounter any issues:

1. Verify your LambdaTest credentials are set correctly
2. Ensure the HyperExecute CLI is installed properly
3. Check the HyperExecute YAML file for any syntax errors
4. Review the test logs for specific error messages

For more information, visit the [HyperExecute Documentation](https://www.lambdatest.com/support/docs/hyperexecute-cli-run-tests-on-hyperexecute-grid/).
