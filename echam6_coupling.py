"""
Allows for coupling between ``ECHAM6`` and a **generic ice sheet**

- - - - 
"""

# Standard Library Imports:
import glob

# This Library Imports:
from echam.echam_simulation import EchamCompute

# External Imports:
import cdo

ACCELERATION_DUE_TO_GRAVITY = 9.81  # m/s**2

# Ok, so first we need to find out if this should be a seperate class or just
# part of something else...  Either way, we can construct an object to contain
# all the functionality:


class EchamCouple_Ice(EchamCompute):
    """ Contains functionality to cut out ice sheet forcing from ECHAM6 output """
    def __init__(self):
        # FIXME: real syntax for the next line...
        super().__init__()

        self.__cleanup_list = []
        self._cdo_stderr = open("EchamCouple_Ice_cdo_log", "w")
        self._nco_stderr = open("EchamCouple_Ice_nco_log", "w")
        self.CDO = cdo.Cdo(logging=True, logFile=self._cdo_stderr)

    def send_ice(self):
        """ Sends a generic atmosphere field for an ice sheet model """
        self._generate_ice_forcing_file()
        self._write_grid_description()
        self._write_variable_description()
        self.files['couple'].digest()
        for tmpfile in self.__cleanup_list:
            os.remove(tmpfile)
        self.CDO.cleanTempDir()

    def _generate_ice_forcing_file(self):
        """Makes a forcing file for an ice sheet.

        The following information is included:
        + ...
        """
        logging.info("\t\t Preparing echam6 file for processing in an ice sheet model...")

        start_date = self.calendar.coupling_start_date
        end_date = self.calendar.coupling_end_date

        file_list = self._construct_input_list(start_date, end_date)
        files_with_selected_variables = self._select_relevant_variables(file_list)

        final_output = self._concatenate_files(files_with_selected_variables)
        if ECHAM_TO_ISM_multiyear_mean:
            final_output = self._multiyear_mean(final_output)

        self.files["couple"]["atmosphere_file_for_ice"] = ComponentFile(src=final_output,
                                                                        dest=self._couple_dir+"/atmosphere_file_for_ice.nc")
        logging.info("\t\t ...done!")

    def _write_grid_description(self):
        """ Writes echam6 grid descrption to atmosphere.griddes """
        logging.info("\t\t Writing echam6 grid description to generic file atmosphere.griddes...")
        logging.info("\t\t *   generatic griddes")
        ofile = self.CDO.griddes(input=self.files["couple"]["atmosphere_file_for_ice"].src)
        self.files["couple"]["atmosphere_grid_description"] = ComponentFile(src=ofile, dest=self._couple_dir+"/atmosphere.griddes")
        logging.info("\t\t ...done!")

    def _write_variable_description(self):
        """Writes variable descrptions to a file"""
        pass

    def _construct_file_list(self, start_date, end_date):
        logging.info("\t\t *   constructing input list...")
        file_list =  [glob.glob(self.outdata_dir+"/"+self.expid+"_echam6_echam_"+start_date+"-"+end_date+"*.nc")]
        return file_list

    def _select_relevant_variables(self, file_list):
        logging.info("\t\t *   selecting relevant variables...")
        files_with_selected_variables = []
        for this_file in file_list:
            ofile = self.CDO.expr("orog=geosp/%s(ACCELERATION_DUE_TO_GRAVITY); aprt=aprl+aprc; temp2=temp2" % (ACCELERATION_DUE_TO_GRAVITY),
                             input=this_file)
            for lst in files_with_selected_variables, self.__cleanup_list:
                lst.append(ofile)
        return files_with_selected_variables

    def _concatenate_files(self, file_list):
        logging.info("\t\t *   concatenating files...")
        ofile = self.CDO.cat(input=file_list)

