
""" https://github.com/jaraco/wolframalpha """

import wolframalpha 

input = raw_input("Question: ")
app_id = "VKAVEK-RKGXQHL64W"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
print type(answer)

a = str(answer)
print type(a)