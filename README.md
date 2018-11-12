# RobotFramework TRailLibrary

## Description

[Robot Framework](http://www.robotframework.org) listener library that provides a simple way to log test results to [TestRail](http://www.gurock.com/testrail/) test case management system

## Installation

```
pip install git+https://github.com/gennadii-borodin/robotframework-traillibrary.git
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

## Usage with CI systems

Test run should exist before the library can log result to Test Rail.
`createtestrun.py` script can be used to create a test run from a CI system.
The script can create test run with multiple configurations at a time.

### Script usage

```
python createtestrun.py -user user@domain.com -url https://server -key test_rail_api_key_here -project "Project" -plan "Continous Testing" -run "Run Name" -d "Plan description" -configs "[{'Browser':'FireFox', 'OS':'Ubuntu'}, {'Browser':'IE', 'OS':'Windows'}]" -caseids [1, 2, 3, 10, 100]
```
