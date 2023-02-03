from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('bill/', views.bill, name='bill'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)