﻿'''_2540.py

ClutchConnectionCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2023
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2380
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2556
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ClutchConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundSystemDeflection',)


class ClutchConnectionCompoundSystemDeflection(_2556.CouplingConnectionCompoundSystemDeflection):
    '''ClutchConnectionCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2023.ClutchConnection':
        '''ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2023.ClutchConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def connection_design(self) -> '_2023.ClutchConnection':
        '''ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2023.ClutchConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2380.ClutchConnectionSystemDeflection]':
        '''List[ClutchConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2380.ClutchConnectionSystemDeflection))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2380.ClutchConnectionSystemDeflection]':
        '''List[ClutchConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2380.ClutchConnectionSystemDeflection))
        return value
