# my task solution
def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


url = "http://github.com/carbonfive/raygun"
url = "http://www.zombie-bites.com"
url = "https://www.cnet.com"

print(domain_name(url))

# codewars task best solution
import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


# codewars task best solution
def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]