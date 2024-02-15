from rest_framework import serializers
from .models import *

class Student_serializer( serializers.ModelSerializer):
    class Meta :
        model = Students
        fields = '__all__'

    def validate(self ,data):
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error' : "name does not contain any numerical value"})

        return data
    

class Category_serializer( serializers.ModelSerializer ):
    class Meta :
        model = Category
        fields = '__all__'

class Book_serializer( serializers.ModelSerializer ):
    category = Category_serializer()
    class Meta :
        model = Book
        fields = '__all__'

  
