import pandas as pd

df0 = pd.read_csv('beer_reviews.csv')
df0['CreatedDate'] = pd.to_datetime(df0['review_time'], origin='unix', unit='s')

newest_date0 = df0.groupby('beer_beerid')['CreatedDate'].max().reset_index()
newest_date = df0.merge(newest_date0, on=['CreatedDate','beer_beerid'], how = 'inner' )

print(df0.columns)

a1 = newest_date.loc[(newest_date['review_aroma'] == 5) & (newest_date['review_appearance'] == 5)]
a2 = a1.groupby('beer_style')['beer_beerid'].count().reset_index()
a3 = a2.sort_values(by = 'beer_beerid', ascending = False).reset_index()
a3['beer_style'].unique()

choose_brewery = a1.loc[(a1['beer_style'] == 'Fruit / Vegetable Beer') & (a1['review_overall'] == 5.0) ]
choose_id = choose_brewery['brewery_id']
brew_all = newest_date.loc[newest_date['brewery_id'].isin(choose_id)]
brew_all.groupby('brewery_id')['review_overall'].mean().reset_index()
# the best brewery 1471
best = choose_brewery.loc[choose_brewery['brewery_id'] == 1471]