#import matplotlib
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("flavors_of_cacao.csv", 
            names=[
                'Company',
                'Specific Origin',
                'REF',
                'Review Date',
                'Cacao Percent',
                'Company Location',
                'Rating',
                'Bean Type',
                'Broad Origin'],
            header=0,
            converters={
                4: lambda p: float(p.strip('%'))/100
            })


def chocolateRatings():
    ratings = df['Rating']
    ratingsDict = defaultdict(int)
    for r in ratings:
        ratingsDict[r] += 1

    print("Number of chocolates per rating:")
    for k in sorted(ratingsDict.keys(), reverse=True):
        print("\t{0}: {1}".format(k, ratingsDict[k]))
    plt.bar(list(ratingsDict.keys()), list(ratingsDict.values()), color="g")
    plt.title("Number of chocolates per rating")
    plt.xlabel("Ratings")
    plt.ylabel("# of Chocolates")
    plt.show()


def top5Countries():
    meanRatingByCountry = df.groupby(['Company Location'], as_index=False)[['Rating']].mean() \
                            .sort_values('Rating', ascending=False) \
                            .rename(columns={'Rating': 'Mean Rating'})
    
    print('\nTop 5 countries:  (highest mean rating)')
    print(meanRatingByCountry.head(5).to_string(index=False))


def univariateValues():
    print('\nUnivariate values:')
    
    # Mean cacao percentage
    meanCacao = df['Cacao Percent'].mean()
    print('\tMean cacao percentage: {0:.1f}%'.format(meanCacao*100))

    # Range of cacao percentage
    rangeCacao = df['Cacao Percent'].max() - df['Cacao Percent'].min()
    print('\tRange of caco percentage: {0:.1f}%'.format(rangeCacao*100))

    



# Run program
# chocolateRatings()
top5Countries()
univariateValues()