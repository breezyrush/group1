from django.conf.urls import include, url
from django.contrib import admin
from musixscore import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^browse/', views.browse, name='browse'),
]
