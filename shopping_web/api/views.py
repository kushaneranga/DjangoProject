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

    typc2 = TypesCode()
    typc2.name = 'Lorem ipsum dolor'
    typc2.oldprice = '170,000'
    typc2.newprice = '150,000'
    typc2.img = 'kouji-tsuru-btDoDMsVnZc-unsplash.jpg'

    typc3 = TypesCode()
    typc3.name = 'Lorem ipsum dolor'
    typc3.oldprice = '170,000'
    typc3.newprice = '150,000'
    typc3.img = 'sebastian-coman-travel-dtOTQYmTEs0-unsplash.jpg'

    typc4 = TypesCode()
    typc4.name = 'Lorem ipsum dolor'
    typc4.oldprice = '170,000'
    typc4.newprice = '150,000'
    typc4.img = 'lina-verovaya-TeBKnxH_9XA-unsplash.jpg'

    typc5 = TypesCode()
    typc5.name = 'Lorem ipsum dolor'
    typc5.oldprice = '170,000'
    typc5.newprice = '150,000'
    typc5.img = 'barrett-ward-P44RIGl9V54-unsplash.jpg'

    typc6 = TypesCode()
    typc6.name = 'Lorem ipsum dolor'
    typc6.oldprice = '170,000'
    typc6.newprice = '150,000'
    typc6.img = 'patrick-hendry-lsJsaERGu4c-unsplash.jpg'

    typc7 = TypesCode()
    typc7.name = 'Lorem ipsum dolor'
    typc7.oldprice = '170,000'
    typc7.newprice = '150,000'
    typc7.img = 'waldemar-brandt-UP9DtTjRYpI-unsplash.jpg'

    typc8 = TypesCode()
    typc8.name = 'Lorem ipsum dolor'
    typc8.oldprice = '170,000'
    typc8.newprice = '150,000'
    typc8.img = 'artem-beliaikin-hg9da2n4QD8-unsplash.jpg'

    typcs=[typc1, typc2, typc3, typc4, typc5, typc6, typc7, typc8]

    return render(request, 'index.html', {'typcs':typcs})
