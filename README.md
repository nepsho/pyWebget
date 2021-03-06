
# WebGet (Python)

[![image](https://raw.githubusercontent.com/nepsho/nepsho.github.io/master/lib/img/webget_cover_plain.jpg)](https://pypi.org/project/webget/)

[![image](https://img.shields.io/pypi/v/webget.svg?style=plastic&label=WebGet&color=success)](https://pypi.org/project/webget/)
[![image](https://img.shields.io/pypi/l/webget.svg?style=plastic&color=orange)](https://github.com/nepsho/pyWebget/blob/master/License.txt)
[![image](https://img.shields.io/pypi/pyversions/webget.svg?style=plastic)](https://pypi.org/project/webget/)
[![image](https://img.shields.io/github/contributors/nepsho/pyWebget.svg?style=plastic&color=blueviolet)](https://github.com/nepsho/webget/graphs/contributors)
[![image](https://img.shields.io/pypi/status/webget.svg?style=plastic)](https://pypi.org/project/webget/)


Python website info getter.

## install
```bash
pip install webget
```
**import**
```python
>>> import webget
```
**Get html of website:**
```python
>>> result = webget.getHtml("https://nepsho.github.io/example/meta_tags.html")
```
```js
{
	'success': True,
	'html': 'Html of website'
}
```
**Get images from website:**
```python
>>> result = webget.getImages("https://nepsho.github.io/example/meta_tags.html")
```
```js
{
	'success': True,
	'images': [ArrayOfImagesOnWebsite]
}
```
**Get meta data of website:**
```python
>>> result = webget.getMeta("https://nepsho.github.io/example/meta_tags.html")
```
```js
{
	'success': True, 
	'logo': 'http://nepsho.github.io/lib/img/logo.png', 
	'description': 'Promise and callback based website-info getter using metadata of websites...', 
	'title': 'webget', 
	'keywords': 'NepSho ,Open source, webget, api, nodejs, python, meta, javascript, programming', 
	'subject': 'Open source', 
	'copyright': 'NepSho', 
	'language': 'en', 
	'robots': 'index,follow', 
	'revised': 'Sunday, May 9th, 2019, 0:00 am', 
	'abstract': 'NepSho abstract', 
	'topic': 'Tech', 
	'summary': 'tech is super', 
	'author': 'BCrazyDreamer, bcrazydreamer@gmail.com', 
	'designer': 'bcrazydreamer', 
	'reply-to': 'bcrazydreamer@gmail.com', 
	'url': 'https://nepsho.github.io', 
	'category': 'Web', 
	'site_name': 'webget', 
	'email': 'bcrazydreamer@gmail.com', 
	'country-name': 'INDIA', 
	'phone_numbe': '123-456-7890'
}
```
## licence
MIT [licence](https://github.com/nepsho/pyWebget/blob/master/License.txt)

## Author
@BCrazyDreamer