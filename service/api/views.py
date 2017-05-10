
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'workflows': reverse('workflow-list', request=request, format=format),
        'cases': reverse('case-list', request=request, format=format),
        'actions': reverse('action-list', request=request, format=format),
        'parameters': reverse('parameter-list', request=request, format=format),
        'values': reverse('value-list', request=request, format=format),
        'conditions': reverse('condition-list', request=request, format=format),
        'messages': reverse('message-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
    })

