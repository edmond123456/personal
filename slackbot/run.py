"""
 https://www.youtube.com/watch?v=cuKQ9w9nr1o
https://api.slack.com/methods/chat.postMessage/test
https://api.slack.com/apps/AH25TSLQ4/general

"""

import requests
import json

web_hook_url = 'https://hooks.slack.com/services/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'

slack_msg ={'text': ' test'}

requests.post(web_hook_url,data=json.dumps(slack_msg))