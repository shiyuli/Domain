# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup as BS
from multiprocessing import Process

class Domain(object):
	def __init__(self):
		pass

	def run(self, maxProcess):
		for i in range(0, maxProcess):
			p = Process(target=self.pre)
			p.start()

	def pre(self):
		with open('domainLists.txt', 'rb') as domainLists:
			while True:
				domain = domainLists.readline().strip()
				print domain
				if domain == '':
					break
				try:
					self.check(domain)
				except (urllib2.URLError, urllib2.HTTPError), e:
					with open(('result/error/'+domain), 'wb') as f:
						f.write(domain)
						f.close()
					print 'urllib2.HTTPError'

			domainLists.close()
			print 'Done!'

	def check(self, domain):
		# url = 'https://wanwang.aliyun.com/domain/searchresult/?keyword={0}&suffix={1}'.format(domain, domain_type)
		domain_type = 'com'
		url = 'http://whois.chinaz.com/{}.{}'.format(domain, domain_type)
		# urllib2.ssl._create_default_https_context = urllib2.ssl._create_unverified_context
		HTML = urllib2.urlopen(url).read()
		soup = BS(HTML, 'html.parser', from_encoding='utf-8')
		temp = 0
		for i in range(0, len(soup.find_all('div'))):
			a = soup.find_all('div')[i]
			if u'您的请求过于频繁' in a:
				with open(('result/re/'+domain), 'wb') as f:
					f.write(domain)
					f.close()
				temp = 1
				print domain, u'您的请求过于频繁'
				break

		if temp == 0:
			for i in range(0, len(soup.find_all('a'))):
				a = soup.find_all('a')[i]
				if u'未被注册或被隐藏' in a:
					with open(('result/'+domain), 'wb') as f:
						f.write(domain)
						f.close()
					print domain, u'未被注册或被隐藏'
					break

if __name__ == '__main__':
	Domain().run(10)