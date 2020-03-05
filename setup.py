from setuptools import setup

setup(name='focusmode',
      version='0.0.1',
      description='',
      url='https://github.com/lokijuhy/focus-mode',
      packages=['focusmode'],
      python_requires='>3.5.0',
      install_requires=[

      ],
      entry_points = {
              'console_scripts': ['focusmode=focusmode.command_line:main'],
          },
      zip_safe=False)
