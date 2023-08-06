﻿'''_4841.py

WormGearCompoundModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.gears import _2294
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4713
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4776
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'WormGearCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCompoundModalAnalysisAtAStiffness',)


class WormGearCompoundModalAnalysisAtAStiffness(_4776.GearCompoundModalAnalysisAtAStiffness):
    '''WormGearCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2294.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2294.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4713.WormGearModalAnalysisAtAStiffness]':
        '''List[WormGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4713.WormGearModalAnalysisAtAStiffness))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4713.WormGearModalAnalysisAtAStiffness]':
        '''List[WormGearModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4713.WormGearModalAnalysisAtAStiffness))
        return value
