# from django.urls import path
# from .views import predict_price
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('', RedirectView.as_view(url='predict/')),  # root redirects
#     path('predict/', predict_price),
# ]

from django.urls import path
from .views import predict_price, home

urlpatterns = [
    path('', home),            # UI
    path('predict/', predict_price),  # API
]
