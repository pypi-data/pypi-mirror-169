from setuptools import setup

# reading long description from file
with open("DESCRIPTION.txt") as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ["requests"]

# some more details
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Topic :: Internet",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

# calling the setup function
setup(
    name="test_suraj_mygmap",
    version="0.0.2",
    description="A small wrapper around google maps api",
    # long_description=long_description,
    url="https://github.com/nikhilkumarsingh/mygmap",
    author="Suraj Gaire <surajgaire0@gmail.com>, Niraj Gaire <nirajgaire@gmail.com",
    # author_email="surajgaire0@gmail.com, nirajgaire@gmail.com",
    license="MIT",
    packages=["geo"],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords="maps location address",
)
