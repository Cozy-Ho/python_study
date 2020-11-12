def makepass(url):
    url = url[7:]
    url = url[:url.index(".")]
    password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
    return password

print(makepass("http://naver.com"))
print(makepass("http://google.com"))