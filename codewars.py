# Sum of pairs
def sum_pairs(ints, s):
    complement_dict = {}
    
    for i in ints:
        if i in complement_dict:
            return [s-i, i]
        else:
            complement_dict[s - i] = i
            
    return None

# Convert to camel case
def to_camel_case(text):
    list = [x for x in text]
    if len(list) !=0:
        for i in range(len(list)):
            if list[i] in ('_', '-'):
                list[i+1] = list[i+1].upper()
    list = ''.join([i for i in list if i not in('_', '-')])
    return list

# array difference
def array_diff(a, b):
    return [x for x in a if x not in b]

# Duplicate encode
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# Replace With Alphabet Position
def alphabet_position(text):
    
    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])