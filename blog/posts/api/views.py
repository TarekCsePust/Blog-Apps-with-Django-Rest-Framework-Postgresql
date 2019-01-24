from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


from posts.models import Post
from .serializers import PostListSerializer,PostDetailSerializer, PostCreateUpdateSerializer



class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,title="change by code")


class PostListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list



class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
   # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"


class PostDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'