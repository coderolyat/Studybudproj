from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loutoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name= "home"),
    # path('room<str:pk>/', views.room, name="room"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>',views.userProfile, name="user-profile"),

    path('create-room/',views.createRoom, name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/',views.updateRoom, name="delete-room"),    
    path('delete-message/<str:pk>/',views.updateMessage, name="delete-message"),   

    path('udate-user/', views.updateUser, name="udate-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]