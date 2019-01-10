from django.conf.urls import include, url
from django.contrib import admin
from clientexpenses import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^client', views.ClientView.as_view(),name='client'),
    url(r'^expense/(?P<id>\d+)', views.ExpenseView.as_view(),name='expense')
]
