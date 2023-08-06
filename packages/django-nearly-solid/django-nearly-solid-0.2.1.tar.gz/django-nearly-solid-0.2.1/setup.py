from setuptools import setup, find_packages

version = '0.2.1'

packages = find_packages()

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-nearly-solid',
    version=version,
    author="Artem Romanukov",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=packages,
    requires=[
        'django',
        'pydantic',
    ]
)
