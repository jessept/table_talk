from chat import KafkaChat
import time
import argparse
parser = argparse.ArgumentParser(description='Chat via local Kafka instance.')
parser.add_argument('--channel', '-t', type=str, help='Channel to subscribe/write to')
parser.add_argument('--channel_list_flag', '-ts', action='store_true', help='List active channels')
parser.add_argument('--user_list_flag', '-u', action='store_true', help='List active users')

args = parser.parse_args()
channel = args.channel
channel_list_flag = args.channel_list_flag
user_list_flag = args.user_list_flag


def main():
    if not channel:
        connection = KafkaChat()
    else:
        connection = KafkaChat(topic=channel)

    if channel_list_flag:
        connection.parse_commands('channels')
    elif user_list_flag:
        connection.parse_commands('users')
    else:
        print('Starting up app!')
        for sec in range(5, 0, -1):
            time.sleep(0.5)
            print('{}'.format(sec))
        connection.open_chat_session()

if __name__ == '__main__':
    main()


