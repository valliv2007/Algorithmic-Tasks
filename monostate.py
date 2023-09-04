class ThreadData:
    _shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }
 
    def __init__(self):
        self.__dict__ = self._shared_attrs

th1 = ThreadData()
th2 = ThreadData()
print(ThreadData._shared_attrs)
print(th1._shared_attrs)
print(th2._shared_attrs)
print(th1.__dict__)
print(th2.__dict__)
th2.id = 3
print(th1.__dict__)
print(th2.__dict__)
print(ThreadData._shared_attrs)
print(th1._shared_attrs)
print(th2._shared_attrs)