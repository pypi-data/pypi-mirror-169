from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_local3d_crs import AbstractLocal3DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalDepth3DCrs(AbstractLocal3DCrs):
    """Defines a local depth coordinate system.

    the geometrical origin and location are defined by the elements of
    the base class AbstractLocal3dCRS. This CRS uses the units of
    measure of its projected and vertical CRS.
    """
    class Meta:
        name = "LocalDepth3dCrs"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
