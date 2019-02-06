class dataset(object):

    def test_year(self, year, start_valid, end_valid):
        return (start_valid <= year) and (year <= end_valid)

    def find(self, name, year):
        for key, value in getattr(self, name).items():
            if self.test_year(year, value["from"], value["to"]):
                return key.replace("@YEAR@", str(year))

class r0007(dataset):
    def __init__(self, res):
        self.res = res

        self.histsst = {
                self.res+"_ozone_historical_1850.nc": {"from": -9e10, "to": 1850},
                self.res+"_ozone_historical_@YEAR@.nc": {"from": 1851, "to": 2008},
                }


my_r0007 = r0007("T63")
print(my_r0007.find("histsst", 1750))
print(my_r0007.find("histsst", 1965))
