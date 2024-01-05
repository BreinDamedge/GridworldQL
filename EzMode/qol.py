def progress_bar(max:int, at:int, min:int=0, width:int=20, add_percent:bool=True) -> str:
    fpercent = ((at-min)/(max-min))
    eqs = ['=']*(int(width*fpercent))
    spaces = [' ']*(width-len(eqs))
    out = '|'
    for tok in eqs:
        out += tok
    for tok in spaces:
        out += tok
    out += f'|{int(fpercent*100)}'
    if add_percent:
        out += '%'
    return out


def print_progress_bar(max:int, at:int, min:int=0, width:int=20, add_percent:bool=True, end_newline_=False):
    if end_newline_ and int(((at-min)/(max-min))*100) == 100:
        print(progress_bar(max, at, min, width, add_percent))
    else:
        print(progress_bar(max, at, min, width, add_percent), end="\r")