from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    context = {
        "name": "Khánh Trung", 
        "age": 20, 
        "email": "lytrung15901@gmail.com"
        }
    return render(request, "relax/test.html", context)

def home(request):
    return render(request, "relax/home.html")