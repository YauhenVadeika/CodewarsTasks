"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def domain_name(url):
    if url[:3] != 'htt' and url[:3] != 'www':
        return url.split('.')[0]
    elif url[:3] == 'www':
        return url.split('.')[1]
    else:
        arr = "".join((url.split('/')[2::])).split('.')
        return [arr[i] for i in range(len(arr)) if arr[i] != "www"][0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("5sbzb0u2t25y06.tv/img/"))
print(domain_name("icann.org"))


# codewars task best solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# codewars task best solution
import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.',
                     url).group('name')


# codewars task best solution
def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]


# codewars task best solution
def domain_name(url):
    from re import findall, VERBOSE

    try:
        url = findall(
            """\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing
                        
                        (?: www.)?    # matches www. or nothing
                        
                        ([- a-z]+)    # matches a sequence of letters and dashes
                        
                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."


# codewars task best solution
def domain_name(url):
    return url.split("://")[-1].split(".")[-2]


# codewars task best solution
import re


def domain_name(url):
    return re.search("(//|www.)(\w+)[.]", url).group(2)


# codewars task best solution
def domain_name(url):
    url = url.split('//')[-1]
    url = url.split('/')[0]
    url = url.split('.')[-2]
    return url


# codewars task best solution
from urlparse import urlparse


def domain_name(url):

    def f(hostname):
        hostname = hostname.split('.')
        if len(hostname) > 2:
            f(".".join(hostname[1:]))
        return hostname[-2]

    if url.startswith('http'):
        url = urlparse(url).netloc
    return f(url)


# codewars task best solution
#bob0921
def domain_name(url):
    print(url)
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    end = url.find(".")
    return url[0:end]


# codewars task best solution
def domain_name(url):

    if ("www" not in url): return url.split("//")[1].split(".")[0]
    else: return url.split(".")[1]
