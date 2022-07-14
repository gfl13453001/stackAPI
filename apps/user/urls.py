from django.urls import path
from rest_framework_simplejwt.views import token_refresh
from rest_framework.routers import  SimpleRouter

from apps.user.views import (UserLoginViewSet, UserRegisterViewSet, MyAccountCenterViewSet, AccountCentersViewSet,
                             testCentersViewSet)

router = SimpleRouter(trailing_slash=False,)
router.register(r'register', UserRegisterViewSet, basename='register',)
# router.register(r'cms/user/account', UserAccounStatustViewSet, basename='用户管理',)
urlpatterns = [
    # 先通过用户名密码 得到Token  VUE将refresh以及access保存  通过access请求服务器   通过refresh获取新的access
    path('login',UserLoginViewSet.as_view(),name='login'),
    path('account/my/info',MyAccountCenterViewSet.as_view({"get":"list"}),name=''),
    path('account/username/exist',AccountCentersViewSet.as_view({"get":"list"}),name=''),
    path('test',testCentersViewSet.as_view({"get":"list"}),name=''),
]
urlpatterns += router.urls
