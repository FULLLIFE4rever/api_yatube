from django.urls import include, path
from rest_framework.authtoken import views as av
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostsViewSet

router = SimpleRouter()

router.register('posts', PostsViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')


urlpatterns = [
    path('api-token-auth/', av.obtain_auth_token),
    path('', include(router.urls))
]
