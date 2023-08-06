﻿'''_7040.py

CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.cycloidal import _2083
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6577
from mastapy.system_model.analyses_and_results.system_deflections import _2475
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6993
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection',)


class CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection(_6993.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection):
    '''CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2083.CycloidalDiscPlanetaryBearingConnection':
        '''CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2083.CycloidalDiscPlanetaryBearingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6577.CycloidalDiscPlanetaryBearingConnectionLoadCase':
        '''CycloidalDiscPlanetaryBearingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6577.CycloidalDiscPlanetaryBearingConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2475.CycloidalDiscPlanetaryBearingConnectionSystemDeflection]':
        '''List[CycloidalDiscPlanetaryBearingConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2475.CycloidalDiscPlanetaryBearingConnectionSystemDeflection))
        return value
