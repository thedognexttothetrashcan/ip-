import random
from time import sleep, time


def total(fun):
    def wrap(*args, **kwargs):

        before = time()
        fun(*args, **kwargs)
        after = time()

        print("共执行", after-before)

    return wrap


@total
def play():

    print("开始干游戏了")

    sleep(random.randrange(10))

    print("玩累了不玩了")


@total
def eat(meat, drink="water"):

    print("准备吃", "准备喝", drink)

    sleep(random.randrange(10))

    print("吃累了，不吃了")


def control_upgrade_wrap(param):
    def control_upgrade(fun):

        def wrap():

            if random.randrange(10) > param:
                print("装备升级成功")
            else:
                fun()

        return wrap
    return control_upgrade


@control_upgrade_wrap(10)
def upgrade():

    print("装备准备升级")

    print("装备升级失败,变成了一堆废渣")


if __name__ == '__main__':
    # before = time()
    # play()
    # after = time()
    # print("共游戏", after - before)

    # play()

    # eat("牛肉", drink="二锅头")


    upgrade()