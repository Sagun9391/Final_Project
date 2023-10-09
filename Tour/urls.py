from django.urls import path
from .Views import views, signup, login, package
from .Views.login import logout
from django.conf import settings
from django.conf.urls.static import static
from .Views.wishlist import Wishlist, Detail
from .Views.My_Booking import my_booking
from .Views.Contact_us import Contact_Us
from .Views.Payment import KhaltiRequest
from .Views.Booking import BookingView
from .Views.Payment import KhaltiVerify
from .Views.Location import LocationListView


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup.Signup.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('Customer_Home/', views.Customer_Home, name='Customer_Home'),
    path('Package_page/', package.Package_page.as_view(), name='Package_page'),
    path('logout/', logout, name='logout'),
    path('wishlist/', Wishlist.as_view(), name='wishlist'),
    path('Details/<int:package_id>/', Detail.as_view(), name='Details'),
    path('my_booking/', my_booking, name='my_booking'),
    path('Contact_us/', Contact_Us.as_view(), name='Contact_us'),
    path('Booking/<int:package_id>/', BookingView.as_view(), name='Booking'),
    path('Payment/<int:package_id>', KhaltiRequest.as_view(), name='Payment'),
    path('Payment_Verify/<int:package_id>/', KhaltiVerify.as_view(), name='Payment_Verify'),
    path('Location/', LocationListView.as_view(), name='Location')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
