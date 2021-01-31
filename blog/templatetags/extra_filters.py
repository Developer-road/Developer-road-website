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

@register.filter(name='replace_title') 
def replace_and_title(value):
    """
    Replace the '-' for ' ' and Title the string
    """
    replaced = str(value).replace("-", " ")
    final = replaced.title()
    return final

@register.filter(name='mydate') 
def format_normal_date(value):
    """
    Return a format 'd-m-Y'
    """
    normal_date = value.split("T")[0]
    y, m, d = normal_date.split("-")
    
    return f"{d}-{m}-{y}"
