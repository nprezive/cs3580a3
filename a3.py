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
    df = df.rename(columns={df.columns[0]:"Company",
                                df.columns[1]:"Specific Origin", 
                                df.columns[3]:"Review Date", 
                                df.columns[4]:"Cocoa Percent", 
                                df.columns[5]:"Company Location", 
                                df.columns[7]:"Bean Type", 
                                df.columns[8]:"Broad Origin"})
    print(df)

# Run program
# basicInfo()
pandasTest()