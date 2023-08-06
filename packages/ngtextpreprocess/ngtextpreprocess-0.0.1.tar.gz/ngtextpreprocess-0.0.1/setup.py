import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ngtextpreprocess",
    packages=['ngtextpreprocess'],
    version="0.0.1",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International',
    author="Ngenux Solutions Pvt. Ltd.",
    author_email="connect@ngenux.com",
    description="A small text cleaning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngenux/ngtextpreprocess.git",
    project_urls={
        "Bug Tracker": "https://github.com/ngenux/ngtextpreprocess.git/issues",
    },
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: Common Public License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    install_requires=[
        'spacy',
        'autocorrect',
        'contractions'
    ],
    download_url="https://github.com/ngenux/ngtextpreprocess/archive/refs/tags/0.0.1.tar.gz"
)
