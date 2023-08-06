from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = "kiqnetworktools",
    version = "0.0.3",
    author = "Luis Cueva",
    author_email = "lecuevad@gmail.com",
    description = "Tools for Networking",
    license = "MIT",
    keywords = "kiqnetworktools",
    url = '',
    packages=find_packages(),
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    install_requires=['textfsm==1.1.2',
                      'netmiko==4.1.2',
                      'python-nmap==0.7.1']
)