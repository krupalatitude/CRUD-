from django.urls import path
from .views import IndexView, DeleteView, EditView

urlpatterns = [
    path('', IndexView, name='index'),
    path('delete/<int:id>/', DeleteView, name='delete'),
    path('edit/<int:id>/', EditView, name='edit'),
]
