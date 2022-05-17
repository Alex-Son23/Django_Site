from django.urls import path
from .views import products, product
#FOR MEDIA
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('category/<int:pk>/', products, name='category'),
    path('category/page/<int:page>/', products, name='page'),
    path('<int:pk>/', product, name='detail'),
]


#FOR MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

