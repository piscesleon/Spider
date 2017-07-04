# pip install python-whois # from \Anaconda3\Scripts folder
# need SOCKS connection(port:443)

'''
import whois
print(whois.whois('baidu.com')) #查询域名所属
'''

import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl() #setup c as Curl type
c.setopt(c.URL, 'http://pycurl.io/')
c.setopt(c.WRITEDATA, buffer)
c.perform() #exec
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))