﻿'''_5083.py

StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2289
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5081, _5082, _4994
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4954
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed',)


class StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed(_4994.BevelGearSetCompoundModalAnalysisAtASpeed):
    '''StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2289.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2289.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2289.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2289.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def straight_bevel_diff_gears_compound_modal_analysis_at_a_speed(self) -> 'List[_5081.StraightBevelDiffGearCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearCompoundModalAnalysisAtASpeed]: 'StraightBevelDiffGearsCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundModalAnalysisAtASpeed, constructor.new(_5081.StraightBevelDiffGearCompoundModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_diff_meshes_compound_modal_analysis_at_a_speed(self) -> 'List[_5082.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed]: 'StraightBevelDiffMeshesCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundModalAnalysisAtASpeed, constructor.new(_5082.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4954.StraightBevelDiffGearSetModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4954.StraightBevelDiffGearSetModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4954.StraightBevelDiffGearSetModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4954.StraightBevelDiffGearSetModalAnalysisAtASpeed))
        return value
