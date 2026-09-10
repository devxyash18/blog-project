from django.urls import path
from . import views
urlpatterns = [
    path("",views.starting_page,name="starting-page"),
    path("posts",views.posts,name="posts-page"),
    path("posts/<slug:slug>",views.post_detail, name="post-detail-page")
]

# posts/my-first-post (such urls which are dynamic are used to build wit these placeholders and this method is called slug)
