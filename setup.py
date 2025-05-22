from setuptools import setup

setup(
    name="emnist_preprocessing",
    version="0.1",
    description="Shared preprocessing for EMNIST models",
    packages=["emnist_preprocessing"],
    install_requires=["numpy", "Pillow"],
)
