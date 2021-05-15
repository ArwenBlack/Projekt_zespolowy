from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# TODO: csrf protect
@csrf_exempt
def index(request):
    if request.method == 'POST':
        # lista wpisanych i zatwierdzonych tagów
        print(request.POST)

    return render(request, "startpage.html")