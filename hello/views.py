from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def page(request):
    url = request.GET.get('url', "")
    print("RECEIVED URL:", url)
    if not url:
        return HttpResponse('<form><input type="text" name="url"><input type="submit"></form>')
    else:
        r = requests.get(url)
        result = ""
        if r.status_code == 200:
            result = r.content
        return HttpResponse(result)