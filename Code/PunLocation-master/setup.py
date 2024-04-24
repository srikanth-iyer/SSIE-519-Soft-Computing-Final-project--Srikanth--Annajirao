# setup.py

from setuptools import setup, find_packages

setup(
    name="semantic_shape_of_puns",
    version="0.1",
    description="My Python project",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "plotly",
        "ipywidgets",
        "seaborn",
        "black",
        "transformers",
        "tqdm",
        "scikit-learn",
        "torch",
        "torchvision",
        "re",
        "config",
        "copy",
        "argparse",
        "os",
        "sys",
        "models",
        "utils",
        "inference",
        "sklearn",
        
        # Add other required packages here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)