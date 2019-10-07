from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='welcome'),
    url(r'^about$',views.about,name='about'),
    url(r'^skill$',views.skill,name='skill'),
    url(r'^all_project',views.all_project,name='all_project'),
    url(r'^contact',views.contact,name='contact')
       

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
