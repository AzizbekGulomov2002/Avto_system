from django.urls import path, include
from app.views import AvtoViews, main, avto_haqida
 
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
   
    path('', main, name='avtolar'),
    path('all_avto', AvtoViews.as_view(), name='all_avto'),
    path('avto_haqida/<str:id>/', avto_haqida, name='avto_haqida'),
    path('posts/', main, name='posts')
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 