from FileLoader import FileLoader
from MyPLotLib import MyPlotLib

loader = FileLoader()
data = loader.load('athlete_events.csv')

MyPlotLib.density(data, ['Year', 'Medal'])