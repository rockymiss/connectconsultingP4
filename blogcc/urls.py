"""
urls for blog app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.BlogPostList.as_view(), name='blog'),
    path('create_blog/', views.CreateBlogView.as_view(), name='create_blog'),
    path('blog_detail/<slug:slug>/',
         views.BlogDetail.as_view(), name="blog_detail"),
    path('create_testimonial/',
         views.CreateTestimonView.as_view(), name="create_testimonial"),
    path('blog_favourite/<slug:slug>/',
         views.Favourites.as_view(), name="blog_favourite"),
    path('blog_review/<slug:slug>/',
         views.BlogUpdate.as_view(), name="blog_review"),
    path('blog_delete/<slug:slug>/',
         views.BlogDelete.as_view(), name="blog_delete"),
    path('review_comments/',
         views.ReviewComments.as_view(), name="review_comments"),
    path('approve_comment/<int:pk>/',
         views.ApproveComment.as_view(), name="approve_comment"),
    path('delete_comment/<int:pk>/',
         views.DeleteComment.as_view(), name="delete_comment"),
    path('review_testimonial/',
         views.ReviewTestimonials.as_view(), name="review_testimonial"),
    path('testimonial/', views.TestimonList.as_view(), name="testimonial"),
    path('approve_testimonial/<int:pk>/',
         views.ApproveTestimon.as_view(), name="approve_testimonial"),
    path('delete_testimonial/<int:pk>/',
         views.DeleteTestimonial.as_view, name="delete_testimonial")
]
