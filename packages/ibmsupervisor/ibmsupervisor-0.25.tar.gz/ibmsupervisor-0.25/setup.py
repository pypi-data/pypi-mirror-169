from setuptools import * 
from pathlib import Path

THIS_DIRECTORY = Path(__file__).parent
LONG_DESCRIPTION = (THIS_DIRECTORY / "README-PyPi.md").read_text()

DESCRIPTION = 'Extract the supervisor password from the ROM dump of an IBM ThinkPad'
VERSION = '0.25'

setup(
    data_files=[
    ('', [
        'README-PyPi.md',
    ]),
    ],
    name='ibmsupervisor',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/eloydegen/ibmsupervisor',
    author='Eloy',
    author_email='degeneloy@gmail.com',
    license='MIT License',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            'ibmsupervisor=ibmsupervisor.main:main'
        ]
    },
    include_package_data=True
)
