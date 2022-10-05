from django import template
from news.models import Category

register = template.Library()

# """Varianta 1"""
# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return Category.objects.all()

"""Varianta 2"""
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}