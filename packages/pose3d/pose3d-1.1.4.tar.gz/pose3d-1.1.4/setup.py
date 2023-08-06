from pathlib import Path
from setuptools import setup, find_packages

VERSION = '1.1.4'
DESCRIPTION = 'Transforming and handling 3D poses and frames.'

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Add resource links
project_urls = {
    'Documentation': 'https://johnhal.gitlab.io/pose_python',
    'Repository': 'https://github.com/johnhalz/pose3d'
}

# Setting up
setup(
    name="pose3d",
    version=VERSION,
    author="John Halazonetis",
    author_email="<john.halazonetis@icloud.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'pandas'],
    keywords=['python', 'pose', 'transform'],
    project_urls=project_urls,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
