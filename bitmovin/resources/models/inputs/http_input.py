from . import AbstractInput


class HTTPInput(AbstractInput):

    def __init__(self, host, username=None, password=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.host = host
        self.username = username
        self.password = password

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        http_input = HTTPInput(
            host=host, username=username, password=password, id_=id_)
        return http_input
