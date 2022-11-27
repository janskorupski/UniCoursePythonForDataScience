from csv import reader # that's literally worthless, this can be rewritten without this dependency


def load(filedir,sep = ","):
    # i cant believe I had to implement this
    # really, what is the point of the 'csv' package if it can't even read a csv file? xddd

    mtx = []
    with open(filedir) as file:
        for line in file:
            row = line.replace("\n","").split( sep )

            # converting to numeric values, where possible
            for i in len(row):
                row[i] = row[i].replace("'",'"')
                if '"' in row[i]:
                    row[i] = row[i].replace('"',"")
                elif row[i].isdecimal():
                    row[i] = int( row[i] )
                elif row[i].isnumeric():
                    row[i] = float( row[i] )

            mtx.append(row)
    return mtx


# the code below uses the 'csv' package, but is stupid and will not be used
"""
def iCantBelieveIHadToImplementThis(filedir):
    # this could just as well be done with: newline.split(";") and it would achieve the exact same effect
    # without the need for importing a package.

    # reading the data
    mtx = []
    with open(filedir , newline =" ") as file:
        rdr = reader( file )
        for row in rdr:
            mtx.append(row)

    # converting strings to numeric values (I know it should be done differently, but that's ok for iris data)
    for row in len(mtx):
        for col in len(mtx[row]):
            if mtx[row][col].isdecimal():
                mtx[row][col] = int( mtx[row][col] )
                continue
            elif mtx[row][col].isnumeric():
                mtx[row][col] = float( mtx[row][col] )

    return mtx
"""