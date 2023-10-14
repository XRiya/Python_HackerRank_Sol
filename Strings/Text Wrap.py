import textwrap

def wrap(string, max_width):
    wrapped_text = textwrap.wrap(string, width=max_width)
    
    # Join the wrapped lines with newline characters and return the result
    return '\n'.join(wrapped_text)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
