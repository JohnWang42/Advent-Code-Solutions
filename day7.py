import re

class Wire:
    def __init__(self, key1 = None, key2 = None, op = None, val = None):
        self.key1 = key1
        self.key2 = key2
        self.op = op
        self.val = val
    def resolve(self, wires):
        if(self.op == None):
            if(not isinstance(self.val, int) and not self.val.isdigit()):
                self.val = wires[self.val].resolve(wires)
            return str(self.val)
        elif(self.op == "NOT"):
            if(not self.key1.isdigit()):
                self.key1 = wires[self.key1].resolve(wires)
            return str(65535 - int(self.key1))
        elif(self.op in "LSHIFT RSHIFT AND OR"):
            if(not isinstance(self.key1, int) and not self.key1.isdigit()):
                self.key1 = wires[self.key1].resolve(wires)
            if(not isinstance(self.key2, int) and not self.key2.isdigit()):
                self.key2 = wires[self.key2].resolve(wires)
            if(self.op == "LSHIFT"):
                return int(self.key1) << int(self.key2)
            elif(self.op == "RSHIFT"):
                return int(self.key1) >> int(self.key2)
            elif(self.op == "AND"):
                return int(self.key1) & int(self.key2)
            elif(self.op == "OR"):
                return int(self.key1) | int(self.key2)

def process(storeList, data):
    for i, line in enumerate(data):
        ops = re.findall('([a-z0-9]{1,3})\s(AND|OR|LSHIFT|RSHIFT)\s([a-z0-9]{1,3})\s->\s([a-z]{1,3})', line)
        nt = re.findall('(NOT)\\s([a-z]{1,3})\\s->\\s([a-z]{1,3})', line)
        assign = re.findall('([a-z0-9]{1,5})\\s->\\s([a-z]{1,3})', line)
        tempWire = Wire()
        store = ''
        if(len(ops) > 0):
            tempWire.key1 = ops[0][0]
            tempWire.op = ops[0][1]
            tempWire.key2 = ops[0][2]
            store = ops[0][3]
        elif(len(nt) > 0):
            tempWire.op = "NOT"
            tempWire.key1 = nt[0][1]
            store = nt[0][2]
        elif(len(assign) > 0):
            tempWire.val = assign[0][0]
            store = assign[0][1]
        storeList[store] = tempWire

data = open('input-day7.txt', 'r').read().split('\n')
testData = ['123 -> x',
'456 -> y',
'x AND y -> d',
'x OR y -> e',
'x LSHIFT 2 -> f',
'y RSHIFT 2 -> g',
'NOT x -> h',
'NOT y -> i']
wires = {}
process(wires, data)
evalA = str(wires['a'].resolve(wires))
print "First Part 'A Evaluation': " + evalA

wires = {}
process(wires, data)
wires['b'] = Wire(None, None, None, evalA)
print "Second Part 'A Evaluation': " + str(wires['a'].resolve(wires))
