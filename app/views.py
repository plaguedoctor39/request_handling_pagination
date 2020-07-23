from csv import DictReader
from app import settings
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from urllib.parse import urlencode
bus_stations_list = []
with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
    bus_stations_reader = DictReader(csvfile)
    for row in bus_stations_reader:
        bus_stations_list.append(row)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    print(reverse(bus_stations))
    paginator = Paginator(bus_stations_list, 10)
    current_page = int(request.GET.get('page', 1))
    articles = paginator.get_page(current_page)
    prev_page_url, next_page_url = None, None
    if articles.has_previous():
        prev_page = articles.previous_page_number
        prev_page_url = '?'.join((reverse(bus_stations), urlencode({'page': articles.previous_page_number()})))
    if articles.has_next():
        next_page = articles.next_page_number
        next_page_url = '?'.join((reverse(bus_stations), urlencode({'page': articles.next_page_number()})))

    print(next_page_url)
    return render_to_response('index.html', context={
        'bus_stations': articles,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
