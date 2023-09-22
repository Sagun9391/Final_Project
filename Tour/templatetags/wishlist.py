from django import template

register = template.Library()

@register.filter(name='is_in_wishlist')
def is_in_wishlist(package, wishlist):
    keys = wishlist.keys()
    for id in keys:
        if int(id) == package.id:
            return True
    return False;
