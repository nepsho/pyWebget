from .Constants import *
from .Validator import *
import requests
from requests.exceptions import *

def ErrCallBackMaker(errType):
	return {"success" : False, "type" : errType, "reason" : errorMsg[errType]}

def SuccessCallBackMaker(html):
	html = str(html)
	return {"success" : True, "html" : html}

def WebThief(url):
	if validUrl(url) == False:
		return ErrCallBackMaker("InvalidUrl")
	try:
		req = requests.get(url)
		return SuccessCallBackMaker(str(req.content))
	except HTTPError as httpErr:
		return ErrCallBackMaker("httpErr")
	except SSLError as sslErr:
		return ErrCallBackMaker("sslErr")
	except ConnectionError as connectionErr:
		return ErrCallBackMaker("unreachableSite")
	except Exception as err:
		print(err)
		return ErrCallBackMaker("unknownErr")
