from itertools import count

temp_counter = count()
# Grammar Productions
productions = [
    ["P'", 'P'],
    ['P', 'S'],
    ['S', 'A'],
    ['S', 'while', 'M', 'E', 'do', 'M', 'S'],
    ['M'],
    ['A', 'id', '=', 'E'],
    ['E', 'E', '+', 'T'],
    ['E', 'E', '-', 'T'],
    ['E', 'T'],
    ['T', 'T', '*', 'F'],
    ['T', 'T', '/', 'F'],
    ['T', 'F'],
    ['F', '(', 'E', ')'],
    ['F', 'id']
]

# Bottom-Up Parser Table
action_table={
    (0,"while"):"s4",
    (0,"id"):"s5",
    (1,"$"):"acc",
    (2,"$"):"r1",
    (3,"$"):"r2",
    (4,"while"):"r4",
    (4,"id"):"r4",
    (4,"("):"r4",
    (5,"="):"s7",
    (6,"id"):"s12",
    (6,"("):"s11",
    (7,"id"):"s12",
    (7,"("):"s11",
    (8,"do"):"s14",
    (8,"+"):"s15",
    (8,"-"):"s16",
    (9,"do"):"r8",
    (9,"+"):"r8",
    (9,"-"):"r8",
    (9,"*"):"s17",
    (9,"/"):"s18",
    (9,")"):"r8",
    (9,"$"):"r8",
    (10,"do"):"r11",
    (10,"+"):"r11",
    (10,"-"):"r11",
    (10,"*"):"r11",
    (10,"/"):"r11",
    (10,")"):"r11",
    (10,"$"):"r11",
    (11,"id"):"s12",
    (11,"("):"s11",
    (12,"do"):"r13",
    (12,"+"):"r13",
    (12,"-"):"r13",
    (12,"*"):"r13",
    (12,"/"):"r13",
    (12,")"):"r13",
    (12,"$"):"r13",
    (13,"+"):"s15",
    (13,"-"):"s16",
    (13,"$"):"r5",
    (14,"while"):"r4",
    (14,"id"):"r4",
    (14,"("):"r4",
    (15,"id"):"s12",
    (15,"("):"s11",
    (16,"id"):"s12",
    (16,"("):"s11",
    (17,"id"):"s12",
    (17,"("):"s11",
    (18,"id"):"s12",
    (18,"("):"s11",
    (19,"+"):"s15",
    (19,"-"):"s16",
    (19,")"):"s25",
    (20,"while"):"s4",
    (20,"id"):"s5",
    (21,"do"):"r6",
    (21,"+"):"r6",
    (21,"-"):"r6",
    (21,"*"):"s17",
    (21,"/"):"s18",
    (21,")"):"r6",
    (21,"$"):"r6",
    (22,"do"):"r7",
    (22,"+"):"r7",
    (22,"-"):"r7",
    (22,"*"):"s17",
    (22,"/"):"s18",
    (22,")"):"r7",
    (22,"$"):"r7",
    (23,"do"):"r9",
    (23,"+"):"r9",
    (23,"-"):"r9",
    (23,"*"):"r9",
    (23,"/"):"r9",
    (23,")"):"r9",
    (23,"$"):"r9",
    (24,"do"):"r10",
    (24,"+"):"r10",
    (24,"-"):"r10",
    (24,"*"):"r10",
    (24,"/"):"r10",
    (24,")"):"r10",
    (24,"$"):"r10",
    (25,"do"):"r12",
    (25,"+"):"r12",
    (25,"-"):"r12",
    (25,"*"):"r12",
    (25,"/"):"r12",
    (25,")"):"r12",
    (25,"$"):"r12",
    (26,"$"):"r3",
}

goto_table = {
    (0,"P") : 1,
    (0,"S") : 2,
    (0,"A") : 3,
    (4,"M") : 6,
    (6,"E") : 8,
    (6,"T") : 9,
    (6,"F") : 10,
    (7,"E") : 13,
    (7,"T") : 9,
    (7,"F") : 10,
    (11,"E") :19,
    (11,"T") :9,
    (11,"F") : 10,
    (14,"M") : 20,
    (15,"T"): 21,
    (15,"F"): 10,
    (16,"T"): 22,
    (16,"F"): 10,
    (17,"F"): 23,
    (18,"F"): 24,
    (20,"S"): 26,
    (20,"A") :3,
}

code = []

class StackItem:
    def __init__(self, name, place="-", quad=None):
        self.name = name
        self.place = place
        self.quad = quad
        self.next = []
        self.true = []
        self.false = []
  
def newtemp():
    return f'T{next(temp_counter)}'

def nextQuad():
    return len(code)

def backpatch(to_back_patch, quad):
    for line_no in to_back_patch:
        code[line_no] += str(quad)

def gen(*args):
    code.append(" ".join(args))

def semantic_action(production_index, LHS, RHS):
    match production_index:
        case 1:
            S = RHS.pop()
            backpatch(S.next, nextQuad())

        case 2:
            return StackItem("S")
        
        case 3:
            RHS.pop()
            M1 = RHS.pop()
            E = RHS.pop()
            RHS.pop()
            M2 = RHS.pop()
            S1 = RHS.pop()
            
            backpatch(E.true, M2.quad)
            backpatch(S1.next, M1.quad)
            S = StackItem("S")
            S.next = E.false
            gen("goto", str(M1.quad))
            return S
        case 4:
            return StackItem("M",quad=nextQuad())
        
        case 5:
            id = RHS.pop()
            RHS.pop()
            E = RHS.pop()
            gen(id.place, "=", E.place)
            return StackItem("A")
        case 6:
            E1 = RHS.pop()
            RHS.pop()
            T = RHS.pop()
            E = StackItem(LHS, newtemp())
            gen(E.place, "=", E1.place, "+", T.place)
            return E

        case 7:
            E1 = RHS.pop()
            RHS.pop()
            T = RHS.pop()
            E = StackItem(LHS, newtemp())
            gen(E.place, "=", E1.place, "-", T.place)
            return E

        case 8:
            E = RHS.pop()
            T = StackItem(LHS, E.place)
            return T
        
        case 9:
            T1 = RHS.pop()
            RHS.pop()
            F = RHS.pop()
            T = StackItem(LHS, newtemp())
            gen(T.place, "=", T1.place, "*", F.place)
            return T

        case 10:
            T1 = RHS.pop()
            RHS.pop()
            F = RHS.pop()
            T = StackItem(LHS, newtemp())
            gen(T.place, "=", T1.place, "/", F.place)
            return T
        
        case 11:
            F = RHS.pop()
            T = StackItem(LHS, F.place)
            return T
        
        case 12:
            E = RHS.pop()
            F = StackItem(LHS, E.place)
            return F
        
        case 13:
            id = RHS.pop()
            F = StackItem(LHS, id.place)
            return F
            
            


def parse_input_tokens(input_tokens):
    stack = [0]
    input_tokens.append('$')
    i = 0
    while True:
        state = stack[-1]
        token = input_tokens[i]

        if token in ['a', 'b', 'c', 'd', 'e', 'x']:
            action = action_table[(state, "id")]
        else:
            action = action_table[(state, token)]

        if action[0] == 's':
            if token in ['a', 'b', 'c', 'd', 'e', 'x']:
                stack.append(StackItem("id", token))
            else:
                stack.append(StackItem(token))

            stack.append(int(action[1:]))
            i += 1
        elif action[0] == 'r':
            production_index = int(action[1:])
            production = productions[production_index]
            popped_items = []
            for _ in range(len(production)-1):
                stack.pop()
                popped_items.append(stack.pop())
            
            state = stack[-1]
            stack.append(semantic_action(production_index, production[0], popped_items))
            stack.append(int(goto_table[(state, production[0])]))

        elif action == 'acc':
            return True
        else:
            return False

# Input to be parsed

input_string = "while a do x = a + b * c * d"
input_tokens = input_string.split()

print(parse_input_tokens(input_tokens))

i = 0
for line in code:
    print(f"{i}: ", end="")
    print(line)
    i+=1