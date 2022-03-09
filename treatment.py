# ---Encoding/decoding---#

def encodeLab(tab):
    lab = {}
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            lab[(i, j)] = []
            l = lab[(i, j)]
            if 'h' in tab[i][j]:
                l += [(i-1, j)]
            if 'd' in tab[i][j]:
                l += [(i, j+1)]
            if 'b' in tab[i][j]:
                l += [(i+1, j)]
            if 'g' in tab[i][j]:
                l += [(i, j-1)]
    lab["nlines"] = len(tab)
    lab["ncolumns"] = len(tab[0])
    return lab


def decodeLab(lab):    
    tab = [["" for j in range(lab["ncolumns"])] for i in range(lab["nlines"])]
    for i in range(len(t)):
        for j in range(len(t[i])):
            if (i-1, j) in lab[(i, j)]:
                tab[i][j] += 'h'
            if (i, j+1) in lab[(i, j)]:
                tab[i][j] += 'd'
            if (i+1, j) in lab[(i, j)]:
                tab[i][j] += 'b'
            if (i, j-1) in lab[(i, j)]:
                tab[i][j] += 'g'
    return t


#---Misc---#

def adjacent(cell):
    
    return [
        (cell[0]-1, cell[1]  ),
        (cell[0]  , cell[1]-1),
        (cell[0]+1, cell[1]  ),
        (cell[0]  , cell[1]+1)
    ]


#---Check---#

def get_cell_occurence(lab, cell=(0, 0), previous=None, markList=None):
    if markList == None:
        markList = [[0 for j in range(lab["ncolumns"])] for i in range(lab["nlines"])]
    y, x = cell[0], cell[1]
    markList[y][x]+=1
    if markList[y][x] >= 2:
        return markList
    for adj in adjacent(cell):
        if adj in lab[cell] and adj != previous:
            markList = get_cell_occurence(lab, cell = adj, previous = cell, markList=markList)
    return markList

def is_true_lab(lab):
    for line in get_cell_occurence(lab):
        for cell in line:
            if cell !=1:
                return False
    return True


#---Generation---#