from typing import Any

class Queue:

    def __init__(self, max_size: int):
        self.__MAX_SIZE = max_size
        self.__front = -1
        self.__rear = -1
        self.__queue = []

    @property
    def is_empty(self) -> bool:
        return self.__front == self.__rear

    @property
    def is_full(self) -> bool:
        return self.__rear == self.__MAX_SIZE - 1


    def add(self, item: Any) -> bool:
        
        if not self.is_full:
            self.__rear += 1
            self.__queue.append(item)
            return True
        
        print("queue is full")
        return False

    def pop(self) -> Any:
        
        if not self.is_empty:
            item = self.__queue[self.__front]
            self.__front += 1
            return item
        
        print("queue is empty")
        return None

    def process(self) -> Any:
        if self.__front > -1:
            item =  self.__queue[self.__front]
            self.__front -= 1
            return item
        
        print("queue is empty or not item in queue")
        return None



if __name__ == "__main__":
    my_queue = Queue(20)
    