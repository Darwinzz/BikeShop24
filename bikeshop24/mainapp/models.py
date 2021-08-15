from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# settings.AUTH_USER_MODEL

User = get_user_model()

# Create models for our e-store.
# Models in our project
# ***********************************
# 1 Category
# 2 Product
# 3 CartProduct
# 4 Cart
# 5 Order
# 6 Customer
# 7 Specification


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image')
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.title


class Bicycle(Product):

    usage_type = models.CharField(max_length=255, verbose_name='Bicycle type by use')
    wheel_size = models.CharField(max_length=255, verbose_name='Wheel Size')
    frame_size = models.CharField(max_length=255, verbose_name='Frame Size')
    color = models.CharField(max_length=255, verbose_name='Color')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Helmet(Product):

    helmet_size = models.CharField(max_length=255, verbose_name='Helmet Size')
    helmet_color = models.CharField(max_length=255, verbose_name='Helmet Color')
    helmet_weight = models.CharField(max_length=255, verbose_name='Helmet Weight')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)



class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Customer name', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')

    def __str__(self):
        return "Product: {} (for Cart)".format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total Price')
    
    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return "Customer: {} {}".format(self.user.first_name, self.user.last_name)


