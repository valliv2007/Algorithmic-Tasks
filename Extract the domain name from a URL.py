"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

import re 

def domain_name(url):
    first_split = re.split(r'://', url)
    second_split = re.split(r'www.', re.split(r'://', url)[-1])
    return re.split(r'www.', re.split(r'://', url)[-1])[-1].split('.')[0]

print(domain_name("www.xakep.ru"))