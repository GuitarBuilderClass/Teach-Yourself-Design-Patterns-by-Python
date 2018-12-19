#! /usr/bin/env python3


class PM(object):

    def __init__(self):
        self.se = SE()

    def request_report(self):
        print("PM -> SE: 報告書作成依頼")
        self.se.request_report()
        print("PM: 受領")


class SE(object):

    def __init__(self):
        self.pg = PG()

    def request_report(self):
        print("SE -> PG: 調査依頼")
        self.pg.make_report()
        print("SE -> PM: 報告書")


class PG(object):

    @staticmethod
    def make_report():
        print("PG -> SE: 調査結果")


pm = PM()
pm.request_report()
