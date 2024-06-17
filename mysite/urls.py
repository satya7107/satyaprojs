from django.urls import path
from mysite import views as aviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',aviews.home,name='home')

]