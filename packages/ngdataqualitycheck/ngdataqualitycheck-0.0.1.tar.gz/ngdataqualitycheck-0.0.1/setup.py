import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ngdataqualitycheck",
    packages=['ngdataqualitycheck'],
    version="0.0.1",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International',
    author="Ngenux Solutions Pvt. Ltd.",
    author_email="connect@ngenux.com",
    description="Package for checking data quality.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ngenux/ngdataqualitycheck",
    project_urls={
        "Bug Tracker": "https://github.com/ngenux/ngdataqualitycheck/issues",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: Common Public License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    install_requires=[
        'numpy',
        'pandas',
        'python-docx',
        'matplotlib',
        'seaborn',
        'beautifulsoup4',
        'wordcloud',
        'nltk',
        'missingno'
    ],
    download_url="https://github.com/ngenux/ngdataqualitycheck/archive/refs/tags/0.0.1.tar.gz"
)
