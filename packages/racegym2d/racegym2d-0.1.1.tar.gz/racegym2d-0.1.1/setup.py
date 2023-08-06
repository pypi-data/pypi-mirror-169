import setuptools

setuptools.setup(
    name='racegym2d',
    version='0.1.1',
    author='Christoph Hoeppke',
    description='Gym environments for 2D vehicle racing',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'sympy',
        'racegym2d',
        'pyracetrack',
        'numba',
        'pytorch',
        'gym',
    ]
)
