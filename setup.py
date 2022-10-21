from setuptools import setup, find_packages


with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.2",
    author="Lucas Oliveira de Borba",
    author_email="lucas_borba@outlook.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="git remote add origin https://github.com/oliverborba/DIO_image_processing.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)