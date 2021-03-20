from django.shortcuts import render
# from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
# Create your views here.
from tours import data




def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    return render(request, "tours/departure.html")


def tour_view(request, tour_id):
    tours = data.tours[tour_id]
    tours['hotelstars'] = int(tours['stars']) * '★'
    tours['pricetofit'] = '{:,}'.format(tours['price']).replace(',', ' ')
    return render(request, "tours/tour.html", context = {
        'tours':tours,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound("<h2><b>404</b> Очень жаль, но такой страницы не существует.</h2>")


def custom_handler500(request):
    return HttpResponseServerError("<h2><b>500</b> Ошибка на сервере. Мы скоро все починим.</h2>")
