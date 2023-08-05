"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from .custom_site import custom_site
from rest_framework.documentation import include_docs_urls
from blog.apis import post_list, PostList, CategoryViewSet

# from .autocomplete import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostList, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    path('admin/', custom_site.urls),
    path('super_admin', admin.site.urls),

    path('', include('blog.urls')),
    path('', include('config.urls')),
    path('', include('comment.urls')),

    path('api/docs/', include_docs_urls(title='typeidea apis')),
    # path('api/post/', post_list, name='post_list'),
    # path('api/post/', PostList.as_view(), name='post_list'),
    path('api/', include(router.urls)),

    # path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    # path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
