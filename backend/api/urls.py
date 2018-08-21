from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from . import views

urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addresses/', views.AddressView.as_view(), name="addresses"),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name="address_detail"),
    path('phone-numbers/', views.PhoneNumberView.as_view(), name="phones"),
    path('phone-numbers/<int:pk>/', views.PhoneNumberDetailView.as_view(), name="phone_detail"),
    path('emails/', views.EmailView.as_view(), name="emails"),
    path('emails/<int:pk>/', views.EmailDetailView.as_view(), name="email_detail"),
    path('contacts/', views.CreateView.as_view(), name="create"),
    path('contacts/<int:pk>/', views.DetailsView.as_view(), name="details"),
    path('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
