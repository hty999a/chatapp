from allauth.account.adapter import DefaultAccountAdapter


# allauth で画像を保存するためのクラス
class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(AccountAdapter,self).save_user(request, user, form, commit=False)
        user.icon = form.cleaned_data.get('icon')
        user.save()
        if commit:
            user.save()

        return user