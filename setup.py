from setuptools import setup

setup(
    name="pro_filer",
    description="Projeto Pro Filer",
    install_requires=["pypubsub==4.0.3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
