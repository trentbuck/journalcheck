#!/usr/bin/python3
import setuptools
setuptools.setup(
    name='journalcheck',
    version='1.0',
    packages=['journalcheck'],
    # This makes /usr/bin/foo which are basically #!/bin/sh ↲ exec python3 -m foo "$@"
    # Ref. https://packaging.python.org/tutorials/distributing-packages/#console-scripts
    # Ref. https://github.com/pypa/sampleproject
    entry_points={
        'console_scripts': [
            'journalcheck=journalcheck.main'
        ]
    }
)
