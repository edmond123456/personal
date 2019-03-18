""" https://www.youtube.com/watch?v=cuKQ9w9nr1o"""

import requests
import json

web_hook_url = 'https://hooks.slack.com/services/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'

slack_msg ={'text': ' 飲み会やりたい'}

requests.post(web_hook_url,data=json.dumps(slack_msg))