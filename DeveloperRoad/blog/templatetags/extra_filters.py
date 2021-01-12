from django import template

register = template.Library()

@register.filter(name='myslug') 
def myslug(value):
    """
    Returns a slug without altering the Uppercase string letters 
    
    """
    return str(value).replace(" ", "-")

@register.filter(name='string') 
def string(value):
    """
    Returns a slug without altering the Uppercase string letters 
    
    """
    return str(value)