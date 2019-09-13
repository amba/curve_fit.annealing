import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "curve_fit.annealing",
    version = "0.0.2",
    author = "Simon Reinhardt",
    author_email = "simon.reinhardt@physik.uni-regensburg.de",
    description = "Curve fitting with global optimization routines",
    long_description = long_description,
    keywords='curve fitting global optimization simulated annealing',
    long_description_content_type = "text/markdown",
    url = "https://github.com/amba/curve_fit.annealing",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'scipy >= 1.2.0',
    ],
    python_requires='>=3.5',
    );

    
