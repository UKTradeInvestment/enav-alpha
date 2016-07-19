import urllib
from django import template


register = template.Library()


@register.simple_tag
def breadcrumblink(query, *params):
    """
    Format query string, according passed paramseters
    """
    par = urllib.parse.parse_qs(query)
    queryparams = ''
    for param in params:
        if param in par:
            for value in par[param]:
                queryparams += "{0}={1}&".format(param, value)

    return queryparams[:-1].replace(' ', '+')
