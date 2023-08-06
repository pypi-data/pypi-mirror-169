from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_activity_parameter import AbstractActivityParameter
from witsml20.parameter_kind import ParameterKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ParameterTemplate:
    """
    Description of one parameter that participate in one type of activity.

    :ivar allowed_kind: If no allowed type is given, then all kind of
        datatypes is allowed.
    :ivar is_input: Indicates if the parameter is an input of the
        activity. If the parameter is a data object and is also an
        output of the activity, it is strongly advised to use two
        parameters : one for input and one for output. The reason is to
        be able to give two different versions strings for the input and
        output dataobject which has got obviously the same UUID.
    :ivar key_constraint: Allows to indicate that, in the same activity,
        this parameter template must be associated to another parameter
        template identified by its title.
    :ivar is_output: Indicates if the parameter is an output of the
        activity. If the parameter is a data object and is also an input
        of the activity, it is strongly advised to use two parameters :
        one for input and one for output. The reason is to be able to
        give two different versions strings for the input and output
        dataobject which has got obviously the same UUID.
    :ivar title: Name of the parameter in the activity. Key to identify
        parameter.
    :ivar data_object_content_type: When parameter is limited to data
        object of given types, describe the allowed types. Used only
        when ParameterType is dataObject
    :ivar max_occurs: Maximum number of parameters of this type allowed
        in the activity. If the maximum number of parameters is
        infinite, use -1 value.
    :ivar min_occurs: Minimum number of parameter of this type required
        by the activity. If the minimum number of parameters is
        infinite, use -1 value.
    :ivar constraint: Textual description of additional constraint
        associated with the parameter. (note that it will be better to
        have a formal description of the constraint)
    :ivar default_value:
    """
    allowed_kind: List[ParameterKind] = field(
        default_factory=list,
        metadata={
            "name": "AllowedKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    is_input: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsInput",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    key_constraint: List[str] = field(
        default_factory=list,
        metadata={
            "name": "KeyConstraint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    is_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsOutput",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    data_object_content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataObjectContentType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    max_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    min_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    constraint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    default_value: List[AbstractActivityParameter] = field(
        default_factory=list,
        metadata={
            "name": "DefaultValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
