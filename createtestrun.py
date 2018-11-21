"""Script to crete test run in Test Rail

    Args:
            user:               TestRail user
            url:                TestRail server URL
            key:                TestRail API key
            project:            TestRail project
            suite:              TestRail test suite. ''Master'' if ommited
            plan:               TestRail test plan
            run:                The name of TestRail test run that will be created
            d:                  TestRail test run dscription
            configs:            List of dictionaries containing TestRail configurations
                                    Example: -configs [{'Browser':'ie', 'OS':'Windows'},
                                                       {'Browser':'FireFox', 'OS':'Ubuntu'}]
            caseids:            Array of case ids to be included to the new test run
"""

import argparse, pprint, ast
from TRailLibrary import TestRailAdaptor

def main():

    """Crate test run in Test Rail

    """

    parser = argparse.ArgumentParser(description='Create a Test Run in Test Rails',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-user', action='store', dest='tr_user', required=True,
                        help='TestRail user', metavar='\b')
    parser.add_argument('-url', action='store', dest='tr_url', required=True,
                        help='TestRail server URL', metavar='\b')
    parser.add_argument('-key', action='store', dest='tr_key', required=True,
                        help='TestRail API key', metavar='\b')
    parser.add_argument('-project', action='store', dest='project', required=True,
                        help='TestRail project', metavar='\b')
    parser.add_argument('-suite', action='store', dest='test_suite', default='Master',
                        help='TestRail test suite. ''Master'' if ommited', metavar='\b')
    parser.add_argument('-plan', action='store', dest='test_plan', required=True,
                        help='TestRail test plan', metavar='\b')
    parser.add_argument('-run', action='store', dest='test_run', required=True,
                        help='The name of TestRail test run that will be created',
                        metavar='\b')
    parser.add_argument('-d', action='store', dest='run_description', default=None,
                        help='TestRail test run dscription', metavar='\b')
    parser.add_argument('-configs', action='store', dest='configset', required=False,
                        default='[]', help='Optional list of dictionaries containing '
                        'TestRail configurations sets', metavar='\b')
    parser.add_argument('-caseids', action='store', dest='case_ids', required=False,
                        default='[]', help='Optional list of case IDs to be included'
                        'to the test run', metavar='\b')

    args = parser.parse_args()
    pprint.pprint("")
    pprint.pprint("")
    pprint.pprint("Arguments:")
    pprint.pprint("==========")
    pprint.pprint(args._get_kwargs())

    test_rail = TestRailAdaptor(args.tr_url, args.tr_user, args.tr_key)
    test_rail.select_project(args.project)
    test_rail.select_plan(args.test_plan)

    cases = ast.literal_eval(args.case_ids)

    result = test_rail.create_run(args.test_run, args.run_description,
                                  args.test_suite, ast.literal_eval(args.configset),
                                  case_ids=cases)

    pprint.pprint("")
    pprint.pprint("")
    pprint.pprint("Result:")
    pprint.pprint("=======")
    pprint.pprint(result)

if __name__ == "__main__":
    main()
