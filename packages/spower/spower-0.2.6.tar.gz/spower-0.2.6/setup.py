import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='spower',  # should match the package folder
    packages=['spower'],  # should match the package folder
    version='0.2.6',  # important for updates
    python_requires=">=3.4",
    license='Apache 2.0',  # should match your chosen license
    description='Free searcher with python, no API keys are required',
    long_description=long_description,  # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='MishaKorzhik_He1Zen',
    author_email='developer.mishakorzhik@gmail.com',
    url="https://github.com/mishakorzik/Spower",
    project_urls={  # Optional
        "Bug Tracker": "https://github.com/mishakorzik/Spower/issues",
        "Sponsor": "https://www.buymeacoffee.com/misakorzik",
    },
    install_requires=['googlesearcher' 'shodan', 'urllib3'],
    keywords=["search", "google", "duck", "duckduckgo", "searcher", "shodan", "api", "easy", "pip", "pypi", "dork", "dorks", "dorking"],  # descriptive meta-data
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
    ],

)
