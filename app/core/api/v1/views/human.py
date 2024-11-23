from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.v1.serializers.human import HumanSerializer
from core.models import Human
from core.services.ancestors import find_ancestors


class HumanViewSet(ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all().order_by('id')
    permission_classes = (AllowAny,)


    @action(methods=['GET'], detail=True, url_path='ancestors')
    def ancestors(self, request, pk=None):
        try:
            depth = int(request.query_params['depth'])
        except (KeyError, ValueError):
            depth = None

        human: Human = self.get_object()
        human_data = find_ancestors(human, depth=depth)

        return Response(human_data)
