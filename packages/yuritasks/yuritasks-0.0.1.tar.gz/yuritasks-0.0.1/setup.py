from setuptools import setup

setup(
    name = 'yuritasks', 
    version = '0.0.1',
    description = 'Task automation tool, automate those boring and repetitive tasks.',
    package_dir = {'':'src'},
    packages = ["yuritasks"],
    author = 'edo0xff',
    author_email = 'edo0xff@pronton.me',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/edo0xff/yuri',
    include_package_data=True,

    classifiers  = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
    ],
    
    install_requires = [
        'colorama'
    ],
    
    keywords = ['Task automation', 'Tool'],
)