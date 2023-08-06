import setuptools

# read the description file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'doc/description.md'), encoding='utf-8') as f:
    long_description = f.read()

version_text = ""
with open(path.join(this_directory, 'version.md'), encoding='utf-8') as f:
    version_text = f.read().strip()

setuptools.setup(
    name="pycinema",
    version=version_text,
    author="David H. Rogers",
    author_email="dhr@lanl.gov",
    description="Cinema scientific toolset.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/cinemascience/pycinema",
    include_package_data=True,
    packages=[  "pycinema",
                "pycinema.smoke"
    ],
    install_requires=[
        "cv2",
        "numpy",
        "scipy",
        "h5py",
        "matplotlib",
        "py",
        "Pillow",
        "ipywidgets",
        "pytest",
        "pytest-xvfb",
        "moderngl<6",
        "opencv-python",
        "torch"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'cinema',
        'doc/description.md', 
        'version.md'
    ],
)
