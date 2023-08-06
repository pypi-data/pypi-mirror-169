﻿'''_3923.py

RollingRingConnectionCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _1973
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3792
from mastapy.system_model.analyses_and_results.power_flows.compound import _3895
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'RollingRingConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionCompoundPowerFlow',)


class RollingRingConnectionCompoundPowerFlow(_3895.InterMountableComponentConnectionCompoundPowerFlow):
    '''RollingRingConnectionCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_CONNECTION_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_1973.RollingRingConnection':
        '''RollingRingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1973.RollingRingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def connection_design(self) -> '_1973.RollingRingConnection':
        '''RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1973.RollingRingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3792.RollingRingConnectionPowerFlow]':
        '''List[RollingRingConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_3792.RollingRingConnectionPowerFlow))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3792.RollingRingConnectionPowerFlow]':
        '''List[RollingRingConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_3792.RollingRingConnectionPowerFlow))
        return value
