from math import lcm

class Monkey():
    def __init__(self, id, items, op1, op2, operation, test, iftrue, iffalse):
        self.id = id
        self.items = items
        self.op1 = op1
        self.op2 = op2
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.business = 0

    def __str__(self):
        return f'Monkey {self.id}: {str(self.items)} | Business: {self.business}'

    def inspect_item(self, item):
        op2 = ''
        if self.op2 == 'old':
            op2 = int(item)
        else:
            op2 = int(self.op2)
        op1 = int(item)

        return self.update_item(op1, op2)

    def update_item(self, op1, op2):
        if self.operation == '*':
            return op1*op2
        elif self.operation == '+':
            return op1+op2

    def copy(self):
        return Monkey(self.id, self.items, self.op1, self.op2, self.operation, self.test, self.iftrue, self.iffalse)


with open('problem11.txt', 'r') as input:
    lines = input.readlines()
    monkeys = []
    for i in range(0, len(lines), 7):
        id = int(i / 7)
        items_line = lines[i+1].replace('\n', '').split(' ')
        items = []
        for j in range(4, len(items_line)):
            items.append(int(items_line[j].replace(',', '')))
        operation_line = lines[i+2].replace('\n', '').split(' ')
        op1 = operation_line[5]
        op2 = operation_line[7]
        operation = operation_line[6]
        test = int(lines[i+3].replace('\n', '').split(' ')[5])
        iftrue = int(lines[i+4].replace('\n', '').split(' ')[-1])
        iffalse = int(lines[i+5].replace('\n', '').split(' ')[-1])
        monkey = Monkey(id, items, op1, op2, operation, test, iftrue, iffalse)
        monkeys.append(monkey)
    
    N_CYCLES = 20 # 20 for part 1
    for cycle in range(0, N_CYCLES):
        for monkey in monkeys:
            print(monkey)
            while len(monkey.items):
                monkey.business += 1
                item = monkey.items.pop(0)
                print(f' Monkey inspect an item with a worry level of {item}')
                item = monkey.inspect_item(item)
                print(f'  Worry level is multiplied by {monkey.op2} to {item}')
                item = int(item / 3)
                print(f'  Monkey gets bored with item. Worry level is divided by 3 to {item}')
                if item % monkey.test == 0:
                    print(f'  Current worry level is divisible by {monkey.test}')
                    monkeys[monkey.iftrue].items.append(item)
                    print(f'  Item with worry level {item} is thrown to monkey {monkey.iftrue}')
                else:
                    print(f'  Current worry level is not divisible by {monkey.test}')
                    monkeys[monkey.iffalse].items.append(item)
                    print(f'  Item with worry level {item} is thrown to monkey {monkey.iffalse}')

    business_level = 1
    for monkey in monkeys:
        print(monkey)
        business_level = business_level * monkey.business

    best = sorted([m.business for m in monkeys], key=abs, reverse=True)
    print('2-highest Business level: ', best[0]*best[1])

    print("================== PART TWO ===============")
    # i have to duplicate code, no time for editing code today :/
    monkeys = []
    for i in range(0, len(lines), 7):
        id = int(i / 7)
        items_line = lines[i+1].replace('\n', '').split(' ')
        items = []
        for j in range(4, len(items_line)):
            items.append(int(items_line[j].replace(',', '')))
        operation_line = lines[i+2].replace('\n', '').split(' ')
        op1 = operation_line[5]
        op2 = operation_line[7]
        operation = operation_line[6]
        test = int(lines[i+3].replace('\n', '').split(' ')[5])
        iftrue = int(lines[i+4].replace('\n', '').split(' ')[-1])
        iffalse = int(lines[i+5].replace('\n', '').split(' ')[-1])
        monkey = Monkey(id, items, op1, op2, operation, test, iftrue, iffalse)
        monkeys.append(monkey)

    N_CYCLES = 10000 # 20 for part 1
    modulo = lcm(*[m.test for m in monkeys])
    print(lcm)
    for cycle in range(0, N_CYCLES):
        for monkey in monkeys:
            # print(monkey)
            while len(monkey.items):
                monkey.business += 1
                item = monkey.items.pop(0)
                # print(f' Monkey inspect an item with a worry level of {item}')
                item = monkey.inspect_item(item)
                # print(f'  Worry level is multiplied by {monkey.op2} to {item}')
                item = item % modulo
                # print(f'  Monkey gets bored with item. Worry level is divided by 3 to {item}')
                if item % monkey.test == 0:
                    # print(f'  Current worry level is divisible by {monkey.test}')
                    monkeys[monkey.iftrue].items.append(item)
                    # print(f'  Item with worry level {item} is thrown to monkey {monkey.iftrue}')
                else:
                    # print(f'  Current worry level is not divisible by {monkey.test}')
                    monkeys[monkey.iffalse].items.append(item)
                    # print(f'  Item with worry level {item} is thrown to monkey {monkey.iffalse}')

    business_level = 1
    for monkey in monkeys:
        print(monkey)
        business_level = business_level * monkey.business

    best = sorted([m.business for m in monkeys], key=abs, reverse=True)
    print('2-highest Business level: ', best[0]*best[1])