from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='VisageScript',
    version='0.0.1',
    packages=['VisageScript'],
    url='https://github.com/PythonApkDev/PythonApkDev.github.io/tree/main/advanced-projects/VisageScript',
    license='MIT',
    author='PythonApkDev',
    author_email='pythonapkdev2022@gmail.com',
    description='This package contains implementation of VisageScript programming language.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "VisageScript=VisageScript.VisageScript:main",
        ]
    }
)