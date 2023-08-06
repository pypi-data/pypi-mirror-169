# Autocord

Autocord is a Python API wrapper for Discord centered around automation. Using Autocord, you can easily send messages, create tasks, and much more. The purpose of Autocord is to provide users with less hassle when using requests.

**Installing**
<br>
Requires `python>3.7`
<br>
`pip install autocord`

**Quick Example**
```py
# inialize autocord client
client = autocord.client('TOKEN')

# send the message 'hi'
client.SEND_MESSAGE('Hi', CHANNEL_ID)

# create a task that sends the message 'hi' every 5 seconds
id = client.CRATE_TASK({'Hi', 5}, CHANNEL_ID)
print(client.ongoing_tasks)

# end the task
client.END_TASK(id)
```