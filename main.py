from webserver import keep_alive
import requests

channelID = 987640402481930301
headers = {
    "authorization":
    "OTk4OTYzNTcxNzE3MzIwNzE1.GhIfic.NLgadn-YwcZHGfCNINWDELUYLPlYUOktx789Tg"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
