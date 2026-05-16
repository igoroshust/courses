import dis

def multiply(a, b):
    result = a * b
    return result

dis.dis(multiply)