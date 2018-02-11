#import matplotlib
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("flavors_of_cacao.csv", 
            names=[
                'Company',
                'Specific_Origin',
                'REF',
                'Review_Date',
                'Cacao_Percent',
                'Company_Location',
                'Rating',
                'Bean_Type',
                'Broad_Origin'],
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
    meanRatingByCountry = df.groupby(['Company_Location'], as_index=False)[['Rating']].mean() \
                            .sort_values('Rating', ascending=False) \
                            .rename(columns={'Rating': 'Mean Rating'})
    
    print('\nTop 5 countries:  (highest mean rating)')
    print(meanRatingByCountry.head(5).to_string(index=False))


def univariateValues():
    print('\nUnivariate values:')
    
    # Mean cacao percentage
    meanCacao = df['Cacao_Percent'].mean()
    print('\tMean cacao percentage: {0:.1f}%'.format(meanCacao*100))

    # Range of cacao percentage
    rangeCacao = df['Cacao_Percent'].max() - df['Cacao_Percent'].min()
    print('\tRange of caco percentage: {0:.1f}%'.format(rangeCacao*100))

    # Mode of Bean Type
    beanTypeMode = (df[df.Bean_Type != '\xa0'])['Bean_Type'].mode()
    print('\tMode of bean type: {0}'.format(beanTypeMode.to_string(index=False)))

    # Mode of Broad Origin
    broadOriginMode = df['Broad_Origin'].mode()
    print('\tMode of broad bean origin: {0}'.format(broadOriginMode.to_string(index=False)))

    # Mode of Company Location
    companyLocationMode = df['Company_Location'].mode()
    print('\tMode of company location: {0}'.format(companyLocationMode.to_string(index=False)))


def correlations():
    print('\nCorrelations:')

    corrPercentCacaoAndRating = df['Cacao_Percent'].corr(df['Rating'])
    print('\tCorrelation between percent of cacao and rating: {0:.3f}'.format(corrPercentCacaoAndRating))
    #scatter plot
    plt.title('Correlation between percent of cacao and rating')
    plt.xlabel('% Cacao')
    plt.ylabel('Rating')
    #regression line
    fit = np.polyfit(df['Cacao_Percent'], df['Rating'], 1)
    fit_fn = np.poly1d(fit) 
    plt.plot(df['Cacao_Percent'], df['Rating'], 'yo', df['Cacao_Percent'], fit_fn(df['Cacao_Percent']), '--k')
    plt.show()
    print("\tWith a correlation coefficient so small, it looks like there's no correlation between the two.")

    


# Run program
# chocolateRatings()
# top5Countries()
# univariateValues()
correlations()