from setuptools import setup, find_packages

setup(
    name='croft',
    version='0.5.0',    
    description='Small dataset web publication tool',
    url='https://github.com/atiro/croft',
    author='Richard Palmer',
    author_email='r.palmer@vam.ac.uk',
    license='BSD 2-clause',
    packages=find_packages( include=['croft*']),
    scripts=['crofter'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

