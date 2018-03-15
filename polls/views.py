from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader


def index(request):
    return render(request, 'polls/index.html', {})

# Create your views here.
