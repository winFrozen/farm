from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from .forms import ContactForms, NewsletterForms
from blog.models import Farmers, Blogs, Products, Commenters, Aboutus, Features, Banner, Newsletter
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView

# Create your views here.
def index(request):
    farmer = Farmers.objects.all()
    print("Malumotlar -- >", farmer)
    blog = Blogs.objects.all()
    product = Products.objects.all()
    commenter = Commenters.objects.all()
    about = Aboutus.objects.all()
    feature = Features.objects.all()
    banner = Banner.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "farmer": farmer,
        "blog": blog,
        "product": product,
        "commenter": commenter,
        "about": about,
        "feature": feature,
        "banner": banner,
        "form": form
    }
    return render(request, "index.html", context=context)


def about(request):
    farmer = Farmers.objects.all()
    about = Aboutus.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "farmer": farmer,
        "about": about,
        "form": form
    }
    return render(request, "about.html", context=context)


def blog(request):
    blog = Blogs.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "blog": blog,
        "form": form
    }
    return render(request, "blog.html", context=context)


def contact(request):
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")
    context = {
        "form": form,
    }
    return render(request, 'contact.html', context=context)


def detail(request):
    commenter = Commenters.objects.all()
    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "detail": detail,
        "form": form,
        "commenter": commenter
    }
    return render(request, "detail.html", context=context)


def feature(request):
    feature = Features.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "feature": feature,
        "form": form
    }
    return render(request, "feature.html", context=context)


def product(request):
    product = Products.objects.all()
    feature = Features.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "product": product,
        "feature": feature,
        "form": form
    }
    return render(request, "product.html", context=context)




def service(request):
    commenter = Commenters.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "service": service,
        "commenter": commenter,
        "form": form
    }
    return render(request, "service.html", context=context)


def team(request):
    farmer = Farmers.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "farmer": farmer,
        "form": form
    }
    return render(request, "team.html", context=context)


def testimonial(request):
    commenter = Commenters.objects.all()

    form = NewsletterForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz amalga oshirildi</h2>")

    context = {
        "commenter": commenter,
        "form": form
    }
    return render(request, "testimonial.html", context=context)


def farmerdetailview(request, id):
    try:
        farmer = Farmers.objects.get(id=id)
        context = {
            "farmer": farmer
        }
    except contact.DoesNotExist:
        raise Http404("No blog found")
    return render(request, "farmer_detail.html", context=context)

def productdetailview(request, product):
    product = get_object_or_404(Products, slug=product)
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context=context)

class ProductsCreateView(CreateView):
    model = Features
    template_name = "productCreate.html"
    fields = ("name", "price", "slug")

class ProductsUpdateView(UpdateView):
    model = Features
    fields = ('name', 'price', 'slug')
    template_name = 'productEdit.html'

class ProductsDeleteView(DeleteView):
    name = Features
    template_name = 'productDelete.html'
    success_url = reverse_lazy('index')













