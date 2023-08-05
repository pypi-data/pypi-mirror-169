from setuptools import setup, find_packages


setup(
    name='Word4Univer',
    version='0.1.0',
    package_dir={'': "."},
    packages=find_packages(".", exclude=["tests*"]),
    url='',
    license='MIT',
    author='chiririll',
    author_email='sstive39@gmail.com',
    description='',
    install_requires=['Jinja2~=3.1.2']
)
