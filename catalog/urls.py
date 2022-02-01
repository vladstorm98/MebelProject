from django.urls import path

from .views import *

urlpatterns = [
    path('', CatalogHome.as_view(), name='home'),

    path('payment_and_delivery/', PaymentAndDelivery.as_view(), name='payment_and_delivery'),
    path('stores/', Stores.as_view(), name='stores'),
    path('customer_reviews/', CustomerReviews.as_view(), name='customer_reviews'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('add_post/', AddPage.as_view(), name='add_post'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('categories', CatalogCategories.as_view(), name='categories'),
    path('category/<slug:cat_slug>/', CatalogCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]

