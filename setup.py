from setuptools import setup, find_packages

setup(
    name='django-oneforty',
    version=__import__('oneforty').__version__,
    description='django-oneforty is designed to be a simple, lightweight status/update engine.',
    long_description=open('README.txt').read(),
    author='Pure Blue Inc',
    author_email='dave@purebluedesign.com',
    url='http://github.com/davemerwin/django-oneforty/tree/master',
    download_url='http://github.com/davemerwin/django-oneforty/archives/master',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

