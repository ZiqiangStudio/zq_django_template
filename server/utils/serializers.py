from rest_framework.serializers import ListSerializer


class LimitedListSerializer(ListSerializer):
    """
    用于外键序列化过滤
    """

    def filter_data(self, data):
        return data.filter(approval=True, public=True)[:5]

    def to_representation(self, data):
        data = self.filter_data(data)
        return super().to_representation(data)
