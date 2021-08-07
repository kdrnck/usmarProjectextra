from django.urls import path

from . import views

app_name = 'sepet'

urlpatterns = [
    path('', views.sepet_summary, name='sepet_summary'),
    path('add/', views.sepet_add, name="sepet_add"),
    path('delete/', views.sepet_delete, name="sepet_delete"),
    path('clear/', views.sepet_clear, name="sepet_clear"),
    path('update/', views.sepet_update, name="sepet_update"),
]
