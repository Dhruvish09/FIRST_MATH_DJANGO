from django.shortcuts import render

def home(request):
    return render(request,'math.html')

def expression(request):
    a=int(request.GET['Num1'])
    b=int(request.GET['Num2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})