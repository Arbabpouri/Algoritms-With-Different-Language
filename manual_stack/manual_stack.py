from typing import Any


class ManualStack:


    def __init__(self, max_size: int):
        self.MAX_SIZE = max_size
        self.__top = -1
        self.__stack = []

    @property
    def is_empty(self) -> bool:
        return self.__top == -1
    
    @property
    def is_full(self) -> bool:
        return self.__top == self.MAX_SIZE - 1
    
    def push(self, item: Any) -> bool:
        
        if not self.is_full:
            self.__top += 1
            self.__stack.append(item)
            return True
        print("stack is full")
        return False
    
    def pop(self) -> Any:

        if not self.is_empty:
            item = self.__stack[self.__top]
            self.__top -= 1
            return item
        
        print("stack is empty")
            

if __name__ == "__main__":
    my_stack = ManualStack(20)
