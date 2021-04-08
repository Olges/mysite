# ссылка на приложение и его составляющие

from django.urls import path
from django.conf.urls import url
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$',views.user_logout, name='logout'),
]
