from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    CONTENT = {
        'Name' : [],
        'Street' : [],
        'District': [],
    }
    page = 1
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        list_name = []
        list_street = []
        list_district = []
        for row in reader:
            list_name.append(row[('Name')])
            list_street.append(row[('Street')])
            list_district.append((row['District']))

    CONTENT['Name'] = list_name
    CONTENT['Street'] = list_street
    CONTENT['District'] = list_district
    paginator_bus = Paginator(CONTENT,10)
    bus_stations = paginator_bus.get_page(page)
    context = {
        'bus_stations': bus_stations,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
