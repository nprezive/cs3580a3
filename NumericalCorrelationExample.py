import pandas as pd
import matplotlib.pyplot as plt
import webbrowser, os

path = 'auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None, names = ['mpg', 'cylinders', 'displacement','horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'], na_values='?')

mpg_data.info()

correlation = mpg_data['mpg'].corr(mpg_data['weight']) #Spearman, Pearson, or Kendall can be specified. Pearson is the default.

print("Correlation between mpg and weight =",correlation)

# pairwise correlation
pairwise = mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='spearman')
#print it to the screen
print(pairwise)

#make a heatmap, save it as HTML and open it:
myhtml = mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1).render()
htmlFile = open("tableExample.html","w")
htmlFile.write(myhtml)
htmlFile.close()
webbrowser.open('file://' + os.path.realpath("tableExample.html"))


# plot correlated values using charts:
plt.rcParams['figure.figsize'] = [16, 6]

fig, ax = plt.subplots(nrows=1, ncols=3)

ax=ax.flatten()

cols = ['weight', 'horsepower', 'acceleration']
colors=['#415952', '#f35134', '#243AB5', '#243AB5']
j=0

for i in ax:
    if j==0:
        i.set_ylabel('MPG')
    i.scatter(mpg_data[cols[j]], mpg_data['mpg'],  alpha=0.5, color=colors[j])
    i.set_xlabel(cols[j])
    i.set_title('Pearson: %s'%mpg_data.corr().loc[cols[j]]['mpg'].round(2)+' Spearman: %s'%mpg_data.corr(method='spearman').loc[cols[j]]['mpg'].round(2))
    j+=1

plt.show()

