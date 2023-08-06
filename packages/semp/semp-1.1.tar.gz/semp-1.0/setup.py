from setuptools import setup

setup(name='semp',
      version='1.0',
      description='Selenium made simple(just a bit)!',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords='selenium python library manipulate website geckodriver firefox automation webbot bot dogukan meral',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
					'Operating System :: MacOS',
          'Programming Language :: Python :: 3.8',
					'Topic :: Internet',
					'Topic :: Software Development :: Libraries',
					'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Utilities',
          ],
      url='http://github.com/dogonso/semp',
      author='Dogukan Meral',
      author_email='dogukan.meral@yahoo.com',
      license='MIT',
      include_package_data=True,
      packages=['semp'],
      entry_points = {
          'console_scripts': ['semp=semp.command_line:main'],
          },
      install_requires=[
          'webdriver-manager',
          'selenium',
          ],
      zip_safe=False)
