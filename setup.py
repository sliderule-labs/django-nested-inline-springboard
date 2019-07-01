from setuptools import setup, find_packages

from nested_inline import __version__

github_url = 'https://github.com/sliderule-labs/django-nested-inline-springboard'
long_desc = open('README.md').read()

setup(
    name='django-nested-inline-springboard',
    version='.'.join(str(v) for v in __version__),
    description='Recursive nesting of inline forms for Django Admin',
    long_description=long_desc,
    url=github_url,
    author='Josh Rowe',
    author_email='josh@s-block.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
