﻿'''_7089.py

RollingRingConnectionAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _2037
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6667
from mastapy.system_model.analyses_and_results.system_deflections import _2536
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7060
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'RollingRingConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionAdvancedSystemDeflection',)


class RollingRingConnectionAdvancedSystemDeflection(_7060.InterMountableComponentConnectionAdvancedSystemDeflection):
    '''RollingRingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2037.RollingRingConnection':
        '''RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2037.RollingRingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6667.RollingRingConnectionLoadCase':
        '''RollingRingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6667.RollingRingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingConnectionAdvancedSystemDeflection]':
        '''List[RollingRingConnectionAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingConnectionAdvancedSystemDeflection))
        return value

    @property
    def connection_system_deflection_results(self) -> 'List[_2536.RollingRingConnectionSystemDeflection]':
        '''List[RollingRingConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2536.RollingRingConnectionSystemDeflection))
        return value
