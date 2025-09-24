from django.http import HttpResponse

def startpage(response):
    return HttpResponse("<h1>Hallo!</h1>")
def index(response, id):
    return HttpResponse("<h1>%s</h1>" % id)

#def v1(response):
    #return HttpResponse("<h1>View 1!<!h1>")
