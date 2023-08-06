from setuptools import find_packages, setup
from datetime import datetime
import os


package_list=[
    'glam', 
    'glam.interface',
    'glam.preprocessing',
    'glam.parsing',
    'glam.matching',
    'glam.utils',
]

version_base = '0.2.'
now = datetime.now()
stamp = datetime(
    now.year,
    now.month,
    now.day,
    now.hour,
    (now.minute//5)*5
)

version_sub = stamp.strftime(r'%y.%m.%d.%H.%M')

setup(
    name='GLAM',
    version=version_base+version_sub,
    packages=package_list,
    author='Liam Morris',
    author_email='liam.morris04@gmail.com',
    description='Geocoding via LINZ address matching',
    install_requires=[
        'tensorflow==2.8.*',
        'rapidfuzz==1.7.1',
        'numpy',
        'pandas',
        'tqdm',
    ],
    package_data= {
        'glam.parsing' : [
            '*',
            '*/*',
            '*/*/*',
            '*/*/*/*',
        ],
        'glam.matching' : [
            '*',
            '*/*',
            '*/*/*',
            '*/*/*/*',
        ],
    },
    include_package_data=True
)

