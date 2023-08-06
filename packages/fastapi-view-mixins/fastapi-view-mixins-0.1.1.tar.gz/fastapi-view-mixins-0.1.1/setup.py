from pathlib import Path

from setuptools import find_packages, setup

VERSION = '0.1.1'
DESCRIPTION = 'Fastapi view mixins'
# read the contents of your README file
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "readme.md").read_text()

# Setting up
setup(
    name="fastapi-view-mixins",
    version=VERSION,
    author="Patryk Dąbrowski",
    author_email="tibiasportex@gmail.com",
    license_files=('LICENSE.txt',),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools_git >= 0.3'],
    install_requires=['fastapi', 'sqlalchemy', 'pymongo', 'motor'],
    exclude_package_data={'': ['.gitignore', 'requirements.txt']},

    keywords=['python', 'paginator', 'pagination', 'views'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
