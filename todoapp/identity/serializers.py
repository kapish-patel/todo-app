from rest_framework import serializers

from .models import Identity



class IdentitySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    categories = serializers.JSONField()

    class Meta:
        model = Identity
        fields = ('id', 'username', 'email', 'password', 'categories')

    def validate_categories(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Categories should be a list.")
        return value

    def create(self, validated_data):
        return Identity.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        password = validated_data.get('password', None)
        if password:
            instance.password = password
        
        instance.categories = validated_data.get('categories', instance.categories)
        instance.save()
        return instance