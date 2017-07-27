from django.conf.urls import url
from django.views.generic.list import ListView

from .models import Laserapp
from .views import index, details, edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list$', ListView.as_view(
        model=Laserapp,
        paginate_by=2,
        template_name='list.html',
    )),
    url(r'^details/(?P<slug>\S+)$', details, name='details'),
    url(r'^edit/(?P<slug>\S+)$', edit, name='edit'),
]