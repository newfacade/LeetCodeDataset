import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="leetcote",
    py_modules=["leetcote"],
    version="1.0",
    description="",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = leetcote.evaluate_functional_correctness",
            "eval_lct = leetcote.evaluate:cli",
        ]
    }
)