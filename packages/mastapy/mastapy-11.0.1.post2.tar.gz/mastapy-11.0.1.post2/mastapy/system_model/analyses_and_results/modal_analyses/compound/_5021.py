﻿'''_5021.py

SynchroniserSleeveCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4875
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _5020
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'SynchroniserSleeveCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveCompoundModalAnalysis',)


class SynchroniserSleeveCompoundModalAnalysis(_5020.SynchroniserPartCompoundModalAnalysis):
    '''SynchroniserSleeveCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2282.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.SynchroniserSleeve)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4875.SynchroniserSleeveModalAnalysis]':
        '''List[SynchroniserSleeveModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4875.SynchroniserSleeveModalAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4875.SynchroniserSleeveModalAnalysis]':
        '''List[SynchroniserSleeveModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4875.SynchroniserSleeveModalAnalysis))
        return value
