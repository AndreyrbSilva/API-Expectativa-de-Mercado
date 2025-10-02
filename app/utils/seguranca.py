import re

def uri_valida(uri):
    padrao = r"^mongodb\+srv:\/\/.*"
    return bool(re.match(padrao, uri))
