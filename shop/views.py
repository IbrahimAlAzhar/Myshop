from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None): # the function take the category_slug value from url and then identify the products of this category
    category = None  # initially category set to None,after get object it will be change
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) # if the availability of this products

    # if u type category_slug in url
    if category_slug: # optional category_slug parameter to optionally filter products by a given category
        category = get_object_or_404(Category, slug=category_slug) # slug is set to category slug,Category is model
        products = products.filter(category=category) # take those products which category is same as this category,means take products of this category
    return render(request,'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products }) # if passing the category_slug value then products is this category products instead of all products


def product_detail(request, id, slug): # id,slug use for retrive product instanc,id is unique attribute and include slug in the url to build in SEO friendly url
    product = get_object_or_404(Product, id=id, slug=slug, available=True) # get object using id,slug
   # cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  { 'product': product
                   # 'cart_product_form': cart_product_form  # passing two variables through dictionar
                  })