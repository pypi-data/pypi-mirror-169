from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_disposition import AbstractDisposition
from prodml22.terminal_lifting import TerminalLifting

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TerminalLiftingDisposition(AbstractDisposition):
    """Use to report  terminal lifting as dispositions within the periodic
    asset production volumes reporting.

    The components of petroleum disposition are stock change, crude oil losses, refinery inputs, exports, and products supplied for domestic consumption (https://www.eia.gov/dnav/pet/TblDefs/pet_sum_crdsnd_tbldef2.asp)
    """
    terminal_lifting: Optional[TerminalLifting] = field(
        default=None,
        metadata={
            "name": "TerminalLifting",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
