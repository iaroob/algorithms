from algoritmia.datastructures.sets import ISet
from algoritmia.datastructures.lists import LinkedList

class ListSet(ISet): #[listset
    def __init__(self, it: "Iterable<T>"=[], createList: "->IList<T>"=list):
        self.createList = createList
        self._list = self.createList()
        for item in it:
            if item not in self._list:
                self._list.add(item)

    def add(self, item: "T"):
        if item not in self._list: self._list.append(item)

    def add_unchecked(self, item: "T"):
        self._list.add(item)

    def remove(self, item: "T"):
        if item not in self._list: raise KeyError(item)
        self._list.remove(item)

    def discard(self, item: "T"):
        try:
            self._list.remove(item)
        except ValueError:
            pass
        
    def __contains__(self, item: "T") -> "bool":
        return item in self._list

    def __len__(self) -> "int":
        return len(self._list)

    def clear(self):
        self._list = self.createList()

    def __iter__(self) -> "Iterable<T>":
        for item in self._list: yield item

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, self._list) #]listset
    
class LinkedListSet(ListSet): #[linkedlistset
    def __init__(self, it: "Iterable<T>"=[]):
        super().__init__(it, createList=LinkedList) #]linkedlistset