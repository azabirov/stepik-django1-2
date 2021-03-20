import random
# from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
# Create your views here.
from tours import data


def main_view(request):
    tours = []
    tour_id_list = []
    image_random = random.choice(["https://cdn.pixabay.com/photo/2016/03/27/07/32/light-1282314_1280.jpg",
                                  "https://megapornpics.com/wp-content/uploads/2018/12/monica_rambe-8240.jpg",
                                  ])
    for tour_id in range(6):
        while True:
            tour_id = random.randint(1, len(data.tours))
            if tour_id not in tour_id_list:
                break
        tours_element = data.tours[tour_id]
        tours_element['tourid'] = tour_id
        tours.append(tours_element)
        tour_id_list.append(tour_id)
    return render(request, "tours/index.html", context={
        'tours': tours,
        'image_random': image_random,
    })


def departure_view(request, departure):
    tours = []
    tour_id = 0
    for number in data.tours:
        tour_id += 1
        data.tours[number]['tour_id'] = str(tour_id)
        if data.tours[number]['departure'] == departure:
            tours.append(data.tours[number])
            data.tours[number]['pricetofit'] = '{:,}'.format(data.tours[number]['price']).replace(',', ' ')
        minprice = '{: ,}'.format(min([int(data.tours[tour]['price'])
                                       for tour in data.tours if data.tours[tour]['departure'] == departure]))\
            .replace(',', ' ')
        maxprice = '{: ,}'.format(max([int(data.tours[tour]['price'])
                                       for tour in data.tours if data.tours[tour]['departure'] == departure]))\
            .replace(',', ' ')
        minnights = '{: ,}'.format(min([int(data.tours[tour]['nights'])
                                        for tour in data.tours if data.tours[tour]['departure'] == departure]))\
            .replace(',', ' ')
        maxnights = '{: ,}'.format(max([int(data.tours[tour]['nights'])
                                        for tour in data.tours if data.tours[tour]['departure'] == departure]))\
            .replace(',', ' ')
    return render(request, "tours/departure.html", context={
        'departure': departure,
        'tours': tours,
        'minprice': minprice,
        'maxprice': maxprice,
        'minnights': minnights,
        'maxnights': maxnights,
    })


def tour_view(request, tour_id):
    tours = data.tours[tour_id]
    tours['hotelstars'] = int(tours['stars']) * '★'
    tours['pricetofit'] = '{:,}'.format(tours['price']).replace(',', ' ')
    return render(request, "tours/tour.html", context={
        'tours': tours,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound("<h2><b>404</b> Очень жаль, но такой страницы не существует.</h2>")


def custom_handler500(request):
    return HttpResponseServerError("<h2><b>500</b> Ошибка на сервере. Мы скоро все починим.</h2>")
