
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
    path('departments/',views.departments,name='departments'),
    path('appointment/',views.appointment,name='appointment'),
    path('branches/',views.branches,name='branches'),
    path('show/',views.show,name='show'),
    path('/delete/<int:id>',views.delete,),
    path('/edit/<int:id>',views.edit,),
    path('update/<int:id>',views.update,),
    path('register/', views.register, name='register'),

]
