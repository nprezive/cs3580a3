#import matplotlib
from collections import defaultdict
import pandas as pd


def basicInfo():
    print("Basic information")
    print()
    print("\tNumber of chocolates per rating")

    barCountByRating = defaultdict(int)

    with open("flavors_of_cacao.csv") as f:
        next(f)
        for line in f:
            lineList = line.split(",")
            print(lineList)
            rating = lineList[6]
            barCountByRating[rating] += 1
    
    print(barCountByRating)


def pandasTest():
    df = pd.read_csv("flavors_of_cacao.csv")
    thingy = df.rename(index=str, columns={"Company \n(Maker-if known)":"Company", 
                        "Specific Bean Origin\nor Bar Name":"Specific Origin", 
                        "Review\nDate":"Review Date", 
                        "Cocoa\nPercent":"Cocoa Percent", 
                        "Company\nLocation":"Company Location", 
                        "Bean\nType":"Bean Type", 
                        "Broad Bean\nOrigin":"Broad Origin"})
    thingy2 = df.rename(index=int, columns={1:"Company"})
    print(thingy2)

# Run program
# basicInfo()
pandasTest()