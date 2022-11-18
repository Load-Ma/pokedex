from django.urls import path

from . import views

urlpatterns = [
    path('all', views.getAllPokemon, name='accueil'),
    path('<int:number>', views.getPokemon, name='index'),
    path('team/add', views.addPokemon, name='add'),
    path('team/remove', views.removePokemon, name='remove')
]
