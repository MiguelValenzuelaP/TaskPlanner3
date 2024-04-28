from django.db.models import CharField, TextField, BooleanField, Model


# Create your models here.
class Task(Model):
    title = CharField(max_length=200)
    description = TextField(blank=True)
    done = BooleanField(default=False)
    other = BooleanField(default=False)

    def __str__(self):
        return self.title
