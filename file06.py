def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    n = 0
    m = 0
    l = []
    for i in range(len(data)):
        if data[i].index():
            m+=1
        else:
            n+=1
    l.append(m)
    l.append(n)
    return l

f = open("txt_file/data06.txt")
a = f.read()
print(main(a))
# Read data from file