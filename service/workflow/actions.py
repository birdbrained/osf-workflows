from workflow import models


def request_data(case, action):
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

