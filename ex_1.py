import pandas as pd

df0 = pd.read_csv('beer_reviews.csv')

#cleaning
df0['CreatedDate'] = pd.to_datetime(df0['review_time'], origin='unix', unit='s')
df00 = df0.groupby('beer_beerid')['CreatedDate'].max().reset_index()
df = df00.merge(df0, on=['CreatedDate','beer_beerid'], how = 'inner' )

max_abv = df['beer_abv'].max()

help_tab = df[['brewery_id', 'beer_abv']].loc[df['beer_abv'].notna()]
df_agg_mean = help_tab.groupby(['brewery_id']).agg({'beer_abv': 'mean'}).reset_index()
df_agg_mean_2 = df_agg_mean.sort_values(['beer_abv'], ascending = False).head(5)
df_agg_mean_2['stats'] = 'mean'

df_agg_median = help_tab.groupby(['brewery_id']).agg({'beer_abv': 'median'}).reset_index()
df_agg_median_2 = df_agg_median.sort_values(['beer_abv'], ascending = False).head(5)
df_agg_median_2['stats'] = 'median'

df_agg_stats = pd.concat([df_agg_median_2, df_agg_mean_2])


