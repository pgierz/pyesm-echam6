# NOTE: Please inherit from object until we switch fully to python >= 3
class Dataset(object):
    """
    Describes the released ``ECHAM6`` dataset.

    The ``dataset`` object describes the set of files that are used for input,
    forcing, etc. for a specific version of ``ECHAM6``. While the base class
    doesn't define any files, there are methods defined here which are used to
    sort files according to specific years for which they are valid, and for
    finding a "class" for files; e.g.:
        + SST files (Sea Surface Temperature)
        + SIC files (Sea Ice Concentration)
        + ...
    """
    # The keys here would correspond to filepaths, the values are a dictionary
    # of "from": minimum valid year, "to": maximum valid year
    example_fileset = {
            "big_bang": {"from": -9e10, "to": 2016},
            "Trump_Time_and_Sadness": {"from": 2016, "to": 2020},
            "The_Future_at_@YEAR@": {"from": 2020, "to": 9e10}
            }

    def check_year(self, year, start_valid, end_valid):
        """ Checks if a year is within a valid range.

        Parameters:
        -----------
        year: int
            The year to check
        start_valid: int
            The minimum bound for validity of a specific year.
        end_valid: int
            The maximum bound for vaility of a specific year

        Returns:
        --------
            bool: True or False depending on if the year is valid or not.
        """
        return (start_valid <= year) and (year <= end_valid)

    def find(self, name, year):
        """ Finds a specific file for a given year, based upon the tag given in name.

        Returns the **key** of the dictionary stored in the attribute specified
        by ``name`` based upon a value found in ``year``.

        Notes:
        ------
            The returned value will have any substring @YEAR@ replaced by a
            string representation of the argument ``year``.

        Parameters:
        -----------
            name: str
                The ``name`` parameter is used to get the dictionary of files
                to check through.
            year: int
                The ``year`` parameter is used to check the vailidity of a
                specific file, and is **also** used in replacement of a special
                string @YEAR@.

        Returns:
        --------
            str:
                A string for the **key** of the dictionary defined in **name**
                which corresponds to a file defined by the rules following
                **year**.
        """
        for key, value in getattr(self, name).items():
            # FIXME: This is a problem. We only return something within the
            # valid range. Actually, we **always** want to return something,
            # but want to specifically replace it during a specific range. I
            # would recommend re-writing this. The replacement is still needed;
            # but it might be better to check against the existance of "from"
            # and "to" in the dictionary, and if **both** exist, then replace a
            # year, otherwise, return something else...
            if self.check_year(year, value["from"], value["to"]):
                return key.replace("@YEAR@", str(year))

class r0007(Dataset):
    def __init__(self, res):
        self.res = res

        self.histsst = {
                self.res+"_ozone_historical_1850.nc": {"from": -9e10, "to": 1850},
                self.res+"_ozone_historical_@YEAR@.nc": {"from": 1851, "to": 2008},
                }
