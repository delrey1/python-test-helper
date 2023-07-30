from setuptools import setup, find_packages  # noqa: H301

requires = [
    'setuptools >= 21.0.0',
    'requests >= 2.28.2',
    'pydantic',
    'pyJWT'
]

readme = open('README.md').read()

NAME = "python_test_helper"

setup(
    name=NAME,
    version='0.0.2',
    description="Simple Methods to help you in your tests",
    keywords=["python"],
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requires,
    packages=find_packages(exclude=('tests*',)),
    test_suite='tests',
    python_requires='>=3.7',
    include_package_data=True,
    url="https://github.com/delrey1/python-test-helper",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ])
