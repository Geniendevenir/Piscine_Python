import pandas as pd

data = {
    'Year': [2004, 2004, 2004, 2004],
    'Sex': ['M', 'M', 'M', 'M'],
    'Sport': ['Basketball', 'Soccer', 'Basketball', 'Soccer']
}
test_df = pd.DataFrame(data)

def proportion_by_sport(df, year, sport, gender):
    filter_total = df[(df['Year'] == year) & (df['Sex'] == gender)]
    total = len(filter_total)
    filter_portion = filter_total[filter_total['Sport'] == sport]
    portion = len(filter_portion)
    print(f"Total: {total}, Portion: {portion}")
    print(portion / total if total > 0 else None)

# Expect 0.5 because 2 out of 4 are Basketball
proportion_by_sport(test_df, 2004, 'Basketball', 'M')