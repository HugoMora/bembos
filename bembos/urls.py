"""bembos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.orders.url import router
from rest_framework.authtoken import views
from apps.orders.views import Login,Logout
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='BembosWs API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/TipoComponente',TipoComponenteAPI.as_view(),name = 'api_create_tipocomponente')    
    path('api/',include(router.urls)),
    path('api_documentation/', schema_view),
    path('api_token',views.obtain_auth_token),
    path('login/',Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
