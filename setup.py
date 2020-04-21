from pathlib import Path
from setuptools import setup, find_packages


version = '0.0.1'


setup(
    name='ChemistryTool',
    version=version,
    packages=find_packages(),
    url='https://github.com/dcloudf/ChemistyTool',
    license='LGPLv3',
    python_requires='>=3.6.0',
    entry_points={'console_scripts': []},
    install_requires=[],
    extras_require={},
    long_description=(Path(__file__).parent / 'README.md').open().read(),
    classifiers=['Environment :: Plugins',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Topic :: Scientific/Engineering :: Chemistry',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 ]
)
