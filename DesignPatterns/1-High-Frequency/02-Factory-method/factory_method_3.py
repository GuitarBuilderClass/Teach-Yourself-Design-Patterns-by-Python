#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from enum import Enum


class Object(Enum):
    STANDALONE = 0
    NETWORKING = 1


class DataObjectFactory:
    # 戻り値となるクラスを DataObject クラスを継承しているものと入れ替えれば
    # Client クラス側は DataObject.create() を呼び出すだけでよく、変更後の影響範囲は少ない

    @staticmethod
    def create(data_type):
        if data_type == Object.STANDALONE:
            return FileDataObject()
        elif data_type == Object.NETWORKING:
            return DbDataObject()


class DataObject(metaclass=ABCMeta):
    @abstractmethod
    def read_data_object(self, num):
        pass


class FileDataObject(metaclass=ABCMeta):

    def __init__(self):
        self.data_list = list()

        with open('test.csv', 'r') as f:
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

    def __init__(self):
        self.factory = DataObjectFactory.create(Object.STANDALONE)

    def operating(self, num):
        # DataObject.create() で FileDataObject を呼び出しているため
        # 呼び出し元のクラスは FileDataObject から別のクラスへ容易に変更ができる
        # つまり、 Client クラスはFileDataObject の存在を知らなくても FileDataObject を利用できる
        # コーディングする時は DataObject.create() を呼び出すだけなので Client クラス側には変更の影響が少なくなる
        person = self.factory.read_data_object(num)
        return person


if __name__ == '__main__':
    client = Client()

    i = 0
    while True:
        try:
            print(client.operating(i), end="")
            i += 1
        except IndexError:
            break

    row = client.operating(1)
    print("\n")
    print(row)
