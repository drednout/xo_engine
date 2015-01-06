from setuptools import setup

setup(
    name='xo_engine',
    version='1.0',
    author='Alexei Romanov',
    author_email='drednout.by@gmail.com',
    description = ("Simple game engine for XO game"),
    license="GPLv2",
    keywords="game engine xo",
    url="https://github.com/drednout/xo_engine",
    packages=['xo_engine'],
    long_description=open('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment :: Board Games",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    #install_requires = ['docutils>=0.3'],
)
