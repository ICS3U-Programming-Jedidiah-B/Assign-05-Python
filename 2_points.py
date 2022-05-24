# this function calculates distance bewteen 2 points
def distance(x1, x2, y1, y2):
    result = ((((x2 - x1)**2) + ((y2-y1)**2))**0.5)
    return result


# this function gets input from user and displays distance
def main():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    try:
        x1 = int(input("Please enter the 1st point 'x1' (?,?): "))

        y1 = int(input("Please enter the 1st point 'y1' ({},?): ".format(x1)))

        x2 = int(input("Please enter the 2nd point 'x2' (?,?): "))

        y2 = int(input("Please enter the 2nd point 'y2' ({},?): ".format(x1)))
    except ValueError:
        print("please enter an intger")
    distance(x1, x2, y1, y2)
    answer = distance(x1, x2, y1, y2)
    print("The distance between ({},{}) and ({},{}) points is {}".format(
        x1, x2, y1, y2, answer))


if __name__ == "__main__":
    main()
