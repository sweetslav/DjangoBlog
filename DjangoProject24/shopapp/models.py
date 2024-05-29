from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Name: {self.name},\n'
                f'Email: {self.email},\n'
                f'Phone: {self.phone},\n'
                f'Address: {self.address},\n'
                f'Date: {self.date_registered}\n')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos', blank=True, null=True)

    def __str__(self):
        return f'\nName: {self.name},\tPrice: {self.price},\tQuantity: {self.quantity} '


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return (
            f'\t{self.client.name}\t{", ".join(str(product) for product in self.products.all())}'
            f'\tStatus: {self.get_status_display()}')
