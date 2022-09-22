from datetime import datetime
from re import M
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(resquest):
    return HttpResponse("<h1>Hola Mundo!!!!!!!!! :3</h1>")

def displayDateTime(request):
    st=datetime.now()
    s="<b>Estas son la fecha y hora actuales: <b>"+str(st)+"</b>"
    return HttpResponse(s)
