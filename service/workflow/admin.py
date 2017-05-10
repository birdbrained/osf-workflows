from django.contrib.admin import register
from django.contrib.admin import ModelAdmin
from django.contrib.admin import SimpleListFilter

from django.core.exceptions import FieldError

from django.contrib.auth.models import User, Group

from workflow.models import Workflow
from workflow.models import Case
from workflow.models import Action
from workflow.models import Parameter
from workflow.models import Condition
from workflow.models import Message
from workflow.models import Value


class WorkflowListFilter(SimpleListFilter):
    """Filter an object list by workflow"""

    title = 'Workflow'
    parameter_name = 'workflow'
    default_value = None

    def lookups(self, request, model_admin):
        """Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar."""

        return sorted([(str(workflow.id), workflow.name)
            for workflow in Workflow.objects.all()])

    def queryset(self, request, queryset):
        """Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`."""

        if self.value():
            try:
                return queryset.filter(workflow_id=self.value())
            except FieldError:
                return queryset.filter(workflows=self.value())
        return queryset


class CaseListFilter(SimpleListFilter):
    """Filter an object list by workflow"""

    title = 'Case'
    parameter_name = 'case'
    default_value = None

    def lookups(self, request, model_admin):
        """Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar."""

        return sorted([(str(case.id), case.id)
            for case in Case.objects.all()])

    def queryset(self, request, queryset):
        """Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`."""

        if self.value():
            try:
                return queryset.filter(case_id=self.value())
            except FieldError:
                return queryset.filter(case=self.value())
        return queryset


@register(Workflow)
class WorkflowAdmin(ModelAdmin):

    list_display = [
        'name',
        'description'
    ]


@register(Case)
class CaseAdmin(ModelAdmin):

    def get_workflow_name(self, object):
        return object.workflow.name

    get_workflow_name.admin_order_field = 'name'  # Allows column order sorting
    get_workflow_name.short_description = 'Workflow Name'  # Renames column head

    list_display = [
        "id",
        "get_workflow_name"
    ]

    list_filter = [
        WorkflowListFilter
    ]


@register(Action)
class ActionAdmin(ModelAdmin):

    list_display = [
        'name',
        'description',
        'action_function'
    ]

    list_filter = [
        WorkflowListFilter
    ]


@register(Parameter)
class ParameterAdmin(ModelAdmin):

    list_display = [
        "name",
        "view"
    ]

    list_filter = [
        WorkflowListFilter
    ]


@register(Value)
class ValueAdmin(ModelAdmin):

    list_display = [
        'case',
        'parameter',
        'value',
        'state'
    ]

    list_filter = [
        WorkflowListFilter,
        CaseListFilter
    ]


@register(Condition)
class ConditionAdmin(ModelAdmin):

    def get_action_name(self, object):
        return object.action.name

    def get_data_name(self, object):
        return object.data.name

    def get_workflow_name(self, object):
        return object.workflow.name

    get_action_name.admin_order_field = 'name'
    get_data_name.admin_order_field = 'name'
    get_workflow_name.admin_order_field = 'name'

    get_action_name.short_descripition = 'Action'
    get_data_name.short_description = 'Data'
    get_workflow_name.short_description = 'Workflow Name'

    list_display = [
        'get_data_name',
        'state',
        'type',
        'get_action_name',
        'get_workflow_name'
    ]

    list_filter = [
        WorkflowListFilter
    ]


@register(Message)
class MessageAdmin(ModelAdmin):

    def get_case_id(self, object):
        return object.case.id

    get_case_id.admin_order_field = 'id'
    get_case_id.short_description = 'case'

    list_display = [
        'id',
        'case',
        'timestamp'
    ]

    list_filter = [
        WorkflowListFilter,
        CaseListFilter
    ]


#
