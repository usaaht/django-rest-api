from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify


class TodoSerial(serializers.ModelSerializer):

    slug =  serializers.SerializerMethodField()

    class Meta:
        model = Todo
        exclude = ['created_at']

    def get_slug(self, obj):
         
        return slugify(obj.todo_title)


    def validate(self, validated_data):
        if validated_data.get('todo_title'):
                todo_title = validated_data['todo_title']
                regex = re.compile(r'[!@#$%^&*()]')
                if regex.search(todo_title):
                    raise serializers.ValidationError('todo title doesnot contain any type of specail char')
            
        return validated_data