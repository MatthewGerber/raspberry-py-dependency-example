from setuptools import setup, find_packages

setup(
    name='raspberry-py-dependency-example',
    version='0.1.0',
    description='An example of consuming raspberry-py via PyPI dependency',
    author='Matthew Gerber',
    author_email='gerber.matthew@gmail.com',
    url='https://matthewgerber.github.io/raspberry-py-dependency-example',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='~=3.9',
    install_requires=[
        'raspberry-py==0.3.0'
    ]
)
