from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_feature import AbstractFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockVolumeFeature(AbstractFeature):
    """A continuous portion of rock material bounded by definite rock
    boundaries.

    It is a volume object. Some of these rock volumes are "static",
    while others are "dynamic". Reservoir fluids are dynamic because
    their properties, geometries, and quantities may change over time
    during the course of field production. A RockVolume feature is a
    geological feature--which is the general concept that refers to the
    various categories of geological objects that exist in the natural
    world, for example, the rock volume or the fluids that are present
    before production. The geological feature is not represented in the
    RESQML design.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
