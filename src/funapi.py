import ssl
from urllib.request import urlopen
def llamaApi(distrito):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    distrito=distrito.replace(" ","%20")
    url = "https://datos.madrid.es/egob/catalogo/209426-0-templos-catolicas.json?distrito_nombre={}".format(distrito)
    res = urlopen(url, context=ctx) 
    return res
