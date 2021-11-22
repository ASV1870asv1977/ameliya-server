from django import template
from wagtail.core.models import Site

from home.snippets_models import Footer, Header

register = template.Library()


@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'request': context['request'],
        'header': Header.objects.first(),
    }


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first(),
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page


def has_menu_children(page):
    # This is used by the top_menu property
    # get_children is a Treebeard API thing
    # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
    return page.get_children().live().in_menu().exists()


def has_children(page):
    # Generically allow index pages to list their children
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return (current_page.url_path.startswith(page.url_path) if current_page else False)


@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
    return {
        # 'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_parent(context, parent, calling_page=None):

    menuitems_parent = parent.get_parent()
    menuitems_children = menuitems_parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
        menuitem.children = menuitem.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.has_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
                           if calling_page else False)
        menuitem.children = menuitem.get_children().live().in_menu()

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'request': context['request'],
    }


@register.simple_tag
def counter(count):
    count += 1
    return count
