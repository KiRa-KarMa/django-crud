from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def home(request):
    return HttpResponse('home')