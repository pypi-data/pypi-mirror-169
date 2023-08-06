import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name = 'sangheeMODEL',
    version = '0.0.0',
    license = 'MIT',
    description = 'sanghee\'s NLP models.',
    author = 'sanghee park',
    author_email = 'parksangheeeee@naver.com',
    url = 'https://github.com/ajskdlf64/sanghee-nlp-tool',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)