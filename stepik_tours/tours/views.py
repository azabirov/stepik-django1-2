from django.shortcuts import render
# from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
# Create your views here.
from tours import data
import random


def main_view(request):
    tours = []
    tour_id_list = []
    image_random = random.choice(["https://cdn.pixabay.com/photo/2016/03/27/07/32/light-1282314_1280.jpg",
                                  "https://megapornpics.com/wp-content/uploads/2018/12/monica_rambe-8240.jpg",
                                  ])
    for tour_id in range(6):
        while True:
            tour_id = random.randint(1, len(data.tours))
            if tour_id not in tour_id_list: break
        tours_element = data.tours[tour_id]
        tours_element['tourid'] = tour_id
        tours.append(tours_element)
        tour_id_list.append(tour_id)
    return render(request, "tours/index.html", context = {
        'tours':tours,
        'image_random':image_random,
    })


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
