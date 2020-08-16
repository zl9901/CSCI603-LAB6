from ring_buffer import ring_buffer
class Queue:
    __slots__ = "q"

    def __init__(self,c):
        self.q=ring_buffer(c)

    def __str__(self):
        return str(self.q)

    def enqueue(self,Val):
        """
        this enqueue method of the Queue
        the function is to add the element into the Queue from the back
        """
        self.q.insert_keep_new(Val)

    def dequeue(self):
        """
        this dequeue method of the Queue
        the function is to remove the element  from the front of a Queue
        """
        self.q.remove_newest()

def test():
     hp=Queue(3)
     hp.enqueue(1)
     hp.enqueue(2)
     hp.enqueue(5)
     print("back is located at the rightmost")
     print("the capacity I defined is 3")
     print(hp)
     hp.dequeue()
     print("dequeue one element from the queue")
     print(hp)
     hp.enqueue(7)
     hp.enqueue(8)
     print("enqueue 7 first and then enqueue 8 into the queue")
     print("the result shown as followed")
     print(hp)




if __name__ == "__main__":
    test()