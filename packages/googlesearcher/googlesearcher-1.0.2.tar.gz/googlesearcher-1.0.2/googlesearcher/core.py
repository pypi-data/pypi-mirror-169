from bs4 import BeautifulSoup as bs
import requests
from typing import List
import urllib

from ua_headers import ua
from .result import Result
from .error import InvalidCalculation, InvalidPhrase, InvalidLocation

class Google:
	def __request(query: str, num: str):
		url = "https://google.com/search?q="+urllib.parse.quote(query)+"&num="+str(num)
		r = requests.get(url, headers={'User-Agent': ua.linux()})
		return bs(r.text, 'html.parser')

	@classmethod
	def search(self, query: str, num="25"):
		req = self.__request(query, "&num="+num)
		res = req.find_all("div", class_="kCrYT")
		reslist = list()
		for i in res:
			if i.a is not None and i.a['href'].startswith("/url"):
				link = urllib.parse.unquote(i.a['href']).split('?q=')[1].split('&sa=')[0]
				children = i.find_all("span", class_="XLloXe AP7Wnd")
				title = i.a.h3.div.text if i.a.h3 is not None else None
				domain = i.a.div.text if i.a.div is not None else None
				kwargs = {
					'link': link,
					'title': title,
					'domain': domain,
				}
				reslist.append(Result(**kwargs))
		return reslist

# Author: medjed
# Modifined: MishaKorzhik_He1Zen
