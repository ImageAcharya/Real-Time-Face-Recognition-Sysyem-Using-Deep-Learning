from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('changepassword/', views.changepass, name='changepass'),
    path('logout/', views.logout, name='logout'),
    path('managestudent/', views.managestd, name='managestd'),
    path('classroom/', views.classroom, name='classroom'),
    path('attendance/', views.attendance, name='attendance'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
