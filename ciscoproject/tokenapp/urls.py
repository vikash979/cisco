from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tokenapp import views

router = DefaultRouter()
router.register(r'toc_model', views.RouterViewset)
router.register(r'ipdata', views.IpViewset)


urlpatterns = [
    re_path('', include(router.urls)),
    re_path(r'^login/$', views.login, name="login"),
    re_path(r'^routerdata/$', views.CustomAuth.as_view(), name="routerdata"),
    re_path(r'^nrouterdata/$', views.AddNrouterView.as_view(), name="nrouterdata"),
    
    re_path(r'^ipp/$', views.ipmacid, name="ipp"),
    re_path(r'^tokenapp/$', views.TokenView.as_view(), name="tokenapp"),
    re_path(r'^tokenupdate/$', views.TokenUpdateView.as_view(), name="tokenupdate"),
    re_path(r'^delete_event/(?P<pk>[0-9]+)/$', views.delete_post, name="delete_event"),
    re_path(r'^update_event/$', views.update_post, name="update_event"),
    re_path(r'^nrouter/$', views.nrouter_post, name="nrouter"),
    re_path(r'^add_router/$', views.AddRouterView.as_view(), name="add_router"),
    #re_path(r'^delete_event$/(?P<pk>\d+)/$',views.delete_post, name='delete_event'),
    

    ]