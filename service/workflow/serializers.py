# -*- coding: utf-8 -*-
"""Workflow Serializers"""


from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework.serializers import CharField
from rest_framework.serializers import JSONField
from rest_framework_json_api.serializers import ModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField

from workflow.models import Workflow
from workflow.models import Case
from workflow.models import Action
from workflow.models import Parameter
from workflow.models import Condition
from workflow.models import Message
from workflow.models import Value


class WorkflowSerializer(ModelSerializer):
    """Workflow Serializer"""

    name = CharField(max_length=128)
    actions = ResourceRelatedField(
        queryset=Action.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        resource_name = 'workflows'
        model = Workflow
        fields = [
            'id',
            'name',
            'description',
            'group',
            'cases',
            'conditions',
            'actions'
        ]


class CaseSerializer(ModelSerializer):
    """Case Serializer"""

    parameters = ResourceRelatedField(
        queryset=Parameter.objects.all(),
        many=True,
        required=False
    )

    workflow = ResourceRelatedField(
        queryset=Workflow.objects.all(),
        required=True
    )

    messages = ResourceRelatedField(
        queryset=Message.objects.all(),
        many=True,
        required=False
    )

    values = ResourceRelatedField(
        queryset=Value.objects.all(),
        many=True,
        required=False
    )

    initial_state = JSONField(
        required=False
    )

    class Meta:
        resource_name = 'cases'
        model = Case
        fields = [
            'id',
            'parameters',
            'values',
            'workflow',
            'initial_state',
            'messages'
        ]


class ActionSerializer(ModelSerializer):
    """Action Serializer"""

    name = CharField(max_length=128)

    group = ResourceRelatedField(
        queryset=Group.objects.all()
    )

    ouput = ResourceRelatedField(
        queryset=Parameter.objects.all()
    )

    conditions = ResourceRelatedField(
        queryset=Condition.objects.all()
    )

    messages = ResourceRelatedField(
        queryset=Message.objects.all()
    )

    class Meta:
        resource_name = 'cases'
        model = Action
        fields = [
            'id',
            'name',
            'description',
            'group',
            'action_function',
            'output',
            'conditions',
            'messages'
        ]



class ParameterSerializer(ModelSerializer):
    """Parameter Serializer"""

    cases = ResourceRelatedField(
        many=True,
        queryset=Case.objects.all()
    )

    sources = ResourceRelatedField(
        many=True,
        queryset=Action.objects.all()
    )

    conditions = ResourceRelatedField(
        many=True,
        queryset=Condition.objects.all()
    )

    values = ResourceRelatedField(
        many=True,
        queryset=Value.objects.all()
    )

    workflows = ResourceRelatedField(
        many=True,
        queryset=Workflow.objects.all()
    )

    class Meta:
        resource_name = 'parameters'
        model = Parameter
        fields = [
            'id',
            'name',
            'view',
            'cases',
            'values',
            'messages',
            'sources',
            'workflows',
            'conditions'
        ]


class ValueSerializer(ModelSerializer):
    """Value Serializer"""

    value = JSONField(
        required=False
    )

    state = CharField(
        max_length=128
    )

    case = ResourceRelatedField(
        queryset=Case.objects.all()
    )

    parameter = ResourceRelatedField(
        queryset=Parameter.objects.all(),
    )

    class Meta():
        resource_name = 'values'
        model = Value
        fields = [
            'id',
            'value',
            'state',
            'case',
            'parameter'
        ]


class ConditionSerializer(ModelSerializer):
    """Condition Serializer"""

    parameter = ResourceRelatedField(
        queryset=Parameter.objects.all()
    )

    action = ResourceRelatedField(
        queryset=Action.objects.all()
    )

    workflow = ResourceRelatedField(
        queryset=Workflow.objects.all()
    )

    class Meta:
        resource_name = 'condition'
        model = Condition
        fields = [
            'id',
            'parameter',
            'data',
            'state',
            'type',
            'action',
            'workflow'
        ]


class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        resource_name = 'messages'
        model = Message
        fields = [
            'id',
            'message_type',
            'timestamp',
            'view',
            'case',
            'origin',
            'response',
            'content',
            'section'
        ]


class UserSerializer(ModelSerializer):
    """User Serializer"""

    class Meta:
        resource_name = 'users'
        model = User
        fields = [
            'id',
            'username'
        ]


class GroupSerializer(ModelSerializer):
    """Group Serializer"""

    class Meta:
        resource_name = 'groups'
        model = Group
        fields = [
            'name'
        ]


#
