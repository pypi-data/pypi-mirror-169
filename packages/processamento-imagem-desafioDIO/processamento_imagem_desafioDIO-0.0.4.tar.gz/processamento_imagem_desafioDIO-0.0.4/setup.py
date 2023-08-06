from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_imagem_desafioDIO",
    version="0.0.4",
    author="Rafael Morais",
    author_email="ra.fa.morais@hotmail.com",
    description="Pacote para processamento de imagens.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelbmorais/processamento-de-imagem-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)