﻿'''_6428.py

StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2222
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6426, _6427, _6339
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6299
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis',)


class StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis(_6339.BevelGearSetCompoundCriticalSpeedAnalysis):
    '''StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2222.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2222.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2222.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2222.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def straight_bevel_diff_gears_compound_critical_speed_analysis(self) -> 'List[_6426.StraightBevelDiffGearCompoundCriticalSpeedAnalysis]':
        '''List[StraightBevelDiffGearCompoundCriticalSpeedAnalysis]: 'StraightBevelDiffGearsCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundCriticalSpeedAnalysis, constructor.new(_6426.StraightBevelDiffGearCompoundCriticalSpeedAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_compound_critical_speed_analysis(self) -> 'List[_6427.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis]':
        '''List[StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis]: 'StraightBevelDiffMeshesCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundCriticalSpeedAnalysis, constructor.new(_6427.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6299.StraightBevelDiffGearSetCriticalSpeedAnalysis]':
        '''List[StraightBevelDiffGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6299.StraightBevelDiffGearSetCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6299.StraightBevelDiffGearSetCriticalSpeedAnalysis]':
        '''List[StraightBevelDiffGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6299.StraightBevelDiffGearSetCriticalSpeedAnalysis))
        return value
