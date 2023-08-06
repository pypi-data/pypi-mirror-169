from setuptools import setup

from setuptools import find_packages

 

#with open('README.md') asf:

#readme = f.read()

 

from pathlib import Path

this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

 

setup(

  name='HugoFILE',

  version='1.0.0',

  #long_description=readme,

  long_description=long_description,

  long_description_content_type='text/markdown',

  author='HUGO',

  author_email='hugo.casella@isen.yncrea.fr',

  url='https://github.com/HugoCsa7/M1-2022-git-workflow',

  packages=find_packages(),

  entry_points={

    'console_script':[

      'hello-world-cli = M1_2022_git_workflow.main:say_hello',

    ],

  },

)
