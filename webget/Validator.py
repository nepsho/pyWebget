from .Regex import *
import re

def validUrl(url):
	try:
		result = re.match(validUrlReg, url, flags = re.IGNORECASE)
		if result:
			return True
		return False
	except:
		return False

def getHostName(url):
	try:
		result = re.match(urlPartsReg, url, flags = re.IGNORECASE)
		if result:
			if result[4]:
				return result[4]
	except:
		pass
	return None

def removeScriptContent(html):
	try:
		html = re.sub(scriptContentReg, '', html, flags = re.I | re.M)
	except:
		pass
	return html

def removeCssContent(html):
	try:
		html = re.sub(cssContentReg, '', html, flags = re.I | re.M)
	except:
		pass
	return html

def removeBodyContent(html):
	try:
		html = re.sub(bodyContentReg, '', html, flags = re.I | re.M)
	except:
		pass
	return html