# Import core types
from typing import Literal

import aind_behavior_services.rig as rig

from {{ _python_package_name }} import __semver__


class {{ _pthon_class_prefix }}Rig(rig.AindBehaviorRigModel):
    version: Literal[__semver__] = __semver__
    ...