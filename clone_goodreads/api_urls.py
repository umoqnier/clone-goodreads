from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
url(r'^authors/', include("modules.authors.urls")),
]