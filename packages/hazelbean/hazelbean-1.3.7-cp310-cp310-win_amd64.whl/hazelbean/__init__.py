from __future__ import division, absolute_import, print_function
import sys, time

use_minimal_importing = 1 # If this is not true, will import all of the HB library on first import, which can take up to 7 seconds.
use_strict_importing = 0 
import_extras = 0
use_strict_importing_for_ui = 0


import hazelbean.config # Needs to be imported before core so that hb.config.LAST_TIME_CHECK is set for hb.timer()
from hazelbean.config import *
# The most important and fast-loading things are in core which will be * imported each time.
from hazelbean import core    # Core is imported first so that I can use hb.timer() for import performance assessment.
from hazelbean.core import *

# Start a timer for assessing import performance.
import_start_time = time.time()

# Define the core features that are not defined in core.py 
from hazelbean.project_flow import ProjectFlow    
from hazelbean.project_flow import Task

import hazelbean.globals
from hazelbean.globals import *

import hazelbean.os_utils
from hazelbean.os_utils import *

import hazelbean.pyramids
from hazelbean.pyramids import *

import hazelbean.spatial_projection
from hazelbean.spatial_projection import *

import hazelbean.geoprocessing
from hazelbean.geoprocessing import *

import hazelbean.geoprocessing_extension
from hazelbean.geoprocessing_extension import *

import hazelbean.spatial_utils
from hazelbean.spatial_utils import *

import hazelbean.utils
from hazelbean.utils import *

import hazelbean.arrayframe
from hazelbean.arrayframe import *


if not use_minimal_importing:
    
    # FOR FUTURE: add init import option for load all into hb namespace., then, reconfigure hazelbean into stats, spatial, parallel, and other TOP LEVEL categories that I will make as subdirectories (i think)
    # from hazelbean.pyramids import *
    
    import hazelbean.geoprocessing_extension
    import hazelbean.spatial_projection
    
    from hazelbean.globals import *
    from hazelbean.config import *

        
    import hazelbean.arrayframe
    from hazelbean.arrayframe import *

    import hazelbean.arrayframe_functions
    from hazelbean.arrayframe_functions import *

    import hazelbean.cat_ears
    from hazelbean.cat_ears import *

    import hazelbean.file_io
    from hazelbean.file_io import *

    import hazelbean.geoprocessing_extension
    from hazelbean.geoprocessing_extension import *

    import hazelbean.os_utils
    from hazelbean.os_utils import *

    import hazelbean.project_flow
    from hazelbean.project_flow import *

    import hazelbean.pyramids
    from hazelbean.pyramids import *

    import hazelbean.spatial_projection
    from hazelbean.spatial_projection import *

    import hazelbean.spatial_utils
    from hazelbean.spatial_utils import *

    import hazelbean.stats
    from hazelbean.stats import *

    import hazelbean.utils
    from hazelbean.utils import *

    import hazelbean.raster_vector_interface
    from hazelbean.raster_vector_interface import *

    if use_strict_importing: # Protect cython imports so that a user without compiled files can still use the rest of hb
        import hazelbean.calculation_core
        from hazelbean.calculation_core import *

        sys.path.insert(0, '../../')
        sys.path.insert(0, '../hazelbean')
        sys.path.insert(0, '../hazelbean/calculation_core')

        import hazelbean.calculation_core
        import hazelbean.calculation_core.cython_functions
        from hazelbean.calculation_core.cython_functions import *

        import hazelbean.calculation_core.aspect_ratio_array_functions
        from hazelbean.calculation_core.aspect_ratio_array_functions import *

        import hazelbean.visualization
        from hazelbean.visualization import *

    else:
        try:
            import hazelbean.calculation_core.cython_functions
            from hazelbean.calculation_core.cython_functions import *

            import hazelbean.calculation_core.aspect_ratio_array_functions
            from hazelbean.calculation_core.aspect_ratio_array_functions import *

            import hazelbean.visualization
            from hazelbean.visualization import *
        except:
            print('Unable to import cython-based functions, but this may not be a problem.')

    # Optional imports for performance

    if import_extras:
        if use_strict_importing_for_ui:

            import hazelbean.ui
            from hazelbean.ui import *

            import hazelbean.ui.auto_ui
            from hazelbean.ui.auto_ui import *

            import hazelbean.watershed_processing
            from hazelbean.watershed_processing import *

        else:
            try:
                import hazelbean.ui
                from hazelbean.ui import *

                import hazelbean.ui.auto_ui
                from hazelbean.ui.auto_ui import *

                import hazelbean.watershed_processing
                from hazelbean.watershed_processing import *

            except:
                pass
print('Hazelbean import time: ' + str(time.time() - import_start_time))






