﻿'''_4060.py

ConceptGearParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2264
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6558
from mastapy.system_model.analyses_and_results.system_deflections import _2460
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4096
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConceptGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearParametricStudyTool',)


class ConceptGearParametricStudyTool(_4096.GearParametricStudyTool):
    '''ConceptGearParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2264.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6558.ConceptGearLoadCase':
        '''ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6558.ConceptGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2460.ConceptGearSystemDeflection]':
        '''List[ConceptGearSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2460.ConceptGearSystemDeflection))
        return value
