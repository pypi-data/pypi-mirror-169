﻿'''_3590.py

ConceptCouplingHalfCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2258
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3457
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3601
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConceptCouplingHalfCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfCompoundStabilityAnalysis',)


class ConceptCouplingHalfCompoundStabilityAnalysis(_3601.CouplingHalfCompoundStabilityAnalysis):
    '''ConceptCouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2258.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2258.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3457.ConceptCouplingHalfStabilityAnalysis]':
        '''List[ConceptCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3457.ConceptCouplingHalfStabilityAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3457.ConceptCouplingHalfStabilityAnalysis]':
        '''List[ConceptCouplingHalfStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3457.ConceptCouplingHalfStabilityAnalysis))
        return value
