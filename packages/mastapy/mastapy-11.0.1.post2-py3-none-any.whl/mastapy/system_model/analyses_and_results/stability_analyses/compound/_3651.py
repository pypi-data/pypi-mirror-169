﻿'''_3651.py

RingPinsCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2246
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3520
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3639
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'RingPinsCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsCompoundStabilityAnalysis',)


class RingPinsCompoundStabilityAnalysis(_3639.MountableComponentCompoundStabilityAnalysis):
    '''RingPinsCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2246.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2246.RingPins)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3520.RingPinsStabilityAnalysis]':
        '''List[RingPinsStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3520.RingPinsStabilityAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3520.RingPinsStabilityAnalysis]':
        '''List[RingPinsStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3520.RingPinsStabilityAnalysis))
        return value
