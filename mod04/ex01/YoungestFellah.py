from FileLoader import FileLoader


def youngest_fellah(df, year):
	youngest = {}
	women_in_year = df[(df['Sex'] == 'F') & (df['Year'] == year)]
	youngest['f'] = float(women_in_year['Age'].min())
	men_in_year = df[(df['Sex'] == 'M') & (df['Year'] == year)]
	youngest['m']  = float(men_in_year['Age'].min())
	print(youngest)
