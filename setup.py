from setuptools import setup, find_packages

with open('README.md') as readme_file:

    long_description = readme_file.read()

setup(
    name = 'vgnr',
    version = '0.1.0',
    packages = find_packages(),
    include_package_data=True,
    license='Apache 2.0 License',
    description='viginar encryption encoding and decoding',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://papermerge.com/',
    author='Eugen Ciur',
    author_email='eugen@papermerge.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires='',
    entry_points = {
        'console_scripts': [
            'vgnr = vgnr.__main__:main'
        ]
    }
)
