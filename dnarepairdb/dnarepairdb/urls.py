"""dnarepairdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from db import views
from contact.views import contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='Home'),
    url(r'^pathways/$', views.all_pathways, name="all_pathways"),
    url(r'^pathway/(?P<pathwayid>\d+)/$', views.pathways, name="pathway"),
    url(r'^orthologs/(?P<organismid>\d+)/$', views.all_orthologs, name="all_orthologs"),
    url(r'^ortholog/(?P<orthologid>\d+)/$', views.orthologs, name="ortholog"),
    url(r'^faculty/$', views.faculty, name="faculty"),
    url(r'^contact/$', contact, name="contact"),
]

if settings.DEBUG:
    """
This helper function should not be used in production, See also:
https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#django.contrib.staticfiles.urls.staticfiles_urlpatterns
    """
    urlpatterns += staticfiles_urlpatterns()
