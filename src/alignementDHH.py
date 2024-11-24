#!/usr/bin/env python
# Homology modeling by the automodel class
from modeller import *              	# Load standard Modeller classes
from modeller.automodel import *    	# Load the automodel class
log.verbose()    			# request verbose output
env = environ()  			# create a new MODELLER environment to build this model in
# directories for input atom files
#env.io.atom_files_directory = ’./../atom_files’
#env.io.atom_files_directory = '/home/../../../modeller'

#Read in HETATM records from template PDBs
env.io.hetatm = True

a = automodel(env,
              alnfile = 'alignementDHH.ali',   # alignment filename
              knowns   = ('2rmn','2xwc','4qo1'),              # codes of the templates
              sequence = 'p63',            # code of the target
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model= 1                 		# index of the first model
a.ending_model =100                  		# index of the last model
                                    		# (determines how many models to calculate)
a.make()                            		# do the actual homology modeling
