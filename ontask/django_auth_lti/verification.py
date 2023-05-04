from django.core.exceptions import PermissionDenied


def is_allowed(request, allowed_roles, raise_exception):
    # allowed_roles can either be a string (for just one)
    # or a tuple or list (for several)
    allowed = (
        allowed_roles
        if isinstance(allowed_roles, (list, tuple))
        else (allowed_roles,)
    )
    if not getattr(request, 'LTI', None):
        raise PermissionDenied

    user_roles = request.LTI.get('roles', [])
    is_user_allowed = set(allowed) & set(user_roles)

    if not is_user_allowed and raise_exception:
        raise PermissionDenied

    return is_user_allowed


def has_lti_roles(request, roles):
    user_roles = request.LTI.get('roles', [])
    return bool(set(user_roles) & set(roles))
