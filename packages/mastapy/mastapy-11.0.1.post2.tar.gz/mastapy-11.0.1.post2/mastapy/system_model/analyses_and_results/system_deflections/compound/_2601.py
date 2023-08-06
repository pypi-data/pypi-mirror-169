﻿'''_2601.py

PartToPartShearCouplingHalfCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2265
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2454
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2557
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PartToPartShearCouplingHalfCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfCompoundSystemDeflection',)


class PartToPartShearCouplingHalfCompoundSystemDeflection(_2557.CouplingHalfCompoundSystemDeflection):
    '''PartToPartShearCouplingHalfCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2265.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2454.PartToPartShearCouplingHalfSystemDeflection]':
        '''List[PartToPartShearCouplingHalfSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_2454.PartToPartShearCouplingHalfSystemDeflection))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2454.PartToPartShearCouplingHalfSystemDeflection]':
        '''List[PartToPartShearCouplingHalfSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_2454.PartToPartShearCouplingHalfSystemDeflection))
        return value
