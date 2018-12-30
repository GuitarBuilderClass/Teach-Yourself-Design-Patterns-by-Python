#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from enum import Enum, auto

# 読み込み対象ファイル
FILE = 'test.txt'


class DataObject(metaclass=ABCMeta):

    @abstractmethod
    def read_data_object(self, num):
        pass


# オブジェクト生成の責任を負うクラス
class DataObjectFactory(Enum):
    STANDALONE = auto()
    NETWORKING = auto()

    def __init__(self, object_type):
        self._type = object_type

    def create(self):
        if self._type == self.STANDALONE:
            return FileDataObject()
        if self._type == self.NETWORKING:
            return DbDataObject()

    def read_data_object(self, num):

class FileDataObject(DataObject):

    def __init__(self):
        self.data_list = list()

        with open(FILE, 'r') as f:
            for line in f:
                self.data_list.append(line)

    def read_data_object(self, row_num):
        return self.data_list[row_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self):
        # DBへの接続手続きなど
        pass

    def read_data_object(self, id_num):
        pass


class Client:

    def __init__(self, object_type):
        self.data_object = DataObjectFactory.create(object_type)

    def operating(self, num):
        person = self.data_object
        return person


if __name__ == '__main__':
    client = Client()

    i = 0
    while True:
        try:
            print(client.operating(i))
            i += 1
        except IndexError:
            break
