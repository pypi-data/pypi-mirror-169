def list_to_str(list):
    key=''.join([str(x) for x in list])
    return key

def getfileformat(file):
    size = len(file)
    output = []
    check = 0
    file = file[::-1]
    for i in range(0,size):
        work = file[check]
        output.append(work)
        if work == '.':
            output= list_to_str(output)
            output = output[::-1]
            return output
        check += 1