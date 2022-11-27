from iris_analysis.io.load import load
from iris_analysis.io.save import save
from iris_analysis.calculate import *

if __name__ == "__main__":
    DATADIR = "iris.csv"

    data = load( DATADIR )

    stats = []
    stats.append( ["statistic" ] + data[0][:-1] )

    data = behead(data)
    data = transpose(data)

    stats.append( ["means"     ] + means(data)      )
    stats.append( ["variances" ] + variances(data)  )
    stats.append( ["medians"   ] + medians(data)    )

    print( stats )

    save( stats , "output.csv" )