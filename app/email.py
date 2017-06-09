from config import Config
from flask import render_template
import requests


def send_email(to_list, subject, template, **kwargs):
    key = Config.MAIL_API
    sandbox = Config.MAIL_DOMAIN

    if not key or not sandbox:
        raise BaseException('Please configure MAIL_API and MAIL_DOMAIN')
    request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)
    for to in to_list:
        requests.post(request_url, auth=('api', key), data={
            'from': Config.MAIL_NAME + '<' + Config.MAIL_ADDRESS + '>',
            'to': to,
            'subject': subject,
            'text': render_template(template + '.txt', **kwargs),
            'html': render_template(template + '.html', **kwargs)
        })
