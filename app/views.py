from django.shortcuts import render,redirect
from .forms import curd
from django.http import HttpResponse
from .models import user
def home(request):
    if request.method=='POST':
        form=curd(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Congratulation")
    else:
        form=curd()

    students=user.objects.all()

    context={
        'form':form,
        'data':students
    }
    return render(request,'app/home.html',context)

