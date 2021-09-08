from django import template 

register = template.Library()


def cut(value,arg):
    return value.replace(arg,'haha') 


register.filter('do',cut)