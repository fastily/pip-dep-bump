import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip-dep-bump",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="Tool for bumping dependencies in requirements.txt files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/pip-dep-bump",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/pip-dep-bump/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["pip_dep_bump"]),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pdb = pip_dep_bump.__main__:_main'
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
