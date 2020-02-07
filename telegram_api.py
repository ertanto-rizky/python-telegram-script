import requests

def run():
    # Prepare bot token and chat id
    bot_token = '819495434:AAElFxIjLCzl6o0_4SwA_0xy3rH-gyvIXg0'
    chat_id = '698315134'
    
    # Compose message
    message = 'Insert message here'

    # Message get request
    message_request = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
        + str(chat_id) + '&parse_mode=Markdown&text=' + message
    
    # Send message
    res = requests.get(message_request)
    print('Message sent')
    print('Result: ', res)
        
if __name__ == '__main__':
    run()
