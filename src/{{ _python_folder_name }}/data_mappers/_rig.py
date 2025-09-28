import logging
import os
from pathlib import Path
from typing import Callable, Optional

from aind_data_schema.core import instrument
from clabe.data_mapper import aind_data_schema as ads
from clabe.launcher import Launcher

from {{ _python_package_name }}.rig import {{ _pthon_class_prefix }}Rig

logger = logging.getLogger(__name__)

class AindRigDataMapper(ads.AindDataSchemaRigDataMapper):
    def __init__(
        self,
        rig_model: {{ _pthon_class_prefix }}Rig,
    ):
        super().__init__()
        self.rig_model = rig_model
        self._mapped: Optional[instrument.Instrument] = None

    def rig_schema(self):
        return self.mapped

    @property
    def session_name(self):
        raise NotImplementedError("Method not implemented.")

    def write_standard_file(self, directory: os.PathLike) -> None:
        self.mapped.write_standard_file(Path(directory))

    def map(self) -> instrument.Instrument:
        logger.info("Mapping aind-data-schema Rig.")
        self._mapped = self._map(self.rig_model)
        return self.mapped

    @property
    def mapped(self) -> instrument.Instrument:
        if self._mapped is None:
            raise ValueError("Data has not been mapped yet.")
        return self._mapped

    def is_mapped(self) -> bool:
        return self.mapped is not None

    @classmethod
    def build_runner(cls) -> Callable[[Launcher[{{ _pthon_class_prefix }}Rig, Any, Any]], "AindRigDataMapper"]:
        def _new(
            launcher: Launcher[{{ _pthon_class_prefix }}Rig, Any, Any],
        ) -> "AindRigDataMapper":
            new = cls(rig_model=launcher.get_rig(strict=True))
            new.map()
            return new

        return _new

    @classmethod
    def _map(cls, rig: {{ _pthon_class_prefix }}Rig) -> instrument.Instrument:
        raise NotImplementedError("Rig mapping not implemented yet.")