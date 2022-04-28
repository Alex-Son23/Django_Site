from django.urls import path
from .views import products
# import mainapp.views as mainapp
#FOR MEDIA
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category')
]


#FOR MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

