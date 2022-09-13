from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.BlogPostList.as_view(), name='blog'),
    path('create_blog/', views.CreateBlogView.as_view(), name='create_blog'),
    path('blog_detail/<slug:slug>/', views.BlogDetail.as_view(), name="blog_detail"),
    path('create_testimonial/', views.CreateTestimonView.as_view(), name="create_testimonial"),
    path('approve_comments/', views.ApproveComments.as_view(), name='approve_comments'),
    path('blog_favourite/<slug:slug>/', views.Favourites.as_view(), name="blog_favourite"),
    path('blog_review/<slug:slug>', views.BlogUpdate.as_view(), name="blog_review"),
    path('blog_delete/<slug:slug>', views.BlogDelete.as_view(), name="blog_delete")
]