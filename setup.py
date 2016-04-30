#!/usr/bin/env python


from setuptools import setup, find_packages

setup(name='django-carousel',
	version='0.1',
	description='Bootstrap based Carousel model, tag, and templates for Django',
	author='John Groszko',
	author_email='john@tinythunk.com',
	url='http://github.com/jgroszko/django-carousel',
	packages=find_packages(),
	install_requires = [
		'django',	
	],
	classifiers = [
        	'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
