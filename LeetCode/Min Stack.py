class MinStack(object):

    def __init__(self):
        self.stack = []
        self.help_stack = []
    def push(self, val):
        self.stack.append(val)
        if not self.help_stack:
            self.help_stack.append(val)
        else:
            min_val = min(val, self.help_stack[-1])
            self.help_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.help_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.help_stack[-1]