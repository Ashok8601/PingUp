from django.db import models

class Pinguser(models.Model):
    name = models.CharField(max_length=100, default="user1")
    email = models.EmailField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=16)
    password = models.CharField(max_length=200)
    pin = models.IntegerField(blank=True, null=True)
    user_photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    bio = models.TextField(blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Chat(models.Model):
    CHAT_TYPE = (
        ("private", "Private"),
        ("group", "Group"),
    )
    chat_type = models.CharField(max_length=10, choices=CHAT_TYPE)
    name = models.CharField(max_length=255, blank=True, null=True)
    members = models.ManyToManyField("Pinguser", through="ChatMember")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_type} - {self.name or 'No Name'}"


class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(Pinguser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default="member")
    joined_at = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(Pinguser, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="message/files/", blank=True, null=True)
    reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)   # better default
    created_at = models.DateTimeField(auto_now_add=True)


class MessageStatus(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="statuses")
    user = models.ForeignKey(Pinguser, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)


class Reaction(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(Pinguser, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=20)
    reacted_at = models.DateTimeField(auto_now_add=True)
