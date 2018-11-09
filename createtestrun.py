"""Script to crete test run in Test Rail

    Args:
            project:            TestRail project
            suite:              TestRail test suite. ''Master'' if ommited
            plan:               TestRail test plan
            run:                The name of TestRail test run that will be created
            d:                  TestRail test run dscription
            configs:            List of dictionaries containing TestRail configurations
                                    Example: -configs [{'Browser':'ie', 'OS':'Windows'},
                                                       {'Browser':'FireFox', 'OS':'Ubuntu'}]
            user:               TestRail user
            url:                TestRail server URL
            key:                TestRail API key
"""

import argparse, pprint, ast
from TRailLibrary import TestRailAdaptor

def main():

    """Crate test run in Test Rail

    """

    parser = argparse.ArgumentParser(description='Create a Test Run in Test Rails')
    parser.add_argument('-user', action='store', dest='tr_user', required=True,
                        help='TestRail user')
    parser.add_argument('-url', action='store', dest='tr_url', required=True,
                        help='TestRail server URL')
    parser.add_argument('-key', action='store', dest='tr_key', required=True,
                        help='TestRail API key')
    parser.add_argument('-project', action='store', dest='project', required=True,
                        help='TestRail project')
    parser.add_argument('-suite', action='store', dest='test_suite', default='Master',
                        help='TestRail test suite. ''Master'' if ommited')
    parser.add_argument('-plan', action='store', dest='test_plan', required=True,
                        help='TestRail test plan')
    parser.add_argument('-run', action='store', dest='test_run', required=True,
                        help='The name of TestRail test run that will be created')
    parser.add_argument('-d', action='store', dest='run_description', default=None,
                        help='TestRail test run dscription')
    parser.add_argument('-configs', action='store', dest='configset', required=True,
                        help='List of dictionaries containing TestRail configurations sets')
    
    args = parser.parse_args()
    pprint.pprint("")
    pprint.pprint("")
    pprint.pprint("Arguments:")
    pprint.pprint("==========")
    pprint.pprint(args._get_kwargs())

    test_rail = TestRailAdaptor(args.tr_url, args.tr_user, args.tr_key)
    test_rail.select_project(args.project)
    test_rail.select_plan(args.test_plan)
    result = test_rail.create_run(args.test_run, args.run_description,
                                  args.test_suite, ast.literal_eval(args.configset))

    pprint.pprint("")
    pprint.pprint("")
    pprint.pprint("Result:")
    pprint.pprint("=======")
    pprint.pprint(result)

if __name__ == "__main__":
    main()
