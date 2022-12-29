import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    result = wrapper.wrap(string)
    return '\n'.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
