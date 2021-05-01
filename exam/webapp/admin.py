from django.contrib import admin
from webapp.models import Product, Feedback

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'img']
    list_filter = ['name']
    search_fields = ['name', 'category', 'description']
    fields = ['id', 'name', 'category', 'description', 'img']
    readonly_fields = ['id']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'feedback_text', 'created_at', 'updated_at', 'moder_check']
    list_filter = ['product', 'author', 'moder_check']
    search_fields = ['feedback_text',]
    fields = ['id', 'author', 'product', 'feedback_text', 'appraisal', 'moder_check', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
