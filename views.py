from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
         {'name': 'Disha Lukhi' , 'age' : 13},
         {'name': 'Ravina Gelani' , 'age' : 20},
    ]


    return render(request,"index.html" , context= {'peoples': peoples})
def succes_page(request):
     return HttpResponse("Hello")