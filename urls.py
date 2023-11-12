from django.contrib import admin
from django.urls import path
from prueba1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acerca/', views.acercaDe),
    path('curso/', views.cursos),
    path('paralelo/<int:idparalelo>', views.paralelo),
    path('', views.paginapri),
    path('web1/', views.paginaweb1),
    path('web2/', views.paginaweb2),
    path('web3/', views.paginaweb3),
    path('web4/', views.paginaweb4),
    path('web5/', views.paginaweb5),
    path('web6/', views.paginaweb6),

]
