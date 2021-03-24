import setuptools

def read(fname):
	with open(fname,'r') as f:
		return f.read()

setuptools.setup(
name='logger',
version='1.0.0',
author='HugeBrain16',
author_email='joshtuck373@gmail.com',
description='A Logger for logging :/',
license='MIT',
keywords='logger logging trace',
url='https://github.com/HugeBrain16/logger',
project_url= {
		"Bug Tracker": 'https://github.com/HugeBrain16/logger/issues'	
	},
packages=setuptools.find_packages(),
long_description=read('README.md'),
long_description_content_type='text/markdown',
classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
	]
)