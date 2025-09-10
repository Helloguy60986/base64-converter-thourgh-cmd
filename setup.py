from setuptools import setup

setup(
    name="base64convert",
    version="1.0.0",
    py_modules=["base64convert"],
    entry_points={
        "console_scripts": [
            "base64convert=base64convert:main"
        ]
    },
    python_requires=">=3.6",
)
