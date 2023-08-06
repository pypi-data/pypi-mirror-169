from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Sort of just a test, there\'s not much point to this.'
LONG_DESCRIPTION = 'lol'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="testmoduletrolol", 
        version=VERSION,
        author="xavvvv",
        author_email="email@email.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)