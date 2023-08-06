﻿'''_2638.py

TorqueConverterConnectionCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2033
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2495
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2556
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'TorqueConverterConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionCompoundSystemDeflection',)


class TorqueConverterConnectionCompoundSystemDeflection(_2556.CouplingConnectionCompoundSystemDeflection):
    '''TorqueConverterConnectionCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2033.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2033.TorqueConverterConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def connection_design(self) -> '_2033.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2033.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2495.TorqueConverterConnectionSystemDeflection]':
        '''List[TorqueConverterConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2495.TorqueConverterConnectionSystemDeflection))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2495.TorqueConverterConnectionSystemDeflection]':
        '''List[TorqueConverterConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2495.TorqueConverterConnectionSystemDeflection))
        return value
