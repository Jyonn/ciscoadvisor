from User.models import User
from base.session import load_session, save_session


def get_user_from_session(request):
    user_id = load_session(request, 'user', once_delete=False)
    if user_id is None:
        return None
    try:
        return User.objects.get(pk=user_id)
    except:
        return None


def save_user_to_session(request, user):
    try:
        request.session.cycle_key()
    except:
        pass
    save_session(request, 'user', user.pk)
    return None


def logout_user_from_session(request):
    load_session(request, 'user')
