# -*- coding: utf-8 -*-
"""

Action Behaviors
================

Implementations for the various behaviors action objects may have.


"""

from workflow import models


def request_data(case, action):
    """Requests a piece of data by creating a message
    that is displayed by the submission form."""
    request_message = models.Message(
        message_type='Request',
        view=action.output.view,
        case=case,
        response=action.output,
        content='The data is requested',
        section='upload'
    )
    request_message.save()
    request_message.origin.add(action),

