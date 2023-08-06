def bar(total,amount,length,background='-',border='||',looks='█'):
    if amount > total:
        amount = total
    output = int(amount*100/total)
    progress = int(amount*length/total)
    background = background*(length-progress)
    looks = f'{looks}'*progress
    if output == 100:
        final = f"{border[0]}{looks + background}{border[1]} Complete"
    else:
        final = f"{border[0]}{looks + background}{border[1]} {output}%"
    return final