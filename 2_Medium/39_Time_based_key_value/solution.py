import bisect

class TimeMap:

    def __init__(self):
        #key:'x' -> value: [value, timestamp]
        self.dictionary ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dictionary:
            self.dictionary[key] = [[],[]]
        self.dictionary[key][0].append(value)
        self.dictionary[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ''
        index = bisect.bisect_right(self.dictionary[key][1], timestamp)
        if index == 0:
            return ''
        return self.dictionary[key][0][index-1]


obj = TimeMap()
obj.set('foo','bar2',2)
obj.set('foo','bar5',5)
obj.set('foo','bar10',10)
obj.set('foo2','bar1',1)
print(obj.get('foo',1))    #return ''
print(obj.get('foo',2))    #return 'bar2'
print(obj.get('foo',4))    #return 'bar2'
print(obj.get('foo',6))    #return 'bar5'
print(obj.get('foo',9))    #return 'bar5'
print(obj.get('foo',10))    #return 'bar10'
print(obj.get('foo',100))    #return 'bar10'