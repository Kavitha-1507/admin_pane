from django.urls import path
from dashboard.views import view_401,view_404,view_500,view_charts, view_index,view_layout_sidenav_light,view_layout_static,view_login,view_password,view_register,view_tables
urlpatterns = [
    path("view/",view_401),
    path("404/",view_404),
    path("500/",view_500),
    path("charts/",view_charts),
    path("index/",view_index),
    path("layout_sidenav_light/",view_layout_sidenav_light),
    path("layout_static/",view_layout_static),
    path("login/",view_login),
    path("password/",view_password),
    path("register/",view_register),
    path("tables/",view_tables),
]
