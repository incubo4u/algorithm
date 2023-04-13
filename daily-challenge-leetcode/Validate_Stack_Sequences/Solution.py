class Solution:

    def validateStackSequences(self, pushed, popped) -> bool:
        s = []
        for n in pushed:
            s.append(n)
            while popped and s and s[-1] == popped[0]:
                s.pop()
                popped.pop(0)
        return not popped
