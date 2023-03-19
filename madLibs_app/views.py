from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


def Story1(request):
    form = InputForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'madLibs_app/story1.html', {'form': form})

