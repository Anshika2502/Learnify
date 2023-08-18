from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save , pre_save

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(default = 'default.jpg', upload_to='avatar')
    stripe_customer_id = models.CharField(blank=True , null= True , max_length = 100)


    def __str__(self):
        return self.user.username

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True,  unique=True)
    stripe_price_id = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField( max_length=10)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, related_name='subscriptions', on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.student.user.email
    
def post_save_student_create(sender , instance , created , *args , **kwargs):
    if created :
        student = Student.objects.create(user=instance)
        free_pricing = Pricing.objects.get(name='Free')
        subscription = Subscription.objects.create(student=student, pricing=free_pricing)
        subscription.save()


def pre_save_pricing(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

post_save.connect(post_save_student_create , sender = User)
pre_save.connect(pre_save_pricing, sender=Pricing)