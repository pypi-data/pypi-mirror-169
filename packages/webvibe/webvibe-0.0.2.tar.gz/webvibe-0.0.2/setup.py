from setuptools import setup, find_packages

setup(
    name='webvibe',
    version='0.0.2',
    license='MIT',
    author="Mohammad Alamin",
    author_email='itsn0b1t4@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/itsn0b1t4',
    keywords= ['webvibe','website tool'],
    install_requires=[
          'requests', 'urllib2', 'lolcat'
      ],

)