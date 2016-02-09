from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^registration$', 'member.views.registration', name='registration'),
    url(r'^registration_process$', 'member.views.registration_process',
        name='registration_process'),
    url(r'^logout_process$', 'member.views.logout_process',
        name='member_logout_process'),


]