import base64
a = input('whats your name?') 
a:bytes = a.encode('gbk')
a = base64.b64encode(a)
print(a)
a = str(a,'gbk')
print(base64.b64decode(a))