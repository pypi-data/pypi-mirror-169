﻿'''_3933.py

SpringDamperConnectionCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2031
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3802
from mastapy.system_model.analyses_and_results.power_flows.compound import _3868
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpringDamperConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCompoundPowerFlow',)


class SpringDamperConnectionCompoundPowerFlow(_3868.CouplingConnectionCompoundPowerFlow):
    '''SpringDamperConnectionCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2031.SpringDamperConnection':
        '''SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2031.SpringDamperConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def connection_design(self) -> '_2031.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2031.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3802.SpringDamperConnectionPowerFlow]':
        '''List[SpringDamperConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3802.SpringDamperConnectionPowerFlow))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3802.SpringDamperConnectionPowerFlow]':
        '''List[SpringDamperConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3802.SpringDamperConnectionPowerFlow))
        return value
