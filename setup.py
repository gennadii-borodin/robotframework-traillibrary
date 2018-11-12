"""
    Robot Framework listener library setup module

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
