# RobotFramework TRailLibrary

## Description

[Robot Framework](http://www.robotframework.org) listener library that provides a simple way to log test results to [TestRail](http://www.gurock.com/testrail/) test case management system

## Installation

```python
python setup.py install
```

## Documentation

See library documentation on [GitHub](https://github.com/gennadii-borodin/robotframework-traillibrary/tree/master/docs)

## Library Usage

1. Import TRailLibrary

   ```robot
   *** Settings ***
   Library    TRailLibrary    url=http:\\server    user=user@domain.com    api_key=key_here    project=My Project    plan=Test Plan    run_name=MyDailyRun    config={'OS':'Windows', 'Browser':'Chrome'}    prefix=C

   ```

2. Mark Robot Framework tests with tag containing Test Rail case ID. Case IDs can be found in Test Rail UI. They looks like the follofing C# (e.g. C17).

3. If multiple tags specified then all corresponding test cases in Test Rail will receive results.

## Examples

### Single tag example

   ```robot
   *** Test Cases ***
   Test With Test Rail tag
       [Tags]    C1    dummy    owner-johndoe
       Log    Hello, world!
   ```

### Multiple tags example

```robot
   *** Test Cases ***
   Test With Test Rail tag
       [Tags]    C1    C2    C45233    dummy    owner-johndoe
       Log    Hello, world!
   ```
