import ast
with open('problem13.txt', 'r') as input:
    lines = input.read().splitlines()
    pairs = [(ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])) for i in range(0, len(lines), 3)]

    def eval_lists(left, right):
        # print("Compare: ", left, right, type(left))
        len1 = len(left) if type(left) == list else 1
        len2 = len(right) if type(right) == list else 1
        for i in range(0, min(len1, len2)):
            #print(left[i], right[i])
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] > right[i]:
                    return False
                elif left[i] < right[i]:
                    return True
            elif type(left[i]) == list and type(right[i]) == int:
                #print("Left is list, right is not")
                return eval_lists(left[i], [right[i]])
            elif type(left[i]) == int and type(right[i]) == list:
                #print("Left is list, right is not")
                return eval_lists([left[i]], right[i])
            else:
                #print("Both are lists: ", left, right)
                result = eval_lists(left[i], right[i])
                if result is not None:
                    return result
            
        result = None
        if len1 < len2:
            result = True
        elif len1 > len2:
            result = False
        if left == right: # comment this block for part 1
            return True
        return result

    
    result = sum([i+1 for i, pair in enumerate(pairs) if eval_lists(pair[0], pair[1])])

    print(result)

    # ============ PART TWO ==============
    new1 = [[2]]
    new2 = [[6]]
    pairs += [(new1, new2)]
    lists = []
    for pair in pairs:
        lists.append(pair[0])
        lists.append(pair[1])

    def compare(item1, item2):
        evaluation = eval_lists(item1, item2)
        if evaluation:
            return -1
        elif not evaluation:
            return 1
        else:
            return 0

    # Calling
    from functools import cmp_to_key
    lists = sorted(lists, key=cmp_to_key(compare))
    print("Decoder key: ", (lists.index(new1)+1)*(lists.index(new2)+1))

    