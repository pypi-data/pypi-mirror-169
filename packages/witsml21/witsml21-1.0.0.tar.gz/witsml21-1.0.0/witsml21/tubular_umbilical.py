from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.component_reference import ComponentReference
from witsml21.tubular_umbilical_cut import TubularUmbilicalCut
from witsml21.tubular_umbilical_osduintegration import TubularUmbilicalOsduintegration

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TubularUmbilical:
    """An umbilical is any control, power or sensor cable or tube run through
    an outlet on the wellhead down to a particular receptacle on a downhole
    component (power or hydraulic line) or simply to a specific depth
    (sensors).

    Examples include Gas lift injection tube, Subsea valve control line,
    ESP power cable, iWire for external gauges, external Fiber Optic
    Sensor cable. Umbilicals are run outside of the casing or completion
    assembly and are typically attached by clamps. Umbilicals are run in
    hole same time as the host assembly. Casing Umbilicals may be
    cemented in place e.g. Fiber Optic.

    :ivar connected_tubular_component: The Tubular component the
        umbilical is connected to.
    :ivar cut: A cut in the umbilical.
    :ivar service_type: The Type of Service the umbilical is
        facilitating.
    :ivar tubular_umbilical_osduintegration: Information about a
        TubularUmbilical that is relevant for OSDU integration but does
        not have a natural place in a TubularUmbilical.
    :ivar umbilical_type: The type of umbilical.
    """
    connected_tubular_component: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "ConnectedTubularComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    cut: List[TubularUmbilicalCut] = field(
        default_factory=list,
        metadata={
            "name": "Cut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    service_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tubular_umbilical_osduintegration: Optional[TubularUmbilicalOsduintegration] = field(
        default=None,
        metadata={
            "name": "TubularUmbilicalOSDUIntegration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    umbilical_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmbilicalType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
