#! /usr/bin/env python3

# 状況:
# 私はフットサル場を経営している
# フットサルコートは一面しかない
# 予約システムを運用しているがダブルブッキングを避けたい


# パターン未適用の場合
class Scheduler:

    HOURS: int = 24

    def __init__(self):
        self.booking = []
        for i in range(Scheduler.HOURS):
            self.booking += " "

    def schedule(self):
        return self.booking

    def schedule(self, hour: int, person: str):
        self.booking[hour - 1] = person


scheduler = Scheduler()
print(f"初期値: {scheduler.booking}")

# 13時から大空さんたちが予約する
scheduler.schedule(13, "大空")
print(f"全体の予約状況: {scheduler.booking}")
