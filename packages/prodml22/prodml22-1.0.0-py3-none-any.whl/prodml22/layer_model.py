from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.data_object_reference import DataObjectReference
from prodml22.layer_to_layer_connection import LayerToLayerConnection
from prodml22.measured_depth import MeasuredDepth
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.pressure_per_flowrate_measure import PressurePerFlowrateMeasure
from prodml22.pressure_per_flowrate_squared_measure import PressurePerFlowrateSquaredMeasure
from prodml22.reservoir_base_model import ReservoirBaseModel
from prodml22.volume_per_time_per_pressure_measure import VolumePerTimePerPressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LayerModel:
    """Contains the data about a layer model for PTA or Inflow analysis.

    This class contains common parameters and then model sections each
    report the parameter values for the pressure transient model used to
    describe the later. These are: near wellbore, reservoir, and
    boundary sections. Example: closed reservoir boundary section model
    will report 4 distances to boundaries.

    :ivar name: The name of the layer for which this later model
        applies.  Probably a geologically meaningful name.
    :ivar aggregate_layers_model: If set to True, indicates that this
        layer represents the analysis of the total number of individual
        layers at this Test Location. Example: it will represent the
        total Kh (permeability-thickness product) and Total Skin of the
        Test Location. If False then this layer represents just one of
        the total number of reservoir layer(s) tested at this Test
        Location.
    :ivar geologic_feature: The name of the geology feature (typically,
        layer or layers) to which this model layer corresponds.
    :ivar md_top_layer: The measured depth top of this layer, as seen
        along the wellbore.
    :ivar md_bottom_layer: The measured depth bottom of this layer, as
        seen along the wellbore.
    :ivar layer_productivity_index: This is the productivity Index of
        the layer, expressed in terms of flowrate/pressure.
    :ivar layer_turbulent_flow_coefficient: This is the coefficient for
        turbulent flow pressure drop in the Inflow Performance
        Relationship.  In which dP=J*Q+F*Q**2. This parameter is F and
        the Productivity Index is J.
    :ivar layer_laminar_flow_coefficient: This is the coefficient for
        laminar flow pressure drop.
    :ivar near_wellbore_model: For this layer model, the Near Wellbore
        Model which is used - which will be a child node of this layer
        model.
    :ivar reservoir_model: For this layer model, the Reservoir Model
        which is used - which will be a child node of this layer model.
    :ivar boundary_model: For this layer model, the Boundary Model which
        is used - which will be a child node of this layer model.
    :ivar layer_to_layer_connection:
    :ivar uid: Unique identifier for this instance of the object.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    aggregate_layers_model: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AggregateLayersModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    geologic_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeologicFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    md_top_layer: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdTopLayer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    md_bottom_layer: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBottomLayer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    layer_productivity_index: Optional[VolumePerTimePerPressureMeasure] = field(
        default=None,
        metadata={
            "name": "LayerProductivityIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    layer_turbulent_flow_coefficient: Optional[PressurePerFlowrateSquaredMeasure] = field(
        default=None,
        metadata={
            "name": "LayerTurbulentFlowCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    layer_laminar_flow_coefficient: Optional[PressurePerFlowrateMeasure] = field(
        default=None,
        metadata={
            "name": "LayerLaminarFlowCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    near_wellbore_model: Optional[NearWellboreBaseModel] = field(
        default=None,
        metadata={
            "name": "NearWellboreModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reservoir_model: Optional[ReservoirBaseModel] = field(
        default=None,
        metadata={
            "name": "ReservoirModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    boundary_model: Optional[BoundaryBaseModel] = field(
        default=None,
        metadata={
            "name": "BoundaryModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    layer_to_layer_connection: List[LayerToLayerConnection] = field(
        default_factory=list,
        metadata={
            "name": "LayerToLayerConnection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
