from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta


def cdt(reqeust):
    return HttpResponse(datetime.now())


def fha(request):
    return HttpResponse(f'After Four Hours:{datetime.now()+timedelta(hours=4)}')

def fhb(request):
    return HttpResponse(f'Before Four Hours:{datetime.now()-timedelta(hours=4)}')