from typing import Any

class CircularQueue:

    def __init__(self, max_size: int):
        self.__MAX_SIZE = max_size
        self.__front = 0
        self.__rear = 0
        self.__queue = []
        for i in range(0, self.__MAX_SIZE):
            self.__queue.append(0)


    @property
    def is_empty(self) -> bool:
        return self.__front == self.__rear


    @property
    def is_full(self) -> bool:
        return self.__front == (self.__rear + 1) % self.__MAX_SIZE


    def add(self, item: Any) -> bool:

        if not self.is_full:
            self.__rear = (self.__rear + 1) % self.__MAX_SIZE
            self.__queue[self.__rear] = item
            return True
        
        print("queue is full")
        return False


    def pop(self) -> Any:
        
        if not self.is_empty:
            self.__front = (self.__front + 1) % self.__MAX_SIZE
            item = self.__queue[self.__front]
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
    my_queue = CircularQueue(20)
    