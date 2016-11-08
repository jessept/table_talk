from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='table_talk',
      version='0.1',
      description='Command line chat client',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
      ],
      keywords='kafka api chat',
      url='http://github.com/jessept/table-talk',
      author='Jesse Prestwood-Taylor',
      license='MIT',
      packages=['table_talk'],
      install_requires=[
          'requests',
          'kafka-python'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['table_talk=table_talk.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)