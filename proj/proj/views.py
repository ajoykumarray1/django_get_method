from django.shortcuts import render
from django.http import HttpResponse

def practice(request):
    n1=request.GET.get("fname")
    n2=request.GET.get("lname")
    data={
        'a':n1,
        'b':n2
    }
    return render(request,"index.html",data)
    