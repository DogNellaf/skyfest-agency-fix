from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotFound
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from snippets.utils.i18n import get_language


def e400(request, exception, **kwargs):
    """400 handler"""
    message = kwargs.get('message', '')
    page = {
        'hero_title': _('Неправильный запрос'),
        'content': _('Неправильный запрос')
    }
    request.LANGUAGE_CODE = get_language(request)
    return HttpResponseBadRequest(
        render_to_string(
            'errors/400.html', {
                'request_path': request.path,
                'message': message,
                'page': page,
                'is_error_page': True
            },
            request=request,
            using='jinja2'
        )
    )


def e403(request, exception, **kwargs):
    """403 handler"""
    message = kwargs.get('message', '')
    page = {
        'hero_title': _('Доступ запрещен'),
        'content': _('Доступ запрещен')
    }
    request.LANGUAGE_CODE = get_language(request)
    return HttpResponseForbidden(
        render_to_string(
            'errors/403.html', {
                'request_path': request.path,
                'message': message,
                'page': page,
                'is_error_page': True
            },
            request=request,
            using='jinja2'
        )
    )


def e404(request, exception, **kwargs):
    """404 handler"""
    message = kwargs.get('message', '')
    page = {
        'hero_title': _('Страница не найдена'),
        'content': _('Страница не найдена')
    }
    request.LANGUAGE_CODE = get_language(request)
    return HttpResponseNotFound(
        render_to_string(
            'errors/404.html', {
                'request_path': request.path,
                'message': message,
                'page': page,
                'is_error_page': True
            },
            request=request,
            using='jinja2'
        )
    )
