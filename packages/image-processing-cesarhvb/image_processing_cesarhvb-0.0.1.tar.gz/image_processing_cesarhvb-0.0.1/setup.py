from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "image_processing_cesarhvb",
    version = "0.0.1",
    author = "César Henrique",
    author_email = "cesaarhvb@gmail.com",
    description = "Image processing package",
    long_description = page_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/cesarhenrq/Python/tree/main/image-processing-cesarhvb-package",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.8',
)