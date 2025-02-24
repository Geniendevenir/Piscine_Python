from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("data.csv")

loader.display(data, 10)
print("\n\n\n")

loader.display(data, -10)