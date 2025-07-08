from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def form(request):
    na=request.POST.get('sample')
    return render(request,'form.html',{'sample':na})