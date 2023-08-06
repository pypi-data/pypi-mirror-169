from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Tigitaal\'s Official Python Package to connect with TigitaalAPI'

# Setting up
setup(
        name="tigitaalconnect", 
        version=VERSION,
        author="Ninjagor",
        author_email="ninjagor.spoon@gmail.com",
        description=DESCRIPTION,
        long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
        packages=find_packages(),
        install_requires=[
            'requests'
        ],
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)