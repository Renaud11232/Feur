import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setuptools.setup(
    name="FeurBot",
    version="0.0.3",
    author="Renaud Gaspard",
    author_email="gaspardrenaud@hotmail.com",
    description="A stupid bot that gives predefined answers to messages matching regex",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Renaud11232/FeurBot",
    packages=setuptools.find_packages(),
    package_data={
        "feur": ["*.json"]
    },
    entry_points={
        "console_scripts": [
            "feur=feur.command_line:main"
        ]
    },
    install_requires=[
        "nextcord>=2.6.0,<3.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)