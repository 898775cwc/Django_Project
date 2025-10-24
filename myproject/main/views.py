from django.http import HttpResponse
from django.shortcuts import render

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=4)
    return render(response, "main/index.html", {})

#def v1(response):
    #return HttpResponse("<h1>View 1!<!h1>")

def home(response):
    return render(response, "main/home.html", {})