
VALID_CHARS = ['T', 'F', '&', '|', '(', ')', ' ']
alternate_char = ['T', 'F', '&', '|']

def operate(op1, op2, token):
    if op1 == "T" and op2 == "T" and token == "&":
        return True
    if op1 == "T" and op2 == "F" and token == "&":
        return False
    if op1 == "F" and op2 == "T" and token == "&":
        return False
    if op1 == "F" and op2 == "F" and token == "&":
        return False
    if op1 == "T" and op2 == "T" and token == "|":
        return True
    if op1 == "T" and op2 == "F" and token == "|":
        return True
    if op1 == "F" and op2 == "T" and token == "|":
        return True
    if op1 == "F" and op2 == "F" and token == "|":
        return False
    

class Tokenizer(object):
    def __init__(self, string):
        self.__string = string.strip()
        self.__curr_idx = 0
        self.__has_next = len(self.__string) > 0
    def peek(self):
        old_curr_idx = self.__curr_idx
        old_has_next = self.__has_next
        next_val = self.next()
        self.__curr_idx = old_curr_idx
        self.__has_next = old_has_next
        return next_val
    def next(self):
        if not self.has_next():
            raise ValueError('String has no additional characters to tokenize.')
        elif self.__string[self.__curr_idx] not in VALID_CHARS:
            raise ValueError('Invalid character in given string.')
        elif self.__string[self.__curr_idx] == ' ':
            self.__curr_idx += 1
            return self.next()
        else:
            self.__curr_idx += 1
            if self.__curr_idx >= len(self.__string):
                self.__has_next = False
            return_val = self.__string[self.__curr_idx - 1]
            if return_val == 'T':
                return_val = True
            elif return_val == 'F':
                return_val = False
            return return_val
    def has_next(self):
        return self.__has_next

class Evaluator(object):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.root = Node(None)

    def evaluate_expression(self):
        return self.parse_or()

    # You can use the above class and compelte the following function.
    def parse_or(self):
        x = self.parse_token()
        if x == 'T':
            return (True)
        else:
            return(True)

# You can use the above class and compelte the following function.
    def parse_and(self):
        x = self.parse_token()
        if x == '&':
            pass

# You can use the above class and compelte the following function.
    def parse_paren(self):
        x = self.parse_token()
        if x == '(':
            pass
        x = self.parse_token()
        if x == ')':
            pass
        
    def parse_token(self):
        return self.tokenizer.next()
   

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    # creates the expression tree
    def create_tree (self,expr):
        self.root = Node()
        stack = Stack()
        curr_node = self.root
        express = expr.split()
        for i in range(len(express)):
            token = express[i]
            #Creates left child, pushes current node onto the stack and makes it the lchild
            if token == "(":
                curr_node.lChild = Node()
                stack.push(curr_node)
                curr_node = curr_node.lChild
            #Pushes current data onto the stack and sets current to rchild
            elif token in VALID_CHARS:
                curr_node.data = token
                stack.push(curr_node)
                curr_node.rChild = Node()
                curr_node = curr_node.rChild
            #If the stack is not empty, make current node parent node
            elif token == ")":
                if stack.is_empty() is not True:
                    curr_node = stack.pop()
                else:
                    return
            else:
                if '.' in token:
                    curr_node.data = float(token)
                else:
                    curr_node.data = int(token)
                if stack.is_empty() is not True:
                    curr_node = stack.pop()

# Do not change the main function!
def main():
    boolean_expr = input()
    print(Evaluator(Tokenizer(boolean_expr)).evaluate_expression())
if __name__ == "__main__":
    main()