from django.urls import path
from .views import index, about, blog, contact, detail, feature, product, service, team, testimonial, farmerdetailview, productdetailview, ProductsDeleteView, ProductsCreateView, ProductsUpdateView

urlpatterns = [
    path("index/", index, name='index'),
    path("about/", about, name='about'),
    path("blog/", blog, name='blog'),
    path("contact/", contact, name='contact'),
    path("detail/", detail, name='detail'),
    path("feature/", feature, name='feature'),
    path("product/", product, name='product'),
    path("service/", service, name='service'),
    path("team/", team, name='team'),
    path("testimonial/", testimonial, name='testimonial'),
    path("farmer/<int:id>", farmerdetailview, name='farmer_detail_view'),
    path("product/<slug:product>", productdetailview, name='product_detail_view'),
    path("product/edit/<slug>/", ProductsUpdateView.as_view(), name="productUpdate"),
    path("product/delete/<slug>/", ProductsDeleteView.as_view(), name="productDelete.html"),
    path("product/create/", ProductsCreateView.as_view(), name="productCreate.html"),
















]