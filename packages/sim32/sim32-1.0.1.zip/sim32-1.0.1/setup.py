from setuptools import setup


PACKAGE_NAME = 'sim32'
VERSION = "1.0.1"

REQUIRES = ["beautiful_repr==1.1.1", "pygame==2.1.2", "pyoverload==1.1.24"]


with open('README.md') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=PACKAGE_NAME,
    description="Library to help you write games",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version=VERSION,
    url="https://github.com/TheArtur128/SimEngine",
    download_url=f"https://github.com/TheArtur128/SimEngine/archive/refs/tags/{VERSION}.zip",
    author="Arthur",
    author_email="s9339307190@gmail.com",
    install_requires=REQUIRES,
    python_requires='>=3.10',
    packages=[
        PACKAGE_NAME,
        f"{PACKAGE_NAME}.pygame_renders",
        f"{PACKAGE_NAME}.example",
        f"{PACKAGE_NAME}.errors"
    ],
    package_dir={
        PACKAGE_NAME: "simengine",
        f"{PACKAGE_NAME}.pygame_renders": "pygame_renders",
        f"{PACKAGE_NAME}.example": "example",
        f"{PACKAGE_NAME}.errors": "errors"
    }
)
