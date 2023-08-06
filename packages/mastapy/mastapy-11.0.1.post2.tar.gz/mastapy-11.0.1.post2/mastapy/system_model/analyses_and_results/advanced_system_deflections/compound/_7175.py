﻿'''_7175.py

UnbalancedMassCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2155
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7046
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7176
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'UnbalancedMassCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundAdvancedSystemDeflection',)


class UnbalancedMassCompoundAdvancedSystemDeflection(_7176.VirtualComponentCompoundAdvancedSystemDeflection):
    '''UnbalancedMassCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2155.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2155.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7046.UnbalancedMassAdvancedSystemDeflection]':
        '''List[UnbalancedMassAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_7046.UnbalancedMassAdvancedSystemDeflection))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7046.UnbalancedMassAdvancedSystemDeflection]':
        '''List[UnbalancedMassAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_7046.UnbalancedMassAdvancedSystemDeflection))
        return value
