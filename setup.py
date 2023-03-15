from setuptools import find_packages, setup

setup(
    name="surreal-formatter",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=["Click", "sly==0.5"],
    entry_points={"console_scripts": ["surreal-formatter = main:cli"]},
)
