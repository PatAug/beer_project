import pandas as pd

df = pd.read_csv('beer_reviews.csv')

df['CreatedDate'] = pd.to_datetime(df['review_time'], origin='unix', unit='s')

newest_date0 = df.groupby('beer_beerid')['CreatedDate'].max().reset_index()
newest_date = df.merge(newest_date0, on=['CreatedDate','beer_beerid'], how = 'inner' )

df_agg = newest_date.groupby(['beer_style']).agg({'review_overall': 'mean', 'brewery_id': 'count'})
df_agg_2 = df_agg.sort_values(['review_overall'], ascending = False).head(5)

good_value = newest_date.loc[newest_date['review_overall'].isin([5])]

def create_sets(name1, beer_type):
    name1 = good_value.loc[(good_value['beer_style'] == beer_type)
                           & (good_value['review_aroma'].isin([5]))
                           & (good_value['review_appearance'].isin([5]))
                           & (good_value['review_palate'].isin([5]))
                           & (good_value['review_taste'].isin([5]))
                           ]
    if name1.empty:
        name1 = good_value.loc[(good_value['beer_style'] == beer_type)
                               & ((good_value['review_aroma'].isin([5]))
                                  | (good_value['review_appearance'].isin([5]))
                                  | (good_value['review_palate'].isin([5]))
                                  | (good_value['review_taste'].isin([5])))
                               ]

    return name1

set_staut = create_sets('set_staut', 'American Double / Imperial Stout')
choose_staut = set_staut.loc[set_staut['beer_abv'] == set_staut['beer_abv'].max()][['brewery_id', 'CreatedDate', 'beer_abv']]



set_lambic = create_sets('set_lambic', 'Lambic - Unblended')
set_lambic['total_review'] = set_lambic['review_aroma'] + set_lambic['review_appearance'] + set_lambic['review_palate'] + set_lambic['review_taste']
choose_lambic = set_lambic.loc[set_lambic['beer_abv'] == set_lambic['beer_abv'].min()][['brewery_id', 'CreatedDate', 'beer_abv', 'total_review']]


set_ais = create_sets('set_lambic', 'American Double / Imperial Stout')
choose_ais = set_ais.loc[set_ais['CreatedDate'] == set_ais['CreatedDate'].max()][['brewery_id', 'CreatedDate', 'beer_abv']]
