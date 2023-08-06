from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.interporosity_flow_parameter import InterporosityFlowParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LayerToLayerConnection:
    """Data about other layers to which this layer connects in terms of a flow
    connection.

    Comprises the identity of the other layer, and the inter-layer flow
    coefficient.

    :ivar connected_layer_ref_id: Reference to another layer to which
        this layer is connected for flow.
    :ivar inter_layer_connectivity: The Flow Parameter value between the
        two Layers.
    """
    connected_layer_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectedLayerRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    inter_layer_connectivity: Optional[InterporosityFlowParameter] = field(
        default=None,
        metadata={
            "name": "InterLayerConnectivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
