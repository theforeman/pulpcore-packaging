import pathlib
from setuptools import setup

setup(
    name="tomli",
    version="@@VERSION@@",
    description="A lil' TOML parser",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=["tomli"],
    package_dir={'':'src'},
    package_data={"tomli": ["py.typed"]},
    python_requires=">=3.6",
    author="Taneli Hukkinen",
    author_email="hukkin@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    keywords=["toml"],
    project_urls={
        "Homepage": "https://github.com/hukkin/tomli",
        "Changelog": "https://github.com/hukkin/tomli/blob/master/CHANGELOG.md",
    },
)
