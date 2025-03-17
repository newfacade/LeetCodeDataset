import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="leetcodedataset",
    py_modules=["leetcodedataset"],
    version="0.1.1",
    description="LeetCodeDataset",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = eval_lcd.evaluate_functional_correctness",
            "eval_lcd = eval_lcd.evaluate:cli",
        ]
    }
)