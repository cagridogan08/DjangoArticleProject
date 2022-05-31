from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout', views.logout, name='logout'),
    path('<int:article_id>/',views.detail,name='detail'),
    path('search',views.search,name='search'),
    path('upload',views.upload,name='upload'),
    path('my_articles',views.my_page,name='my_articles'),
    path('delete/<int:article_id>',views.deletepost,name='delete'),
    path('edit/<int:article_id>',views.editpost,name='edit'),
]