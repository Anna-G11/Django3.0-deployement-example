from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dic={'text':'Hello world', 'number':100}
    return render(request,"index.html",context_dic)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url.html')
