from django.shortcuts import render
from .models import Destination


# Create your views here.
def home(request):
    dests = Destination.objects.all()
    context_dict = {
        'dests': dests
    }
    return render(request, 'travello/index.html', context=context_dict)


def about(request):
    return render(request, 'travello/about.html')


def destinations(request):
    return render(request, 'travello/destinations.html')


def contact(request):
    return render(request, 'travello/contact.html')


def news(request):
    return render(request, 'travello/news.html')


def elements(request):
    return render(request, 'travello/elements.html')
