from django.conf import settings

if settings.ENABLE_ALLAUTH is True:

    from allauth.account.adapter import DefaultAccountAdapter
    from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

    class CustomAccountAdapter(DefaultAccountAdapter):

        def is_open_for_signup(self, request):
            allow_signups = super(CustomAccountAdapter, self).is_open_for_signup(request)
            return getattr(settings, 'ACCOUNT_ALLOW_SIGNUPS', allow_signups)

    class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

        def is_open_for_signup(self, request, sociallogin):
            allow_signups = super(CustomSocialAccountAdapter, self).is_open_for_signup(request, sociallogin)
            return getattr(settings, 'SOCIALACCOUNT_ALLOW_SIGNUPS', allow_signups)

