# from apps.system.views import (SystemNavViewSet, UploadFileView, BannerViewSet)
from rest_framework.routers import  SimpleRouter

from apps.public.views import MenuNavigationViewSet, IndexDataViewSet, UploadFileView

router = SimpleRouter(trailing_slash=False,)
router.register(r'nav/list', MenuNavigationViewSet, basename='首页菜单导航',)
router.register(r'index', IndexDataViewSet, basename='首页',)
router.register(r'upload', UploadFileView, basename='upload',)

urlpatterns = []
urlpatterns += router.urls
