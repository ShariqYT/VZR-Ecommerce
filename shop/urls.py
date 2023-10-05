from django.urls import include, path
from shop.views import *

urlpatterns = [
    path("", home, name="home"),
    path("search/", search, name="search"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    # path("cart/", cart, name="cart"),
    path("products/<int:myid>", productView, name="productView"),
    path("topdeals-products/<int:myid>", dealsView, name="dealsView"),
    path("trackerStatus/", tracker, name="trackerstatus"),
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
    path("pre-build/", pre_build, name="pre-build"),
    path("laptops/", laptops, name="laptops"),
    path("subscription/", subscription, name="subscription"),
    path("checkout/", checkout, name="checkout"),
]
