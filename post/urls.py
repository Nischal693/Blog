from django.urls import path
from post.views import post_list, post_create,post_delete,post_detail,PostEditView,PostCreateView,PostDetailView,PostDeleteView,PostListView
urlpatterns = [
    path("list/",PostListView.as_view(),name="post-list"),
    path("delete/",PostDeleteView.as_view(),name="post-delete"),
    path("create/",PostCreateView.as_view(),name="post-create"),
    path("<int:id>/edit/",PostEditView.as_view(),name="post-edit"),
    path("<int:id>/detail/",PostDetailView.as_view(),name="post-detail"),
]
