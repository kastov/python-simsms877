# -*- coding: utf-8 -*-
from os import path
from setuptools import setup

"""
@author: tezmen, forked and edited by ravensoracle
@contact: https://t.me/tezmen
@license Apache License, Version 2.0, see LICENSE file
Copyright (C) 2019
"""


def long_description():
	"""Build the description from README file """
	this_dir = path.abspath(path.dirname(__file__))
	with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
		return f.read()


def requirements():
	"""Build the requirements list for this project"""
	requirements_list = list()
	with open('requirements.txt') as pc_requirements:
		for install in pc_requirements:
			requirements_list.append(install.strip())
	return requirements_list


setup(
	name='smsactivateru',
	version='1.2.5',
	long_description=long_description(),
	long_description_content_type='text/markdown',
	description='Wrapper for automatic reception of SMS-messages by smshub.org',
	author='tezmen',
	license='Apache License, Version 2.0, see LICENSE file',
	keywords='sms, revice, smshub.org, autoreg',
	author_email='tezmenpro@gmail.com',
	url='https://github.com/ravensoracle/python-smshub-org/',
	download_url='https://github.com/ravensoracle/python-smshub-org/archive/master.zip',
	packages=['smshuborg'],
	install_requires=requirements(),
	classifiers=[
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Environment :: Console',
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: Implementation :: PyPy',
	]
)
