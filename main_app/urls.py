from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('details/', views.details, name='details'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path(
        'cars/<int:car_id>/add-rentalrecord/', 
        views.add_rentalrecord, 
        name='add-rentalrecord'
    ),
    path('cars/<int:car_id>/show_updaterecord/<int:record_id>', views.show_updaterecord, name='show_updaterecord'),
    path('cars/<int:car_id>update_rentalrecord/<int:record_id>', views.update_rentalrecord, name='update_rentalrecord'),
    path('cars/<int:car_id>/delete_rentalrecord/<int:record_id>', views.delete_rentalrecord, name='delete_rentalrecord'),
]