from setuptools import setup

setup(
    name='pp',
    version='1.0.0',
    description='Python test',
    author='I',
    author_email='i@i.com',
    url='https://github.com/testacc7815/pp',
    packages=['pp'],
    package_data={'': ['pp.bin']},
    include_package_data=True,
    install_requires=['numpy>=1.22.3'],
)
