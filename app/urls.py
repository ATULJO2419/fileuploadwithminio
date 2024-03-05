from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
        path('admin_view/<int:document_id>/', views.admin_view, name='admin_view'),

]
