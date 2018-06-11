import os
from setuptools import setup,find_packages
    
setup(
    name='nitro-python',
    version='1.0',
    author='Citrix Netscaler',
    packages=[
        'nssrc',    
        'nssrc.com',
        'nssrc.com.citrix',
        'nssrc.com.citrix.netscaler',    
        'nssrc.com.citrix.netscaler.nitro',
        'nssrc.com.citrix.netscaler.nitro.exception',
        'nssrc.com.citrix.netscaler.nitro.resource',
        'nssrc.com.citrix.netscaler.nitro.util',
        'nssrc.com.citrix.netscaler.nitro.service',
        'nssrc.com.citrix.netscaler.nitro.resource.base',
        'nssrc.com.citrix.netscaler.nitro.resource.config',
        'nssrc.com.citrix.netscaler.nitro.resource.stat'] + 
        [ os.path.join('nssrc.com.citrix.netscaler.nitro.resource.config', mydir) for mydir in find_packages("nssrc/com/citrix/netscaler/nitro/resource/config")] +
        [ os.path.join('nssrc.com.citrix.netscaler.nitro.resource.stat', mydir) for mydir in find_packages("nssrc/com/citrix/netscaler/nitro/resource/stat")],
    classifiers=[
          'Intended Audience :: NS Administrators',
          'Programming Language :: Python',
          'Topic :: Software Development :: API',
    ],
    description='Python SDK for Nitro API',    
    install_requires=[
        "requests >= 2.3.0",
    ],
    scripts=[
        'sample/stat_config.py', 
        'sample/rm_config.py', 
        'sample/set_config.py', 
        'sample/get_config.py',
        'sample/MyFirstNitroApplication.py', 
        'sample/CreateCluster.py', 
    ],
)