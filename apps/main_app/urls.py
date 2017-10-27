from django.conf.urls import url
from . import views

def test(request):
        print """

        firing 

        """

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^newTrip$', views.newTrip),
    url(r'^bookTrip$', views.bookTrip), 
    url(r'^travelInfo/(?P<id>\d+)$', views.travelInfo),
    url(r'^join/(?P<id>\d+)$', views.join),
]
