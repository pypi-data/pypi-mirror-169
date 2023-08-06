from setuptools import setup, find_packages

requirements_file = open("./requirements.txt", "r")
requirements = requirements_file.read().splitlines()

if __name__ == '__main__':
    setup(
        name='QuestionsParser',
        packages=find_packages(),
        version='0.0.2',
        description='A Python library for parsing questions from pdf files',
        author='Andrew Yaroshevych',
        install_requires=requirements,
    )
