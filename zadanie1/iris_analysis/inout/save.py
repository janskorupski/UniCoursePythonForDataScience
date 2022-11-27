def save( data , filename ):

    with open(filename , "w") as file:
        for row in data:
            file.write( ",".join( [ str(cell) for cell in row ] ) )
            file.write( "\n" )