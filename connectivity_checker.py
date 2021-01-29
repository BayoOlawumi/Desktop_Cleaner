import urllib.request

url = 'https://www.google.com'

"""
A function for testing the connectivity

"""
def connect():

    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False
