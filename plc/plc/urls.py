"""plc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from api import views as plc_views
from experiment import views as experiment_views

urlpatterns = [
    url(r'^s2/?', plc_views.s2),
    url(r'^admin/?', admin.site.urls),
    url(r'^test/?', plc_views.test),
    url(r'^plc/?', plc_views.plc),
    url(r'^realtime/?', plc_views.realtime),
    url(r'^odbc', plc_views.odbc),
    url(r'^card/?', plc_views.card),
    url(r'^receive_recipe/?', plc_views.receive_recipe),
    url(r'^mobile/?', experiment_views.mobile),
    url(r'^desktop/?', experiment_views.desktop),
    url(r'^initialize/?', experiment_views.initialize),
    url(r'^retrieve/?', experiment_views.retrieve),
    url(r'^enter/?', experiment_views.enter),
    url(r'^send_recipe/?', plc_views.send_recipe),
    url(r'^log_roll/?', experiment_views.log_roll),
    url(r'^column/?', plc_views.column),
    url(r'^splice_atom/?', plc_views.splice_atom),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
