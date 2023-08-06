from setuptools import setup, find_packages 

with open("README.md", "r") as fh:
    description = fh.read()
  
setup(
    name="dom-tools",
    version="0.0.1",
    author="ElliotTrapp",
    author_email="elliot.trapp@jpl.nasa.gov",
    packages=find_packages('src'),
    description="tools for managing dom",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.jpl.nasa.gov/dom-ops/tools",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
       'click',
       'click-default-group',
       'figlet',
       'psutil',
       'pyaml',
       'pyfiglet',
       'PyInquirer',
       'pytest',
       'python-ldap',
       'PyYAML',
       'sh',
       'tabulate',
    ]
)