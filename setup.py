from setuptools import find_packages, setup


setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Jeet Nandigrami',
    author_email= 'jeetnandigrami2003@gmail',
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages= find_packages()
)