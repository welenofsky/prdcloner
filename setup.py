from setuptools import setup

setup(name='prdcloner',
      version='0.1',
      description='Clones Blogvault site to server',
      url='https://github.com/welenofsky/prdcloner',
      author='Justin Welenofsky',
      author_email='welenofsky@gmail.com',
      license='MIT',
      packages=['prdcloner'],
      scripts=['bin/prdcloner'],
      zip_safe=False)
