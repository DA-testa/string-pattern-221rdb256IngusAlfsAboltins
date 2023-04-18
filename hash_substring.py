#python3
def read_input():
     # this function needs to aquire input both from keyboard and file
     
    # as before, use capital i (input from keyboard) and capital f (input from file) to 
    input_type = input()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
      
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    p = 1000000007
    x = 263
    result = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = 0
    t_hash = 0
    x_p = 1
    for i in range(p_len):
        p_hash = (p_hash + ord(pattern[i]) * x_p) % p
        t_hash = (t_hash + ord(text[i]) * x_p) % p
        if i != p_len - 1:
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

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
