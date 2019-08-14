from django.urls import path

from . import views

app_name = 'team'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.EditView.as_view(), name='edit'),
    path('<int:member_id>/edit', views.memberEdit, name='memberEdit'),
    path('<int:member_id>/delete', views.delete, name='delete'),
    path('add/', views.add, name = 'add'),
    path('addEdit/', views.addEdit, name = 'addEdit'),
]
