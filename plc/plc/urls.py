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
    url(r'^admin/?', admin.site.urls),
    url(r'^test/?', plc_views.test),
    url(r'^plc/?', plc_views.plc),
    url(r'^realtime/?', plc_views.realtime),
    url(r'^odbc', plc_views.odbc),
    url(r'^card/?', plc_views.card),
    url(r'^receive_recipe/?', plc_views.receive_recipe),
    url(r'^ect_mobile/?', experiment_views.mobile),
    url(r'^send_recipe/?', plc_views.send_recipe)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
