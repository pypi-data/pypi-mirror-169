from setuptools import setup

VERSION = '0.0.5'
DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name='simple_preprocessing',
    version=VERSION,
    author='Marco Mungai Coppolino',
    author_email="<marcomungaicoppolino@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=['numpy', 'pandas', 'sklearn'],
    keywords=['python', 'data science', 'preprocessing', 'encoding'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=['simple_preprocessing']
    
)
