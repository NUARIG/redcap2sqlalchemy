import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redcap2sqlalchemy", 
    version="0.0.2",
    author="Firas H. Wehbe",
    author_email="Firas Wehbe <firas.wehbe@northwestern.edu>",
    description="Extracting data from REDCapo and pushing into a relational DB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NUARIG/redcap2sqlalchemy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Database",
    ],
    python_requires='>=3.6',
    install_requires=[
        'sqlalchemy>=1.3',
        'requests>=1'
    ]
)
