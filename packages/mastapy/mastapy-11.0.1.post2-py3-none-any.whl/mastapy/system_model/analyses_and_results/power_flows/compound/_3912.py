﻿'''_3912.py

PartToPartShearCouplingHalfCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2265
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3779
from mastapy.system_model.analyses_and_results.power_flows.compound import _3869
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PartToPartShearCouplingHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfCompoundPowerFlow',)


class PartToPartShearCouplingHalfCompoundPowerFlow(_3869.CouplingHalfCompoundPowerFlow):
    '''PartToPartShearCouplingHalfCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2265.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3779.PartToPartShearCouplingHalfPowerFlow]':
        '''List[PartToPartShearCouplingHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3779.PartToPartShearCouplingHalfPowerFlow))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3779.PartToPartShearCouplingHalfPowerFlow]':
        '''List[PartToPartShearCouplingHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3779.PartToPartShearCouplingHalfPowerFlow))
        return value
