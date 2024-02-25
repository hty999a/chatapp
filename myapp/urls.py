from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.Login.as_view(), name='login'),
    # クラスビュー関数
    path('friends', views.friends, name='friends'),
    path("talk_room/<int:user_id>/", views.talk_room, name="talk_room"),
    # path('talk_room', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),

    path("username_change/", views.username_change, name="username_change"),
    path("mail_change/", views.mail_change, name="mail_change"),
    path("user_img_change/", views.user_img_change, name="user_img_change"),
    path("password_change/", views.PasswordChange.as_view(), name="password_change"),
    path("logout/", views.Logout.as_view(), name="logout"),
]