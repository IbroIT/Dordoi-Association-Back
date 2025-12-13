from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    work_time = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = [
            'id',
            'logo',
            'name',
            'email',
            'phone',
            'work_time',
            'tg_link',
            'wb_link',
            'ins_link',
        ]

    def get_name(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_name(language)
    def get_work_time(self, obj):
        language = self.context.get('language', 'ru')
        return obj.get_work_time(language)
    