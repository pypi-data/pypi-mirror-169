from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_model_section import AbstractModelSection
from prodml22.average_pressure import AveragePressure
from prodml22.horizontal_anisotropy_kx_to_ky import HorizontalAnisotropyKxToKy
from prodml22.horizontal_radial_permeability import HorizontalRadialPermeability
from prodml22.initial_pressure import InitialPressure
from prodml22.lower_boundary_type import LowerBoundaryType
from prodml22.orientation_of_anisotropy_xdirection import OrientationOfAnisotropyXdirection
from prodml22.permeability_thickness_product import PermeabilityThicknessProduct
from prodml22.porosity import Porosity
from prodml22.pressure_datum_tvd import PressureDatumTvd
from prodml22.total_thickness import TotalThickness
from prodml22.upper_boundary_type import UpperBoundaryType
from prodml22.vertical_anisotropy_kv_to_kr import VerticalAnisotropyKvToKr

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReservoirBaseModel(AbstractModelSection):
    """
    Abstract reservoir model from which the other types are derived.
    """
    horizontal_radial_permeability: Optional[HorizontalRadialPermeability] = field(
        default=None,
        metadata={
            "name": "HorizontalRadialPermeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    total_thickness: Optional[TotalThickness] = field(
        default=None,
        metadata={
            "name": "TotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    permeability_thickness_product: Optional[PermeabilityThicknessProduct] = field(
        default=None,
        metadata={
            "name": "PermeabilityThicknessProduct",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    porosity: Optional[Porosity] = field(
        default=None,
        metadata={
            "name": "Porosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    initial_pressure: Optional[InitialPressure] = field(
        default=None,
        metadata={
            "name": "InitialPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    pressure_datum_tvd: Optional[PressureDatumTvd] = field(
        default=None,
        metadata={
            "name": "PressureDatumTVD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    average_pressure: Optional[AveragePressure] = field(
        default=None,
        metadata={
            "name": "AveragePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vertical_anisotropy_kv_to_kr: Optional[VerticalAnisotropyKvToKr] = field(
        default=None,
        metadata={
            "name": "VerticalAnisotropyKvToKr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    horizontal_anisotropy_kx_to_ky: Optional[HorizontalAnisotropyKxToKy] = field(
        default=None,
        metadata={
            "name": "HorizontalAnisotropyKxToKy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    orientation_of_anisotropy_xdirection: Optional[OrientationOfAnisotropyXdirection] = field(
        default=None,
        metadata={
            "name": "OrientationOfAnisotropyXDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    upper_boundary_type: Optional[UpperBoundaryType] = field(
        default=None,
        metadata={
            "name": "UpperBoundaryType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    lower_boundary_type: Optional[LowerBoundaryType] = field(
        default=None,
        metadata={
            "name": "LowerBoundaryType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
