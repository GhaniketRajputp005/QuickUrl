from django.urls import path
from root.views import createURL,routeToURL



urlpatterns = [
   
    path('',createURL),
    path('<slug:key>/',routeToURL)
]