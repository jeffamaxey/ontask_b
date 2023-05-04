# -*- coding: utf-8 -*-

"""Call back view for OAuth2 authentication."""
from django import http
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, reverse
from django.utils.translation import ugettext, ugettext_lazy as _

from ontask.core import SessionPayload
from ontask.core.permissions import is_instructor
from ontask.oauth import services


@user_passes_test(is_instructor)
def callback(request: WSGIRequest) -> http.HttpResponse:
    """Process the call received from the server.

    This is supposed to contain the token so it is saved to the database and
    then redirects to a page previously stored in the session object.

    :param request: Request object
    :return: Redirection to the stored page
    """
    payload = SessionPayload(request.session)

    # If there is no payload, something went wrong.
    if payload is None:
        # Something is wrong with this execution. Return to action table.
        messages.error(
            request,
            _('Incorrect Canvas callback invocation.'))
        return redirect('action:index')

    if error_string := request.GET.get('error'):
        messages.error(
            request,
            ugettext('Error in OAuth2 step 1 ({0})').format(error_string))
        return redirect('action:index')

    if status := services.process_callback(request, payload):
        messages.error(request, status)
        return redirect('action:index')

    return redirect(
        request.session.get(services.return_url_key, reverse('action:index')))
