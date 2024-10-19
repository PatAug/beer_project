import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df0 = pd.read_csv('beer_reviews.csv')
df0['CreatedDate'] = pd.to_datetime(df0['review_time'], origin='unix', unit='s')

newest_date0 = df0.groupby('beer_beerid')['CreatedDate'].max().reset_index()
newest_date = df0.merge(newest_date0, on=['CreatedDate','beer_beerid'], how = 'inner' )

corr_matrix = newest_date[['review_overall','review_aroma', 'review_appearance', 'review_palate', 'review_taste','beer_abv']].corr(method='pearson')

