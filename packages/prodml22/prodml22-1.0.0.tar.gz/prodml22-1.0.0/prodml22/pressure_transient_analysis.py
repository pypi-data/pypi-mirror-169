from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_analysis import AbstractAnalysis
from prodml22.abstract_object import AbstractObject
from prodml22.compressibility_parameters import CompressibilityParameters
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_phase_kind import FluidPhaseKind
from prodml22.interfering_flow_test_interval import InterferingFlowTestInterval
from prodml22.layer_model import LayerModel
from prodml22.pressure_non_linear_transform_kind import PressureNonLinearTransformKind
from prodml22.pseudo_pressure_effect_applied import PseudoPressureEffectApplied
from prodml22.time_non_linear_transform_kind import TimeNonLinearTransformKind
from prodml22.wellbore_base_model import WellboreBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PressureTransientAnalysis(AbstractObject):
    """Contains the data about the analysis and the model used, in a PTA
    Analysis.

    An Analysis may be a pressure transient (PTA), rate transient (RTA)
    or Test Design, depending on which data is supplied. This object
    contains common parameters. The Analysis has one or more Test
    Location Analysis elements and each reports the model details for
    one Test Location.

    :ivar model_name: The name of the model used - textual description
        of the whole model. No semantic meaning. Example: "Dual porosity
        with 2 parallel faults".  The full details of the model are in
        the Wellbore Model and layerModel sections of the
        TestLocationAnalysis.
    :ivar time_applies_from: The time this Analysis was created (ie, the
        time of analysis, not the time of data acquisition).
    :ivar method_name: The name of the method used for analysis -
        textual description. No semantic meaning. Example: "non-linear
        regression".
    :ivar time_applies_to: The time this Analysis was finished (ie, the
        time of analysis, not the time of data acquisition).
    :ivar is_numerical_analysis: Set to TRUE if the Analysis is done
        with numerical modeling.
    :ivar fluid_characterization: A reference, using data object
        reference, to a FluidCharacterization data-object containing the
        fluid parameters for this PTA.
    :ivar numerical_pta_model: A reference, using data object reference,
        to a RESQML data-object containing the root level data for a
        numerical PTA model.
    :ivar flow_test_activity: Abstract wellbore response model from
        which the other wellbore response model types are derived.
    :ivar principal_flow_test_measurement_set_ref: A reference (using
        uid) to the flow test measurement set which contains the data
        concerning the principal test location, in the case of an
        interference test. For standard (non-interference) tests, this
        is not needed to be filled in, since there is only one flow test
        location and therefore only one  flow test measurement set.
    :ivar principal_test_period_ref: A reference (using uid) to the test
        period(s) whose effect the analysis is being performed on.  In
        the case of an interference test, this reference is to the test
        period(s) of the principal flow test location. The test periods
        of interfering flow test locations are included under the
        Interfering Flow Test Interval element(s).
    :ivar wellbore_model: Abstract wellbore response model from which
        the other wellbore response model types are derived.
    :ivar layer_model: Contains the data about a layer model for PTA or
        Inflow analysis. This class contains common parameters and then
        model sections each report the parameter values for the pressure
        transient model used to describe the later. These are: near
        wellbore, reservoir, and boundary sections. Example: closed
        reservoir boundary section model will report 4 distances to
        boundaries.
    :ivar fluid_phase_analysis_kind: An enum of which phases are being
        analysed by this analysis (i.e., single phase or multi-phase
        analyses).
    :ivar pressure_non_linear_transform_kind: Enum for gas or multiphase
        pseudo pressure analyses using pressure transforms. If pseudo
        pressure, then further details on the kind of pseudo pressure
        will be found in the Pseudo Pressure Effect Applied element.
    :ivar pseudo_pressure_effect_applied: Recurring enum used to list
        all the transforms which have been included in the pseudo
        pressure transform. If "Other" is selected, a comment should be
        used to explain.
    :ivar time_non_linear_transform_kind: Enum for gas pseudo time
        analyses using time transforms.
    :ivar remark: Textual description about the value of this field.
    :ivar analysis:
    :ivar compressibility_parameters:
    :ivar interfering_flow_test_interval: Measurements pertaining to the
        interfering flow, in the case of an interference test.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    model_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelName",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    time_applies_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeAppliesFrom",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "max_length": 2000,
        }
    )
    time_applies_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeAppliesTo",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    is_numerical_analysis: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsNumericalAnalysis",
            "type": "Element",
        }
    )
    fluid_characterization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidCharacterization",
            "type": "Element",
        }
    )
    numerical_pta_model: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "NumericalPtaModel",
            "type": "Element",
        }
    )
    flow_test_activity: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    principal_flow_test_measurement_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrincipalFlowTestMeasurementSetRef",
            "type": "Element",
            "max_length": 64,
        }
    )
    principal_test_period_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PrincipalTestPeriodRef",
            "type": "Element",
            "min_occurs": 1,
            "max_length": 64,
        }
    )
    wellbore_model: Optional[WellboreBaseModel] = field(
        default=None,
        metadata={
            "name": "WellboreModel",
            "type": "Element",
        }
    )
    layer_model: List[LayerModel] = field(
        default_factory=list,
        metadata={
            "name": "LayerModel",
            "type": "Element",
        }
    )
    fluid_phase_analysis_kind: Optional[FluidPhaseKind] = field(
        default=None,
        metadata={
            "name": "FluidPhaseAnalysisKind",
            "type": "Element",
            "required": True,
        }
    )
    pressure_non_linear_transform_kind: Optional[PressureNonLinearTransformKind] = field(
        default=None,
        metadata={
            "name": "PressureNonLinearTransformKind",
            "type": "Element",
            "required": True,
        }
    )
    pseudo_pressure_effect_applied: Optional[PseudoPressureEffectApplied] = field(
        default=None,
        metadata={
            "name": "PseudoPressureEffectApplied",
            "type": "Element",
        }
    )
    time_non_linear_transform_kind: Optional[TimeNonLinearTransformKind] = field(
        default=None,
        metadata={
            "name": "TimeNonLinearTransformKind",
            "type": "Element",
            "required": True,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_length": 2000,
        }
    )
    analysis: Optional[AbstractAnalysis] = field(
        default=None,
        metadata={
            "name": "Analysis",
            "type": "Element",
        }
    )
    compressibility_parameters: Optional[CompressibilityParameters] = field(
        default=None,
        metadata={
            "name": "CompressibilityParameters",
            "type": "Element",
        }
    )
    interfering_flow_test_interval: List[InterferingFlowTestInterval] = field(
        default_factory=list,
        metadata={
            "name": "InterferingFlowTestInterval",
            "type": "Element",
        }
    )
