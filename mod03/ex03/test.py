from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("Elon.png")
# Output :
#Loading image of dimensions 200 x 200


from ColorFilter import ColorFilter
cf = ColorFilter()

cf.to_blue(arr)

cf.to_green(arr)

cf.to_red(arr)