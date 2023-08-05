from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name="CONVERSOR_MOEDA_REAL",
    version="0.0.1",
    author="Evaldo Junior",
    author_email="evaldoazeredoc@gmail.com",
    description="Converte numero em Contábil Real",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=['moeda'],
    python_requires='>=3.8',
)