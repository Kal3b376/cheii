
from django.contrib import admin
from django.urls import path
from medicioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('inner/',views.inner,name='inner-page'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),



]
