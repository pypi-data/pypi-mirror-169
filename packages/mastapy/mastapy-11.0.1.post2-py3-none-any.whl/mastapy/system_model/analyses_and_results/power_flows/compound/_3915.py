﻿'''_3915.py

PlanetCarrierCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model import _2147
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3783
from mastapy.system_model.analyses_and_results.power_flows.compound import _3907
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PlanetCarrierCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierCompoundPowerFlow',)


class PlanetCarrierCompoundPowerFlow(_3907.MountableComponentCompoundPowerFlow):
    '''PlanetCarrierCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2147.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2147.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3783.PlanetCarrierPowerFlow]':
        '''List[PlanetCarrierPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3783.PlanetCarrierPowerFlow))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3783.PlanetCarrierPowerFlow]':
        '''List[PlanetCarrierPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3783.PlanetCarrierPowerFlow))
        return value
