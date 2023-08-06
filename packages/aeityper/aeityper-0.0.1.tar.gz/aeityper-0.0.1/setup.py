from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Typer. It types for you if pasting is disabled.'
LONG_DESCRIPTION = 'Simulates pressing of keyboard and type the copied text. Can be used if pasting is disabled.'

# Setting up
setup(
    name="aeityper",
    version=VERSION,
    author="Shreyanshu Malviya",
    author_email="<shreyanshumalviya@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['keyboard', 'pyautogui', 'pyperclip'],
    keywords=['type', 'write', 'paste'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
