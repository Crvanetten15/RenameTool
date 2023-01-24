import setuptools

setuptools.setup(
  name="RenameTool",
  version="0.0.1",
  author="Connor Van Etten",
  description="This PyPi is a small command line extension to help rename singular and mulitple files using python",
  py_modules=['yourscript'],
  install_requires=['Click',],
  entry_points={
    'console_scripts': ['renametool = renametool:cli',],
    },
)