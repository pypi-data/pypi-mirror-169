from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="DZDNeo4jTools",
    description="Tool collection from the DZD Devs for working with a Neo4j Graph Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.connect.dzd-ev.de/dzdpythonmodules/neo4j-tools",
    author="Tim Bleimehl",
    author_email="tim.bleimehl@helmholtz-muenchen.de",
    license="MIT",
    packages=["DZDNeo4jTools"],
    install_requires=["py2neo", "graphio"],
    python_requires=">=3.6",
    zip_safe=False,
    include_package_data=True,
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        # "local_scheme": "node-and-timestamp"
        "local_scheme": "no-local-version",
        "write_to": "version.py",
    },
    setup_requires=["setuptools_scm"],
)
