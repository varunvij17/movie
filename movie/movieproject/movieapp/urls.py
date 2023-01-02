
from django.urls import path, include
from . import views
app_name='movieapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movieid>/',views.detail,name='detail'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:updateid>/',views.update,name='update'),
    path('delete/<int:deleteid>/',views.delete,name='delete')
]