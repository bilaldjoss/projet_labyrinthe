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

def merge_labs(lab1, lab2):
    lab = {}

    lab["ncolumns"] = max(lab1["ncolumns"], lab2["ncolumns"])
    lab["nlines"] = max(lab1["nlines"], lab2["nlines"])

    for y in range(lab["nlines"]):
        for x in range(lab["ncolumns"]):
            lab[(y, x)] = []
            if (y, x) in lab1.keys():
                for cell in lab1[(y, x)]:
                    if cell in lab2[(y, x)]:
                        lab[(y, x)].append(cell)
            if (y, x) in lab2.keys():
                for cell in lab2[(y, x)]:
                    if cell in lab1[(y, x)] and cell not in lab[(y, x)]:
                        lab[(y, x)].append(cell)
    return lab

def reverse_lab(lab):
    for key in lab.keys():
        if type(key) == type("a"):
            continue
        l = []
        for cell in adjacent(key):
            if (
             cell not in lab[key] 
             and cell[0] >= 0 and cell[1] >= 0
             and cell[0] < lab["nlines"] and cell[1] < lab["ncolumns"]
               ):
                l.append(cell)
        lab[key] = l
    return lab

#---Check---#

def is_well_defined(lab):
    keys = lab.keys()

    ymax, xmax = 0, 0
    for key in keys:
        if type(key) == type("a"):
            continue
        if key[0] > ymax: ymax=key[0]
        if key[1] > xmax: xmax=key[1]
        for cell in lab[key]:
            if key not in lab[cell]:
                return False

    if lab["ncolumns"] != xmax+1 or lab["nlines"] != ymax+1:
        return False

    for y in range(lab["nlines"]):
        for x in range(lab["ncolumns"]):
            if (y, x) not in keys:
                return False

    return True

def is_true_lab(lab):
    for line in get_cell_occurence(lab):
        for cell in line:
            if cell !=1:
                return False
    return True


#---Generation---#

def get_bin_list(n, nmax):
    if n == 0:
        return [0 for _ in range(len(bin(nmax))-3)]
    n = bin(n)
    digits = []
    for i in range(len(n)-2):
        digits.append(int(n[i+2]))
    while len(digits) < len(bin(nmax))-3:
        digits.insert(0,0)
    return digits
    
            

def generate_pseudo_lab(ncolumns, nlines):
    nb_ver_walls = 2 ** ((ncolumns-1)*nlines)
    nb_hor_walls = 2 ** (nlines*(ncolumns-1))
    
    ver_labs = []
    for n in range(nb_ver_walls):
        lab = {"nlines":nlines, "ncolumns":ncolumns}
        nbin = get_bin_list(n, nb_ver_walls)
        for i in range(len(nbin)):
            y = i//(ncolumns-1)
            x = i%(ncolumns-1)
            if nbin[i]:
                if (y, x) not in lab.keys():
                    lab[(y, x)] = [(y, x+1)]
                else:
                    lab[(y, x)].append((y, x+1))
                if (y, x+1) not in lab.keys():
                    lab[(y, x+1)] = [(y, x)]
                else:
                    lab[(y, x+1)].append((y, x))
            else:
                if (y, x) not in lab.keys():
                    lab[(y, x)] = []
                if (y, x+1) not in lab.keys():
                    lab[(y, x+1)] = []
        ver_labs.append(reverse_lab(lab))
    
    hor_labs = []
    for n in range(nb_hor_walls):
        lab = {"nlines":nlines, "ncolumns":ncolumns}
        nbin = get_bin_list(n, nb_hor_walls)
        for i in range(len(nbin)):
            y = i//(ncolumns)
            x = i%(ncolumns)
            if nbin[i]:
                if (y, x) not in lab.keys():
                    lab[(y, x)] = [(y+1, x)]
                else:
                    lab[(y, x)].append((y+1, x))
                if (y+1, x) not in lab.keys():
                    lab[(y+1, x)] = [(y, x)]
                else:
                    lab[(y+1, x)].append((y, x))
            else:
                if (y, x) not in lab.keys():
                    lab[(y, x)] = []
                if (y+1, x) not in lab.keys():
                    lab[(y+1, x)] = []
        hor_labs.append(reverse_lab(lab))
    
    labs = []
    for hor_lab in hor_labs:
        for ver_lab in ver_labs:
            labs.append(merge_labs(hor_lab, ver_lab))
    
    return labs
