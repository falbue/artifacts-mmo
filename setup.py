
from setuptools import setup, find_packages

setup(
    name='artifactsmmo',
    version='0.1.0',
    packages=find_packages(where="."),
    include_package_data=True,
    package_data={
        "developer_application": ["*"],
    },
    install_requires=[
    ],
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='falbue',
    author_email='cyansair05@gmail.com',
    url='https://github.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
