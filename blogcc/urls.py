from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.BlogPostList.as_view(), name='blog'),
    path('create_blog/', views.CreateBlogView.as_view(), name='create_blog'),
    path('blog_detail/<slug:slug>/', views.BlogDetail.as_view(), name="blog_detail")
]