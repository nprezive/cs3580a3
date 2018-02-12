from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


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


def firstCorrelations():
    print('\nFirst Correlation:')

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


def secondCorrelations():
    print('\nSecond Correlation:')

    fiveRandomCompanies = random.sample(set(df['Company']), 5)
    dummies = pd.get_dummies(df['Company'])
    new_df = df['Rating']
    for c in fiveRandomCompanies:
        new_df = pd.concat([new_df, dummies[c]], axis=1)
    df_corr = new_df.corr()

    print('\n\tCorrelation matrix of 5 companies and rating:')
    print(df_corr)
    print("\n\tThe Rating column of this matrix tells us the strength of the relationship \
between whether or not a chocolate is from a particular company (a boolean) \
and its rating. Because there are many companies that make chocolates with high \
and low ratings, knowing the company is not enough to determine the rating \
and/or knowing the rating isn't enough to determine the company. Therefore, the \
correlations are quite low.")

    corr_dict = dict(df_corr['Rating'])
    for k, v in corr_dict.items():
        corr_dict[k] = abs(v)
    highestCorrCompany = sorted(corr_dict.items(), key=lambda x:x[1], reverse=True)[1]
    
    print(highestCorrCompany)


    # filtered_df = df[df.Company.isin(fiveRandomComapnies)]
    # dummies = pd.get_dummies(filtered_df['Company'])
    # filtered_df = filtered_df[['Rating']]
    # df_new = pd.concat([filtered_df, dummies], axis=1)
    # print(df_new)
    # print(df_new.corr())


# Run program
# chocolateRatings()
# top5Countries()
# univariateValues()
# firstCorrelations()
secondCorrelations()