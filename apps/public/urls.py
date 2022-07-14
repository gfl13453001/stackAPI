# from apps.system.views import (SystemNavViewSet, UploadFileView, BannerViewSet)
from rest_framework.routers import  SimpleRouter

from apps.public.views import MenuNavigationViewSet, BannerViewSet, UploadFileView

router = SimpleRouter(trailing_slash=False,)
router.register(r'nav/list', MenuNavigationViewSet, basename='首页菜单导航',)
router.register(r'index/banner', BannerViewSet, basename='首页banner',)
router.register(r'upload', UploadFileView, basename='upload',)

urlpatterns = []
urlpatterns += router.urls
