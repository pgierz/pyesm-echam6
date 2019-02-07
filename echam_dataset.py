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
            if self.check_year(year, value["from"], value["to"]):
                return key.replace("@YEAR@", str(year))
	error

class echamrestart(dataset):
    def __init__(self, basedir, parentexpid, parentdate)
	self.parentexpid = parentexpid
	self.parentdate = parentdate
	self.basedir = basedir

	unallowed_streams = ["jsbach", "jsbid", "veg", "yasso", "surf", "hd"]

	filelist = os.listdir(basedir+"/restart_"+self.parentexpid+"_"+self.parentdate+"_*.nc")
	for file in filelist:
		stream=os.path.basename(file).split("_")[-2] 
		if not stream in unallowed_streams:
			setattr(self, stream, "/restart_"+self.parentexpid+"_"+self.parentdate+"_"+stream+".nc") 


class r0007(Dataset):
    def __init__(self, res):
        self.res = res
	self.basedir = basedir

	# input data
	self.rrtmglw = {"/rrtmg_lw.nc" :{"from": -9e9, "to": 9e9}} 
	self.rrtmgsw = {"/rrtmg_sw.nc" :{"from": -9e9, "to": 9e9}} 
	self.cldoptprops = {"/ECHAM6_CldOptProps.nc" :{"from": -9e9, "to": 9e9}} 
	self.tslclim = {"/"+self.res+"/"+self.res+"_TSLCLIM.nc" :{"from": -9e9, "to": 9e9}} 
	self.janspec = {"/"+self.res+"/"+self.res+self.levels+"_jan_spec.nc" :{"from": -9e9, "to": 9e9}} 
	self.vgratclim = {"/"+self.res+"/"+self.res+self.oceres"_VGRATCLIM.nc" :{"from": -9e9, "to": 9e9}}
	self.vltclim = {"/"+self.res+"/"+self.res+self.oceres"_VLTCLIM.nc" :{"from": -9e9, "to": 9e9}}
	self.jansurf = {"/"+self.res+"/"+self.res+self.oceres"_jan_surf.nc" :{"from": -9e9, "to": 9e9}}

	# forcing data
        self.histozone = {
                "/"+self.res+"/ozone/"+self.res+"_ozone_historical_1850.nc": {"from": -9e10, "to": 1850},
                self.res+"_ozone_historical_@YEAR@.nc": {"from": 1851, "to": 2008},
                }

	self.amipsst = { "/"+self.res+"/amip/"+self.res+"_amipsst_@YEAR@.nc": {"from": 1870, "to": 2016}}
	self.amipsic = {"/"+self.res+"/amip/"+self.res+"_amipsic_@YEAR@.nc": {"from": 1870, "to": 2016}}
	self.histaerofin = {
			"/"+self.res+"/aero2/"+self.res+"_aeropt_kinne_sw_b14_fin_1865.nc" : {"from": -9e9, "to": 1864},
			"/"+self.res+"/aero2/"+self.res+"_aeropt_kinne_sw_b14_fin_@YEAR@.nc" : {"from": 1865, "to": 2000}
			}
	self.histaerocoarse = {"/"+self.res+"/aero2/"+self.res+"_aeropt_kinne_sw_b14_coa.nc" : {"from": -9e9, "to": 9e9}}
	self.histaerofarir = {"/"+self.res+"/aero2/"+self.res+"_aeropt_kinne_lw_b16_coa.nc" : {"from": -9e9, "to": 9e9}}
	self.histvolcir = {
			"/"+self.res+"/volcano_aerosols/strat_aerosols_ir_"+self.res+"_1850.nc" : {"from": -9e9, "to": 1850},
			"/"+self.res+"/volcano_aerosols/strat_aerosols_ir_"+self.res+"_@YEAR@.nc" : {"from": 1851, "to": 1999},
			"/"+self.res+"/volcano_aerosols/strat_aerosols_ir_"+self.res+"_1999.nc" : {"from": 2000, "to": 9e9},
			}
	self.histvolcsw = {
			"/"+self.res+"/volcano_aerosols/strat_aerosols_sw_"+self.res+"_1850.nc" : {"from": -9e9, "to": 1850},
			"/"+self.res+"/volcano_aerosols/strat_aerosols_sw_"+self.res+"_@YEAR@.nc" : {"from": 1851, "to": 1999},
			"/"+self.res+"/volcano_aerosols/strat_aerosols_sw_"+self.res+"_1999.nc" : {"from": 2000, "to": 9e9},
			}
	self.histswflux = {
			"/solar_irradiance/swflux_14band_1850.nc" :  {"from": -9e9, "to": 1850},
			"/solar_irradiance/swflux_14band_@YEAR@.nc" :  {"from": 1851, "to": 9e9},
			}
	self.histgreenh = { "/greenhouse_historical.nc" : {"from": -9e9, "to": 9e9}}


        self.piozone = {"/"+self.res+"/"+self.res+"_ozone_picontrol.nc": {"from": -9e10, "to": 9e9}}
	self.pisst = {"/"+self.res+"/"+self.res+self.oceres+"_piControl-LR_sst_1880-2379.nc": {"from": -9e9, "to": 9e9}}
	self.pisic = {"/"+self.res+"/"+self.res+self.oceres+"_piControl-LR_sic_1880-2379.nc": {"from": -9e9, "to": 9e9}}
	self.piaerofin = {"/"+self.res+"/aero/"+self.res+"_aeropt_kinne_sw_b14_fin_1865.nc" : {"from": -9e9, "to": 9e9}}
	self.piaerocoarse = {"/"+self.res+"/aero/"+self.res+"_aeropt_kinne_sw_b14_coa.nc" : {"from": -9e9, "to": 9e9}}
	self.piaerofarir = {"/"+self.res+"/aero/"+self.res+"_aeropt_kinne_lw_b16_coa.nc" : {"from": -9e9, "to": 9e9}}

		
