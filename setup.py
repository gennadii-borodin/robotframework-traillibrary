"""
    ``TRailLibrary`` is a Robot Framework listener library that allows to log test execution results
    to an instanse of Test Rail https://www.gurock.com/testrail Test Case management system

    After the library is imported it starts to listen test execution. When test is finished
    the libray finds the test tags that contain case ids and sends result to corresponding
    cases in Test Rail

    ``TRailLibrary`` sends to Test Rail the following information:
    - test status ``PASS`` or ``FAIL``
    - ``elapsedtime`` in seconds
    - ``path`` longname of the test in Robot Framework suite
    - ``tags`` all test case tags
    - ``message`` test result message


    = Linking test cases =

    Test cases linked throug special Robot Framework tags. Listener finds all tags that match
    the following regexp

    ``prefix(\d{0,}\d$)``

    where ``prefix`` is value of the appropriate `Importing` argument

    = Configurations =
    Test Rails configuration, if used, is passed as a dictionary
    by ``config`` `Importing` argumenet.\n
    Keys are names of Test Rail configuration groups\n
    Values are names of configurations

    | ``{'OS':'Windows', 'Browser':'Chrome'}``


    = Examples =

    In the following example execution result will be assined to case with id ``C1``
    in appropriate ``run_name``

    | ***** Test Cases *****
    | *Test With Test Rail tag*
    |    [Tags]    C1    dummy    owner-johndoe
    |    Log    Hello, world!

    If multiple tags specified all matched cases will receive test result

    | [Tags]    C1    C2    C3    dummy    owner-johndoe

    C1, C2 and C3 accordingly

"""


from setuptools import setup, find_packages

setup(name='robotframework-traillibrary',
      version='0.1',
      description='Robot Framework listener library that provides a simple '
      'way to log test results to TestRail test case management system',
      long_description=__doc__,
      author='Gennady Borodin',
      author_email='',
      license='MIT',
      url='https://github.com/gennadii-borodin/robotframework-traillibrary',
      install_requires=[
          'robotframework >= 3.0.0',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Framework :: Robot Framework :: Library',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Testing :: Acceptance',
          'Topic :: Software Development :: Testing :: BDD',
      ],
      #py_modules = ['TRailLibrary', 'test_rail_adaptor', 'testrail' ],
      package_dir={'': 'src'},
      packages=find_packages('src')
     )

__author__ = 'Gennady Borodin'
