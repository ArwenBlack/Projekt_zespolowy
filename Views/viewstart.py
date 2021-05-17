from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from Forms.application_form import ApplicationForm

# dane testowe
from Views.TestFiles.test_offer import first_offer, second_offer

# TODO: csrf protect
@csrf_exempt
def main_page(request):
    if request.method == 'POST':
        # lista wpisanych i zatwierdzonych tagów
        print(request.POST)

    # filtrowanie ofert na podstawie wpisanych tagów
    # tablica z ofertami, którą prześle się jako argument

    # data = JobOffer.objects.all()
    data = [first_offer, second_offer]

    return render(request, "startpage.html", {'data': data})


def offer_page(request):
    # oferta testowa
    data = first_offer
    # dodać funkcję, która rozdziela dodatkowe korzyści i nice to have
    # na pojedyncze stringi tak jak w tej klasie testowej wyżej
    if request.method == 'POST':
        return render(request, "application_page.html")

    return render(request, "offer.html", {'offer': data})

@csrf_protect
def application_page(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request, "application_sent.html")
    else:
        form = ApplicationForm()

    return render(request, "application_page.html", {'form': form})