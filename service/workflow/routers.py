# -*- coding: utf-8 -*-
"""REST API URLs"""


from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers

from workflow.views import WorkflowViewSet
from workflow.views import CaseViewSet
from workflow.views import ActionViewSet
from workflow.views import ParameterViewSet
from workflow.views import ConditionViewSet
from workflow.views import ValueViewSet
from workflow.views import MessageViewSet
from workflow.views import GroupViewSet
from workflow.views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'workflows', WorkflowViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'parameters', ParameterViewSet)
router.register(r'conditions', ConditionViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'values', ValueViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)


#transition_router = routers.NestedSimpleRouter(router, r'transitions', lookup='transition')
#transition_router.register(r'prerequisites', views.transitions, base_name='task-prerequisite')
