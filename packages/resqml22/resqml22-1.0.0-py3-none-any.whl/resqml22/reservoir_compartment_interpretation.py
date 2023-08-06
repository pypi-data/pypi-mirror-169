from __future__ import annotations
from dataclasses import dataclass
from resqml22.geologic_unit_interpretation import GeologicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ReservoirCompartmentInterpretation(GeologicUnitInterpretation):
    """A portion of a reservoir rock which is differentiated laterally from
    other portions of the same reservoir stratum.

    This differentiation could be due to being in a different fault
    block or a different channel or other stratigraphic or structural
    aspect. A reservoir compartment may or may not be in contact with
    other reservoir compartments.
    """
