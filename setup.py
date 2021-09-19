from setuptools import setup, find_packages

def setup_package():
    setup(
        name='c-stitch',
        version='0.0.1',
        description='Stitcher for FASTEN C-Debian call graphs',
        license='Apache Software License',
        packages=find_packages(),
        install_requires=['flask'],
        entry_points = {
            'console_scripts': [
                'c-stitch=stitcher.__main__:main',
            ],
        },
        classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3'
        ],
        author = 'Stefanos Chaliasos',
        author_email = 'schaliasos@aueb.gr'
    )

if __name__ == '__main__':
    setup_package()
