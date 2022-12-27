# fileparse.py
import csv


def parse_csv(filename, types=None, has_headers=True, select=[], delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select != [] and not has_headers:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        records = []

        if has_headers:
            # Read the file headers
            headers = next(rows)

            indices = []
            if select:
                for i in range(len(select)):
                    indices.append(headers.index(select[i]))
            else:
                indices = list(range(len(headers)))
        else:
            pass

        if not types:
            types = [str for i in range(len(indices))]

        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # record = dict(zip([headers[j] for j in indices], [row[j] for j in indices]))
            if has_headers:
                result = {}
                k = 0
                for j in indices:
                    result[headers[j]] = types[k](row[j])
                    k += 1
            else:
                result = []
                k = 0
                for elt in row:
                    result.append(types[k](elt))
                    k += 1
                result = tuple(result)
            record = result
            records.append(record)

    return records


if __name__ == "__main__":

    # TODO Exercise 3.9: Catching exceptions (https://dabeaz-course.github.io/practical-python/Notes/03_Program_organization/03_Error_checking.html)

    try:
        print("test 3.10")  # (Exercise 3.8)
        portfolio = parse_csv('Data/portfolio.dat', select=['name','price'], has_headers=False)
        print(portfolio)
    except RuntimeError as e:
        print("test passed with RuntimeError", e)

    print("test 3.9")  # (Exercise 3.7)
    portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
    print(portfolio)

    print("test 3.8")
    prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
    print(prices)

    print("test 3.7")
    portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
    print(portfolio)

    print("test 3.6")
    shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
    print(shares_held)

    print("test3.5")
    portfolio = parse_csv('Data/portfolio.csv', select=['shares', 'name'], types=[int, str])
    print(portfolio)

    print("test3")
    portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
    print(portfolio)

    print("test2")
    shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'])
    print(shares_held)

    print("test1")
    portfolio = parse_csv('Data/portfolio.csv')
    print(portfolio)

