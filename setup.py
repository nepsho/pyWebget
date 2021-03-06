import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'webget',
  version = '1.0',
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
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
  ]
)