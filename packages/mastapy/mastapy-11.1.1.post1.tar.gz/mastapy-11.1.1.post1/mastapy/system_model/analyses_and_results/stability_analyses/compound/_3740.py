﻿'''_3740.py

StraightBevelDiffGearSetCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2289
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3738, _3739, _3651
from mastapy.system_model.analyses_and_results.stability_analyses import _3610
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'StraightBevelDiffGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundStabilityAnalysis',)


class StraightBevelDiffGearSetCompoundStabilityAnalysis(_3651.BevelGearSetCompoundStabilityAnalysis):
    '''StraightBevelDiffGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundStabilityAnalysis.TYPE'):
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
    def straight_bevel_diff_gears_compound_stability_analysis(self) -> 'List[_3738.StraightBevelDiffGearCompoundStabilityAnalysis]':
        '''List[StraightBevelDiffGearCompoundStabilityAnalysis]: 'StraightBevelDiffGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundStabilityAnalysis, constructor.new(_3738.StraightBevelDiffGearCompoundStabilityAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_compound_stability_analysis(self) -> 'List[_3739.StraightBevelDiffGearMeshCompoundStabilityAnalysis]':
        '''List[StraightBevelDiffGearMeshCompoundStabilityAnalysis]: 'StraightBevelDiffMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundStabilityAnalysis, constructor.new(_3739.StraightBevelDiffGearMeshCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3610.StraightBevelDiffGearSetStabilityAnalysis]':
        '''List[StraightBevelDiffGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3610.StraightBevelDiffGearSetStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3610.StraightBevelDiffGearSetStabilityAnalysis]':
        '''List[StraightBevelDiffGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3610.StraightBevelDiffGearSetStabilityAnalysis))
        return value
