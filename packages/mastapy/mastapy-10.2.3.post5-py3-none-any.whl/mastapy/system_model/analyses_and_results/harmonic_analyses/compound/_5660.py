﻿'''_5660.py

GuideDxfModelCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2199
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5486
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5624
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'GuideDxfModelCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundHarmonicAnalysis',)


class GuideDxfModelCompoundHarmonicAnalysis(_5624.ComponentCompoundHarmonicAnalysis):
    '''GuideDxfModelCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2199.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2199.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5486.GuideDxfModelHarmonicAnalysis]':
        '''List[GuideDxfModelHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5486.GuideDxfModelHarmonicAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5486.GuideDxfModelHarmonicAnalysis]':
        '''List[GuideDxfModelHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5486.GuideDxfModelHarmonicAnalysis))
        return value
