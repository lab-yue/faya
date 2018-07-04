# -*- coding: UTF-8 -*-
from multiprocessing import Pool, Manager


class Multithread(object):
    def __init__(self):
        self.queue = _Queue()

    @staticmethod
    def execute(f, data_list):
        pool = Pool()
        pool.map(f, data_list)
        pool.close()
        pool.join()


class _Queue(object):
    def __init__(self):
        self.__q = Manager().Queue()
        self.__f = None
        self.__dl = []
        self.__len = 0

    def __put_q(self):
        [self.__q.put(each) for each in self.__dl]

    def execute(self, f, datalist):
        self.__dl = datalist
        self.__len = range(0, len(datalist))
        self.__f = f
        pool = Pool()
        self.__put_q()
        pool.map(self._dummy, self.__len)
        pool.close()
        pool.join()

    def _dummy(self, placeholder):
        self.__f(self.__q.get())


if __name__ == '__main__':
    l = range(0, 5)


    def p(n):
        print(n)


    mp = Multithread()
    mp.execute(p, l)

    print('=' * 10 + 'q' + '=' * 10)

    mp.queue.execute(p, l)
