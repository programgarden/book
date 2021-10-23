import requests

class MyMsg():
    def send_msg(self, msg=""):
        response = requests.post(
            'https://slack.com/api/chat.postMessage',
            headers={
                'Authorization': 'Bearer '+'토큰 복사하기'
            },
            data={
                'channel':'#realmessage',
                'text':msg
            }
        )
        print(response)

MyMsg().send_msg(msg="슬랙으로 전송하기")