import setuptools

setuptools.setup(
    name='racegame2d',
    version='0.1.0',
    author='Christoph Hoeppke',
    description='2D racing games in python based on PyGame2',
    # The line below makes the install stuff be actually not broken,
    # which is nice I guess.
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'sympy',
        'pygame2',
    ]
)
