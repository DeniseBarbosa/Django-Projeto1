from django.urls import path

from receitas.views import contato, home, sobre

urlpatterns = [
    path('', home),  # HOME
    path('sobre/', sobre),  # /SOBRE/
    path('contato/', contato),  # /CONTATO/

]
