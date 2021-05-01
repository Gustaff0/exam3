from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

category_choice = (('electronic', 'Electronic'), ('house', 'House'), ('jobe', 'Jobe'), ('food', 'Food'), ('games', 'Games'), ('sundry', 'Sundry'))
# Create your models here.

class Product(models.Model):
   name = models.CharField(max_length=200, null=False, blank=False)
   category = models.CharField(max_length=200, null=False, blank=False, choices=category_choice, default='sundry')
   description = models.TextField(max_length=2000, null=True, blank=True)
   img = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Картинка')

   def __str__(self):
       return self.name + "'s Product"

   class Meta:
       db_table = 'Product'
       verbose_name = 'Товар'
       verbose_name_plural = 'Товары'

class Feedback(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author',  verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='product', verbose_name='Товар')
    feedback_text = models.TextField(max_length=3000, blank=False, null=False)
    appraisal = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(5), MinValueValidator(1)])
    moder_check = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

