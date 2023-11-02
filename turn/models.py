from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid =  models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField()
    is_done = models.BooleanField()


    def __str__(self) -> str:
        return self.todo_title