# -*- coding: utf-8 -*-
"""Workflow Models"""


from itertools import chain
from uuid import uuid1
from uuid import uuid4

from django.db import transaction
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model
from django.db.models import TextField
from django.db.models import UUIDField
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from workflow import actions
from workflow.utils import camelCase


def print_section_header(string):
    print('\n\n\033[38;2;230;223;196m\033[1m################################################################################')
    print('')
    print(f'{string}')
    print('################################################################################\033[0m\n\n')


def print_subheading_with_context(subheading, context):
    print('\n\n\033[38;2;230;223;196m\033[1m--------------------------------------------------------------------------------')
    print(f'\n{subheading}: \033[0m{context}\033[0m\n')


class ConditionException(Exception):
    pass


class Workflow(Model):
    """Workflow Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    name = CharField(max_length=128)
    description = TextField()

    group = ForeignKey(
        'auth.Group',
        default=1
    )

    parameters = ManyToManyField(
        'Parameter',
        related_name='workflows',
        blank=True
    )

    actions = ManyToManyField(
        'Action',
        related_name='workflows',
        null=True,
        blank=True
    )

    def update(self, case):
        print_section_header('Checking Actions')
        for action in self.actions.all():
            print_subheading_with_context('Action', action.name)
            try:
                if action.conditions.exists():
                    for condition in action.conditions.all():
                        print(f'\n\033[38;2;230;223;196mChecking condition: {condition}\033[0m')
                        print(f'{condition.state} ? {case.state.get(condition.id)}', end='')
                        parameter = condition.data
                        try:
                            value = parameter.values.get(case=case)
                        except:
                            value = Value()
                            value.parameter = parameter
                            value.state
                        if condition.state == value.state:
                            print(' ... \033[38;2;0;255;0m\033[1mOk\033[0m')
                            continue
                        print(' ... \033[38;2;255;0;0m\033[1mFailed\033[0m\n')
                        raise ConditionException
                    print('\n\033[38;2;0;255;0m\033[1m===== ACTION FIRED\n\033[0m')
                    getattr(actions, action.action_function)(case, action)
                else:
                    print('\n\033[94mNo conditions to check.\033[0m\n')
            except ConditionException:
                pass
        print_section_header('Finished Checking Actions')

    def __str__(self):
        return self.name


class Case(Model):
    """Case Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    parameters = ManyToManyField(
        'Parameter',
        related_name='cases',
        blank=True
    )

    content = JSONField(blank=True, default={})
    state = JSONField(blank=True, default={})

    workflow = ForeignKey(
        'Workflow',
        related_name='cases',
        blank=True,
        null=True
    )

    initial_state = JSONField(blank=True, default={})

    def __str__(self):
        return str(self.id.urn)


class Action(Model):
    """Action Model"""

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=128)
    description = TextField()
    group = ForeignKey('auth.Group', default=1)
    action_function = CharField(max_length=128)
    output = ForeignKey('Parameter', related_name='sources', blank=True)

    def __str__(self):
        return self.name


class Parameter(Model):
    """Parameter Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    name = CharField(
        max_length=128,
        null=True,
        blank=True
    )

    view = TextField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Value(Model):
    """Value Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    value = JSONField(
        null=True,
        blank=True
    )

    state = CharField(
        max_length=128,
        null=True,
        blank=True
    )

    parameter = ForeignKey(
        'Parameter',
        related_name='values'
    )

    case = ForeignKey(
        'Case',
        related_name='values'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.case.workflow.update(self.case)


class Condition(Model):
    """Condition Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    data = ForeignKey(
        'Parameter',
        related_name='conditions'
    )

    state = CharField(
        max_length=128,
        null=True,
        blank=True
    )

    type = CharField(
        max_length=1,
        choices=(
            ('E', 'Enable'),
            ('D', 'Disable')
        )
    )

    action = ForeignKey(
        'Action',
        related_name='conditions'
    )

    workflow = ForeignKey(
        'Workflow',
        related_name='conditions'
    )

    def __str__(self):
        return f'{self.action}: {self.type}  {self.data}  {self.state}'


class Message(Model):
    """Message Model"""

    id = UUIDField(
        primary_key=True,
        default=uuid1,
        editable=False
    )

    case = ForeignKey(
        'Case',
        related_name='messages'
    )

    origin = ManyToManyField(
        'Action',
        related_name='messages',
        default=None
    )

    section = CharField(
        max_length=128,
        default='default'
    )

    response = ForeignKey(
        'Parameter',
        related_name='messages',
        default=None,
        null=True
    )

    message_type = CharField(max_length=24)
    view = TextField(null=True, blank=True)
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message: {}'.format(self.id.urn)


#
