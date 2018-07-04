from setuptools import setup, find_packages

setup(name='faya',
      version='4.1.3',
      description='personal robot',
      author='Yue Minatsuki',
      author_email='yue.official.jp@gmail.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.6',
      ],
      entry_points='''
        [console_scripts]
        faya=faya.__init__:faya
    ''',
      python_requires='>=3.6',
      url='https://github.com/minatsuki-yui/faya',
      license="MIT Licence",
      packages=find_packages(exclude=("main_lib", "data", "core", "bot_platform",)),
      install_requires=["requests", "click"]
      )
