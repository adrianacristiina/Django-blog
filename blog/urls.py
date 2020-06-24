from django.urls import path

from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import PostView, PostCreate, PostUpdate, PostDelete

app_name = 'blog'
urlpatterns = [
    # GET ex: /blog/
    path('', home, name='home'),
    # GET ex: /blog/user1
    path('<str:username>', home, name='user_posts'),
    # GET ex: /blog/post/5/
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    # POST ex: /blog/post/create/
    path('post/create/', PostCreate.as_view(), name='create_post'),
    # POST ex: /blog/post/5/update/
    path('post/create/<int:pk>/update', PostUpdate.as_view(), name='update_post'),
    # DELETE ex: /blog/post/5/delete/
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    # POST ex: /blog/post/5/comment/
    path('post/<int:pk>/comment/', CommentCreate.as_view(), name='create_comment')
]
