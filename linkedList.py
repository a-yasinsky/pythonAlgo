class Node:
    def __init__( self,  val) :
        self. data = val
        self. next = None

    def getData( self) :
        return self. data

    def getNext( self) :
        return self. next

    def setData( self,  val) :
        self. data = val

    def setNext( self,  val) :
        self. next = val

class LinkedList:
    def __init__( self) :
        self. head = None

    def isEmpty( self) :
        """Check if the list is empty"""
        return self. head is None

    def add( self,  item) :
        """Add the item to the list"""
        new_node = Node( item)
        new_node. setNext( self. head)
        self. head = new_node

    def size( self) :
        """Return the length/size of the list"""
        count = 0
        current = self. head
        while current is not None:
            count += 1
            current = current. getNext( )
        return count

    def search( self,  item) :
        """Search for item in list. If found, return True. If not found, return False"""
        current = self. head
        found = False
        while current is not None and not found:
            if current. getData( ) is item:
                found = True
            else:
                current = current. getNext( )
        return found
