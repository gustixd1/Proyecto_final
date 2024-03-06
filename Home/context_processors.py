from django.contrib.auth.context_processors import auth
from Users.models import Avatar

def custom_user(request):
    context = auth(request)
    user = context['user']

    if user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        cant = len(avatar)
        if cant > 0:
            context['user_avatar'] = avatar[cant-1]
        else:
            context['user_avatar'] = ""

    return context
