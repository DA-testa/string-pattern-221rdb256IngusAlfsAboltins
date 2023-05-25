import os

def read_input():
    input_type = input().strip()
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_type == 'F':
        this_dir = os.path.dirname(__file__)
        rel_p = "tests/06"
        abs_fp = os.path.join( this_dir, rel_p)
        with open(abs_fp, "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        raise ValueError("Invalid input type")
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 10000000019
    x = 256
    result = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = 0
    t_hash = 0
    x_p = 1
    for i in range(p_len):
        p_hash = (p_hash * x + ord(pattern[i])) % p
        t_hash = (t_hash * x + ord(text[i])) % p
    for i in range(p_len - 1):
        x_p = (x_p * x) % p
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i + p_len] == pattern:
                result.append(i)
        if i != t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * x_p) % p
            t_hash = (t_hash * x) % p
            t_hash = (t_hash + ord(text[i + p_len])) % p
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
