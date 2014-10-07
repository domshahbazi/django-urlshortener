from shorturl.models import urlObj
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
import re

import string
import random
import datetime

# Base url to append short url code to
base_url = '127.0.0.1:8000/shorturl/'

# URL CODE SIZE
CODE_SIZE = 6

# Generate random string of size N for url
def generate_url(size):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

# Shorten URL and return shortened code
def shorten_url(url):
    try:
        url_code = save_url(url)
    except IntegrityError:
        url_code = save_url(url)
    return base_url+url_code

def save_url(url):
    url_code = generate_url(CODE_SIZE) # Generates small url code
    u = urlObj(original_url=url, short_url=url_code, date_created=datetime.date.today())
    u.save()
    return url_code

# Given the shorturl, return the original url
def lookup_url(shorturl):
    u = get_object_or_404(urlObj, short_url=shorturl)
    original_url = u.original_url
    return original_url


