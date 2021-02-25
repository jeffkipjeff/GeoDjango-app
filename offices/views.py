from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import FieldOffice, RegionalOffice, HeadOffice, Issues

latitude = -1.28333
longitude = 36.81667

office_location = Point(longitude, latitude, srid=4326)


# Create your views here.
class Home(generic.ListView):
    model = FieldOffice
    context_object_name = 'field_offices'
    queryset = FieldOffice.objects.annotate(distance=Distance('location', office_location)).order_by('distance')[0:10]
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['head_office'] = HeadOffice.objects.all()
        context['regional_offices'] = RegionalOffice.objects.all()
        context['issues'] = Issues.objects.all()
        return context
