# import package_travel.thailand
# trip_to = package_travel.thailand.ThailandPackage()
# trip_to.detail()

# from package_travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from package_travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))