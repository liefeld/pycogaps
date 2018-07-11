from distutils.core import setup
from distutils.extension import Extension

ext_instance = Extension(
	'Cogaps',
	sources=['Cogapsmoduleboost.cpp'],
	libraries=['boost-python-mt'],
)

setup(
	name='Cogaps',
	version='0.1',
	ext_modules=[ext_instance]
)
