from django.http import HttpResponse
from django.shortcuts import render, loader, get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# dane testowe
from Views.TestFiles.test_offer import first_offer
from Views.TestFiles.test_offeR_2 import second_offer
from Projekt_zespołowy.models import JobOffer

# TODO: csrf protect
@csrf_exempt
def main_page(request):
    tags = []
    data = [first_offer, second_offer]
    if request.method == 'POST':
        # lista wpisanych i zatwierdzonych tagów
        req = request.POST.copy()
        tags = req.getlist('filterList[]')
        print(request.POST)
        print(tags)
        data_filtered = []
        for x in data:
            for t in tags:
                if t in x.description:
                    data_filtered.append(x)
        print(data_filtered)
        return render(request, "startpage.html", {'data': data_filtered})
    # filtrowanie ofert na podstawie wpisanych tagów
    # tablica z ofertami, którą prześle się jako argument

    # data = JobOffer.objects.all()
    return render(request, "startpage.html", {'data': data})

def offer_page(request, offer_title):
    data = [first_offer, second_offer]
    offer = next(filter(lambda x: x.title == offer_title, data))
    template = loader.get_template('offer.html')
    context = {
        'offer': offer,
    }
    return HttpResponse(template.render(context, request))



def offer_page_test(request):
    # oferta testowa
    data = first_offer
    # dodać funkcję, która rozdziela dodatkowe korzyści i nice to have
    # na pojedyncze stringi tak jak w tej klasie testowej wyżej
    return render(request, "offer.html", {'offer': data})
