from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^order/', views.OrderView.as_view(msg="666"), name='order'),
    url(r'^hello/', views.HelloTemplateView.as_view(), name='hello'),
]