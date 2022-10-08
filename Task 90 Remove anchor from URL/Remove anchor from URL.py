# my task solution
def remove_url_anchor(url):
    return url[:url.find('#')] if '#' in url else url


print(remove_url_anchor("www.codewars.com/katas/"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com#about"))

# my task solution
a = "www.codewars.com/katas/"
# if a.count('#'):
if '#' in a:
    print(a[:a.find('#')])
else:
    print(a)


# codewars task best solution
def remove_url_anchor(url):
    return url.split('#')[0]


# codewars task best solution
def remove_url_anchor(url):
    return url.partition('#')[0]


# codewars task best solution
def remove_url_anchor(url):
    import re
    return re.sub('#.*$', '', url)


# codewars task best solution
def remove_url_anchor(url):
    index = url.find('#')
    return url[:index] if index >= 0 else url