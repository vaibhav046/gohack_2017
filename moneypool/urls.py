'''
from django.conf.urls import url
from django.views.generic import TemplateView

from .api import MasterprofileApi, ProfileApi,TransactionApi

urlpatterns = [
    url(r'^masterprofile$', MasterprofileApi.as_view()),
    url(r'^profile$', ProfileApi.as_view()),
    url(r'^transaction$', TransactionApi.as_view()),
 #   url(r'^home', TemplateView.as_view(template_name="moneypool/home.html")),
]
'''
from django.conf.urls import url,include
from django.views.generic import TemplateView
from .api import MasterprofileViewSet, ProfileViewSet,TransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'masterprofile', MasterprofileViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
url(r'^',include(router.urls)),
url(r'^home', TemplateView.as_view(template_name="moneypool/home.html")),
url(r'^master', TemplateView.as_view(template_name="moneypool/master_user.html")),
        ]