from django.shortcuts import render
from django.http import HttpResponse


def project_list(request):
    return HttpResponse("<h2>RP</h2>")
