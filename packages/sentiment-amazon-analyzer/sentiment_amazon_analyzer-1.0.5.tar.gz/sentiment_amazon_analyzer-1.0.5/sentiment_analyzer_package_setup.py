from setuptools import setup, find_packages

VERSION = '1.0.5' 
DESCRIPTION = 'Sentiment Amazon Analyzer package'
LONG_DESCRIPTION = 'A small package used in Sentiment Analyzer app used to perform nlp tasks, save and load pickle, import data in datafeame...'

setup(
    name="sentiment_amazon_analyzer", 
    version=VERSION,
    author="Pavle Aligrudic",
    author_email="<pavleal@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=["sentiment_amazon_analyzer"],
    install_requires=["pandas", "nltk", "numpy"],         
    keywords=['sentiment', 'amazon', 'analysis'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)