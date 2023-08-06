#! /usr/bin/env python

"""BiaoWang CTP GP FACTORS"""

from setuptools import setup, find_packages

setup(name='ctp_factors_biaowang',
      version='0.1.3',
      description='a library for cpt factors',
      long_description=open("README.rst").read(),
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Topic :: Software Development',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10'],
      author='Biao Wang',
      author_email='wangbyz@163.com',
      url='https://github.com/wangbyz',
      license='new BSD',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['scikit-learn>=1.0.2',
                        'pandas',
                        'numpy'])
