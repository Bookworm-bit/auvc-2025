from setuptools import find_packages, setup

import os
virtualenv_name = "tutorials"
home_path = os.path.expanduser("~")
executable_path = os.path.join(home_path, '.virtualenvs', virtualenv_name, 'bin', 'python')

package_name = 'tutorial_virtualenvs'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='devworm',
    maintainer_email='ezhang7708@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'virtualenvs = tutorial_virtualenvs.virtualenvs:main',
        ],
    },
    options={
        'build_scripts': {
            'executable': executable_path,
        }
    },
)
