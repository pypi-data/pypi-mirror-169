﻿'''_7168.py

SynchroniserHalfCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2280
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7038
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7169
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'SynchroniserHalfCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundAdvancedSystemDeflection',)


class SynchroniserHalfCompoundAdvancedSystemDeflection(_7169.SynchroniserPartCompoundAdvancedSystemDeflection):
    '''SynchroniserHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2280.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2280.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7038.SynchroniserHalfAdvancedSystemDeflection]':
        '''List[SynchroniserHalfAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_7038.SynchroniserHalfAdvancedSystemDeflection))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7038.SynchroniserHalfAdvancedSystemDeflection]':
        '''List[SynchroniserHalfAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_7038.SynchroniserHalfAdvancedSystemDeflection))
        return value
