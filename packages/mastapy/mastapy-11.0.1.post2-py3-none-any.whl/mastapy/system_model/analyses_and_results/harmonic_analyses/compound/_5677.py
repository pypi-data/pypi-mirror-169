﻿'''_5677.py

OilSealCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2210
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5509
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5635
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'OilSealCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCompoundHarmonicAnalysis',)


class OilSealCompoundHarmonicAnalysis(_5635.ConnectorCompoundHarmonicAnalysis):
    '''OilSealCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2210.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2210.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5509.OilSealHarmonicAnalysis]':
        '''List[OilSealHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5509.OilSealHarmonicAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5509.OilSealHarmonicAnalysis]':
        '''List[OilSealHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5509.OilSealHarmonicAnalysis))
        return value
