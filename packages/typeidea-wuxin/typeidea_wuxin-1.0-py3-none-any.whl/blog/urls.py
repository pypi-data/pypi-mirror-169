from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    #FBV
    # path('', post_list, name='index'),
    # path('category/<int:category_id>/', post_list, name='category'),
    # path('tag/<int:tag_id>/', post_list, name='tag'),
    # path('post/<int:post_id>.html', post_detail, name='detail'),

    #CBV
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('post/<int:post_id>.html', PostDetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>', AuthorView.as_view(), name='author'),
]