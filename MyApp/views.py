import requests
from django.shortcuts import render
from .models import MyModel

# Create your views here.
def home(request):
    # Get data from API
    # url = 'https://api.thecatapi.com/v1/images/search?limit=10'
    # response = requests.get(url)
    # data = response.json()
    # for cat in data:
    #     name = cat['url']
    #     MyModel.objects.create(name=name, age=1)

    cats = MyModel.objects.all()
    return render(request, 'home.html', {'cats': cats})
