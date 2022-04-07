import pandas as pd

def normalize_data():
    df = pd.read_csv("steam_games.csv")
    numerical_col = ['positive_rev', 'negative_rev', 'mean_forever_playtime', 'median_forever_playtime', 'Concurrent_Users', 'retailprice']

    for attribute in numerical_col:
        norm_val = []
        key = "norm_" + attribute
        min_value = df[attribute].min()
        range_amt = df[attribute].max() - min_value

        for i in range(len(df)):
            value = df.loc[i].at[attribute].item()
            norm_val.append(( value - min_value) / range_amt)
        
        df.insert(loc=len(df.columns), column=key, value=norm_val, allow_duplicates=True)
    
    df.to_csv('norm_steam_games.csv', index=False)

if __name__ == "__main__":
    normalize_data()