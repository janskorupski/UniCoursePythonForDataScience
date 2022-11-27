from statistics import mean, variance, median


def transpose(mtx):
    return [[row[i] for row in mtx] for i in range(len(mtx[1]))]


def behead(mtx):
    return mtx[1:]


def means(mtx):
    return [mean(col)     for col in mtx if type(col[1]) in [int, float]]


def variances(mtx):
    return [variance(col) for col in mtx if type(col[1]) in [int, float]]


def medians(mtx):
    return [median(col)   for col in mtx if type(col[1]) in [int, float]]


if __name__ == "__main__":
    import iris_analysis.io.load as ld

    data = ld.load("../iris.csv")
    print(transpose(data))

    print(means(transpose(behead(data))))
