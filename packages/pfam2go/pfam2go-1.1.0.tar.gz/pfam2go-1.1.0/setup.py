from setuptools import setup

setup(
    name='pfam2go',
    version='1.1.0',
    description='A package to match Pfam accession numbers to corresponding GO terms',
    url='https://github.com/Konstvv/pfam2go',
    author='Konstantin Volzhenin',
    author_email='Konstantin_v_v@outlook.com',
    license='MIT',
    packages=['pfam2go'],
    install_requires=['requests', 'pandas', 'typing', 'numpy'],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],
)
