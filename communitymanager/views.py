from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ProjectIndividuel.communitymanager.models import Communaute


def communautes(request):
    commus = Communaute.object.all()
    return render(request, 'communautes.html', {'communautes':
commus}c)