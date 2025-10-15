from django.contrib import admin
from  user.models import  Pinguser,Chat ,ChatMember,Message,MessageStatus,Reaction
admin.site.register(Pinguser)
admin.site.register(Chat)
admin.site.register(ChatMember)
admin.site.register(Message)
admin.site.register(MessageStatus)
admin.site.register(Reaction)
