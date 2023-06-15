from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home,name='home'),
    path('prediction',views.prediction,name='prediction'),
    path('about',views.about,name='about')
]
