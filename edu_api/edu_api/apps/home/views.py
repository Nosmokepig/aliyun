from rest_framework.generics import ListAPIView

from home.contastnt import BANNER_LENGTH,HEADER_LENGTH,FOOTER_LENGTH
from home.models import Banner, Nav
from home.serializers import BannerModelSerializer, NavModelSerializer


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_delete=False).order_by('-orders')[:BANNER_LENGTH]
    serializer_class = BannerModelSerializer

class HeaderListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True,is_delete=False,position=1).order_by('-orders')[:HEADER_LENGTH]
    serializer_class = NavModelSerializer
class FooterListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True,is_delete=False,position=2).order_by('orders')[:FOOTER_LENGTH]
    serializer_class = NavModelSerializer
