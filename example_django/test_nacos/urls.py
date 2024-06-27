from django.urls import path

from .views import NacosView

urlpatterns = [
    path('nacos', NacosView.as_view()),
]
