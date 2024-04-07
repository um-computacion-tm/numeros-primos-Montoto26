def is_primo (value):
    div = 2
    while div < value:
        if value % div == 0:
            return False
        div += 1
    return True        
