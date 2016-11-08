from table_talk.kafka_client import KafkaClient
import sys
import _thread


class KafkaChat(KafkaClient):
    def __init__(self, topic=''):
        KafkaClient.__init__(self, topic=topic)
        self._command_dict = {'exit': {'post': '{} has exited the room'.format(self._name),
                                       'print': '\nExiting channel {}\n\n'.format(self._topic),
                                       'function': sys.exit},
                              'channels': {'post': '',
                                         'print': '\n CHANNELS: \n',
                                         'function': self.show_channels},
                              'users': {'post': '',
                                        'print': '\n USERS: \n',
                                        'function': self.show_users}
                              }

    def parse_commands(self, command):
        com_dict = self._command_dict
        if com_dict.get(command, {'None': 'None'}) != {'None': 'None'}:
            self.post_to_topic(com_dict[command]['post'])
            sys.stdout.write(com_dict[command]['print'])
            com_dict[command]['function']()
        else:
            pass

    def open_chat_session(self):
        _thread.start_new_thread(self.read_from_topic, ())
        if self._topic == self._name:
            sys.stdout.write('\nSuccessfully opened personal channel, you will see all private messages here\n'
                             'To privately message another person, post to their channel by using BLA BLA BLA')
        else:
            sys.stdout.write(('Successfully opened channel {}, you can start messaging now'.format(self._topic)))
        while True:
            user = self._name
            response = input("\n{0}: ".format(user))
            self.parse_commands(response)
            self.post_to_topic(response)

    def show_channels(self):
        channels = self.get_current_topics()

        for channel in channels:
            if channel[:5] != 'user-':
                sys.stdout.write(channel + '\n')
            else:
                pass

    def show_users(self):
        channels = self.get_current_topics()
        for channel in channels:
            if channel[:5] == 'user-':
                sys.stdout.write(channel + '\n')
            else:
                pass

