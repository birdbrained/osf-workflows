# -*- coding: utf-8 -*-
"""Workflow Views"""


import json
import copy

from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_json_api.views import RelationshipView

from workflow.models import Workflow
from workflow.models import Case
from workflow.models import Action
from workflow.models import Parameter
from workflow.models import Condition
from workflow.models import Message
from workflow.models import Value

from workflow.serializers import WorkflowSerializer
from workflow.serializers import CaseSerializer
from workflow.serializers import ActionSerializer
from workflow.serializers import ParameterSerializer
from workflow.serializers import ConditionSerializer
from workflow.serializers import MessageSerializer
from workflow.serializers import ValueSerializer
from workflow.serializers import UserSerializer
from workflow.serializers import GroupSerializer


class WorkflowViewSet(ModelViewSet):

    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer


class CaseViewSet(ModelViewSet):

    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def perform_create(self, serializer):
        case = serializer.save()
        case.workflow.update(case)


class ActionViewSet(ModelViewSet):

    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ParameterViewSet(ModelViewSet):

    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class ConditionViewSet(ModelViewSet):

    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class MessageViewSet(ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = self.queryset
        case = self.request.query_params.get('filter[case]', None)
        if case is not None:
            queryset = queryset.filter(case=case)
        return queryset


class ValueViewSet(ModelViewSet):

    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#
