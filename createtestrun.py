"""Script to crete test run in Test Rail

    Args:
            project:            TestRail project
            test_suite:         TestRail test suite. ''Master'' if ommited
            test_plan:          TestRail test plan
            test_run:           The name of TestRail test run that will be created
            run_description:    TestRail test run dscription
            configset:          Lisr of dictionaries containing TestRail configurations set.
                                Example: [{'Browser':'ie', 'OS':'Windows'},
                                            {'Browser':'FireFox', 'OS':'Ubuntu'}]
            tr_user:            TestRail user
            tr_url:             TestRail server URL
            tr_key:             TestRail API key


"""

import argparse, pprint, ast
from TRailLibrary import TestRailAdaptor

def main():

    """Crate test run in Test Rail

    """

    parser = argparse.ArgumentParser(description='Create a Test Run in Test Rails')
    parser.add_argument('-pr', action='store', dest='project', required=True,
                        help='TestRail project')
    parser.add_argument('-su', action='store', dest='test_suite', default='Master',
                        help='TestRail test suite. ''Master'' if ommited')
    parser.add_argument('-pl', action='store', dest='test_plan', required=True,
                        help='TestRail test plan')
    parser.add_argument('-tr', action='store', dest='test_run', required=True,
                        help='The name of TestRail test run that will be created')
    parser.add_argument('-rd', action='store', dest='run_description', default=None,
                        help='TestRail test run dscription')
    parser.add_argument('-cset', action='append', dest='configset', required=True,
                        help='TestRail configurations set.')
    parser.add_argument('-us', action='store', dest='tr_user', required=True,
                        help='TestRail user')
    parser.add_argument('-ul', action='store', dest='tr_url', required=True,
                        help='TestRail server URL')
    parser.add_argument('-ak', action='store', dest='tr_key', required=True,
                        help='TestRail API key')
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
