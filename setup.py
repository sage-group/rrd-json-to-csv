import os

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'pandas',
    'rrdtool'
]


def extra_files(directory):
    datafiles = [(d, [os.path.join(d, f) for f in files])
                 for d, folders, files in os.walk(directory)]
    return datafiles


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rrd-json-to-csv',
    version="0.0.1",
    license='apache-2.0',
    description='Convert RRD JSON to CSV',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marian Neagul',
    author_email='mneagul@gmail.com',
    url='https://github.com/sage-group/rrd-json-to-csv',
    keywords=['rrd', 'json', 'csv'],
    install_requires=REQUIRED_PACKAGES,
    package_dir={'': 'src'},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': ['sage-rrd-export=sagetools.rrd.convert:main'],
    },
    extras_require={
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
