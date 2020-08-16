from node import LinkedNode
class ring_buffer:

    __slots__ = "head","tail","c"

    def __init__(self,c):
        self.head=None
        self.tail=None
        self.c=c

    def isEmpty(self):
        """
        to test whether the linkedlist is empty or not
        """
        return self.head is None and self.tail is None

    def insert_keep_old(self,Val):
        """
        this method is equal to the push method in the Stack
        if the capacity is larger than the capacity we defined
        execute the else statement
        """
        if self.capacity() < self.c:
            node=LinkedNode(Val)
            if self.isEmpty():
                self.head=self.tail=node
            else:
                node.next=self.head
                self.head=node
        else:
            node = LinkedNode(Val)
            node.next = self.head
            self.head = node

            self.remove_newest()

    def insert_keep_new(self,Val):
        """
        this method is equal to the enqueue method in the Queue
        if the capacity is larger than the capacity we defined
        execute the else statement
        """
        if self.capacity()<self.c:
            node = LinkedNode(Val)
            if self.isEmpty():
                self.head = self.tail = node
            else:
                self.tail.next=node
                self.tail=node
        else:
            node = LinkedNode(Val)
            self.tail.next = node
            self.tail = node

            self.remove_newest()



    def size(self):
        """
        return the size of a Stack or a Queue
        """
        count=0
        pointer=self.head
        while pointer is not None:
            pointer=pointer.next
            count+=1
        return count

    def find(self,val):
        """
        find the value we are looking for and return the cursor
        """
        cursor=None
        compass=self.head
        while compass is not None:
            if compass.value is val:
                cursor=compass
            compass=compass.next
        return cursor

    def replace(self,cursor,val):
        """
        replace the value we want to replace using the cursor
        """
        if cursor is not None:
            cursor.value=val

    def remove_oldest(self):
        """
        this method is equal to the dequeue method in the Queue
        """

        light = self.head
        while light.next is not self.tail:
            light = light.next
        self.tail = light
        self.tail.next = None

    def remove_newest(self):
        """
        this method is equal to the pop method in the Stack
        """
        self.head = self.head.next

    def capacity(self):
        return self.size()


    def __str__(self):
        """
        the toString method used to test whether the result is true or not
        """

        result = "["
        index=self.head
        while(index is not None):
            result+=" "+str(index.value)
            index=index.next
        result+="]"
        return result



def test():
    rb=ring_buffer(4)
    print(rb)
    # for value in 1, 2, 3:
    #     rb.insert_keep_old( value )
    #     print( rb )
    rb.insert_keep_new(1)
    rb.insert_keep_old(3)
    rb.insert_keep_new(2)


    print(rb.size())
    # cursor=rb.find(2)
    # rb.replace(cursor,5)
    # print(rb)
    # rb.remove_oldest()
    # print(rb)
    # rb.remove_newest()
    # print(rb)
    print(rb.capacity())
    print(rb)
    rb.insert_keep_new(5)
    print(rb)
    rb.insert_keep_new(6)
    print(rb)
    rb.insert_keep_new(7)
    print(rb)

if __name__ == "__main__":
    test()
