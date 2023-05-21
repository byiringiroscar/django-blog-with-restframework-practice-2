from django.urls import path
from .import views

name = 'Sport'

urlpatterns = [
    path('', views.info, name='info'),
    # path('info/<int:id>/', views.detail, name='detail'),
    path('publish', views.publish, name='publish'),
    path('<int:id>/', views.podelete, name='podelete'),

    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.edit_post, name='edit_post'),

]