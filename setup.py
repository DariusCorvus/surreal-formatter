from setuptools import find_packages, setup

setup(
    name="surreal-formatter",
    version="0.0.1",
    package_dir={"": "src", "surreal_formatter": "src/surreal_formatter"},
    packages=["surreal_formatter"],
    py_modules=["main", "config", "surreal_formatter"],
    include_package_data=True,
    install_requires=["Click", "sly==0.5"],
    entry_points={"console_scripts": ["surreal-formatter = main:cli"]},
)
