from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    userId = serializers.IntegerField()
    todobucketid = serializers.IntegerField()
    description = serializers.CharField()
    completed = serializers.BooleanField()

    class Meta:
        model = Todo
        fields = ('id', 'todobucketid', 'description', 'completed', 'userId')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

    def validateBucketId(self, value):
        if 0 < value < 5:
            raise serializers.ValidationError("Bucket ID must be positive.")
        return value
    
    def validateUserId(self, value):
        if value < 0:
            raise serializers.ValidationError("User ID must be positive.")
        return value
