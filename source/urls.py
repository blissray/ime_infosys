from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'ime_infosys.views.home', name='home'),
    url(r'^home$', 'ime_infosys.views.start_page', name='start_page'),
    url(r'^login_process$', 'ime_infosys.views.login_process', name='login_process'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^member/', include('member.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
