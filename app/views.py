from django.shortcuts import render
from django.shortcuts import HttpResponse
#业务处理逻辑的编写
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
    return render(request, 'app/login.html')
def main(request):
    return render(request,'app/main2.html')

def register(request):
    return render(request,'app/register.html')

