class dataset(object):

    def test_year(self, year, start_valid, end_valid):
        return (start_valid <= year) and (year <= end_valid)

    def find(self, name, year):
        for key, value in getattr(self, name).items():
            if self.test_year(year, value["from"], value["to"]):
                return self.basedir+key.replace("@YEAR@", str(year))



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

basedir=pooldir+"/restart/"+parentexpid
thisrestart=echamrestart("/pool/data/ECHAM6/restart/mbe1256", mbe1256, "19781231235320")
thisrestart.co2 

class r0007(dataset):
    def __init__(self, res, basedir):
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

		
