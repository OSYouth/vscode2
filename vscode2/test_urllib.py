import urllib.request as urllib

url = "https://www.baidu.com"

print ('第一种方法')
response1 = urllib.urlopen(url)
print (response1.getcode())
print (len(response1.read()))