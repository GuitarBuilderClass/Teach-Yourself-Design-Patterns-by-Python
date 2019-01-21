#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from typing import List

# クラス追加時に修正ミスで挙動がおかしくなるのを防ぎたい
#


class DataObject(metaclass=ABCMeta):
    @abstractmethod
    def fetch_data_object(self, num: int) -> str:
        # read_data_objectは抽象メソッドで、
        # 実際の処理は子メソッドで実装したものが実行される
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, id_num: int) -> str:
        return self.data_list[id_num]


class DBDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def fetch_data_object(self, id_num: int) -> str:
        pass


class DefaultDataObject(DataObject):
    """デバッグ用クラスを実装する"""

    def __init__(self) -> None:
        pass

    def fetch_data_object(self, id_num: int) -> str:
        pass


class DataObjectFactory(object, metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def create(self):
        pass
    #     if self._db_type == DbMode.STANDALONE:
    #         return FileDataObject()
    #     if self._db_type == DbMode.NETWORKING:
    #         return DbDataObject()
    #
    #     if self._db_type == DbMode.DEBUGGING: <- このように追加するとコード修正時に他の部分へ影響が出るかもしれない
    #         return DefaultDataObject()
    #
    # DataObjectFactory クラスは、パターン2ではオブジェクト生成の責任を負うクラスだったが
    # パターン3ではこれを ABC を用いてインターフェースにする
    #
    # Python で Java のインターフェースのように振る舞うのは Mix-In であり
    # ABC を用いると手っ取り早いみたい？
    #
    # > ABC は直接的にサブクラス化することができ、ミックスイン(mix-in)クラスのように振る舞います。
    # 出典: https://docs.python.org/ja/3.7/library/abc.html
    #
    # .register の使い方がよくわからん。


class FileDataObjectFactory(DataObjectFactory):
    def __init__(self) -> None:
        super().__init__()

    # インターフェースを使用して DataObject を生成する
    def create(self) -> FileDataObject:
        return FileDataObject()


class DBDataObjectFactory(DataObjectFactory):

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> DBDataObject:
        return DBDataObject()


class DefaultObjectFactory(DataObjectFactory):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> DefaultDataObject:
        return DefaultDataObject()


class Client:
    """DataObject側で行を取得できるようにしているので、このクラスで列指定とかしたい"""

    def __init__(self) -> None:
        pass


if __name__ == '__main__':

    client1: DataObject = FileDataObjectFactory().create()
    client2: DataObject = DBDataObjectFactory().create()
    client3: DataObject = DefaultObjectFactory().create()

    i = 0
    while True:
        try:
            print(client1.fetch_data_object(i), end="")
            i += 1
        except IndexError:
            break

    row = client1.fetch_data_object(3)
    print("\n")
    print(row)
