from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import CommonPasswordValidator

class CustomCommonPasswordValidator(CommonPasswordValidator):


    def validate(self, password, user=None):
        if password.lower() in self.passwords:
            raise ValidationError(
                _("このパスワードはよく使われます。推察されやすい為、別のパスワードを設定して下さい。"),
                code='password_too_common',
            )