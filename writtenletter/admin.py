from django.contrib import admin
from writtenletter.models import WrittenLetter, InboxLetter, SentLetter

# Register your models here.

admin.site.register(WrittenLetter)
admin.site.register(InboxLetter)
admin.site.register(SentLetter)
