def save( data , filename ):

    with open(filename , "w") as file:
        for row in data:
            for cell in row:
                file.write( str(cell) )
                file.write( "," )
            file.write( "\n" )