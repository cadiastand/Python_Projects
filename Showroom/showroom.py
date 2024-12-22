class Node:
    def __init__(self, nextNode, prevNode, data) -> None:
        self.data = data
        self.nextNode= prevNode
        self.prevNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

class Car:
    def __init__(self, identification : str , name : str, brand, price : int, active=True) -> None:
        self.brand = brand
        self.price = price
        self.identification = identification
        self.name = name
        self.active = active


db = LinkedList()


def init(cars):
    clean()
    for i in cars:
        add(i)

def add(car):
    new_node = Node(None, None, car)
    if db.head is None:
        db.head = new_node
        return

    current = db.head
    previous = None

    while current is not None and current.data.price <= car.price:
        previous = current
        current = current.nextNode

    if previous is None:
        new_node.nextNode = db.head
        db.head.prevNode = new_node
        db.head = new_node
    else:
        new_node.nextNode = current
        new_node.prevNode = previous
        previous.nextNode = new_node
        if current:
            current.prevNode = new_node



def updateName(identification, name):
    pointer = db.head
    while (pointer is not None):
        if (identification == pointer.data.identification):
            pointer.data.name = name
            return
        pointer = pointer.nextNode


def updateBrand(identification, brand):
    pointer = db.head
    while (pointer is not None):
        if (identification == pointer.data.identification):
            pointer.data.brand = brand
            return
        pointer = pointer.nextNode


def activateCar(identification):
    pointer = db.head
    while (pointer is not None):
        if (identification == pointer.data.identification):
            pointer.data.active = True
            return
        pointer = pointer.nextNode


def deactivateCar(identification):
    pointer = db.head
    while (pointer is not None):
        if (identification == pointer.data.identification):
            pointer.data.active = False
            return
        pointer = pointer.nextNode


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    pointer = db.head
    price_summary = 0
    while (pointer is not None):
        if  ( pointer.data.active == True):
            price_summary = price_summary + pointer.data.price
        pointer = pointer.nextNode
    return price_summary

def clean():
    db.head = None
