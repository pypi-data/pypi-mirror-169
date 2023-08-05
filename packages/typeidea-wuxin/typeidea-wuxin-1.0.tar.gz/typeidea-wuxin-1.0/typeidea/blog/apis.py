from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer

@api_view()
def post_list(request):
    posts = Post.objects.filter(status=Post.STATUS_NORMAL)
    post_serializers = PostSerializer(posts, many=True)
    return Response(post_serializers.data)

class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    # def filter_queryset(self, queryset):
    #     category_id = self.request.query_params.get('category')
    #     if category_id:
    #         queryset = queryset.filter(category_id=category_id)
    #     return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)