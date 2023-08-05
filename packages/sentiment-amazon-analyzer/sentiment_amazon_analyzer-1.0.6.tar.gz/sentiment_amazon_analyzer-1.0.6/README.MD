Classifier

run pytests
    pip install -e . (in a directory where setup.py is created)
    pytest

create and upload package: 
    link: https://www.freecodecamp.org/news/build-your-first-python-package/
    create: python sentiment_analyzer_package_setup.py sdist bdist_wheel
    upload: twine upload --skip-existing dist/*
