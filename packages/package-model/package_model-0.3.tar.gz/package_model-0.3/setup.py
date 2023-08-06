from setuptools import setup, Extension

# PACKAGE DESCRIPTION
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# PROJECT LINKSsdis
project_urls = {
  'GitHub': 'https://github.com/lorenzomarini96/package_model',
  'Documentation': 'https://github.com/lorenzomarini96/package_model'
}

setup(name='package_model',
      version=0.3,
      description='Compute the square of a number',
      author='Lorenzo Marini',
      packages=['package_model'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=["License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.8"],
      project_urls = project_urls,
      zip_safe=False)

