from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    completed = serializers.BooleanField()

    class Meta:
        model = Todo
        fields = ('id', 'description', 'completed')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
    


