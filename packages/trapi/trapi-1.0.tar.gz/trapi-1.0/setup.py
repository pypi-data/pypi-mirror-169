from setuptools import setup, find_packages

with open("requirements.txt") as r:
    requirements = r.read().split("\n")
    r.close()


setup(
   name='trapi',
   version='1.0',
   description='Time API Wrapper using Python and WorldTimeAPI.org',
   license="",
   author='NoKodaAddictions',
   author_email='nokodaaddictions@gmail.com',
   url="https://nokodaaddictions.github.io",
   packages=find_packages(),
   install_requires=requirements
)
#2022 NoKodaAddictions