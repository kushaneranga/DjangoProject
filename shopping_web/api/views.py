from django.shortcuts import render
from django.http import HttpResponse
from .models import TypesCode

# Create your views here.


def main(request):

    typc1 = TypesCode()
    typc1.name = 'Lorem ipsum dolor'
    typc1.oldprice = '170,000'
    typc1.newprice = '150,000'
    typc1.img = 'fabian-heimann-4R_WEmhx8og-unsplash.jpg'

    return render(request, 'index.html', {'typc1':typc1})
