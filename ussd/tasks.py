import requests
from structlog import get_logger

import structlog
structlog.configure(logger_factory=structlog.stdlib.LoggerFactory())


def http_task(request_conf):
    requests.request(**request_conf)


def report_session(session_id, screen_content):
    # to avoid circular import
    from ussd.core import ussd_session, UssdHandlerAbstract

    logger = get_logger(__name__).bind(
        action="report_session_task", session_id=session_id
    )

    ussd_report_session_data = screen_content['ussd_report_session']

    session = ussd_session(session_id)

    if session.get('posted'):
        return

    request_conf = UssdHandlerAbstract.render_request_conf(
        session,
        ussd_report_session_data['request_conf']
    )


    UssdHandlerAbstract.make_request(
        http_request_conf=request_conf,
        response_session_key_save=ussd_report_session_data['session_key'],
        session=session,
        logger=logger
    )

    # check if it is the desired effect
    for expr in ussd_report_session_data['validate_response']:
        if UssdHandlerAbstract.evaluate_jija_expression(
            expr['expression'],
            session=session
        ):
            session['posted'] = True
            session.save()
            return
