from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlantListView.as_view(), name="plant_list"),
    path('<int:pk>/edit/', views.PlantUpdateView.as_view(), name="plant_edit"),
    path('new/', views.PlantCreateView.as_view(), name="plant_new"),
    path('<int:pk>/', views.PlantDetailView.as_view(), name="plant_detail"),
    path('<int:pk>/delete/', views.PlantDeleteView.as_view(), name="plant_delete"),
]
