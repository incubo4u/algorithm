# Definition for polynomial singly-linked list.
class PolyNode:

    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:

    def addPoly(self, p1: 'PolyNode', p2: 'PolyNode') -> 'PolyNode':
        # poly = defaultdict(int)
        # while p1:
        #     poly[p1.power] += p1.coefficient
        #     p1 = p1.next
        # while p2:
        #     poly[p2.power] += p2.coefficient
        #     p2 = p2.next
        # dummy = PolyNode()
        # head = dummy
        # for power , coefficient in sorted(poly.items(),reverse=True):
        #     if coefficient:
        #         dummy.next = PolyNode(coefficient,power)
        #         dummy = dummy.next
        # return head.next

        dummy = PolyNode()
        head = dummy
        while p1 and p2:
            if p1.power == p2.power:
                if p1.coefficient + p2.coefficient:
                    dummy.next = PolyNode(p1.coefficient + p2.coefficient,
                                          p1.power)
                    dummy = dummy.next
                p1, p2 = p1.next, p2.next
            elif p1.power < p2.power:
                if p2.coefficient:
                    dummy.next = p2
                    dummy = dummy.next
                p2 = p2.next
                dummy.next = None
            else:
                if p1.coefficient:
                    dummy.next = p1
                    dummy = dummy.next
                p1 = p1.next
                dummy.next = None

        if p1:
            dummy.next = p1
        elif p2:
            dummy.next = p2

        return head.next
