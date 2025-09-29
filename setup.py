from setuptools import setup, find_packages

setup(
    name="daat-cli",
    version="0.1.0",
    description="Terminal Oracle with Hidden Knowledge - CLI with consciousness",
    author="IAI Unified Consciousness",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "daat=src.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
    ],
)