from itertools import count

# Grammar Productions
productions = [
    ["P'", 'P'],
    ['P', 'S'],
    ['S', 'A'],
    ['S', 'while', 'M', 'B', 'do', 'M', 'S'],
    ['M'],
    ['A', 'id', '=', 'E'],
    ['E', 'E', '+', 'T'],
    ['E', 'E', '-', 'T'],
    ['E', 'T'],
    ['T', 'T', '*', 'F'],
    ['T', 'T', '/', 'F'],
    ['T', 'F'],
    ['F', '(', 'E', ')'],
    ['F', 'id'],
    ['B', 'B', '||', 'M', 'C'],
    ['B', 'C'],
    ['C', 'C', '&&', 'M', 'D'],
    ['C', 'D'],
    ['D', '!', 'G'],
    ['D', 'G'],
    ['G', 'id'],
    ['G', 'id', "relop", 'id']
]

# Bottom-Up Parser Table
action_table= {
    (0, 'id'): 's5',
    (0, 'while'): 's4',
    (1, '$'): 'acc',
    (2, '$'): 'r1',
    (3, '$'): 'r2',
    (4, 'id'): 'r4',
    (4, '!'): 'r4',
    (4, 'while'): 'r4',
    (5, '='): 's7',
    (6, 'id'): 's13',
    (6, '!'): 's11',
    (7, '('): 's17',
    (7, 'id'): 's18',
    (8, 'do'): 's19',
    (8, '||'): 's20',
    (9, '&&'): 's21',
    (9, 'do'): 'r15',
    (9, '||'): 'r15',
    (10, '&&'): 'r17',
    (10, 'do'): 'r17',
    (10, '||'): 'r17',
    (11, 'id'): 's13',
    (12, '&&'): 'r19',
    (12, 'do'): 'r19',
    (12, '||'): 'r19',
    (13, '&&'): 'r20',
    (13, 'do'): 'r20',
    (13, '||'): 'r20',
    (13, 'relop'): 's23',
    (14, '$'): 'r5',
    (14, '+'): 's24',
    (14, '-'): 's25',
    (15, '$'): 'r8',
    (15, ')'): 'r8',
    (15, '*'): 's26',
    (15, '+'): 'r8',
    (15, '-'): 'r8',
    (15, '/'): 's27',
    (16, '$'): 'r11',
    (16, ')'): 'r11',
    (16, '*'): 'r11',
    (16, '+'): 'r11',
    (16, '-'): 'r11',
    (16, '/'): 'r11',
    (17, '('): 's17',
    (17, 'id'): 's18',
    (18, '$'): 'r13',
    (18, ')'): 'r13',
    (18, '*'): 'r13',
    (18, '+'): 'r13',
    (18, '-'): 'r13',
    (18, '/'): 'r13',
    (19, 'id'): 'r4',
    (19, '!'): 'r4',
    (19, 'while'): 'r4',
    (20, 'id'): 'r4',
    (20, '!'): 'r4',
    (20, 'while'): 'r4',
    (21, 'id'): 'r4',
    (21, '!'): 'r4',
    (21, 'while'): 'r4',
    (22, '&&'): 'r18',
    (22, 'do'): 'r18',
    (22, '||'): 'r18',
    (23, 'id'): 's32',
    (24, '('): 's17',
    (24, 'id'): 's18',
    (25, '('): 's17',
    (25, 'id'): 's18',
    (26, '('): 's17',
    (26, 'id'): 's18',
    (27, '('): 's17',
    (27, 'id'): 's18',
    (28, ')'): 's37',
    (28, '+'): 's24',
    (28, '-'): 's25',
    (29, 'id'): 's5',
    (29, 'while'): 's4',
    (30, 'id'): 's13',
    (30, '!'): 's11',
    (31, 'id'): 's13',
    (31, '!'): 's11',
    (32, '&&'): 'r21',
    (32, 'do'): 'r21',
    (32, '||'): 'r21',
    (33, '$'): 'r6',
    (33, ')'): 'r6',
    (33, '*'): 's26',
    (33, '+'): 'r6',
    (33, '-'): 'r6',
    (33, '/'): 's27',
    (34, '$'): 'r7',
    (34, ')'): 'r7',
    (34, '*'): 's26',
    (34, '+'): 'r7',
    (34, '-'): 'r7',
    (34, '/'): 's27',
    (35, '$'): 'r9',
    (35, ')'): 'r9',
    (35, '*'): 'r9',
    (35, '+'): 'r9',
    (35, '-'): 'r9',
    (35, '/'): 'r9',
    (36, '$'): 'r10',
    (36, ')'): 'r10',
    (36, '*'): 'r10',
    (36, '+'): 'r10',
    (36, '-'): 'r10',
    (36, '/'): 'r10',
    (37, '$'): 'r12',
    (37, ')'): 'r12',
    (37, '*'): 'r12',
    (37, '+'): 'r12',
    (37, '-'): 'r12',
    (37, '/'): 'r12',
    (38, '$'): 'r3',
    (39, '&&'): 's21',
    (39, 'do'): 'r14',
    (39, '||'): 'r14',
    (40, '&&'): 'r16',
    (40, 'do'): 'r16',
    (40, '||'): 'r16'
}

goto_table = {
    (0, 'A'): '3',
    (0, 'P'): '1',
    (0, 'S'): '2',
    (4, 'M'): '6',
    (6, 'B'): '8',
    (6, 'C'): '9',
    (6, 'D'): '10',
    (6, 'G'): '12',
    (7, 'E'): '14',
    (7, 'F'): '16',
    (7, 'T'): '15',
    (11, 'G'): '22',
    (17, 'E'): '28',
    (17, 'F'): '16',
    (17, 'T'): '15',
    (19, 'M'): '29',
    (20, 'M'): '30',
    (21, 'M'): '31',
    (24, 'F'): '16',
    (24, 'T'): '33',
    (25, 'F'): '16',
    (25, 'T'): '34',
    (26, 'F'): '35',
    (27, 'F'): '36',
    (29, 'A'): '3',
    (29, 'S'): '38',
    (30, 'C'): '39',
    (30, 'D'): '10',
    (30, 'G'): '12',
    (31, 'D'): '40',
    (31, 'G'): '12'
}

keywords = ['while', 'do']
operators = ['+', '-', '*', '/', '&&', '||', '!', 'relop', '$', '=']




class StackItem:
    def __init__(self, name, place="-", quad=None):
        self.name = name
        self.place = place
        self.quad = quad
        self.next = []
        self.true = []
        self.false = []
  


class TAC_generator:

    def __init__(self, input_string, productions, action_table, goto_table):
        self.code = []
        self.temp_counter = count()
        self.productions = productions
        self.action_table = action_table
        self.goto_table = goto_table
        self.input_tokens = input_string.split()
        

    def newtemp(self):
        return f'T{next(self.temp_counter)}'

    def nextQuad(self):
        return len(self.code)

    def backpatch(self, to_back_patch, quad):
        for line_no in to_back_patch:
            self.code[line_no] += " " +str(quad)

    def gen(self, *args):
        self.code.append(" ".join(args))

    def semantic_action(self, production_index, LHS, RHS):
        match production_index:
            case 1:
                S = RHS.pop()
                self.backpatch(S.next, self.nextQuad())
                return StackItem("P")

            case 2:
                return StackItem("S")
            
            case 3:
                RHS.pop()
                M1 = RHS.pop()
                B = RHS.pop()
                RHS.pop()
                M2 = RHS.pop()
                S1 = RHS.pop()

                self.backpatch(B.true, M2.quad)
                self.backpatch(S1.next, self.nextQuad())
                S = StackItem("S")
                S.next = B.false
                self.gen("goto", str(M1.quad))
                return S
            
            case 4:
                return StackItem("M",quad=self.nextQuad())
            
            case 5:
                id = RHS.pop()
                RHS.pop()
                E = RHS.pop()
                self.gen(id.place, "=", E.place)
                return StackItem("A")
            
            case 6:
                E1 = RHS.pop()
                RHS.pop()
                T = RHS.pop()
                E = StackItem(LHS, self.newtemp())
                self.gen(E.place, "=", E1.place, "+", T.place)
                return E

            case 7:
                E1 = RHS.pop()
                RHS.pop()
                T = RHS.pop()
                E = StackItem(LHS, self.newtemp())
                self.gen(E.place, "=", E1.place, "-", T.place)
                return E

            case 8:
                E = RHS.pop()
                T = StackItem(LHS, E.place)
                return T
            
            case 9:
                T1 = RHS.pop()
                RHS.pop()
                F = RHS.pop()
                T = StackItem(LHS, self.newtemp())
                self.gen(T.place, "=", T1.place, "*", F.place)
                return T

            case 10:
                T1 = RHS.pop()
                RHS.pop()
                F = RHS.pop()
                T = StackItem(LHS, self.newtemp())
                self.gen(T.place, "=", T1.place, "/", F.place)
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
                
            case 14:
                B = RHS.pop()
                RHS.pop()
                M = RHS.pop()
                C = RHS.pop()

                self.backpatch(B.false, M.quad)
                
                B1 = StackItem("B")
                B1.true = list(set(C.true + B.true))
                B1.false = list(C.false)
                return B1
            
            case 15:
                C = RHS.pop()
                
                B = StackItem(LHS)
                B.true = list(C.true)
                B.false = list(C.false)
                return B
            
            case 16:
                C = RHS.pop()
                RHS.pop()
                M = RHS.pop()
                D = RHS.pop()

                self.backpatch(C.true, M.quad)
                
                C1 = StackItem("C")
                C1.false = list(set(C.false + D.false))
                C1.true = list(D.true)
                return C1
            
            case 17:
                D = RHS.pop()
                
                C = StackItem(LHS)
                C.true = list(D.true)
                C.false = list(D.false)
                return C
            
            case 18:
                RHS.pop()
                G = RHS.pop()
                
                D = StackItem("D")
                D.true = list(G.false)
                D.false = list(G.true)
                return D
            
            case 19:
                G = RHS.pop()
                
                D = StackItem("D")
                D.true = list(G.true)
                D.false = list(G.false)
                return D
            
            case 20:
                id = RHS.pop()
                
                E = StackItem("E")
                E.true = [self.nextQuad()]
                E.false = [self.nextQuad()+1]

                self.gen("if", id.place, "goto")
                self.gen("goto")

                return E
            
            case 21:
                id1 = RHS.pop()
                RHS.pop()
                id2 = RHS.pop()

                G = StackItem("G")
                G.true = [self.nextQuad()]
                G.false = [self.nextQuad()+1]

                self.gen("if", id1.place, "relop", id2.place, "goto")
                self.gen("goto")

                return G


    def generateTAC(self):
        if self.parse_input_tokens():
            i = 0
            for line in self.code:
                print(f"{i:>4}:  ", end="")
                print(line)
                i+=1
            print(f"{i:>4}:  ")

    def parse_input_tokens(self):
        stack = [0]
        self.input_tokens.append('$')

        i = 0
        try:
            while True:
                state = stack[-1]
                token = self.input_tokens[i]

                if token not in keywords + operators + ['$']:
                    action = self.action_table[(state, "id")]
                else:
                    action = self.action_table[(state, token)]

                if action[0] == 's':
                    if token not in keywords + operators + ['$']:
                        stack.append(StackItem("id", token))
                    else:
                        stack.append(StackItem(token))

                    stack.append(int(action[1:]))
                    i += 1

                elif action[0] == 'r':
                    production_index = int(action[1:])
                    production = self.productions[production_index]
                    popped_items = []
                    for _ in range(len(production)-1):
                        stack.pop()
                        popped_items.append(stack.pop())
                    
                    state = stack[-1]
                    stack.append(self.semantic_action(production_index, production[0], popped_items))
                    stack.append(int(self.goto_table[(state, production[0])]))

                elif action == 'acc':
                    return True
                
                else:
                    print("[ERROR] INVALID STREAM OF TOKENS")
                    return False
                
        except:
            print("[ERROR] INVALID STREAM OF TOKENS")
            return False


# Input to be parsed
input_string = "while i relop j || j relop k do while i relop k do while j do i = i + 1 * j"

tac = TAC_generator(input_string, productions, action_table, goto_table)
tac.generateTAC()



