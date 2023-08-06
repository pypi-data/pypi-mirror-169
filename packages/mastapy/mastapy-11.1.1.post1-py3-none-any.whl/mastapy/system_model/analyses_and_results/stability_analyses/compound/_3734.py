﻿'''_3734.py

SpiralBevelGearSetCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2287
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3732, _3733, _3651
from mastapy.system_model.analyses_and_results.stability_analyses import _3602
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'SpiralBevelGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundStabilityAnalysis',)


class SpiralBevelGearSetCompoundStabilityAnalysis(_3651.BevelGearSetCompoundStabilityAnalysis):
    '''SpiralBevelGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2287.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2287.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2287.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2287.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def spiral_bevel_gears_compound_stability_analysis(self) -> 'List[_3732.SpiralBevelGearCompoundStabilityAnalysis]':
        '''List[SpiralBevelGearCompoundStabilityAnalysis]: 'SpiralBevelGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundStabilityAnalysis, constructor.new(_3732.SpiralBevelGearCompoundStabilityAnalysis))
        return value

    @property
    def spiral_bevel_meshes_compound_stability_analysis(self) -> 'List[_3733.SpiralBevelGearMeshCompoundStabilityAnalysis]':
        '''List[SpiralBevelGearMeshCompoundStabilityAnalysis]: 'SpiralBevelMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundStabilityAnalysis, constructor.new(_3733.SpiralBevelGearMeshCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3602.SpiralBevelGearSetStabilityAnalysis]':
        '''List[SpiralBevelGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3602.SpiralBevelGearSetStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3602.SpiralBevelGearSetStabilityAnalysis]':
        '''List[SpiralBevelGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3602.SpiralBevelGearSetStabilityAnalysis))
        return value
