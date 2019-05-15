import setuptools
with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'webget',
  version = '0.1',
  license='MIT',
  author = 'BCrazyDreamer',
  author_email = 'bcrazydreamer@gmail.com',
  description = 'Python website info api using meta data',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/nepsho/webget',
  packages=setuptools.find_packages(),
  keywords = ['api', 'web', 'webget' , 'scraping' , 'website' , 'website-info' , 'python'],
  install_requires=[
          'requests'
  ],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
  ]
)