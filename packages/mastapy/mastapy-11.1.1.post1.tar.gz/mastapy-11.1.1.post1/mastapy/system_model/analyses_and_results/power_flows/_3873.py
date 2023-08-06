﻿'''_3873.py

SpringDamperConnectionPowerFlow
'''


from mastapy.system_model.connections_and_sockets.couplings import _2095
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6678
from mastapy.system_model.analyses_and_results.power_flows import _3805
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'SpringDamperConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionPowerFlow',)


class SpringDamperConnectionPowerFlow(_3805.CouplingConnectionPowerFlow):
    '''SpringDamperConnectionPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2095.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2095.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6678.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6678.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
