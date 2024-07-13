from setuptools import setup, find_packages

setup(
    name='merge-kicad-sym',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'merge-kicad-sym=src.main:main',
        ],
    },
    install_requires=[],
    author='Pegasis',
    author_email='me@pegasis.site',
    description='A script to merge KiCad symbol libraries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/McMaster-Rocketry-Team/merge-kicad-sym',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
