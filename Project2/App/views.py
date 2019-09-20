from django.shortcuts import render
from django.http import HttpResponse
from App import forms
import time
# Create your views here.
def fibonacci(n):
    if n in [1,2]:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def index(request):
    if request.method=="POST":
        form=forms.Form_Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data['data']
            start=time.time()
            res=fibonacci(data)
            end=time.time()
            return HttpResponse("<h1>Result is {} <br>Time Taken is {}<h1>".format(res,(end-start)*100000000))
    else:
        form=forms.Form_Data()

    return render(request,'index.html',context={'form':form})

    
