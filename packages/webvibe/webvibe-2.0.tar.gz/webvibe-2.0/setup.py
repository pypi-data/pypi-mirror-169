from setuptools import setup, find_packages

setup(
    name='webvibe',
    packages=find_packages(),
    include_package_data=True,
    version="2.0",
    description='Python2 Web-Tool !',
    author='Mohammad Alamin',
    author_email='itsn0b1t4@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['lolcat','requests', 'urllib2'],
 
    keywords=['itsn0b1t4', 'akxvau', 'devs community', 'reverse ip', 'shared ip', 'geo ip', 'admin finder', 'web tool', 'http header', 'whois', 'subdomin scanner', 'site subdomain finder', 'webvibe', 'web tool', 'hacker', 'spam', 'tool', 'sms', 'bomber', 'call', 'prank', 'termux', 'hack', 'AKXVAU'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'webvibe = webvibe.webvibe:main',
                
            ],
    },
    python_requires='>=2.7'
)
