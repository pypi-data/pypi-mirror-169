from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='passbird',
    version='1.0.0',
    license="MIT",
    description="Python Password Generator - Generate strong and secure passwords!",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="jrt345",
    url="https://github.com/jrt345/PassBird",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
            'passbird = passbird.passbird:main'
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
