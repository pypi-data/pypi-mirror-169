from setuptools import setup, find_packages

version = '0.2.0'

packages = find_packages()


setup(
    name='django-nearly-solid',
    version=version,
    include_package_data=True,
    zip_safe=False,
    packages=packages,
    requires=[
        'django',
        'pydantic',
    ]
)
