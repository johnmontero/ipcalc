import re

module_file = open("ipcalc/__init__.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))
long_description = open('README.rst').read()

from setuptools import setup, find_packages

setup(
    name             = 'ipCalc',
    description      = 'IP Address Calc',
    packages         = find_packages(),
    author           = 'John Montero',
    author_email     = 'jmonteroc [at] gmail.com',
    scripts          = ['bin/ipcalc'],
    install_requires = ['Click','tabulate'],
    version          = metadata['version'],
    url              = 'https://git.yachay.pe/devteam/pukutay',
    license          = "MIT",
    zip_safe         = False,
    keywords         = "ip, address, calc",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 4 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                      ]
)
