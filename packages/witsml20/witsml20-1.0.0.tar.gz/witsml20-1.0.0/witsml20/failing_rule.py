from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FailingRule:
    """
    The FailingRule class holds summary information on which of the rules
    within a policy failed.

    :ivar rule_id: Identifier of the atomic rule being checked against
        the data.
    :ivar rule_name: Human-readable name of the atomic rule being
        checked against the data.
    :ivar severity: Severity of the failure. This could be used to
        indicate that a rule is a high-priority rule whose failure is
        considered as severe or could be used to indicate just how badly
        a rule was contravened. The meaning of this field should be
        standardized within a company to maximize its utility.
    :ivar failing_rule_extensions: This allows extending the FailingRule
        class with as many arbitrary name-value pairs as is required at
        run-time. Uses for this might include why the rule failed or by
        how much.
    """
    rule_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    rule_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    severity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    failing_rule_extensions: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "FailingRuleExtensions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
