﻿'''_4205.py

SpiralBevelGearCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2219
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4077
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4122
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'SpiralBevelGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearCompoundParametricStudyTool',)


class SpiralBevelGearCompoundParametricStudyTool(_4122.BevelGearCompoundParametricStudyTool):
    '''SpiralBevelGearCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2219.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2219.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4077.SpiralBevelGearParametricStudyTool]':
        '''List[SpiralBevelGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4077.SpiralBevelGearParametricStudyTool))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4077.SpiralBevelGearParametricStudyTool]':
        '''List[SpiralBevelGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4077.SpiralBevelGearParametricStudyTool))
        return value
