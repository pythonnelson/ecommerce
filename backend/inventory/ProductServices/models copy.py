from django.db import models
from UserServices.models import Users
from InventoryServices.choices import *

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    image = models.TextField()
    display_order = models.IntegerField(default=0)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_category')
    description = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='added_by_user_id_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    image = models.JSONField()
    description = models.TextField()
    specifications = models.JSONField()
    html_description = models.TextField()
    highlights = models.JSONField()
    sku = models.CharField(max_length=255)
    initial_buying_price = models.FloatField()
    initial_selling_price = models.FloatField()
    weight = models.FloatField()
    dimension = models.CharField(default='0x0x0', max_length=255)
    uom = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    tax_percentage = models.FloatField()
    brand = models.CharField(max_length=255)
    brand_model = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True, choices=PRODUCT_AVAILABILITY, default='Available'),
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    seo_keywords = models.JSONField()
    additional_details = models.JSONField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_id')
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_product')
    added_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='added_by_user_id_product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    status = models.CharField(max_length=100, choices=PRODUCT_QUESTION_STATUS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_question', blank=True, null=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_questions')
    question_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='question_by_user_id')
    answer_by_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='answer_by_user_id_product_question')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    review_images = models.JSONField()
    rating = models.FloatField()
    reviews = models.TextField()
    status = models.CharField(max_length=255, choices=PRODUCT_REVIEWS_STATUS)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews', blank=True, null=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user_id_reviews')
    review_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name='added_by_user_id_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)