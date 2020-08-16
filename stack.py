from ring_buffer import ring_buffer
class Stack:
    __slots__ = "r"

    def __init__(self,c):
        self.r=ring_buffer(c)
        """ 
        此处对ring_buffer(c)的调用与ring_buffer类中的test方法无关
        """

    def __str__(self):
        return str(self.r)

    def push(self,val):
        """
        this push method of the Stack
        the function is to add the element into the Stack from the top
        """
        self.r.insert_keep_old(val)

    def pop(self):
        """
        this pop method of the Stack
        the function is to remove the element  from the top of the Stack
        """
        self.r.remove_newest()

def test():
    s=Stack(3)
    s.push(3)
    s.push(1)
    print("top is located at the leftmost")
    print("the capacity I defined is 3")
    print(s)
    s.push(4)
    print("top is located at the leftmost")
    print(s)
    s.pop()
    print("pop one element from the stack")
    print(s)
    s.push(5)
    s.push(6)
    print("push 5 first and then push 6 into the stack")
    print("the result shown as followed")
    print(s)





if __name__ == "__main__":
    test()