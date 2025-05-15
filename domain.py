# this module returns a str include domain name & top-level domain name
from urllib.parse import urlparse


def get_domain_name(url):
    try: 
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        # return network location part (str)
        return urlparse(url).netloc
    except:
        return ''
