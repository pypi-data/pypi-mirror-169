from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="regression_results",
    version="0.0.1",
    author="jefferson",



    long_description_content_type="text/markdown",
    url="https://github.com/jeffersonAsilva/Gera-o-Tech-Unimed-BH_criacao_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3',
)
