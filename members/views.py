from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Markers
from . import scripts


def index(request):
    mymarkers = Markers.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymarkers': mymarkers,
    }
    return HttpResponse(template.render(context, request))


def marker(request):
    n = request.POST['name']
    d = request.POST['description']
    l = request.POST['video']
    lat = request.POST['lat']
    lng = request.POST['lan']
    diff = request.POST['rate']
    eff = request.POST['rate1']
    try:
        b = request.POST['bike']
    except:
        b = 0
    try:
        c = request.POST['car']
    except:
        c = 0
    try:
        name = scripts.youtube(l)
    except:
        name = ''
    member = Markers(name=n, desc=d, link=name,
                     latlan="[{}, {}]".format(lat, lng), difficulty=diff, effect=eff, bike=b, car=c)
    member.save()
    return HttpResponseRedirect(reverse('index'))
