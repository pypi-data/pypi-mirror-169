from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.osdulineage_assertion import OsdulineageAssertion
from prodml22.osduspatial_location_integration import OsduspatialLocationIntegration
from prodml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Osduintegration:
    """
    Container for elemnts and types needed solely for intagration within OSDU.

    :ivar lineage_assertions:
    :ivar owner_group:
    :ivar viewer_group:
    :ivar legal_tags:
    :ivar osdugeo_json: Optional copy of the GeoJSON created by or for
        OSDU. This presumably contains a WGS84-only version of whatever
        shape represents the toplevel object.
    :ivar wgs84_latitude:
    :ivar wgs84_longitude:
    :ivar wgs84_location_metadata:
    :ivar field_value:
    :ivar country:
    :ivar state:
    :ivar county:
    :ivar city:
    :ivar region:
    :ivar district:
    :ivar block:
    :ivar prospect:
    :ivar play:
    :ivar basin:
    """
    class Meta:
        name = "OSDUIntegration"

    lineage_assertions: List[OsdulineageAssertion] = field(
        default_factory=list,
        metadata={
            "name": "LineageAssertions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    owner_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OwnerGroup",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 256,
        }
    )
    viewer_group: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ViewerGroup",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 256,
        }
    )
    legal_tags: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LegalTags",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 256,
        }
    )
    osdugeo_json: Optional[str] = field(
        default=None,
        metadata={
            "name": "OSDUGeoJSON",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    wgs84_latitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "WGS84Latitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    wgs84_longitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "WGS84Longitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    wgs84_location_metadata: Optional[OsduspatialLocationIntegration] = field(
        default=None,
        metadata={
            "name": "WGS84LocationMetadata",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    field_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    block: Optional[str] = field(
        default=None,
        metadata={
            "name": "Block",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    prospect: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prospect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    play: Optional[str] = field(
        default=None,
        metadata={
            "name": "Play",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    basin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Basin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
