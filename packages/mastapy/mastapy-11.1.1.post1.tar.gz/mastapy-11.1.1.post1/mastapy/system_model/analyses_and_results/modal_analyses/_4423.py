﻿'''_4423.py

StraightBevelGearSetModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2291
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6686
from mastapy.system_model.analyses_and_results.system_deflections import _2555
from mastapy.system_model.analyses_and_results.modal_analyses import _4422, _4421, _4324
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'StraightBevelGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetModalAnalysis',)


class StraightBevelGearSetModalAnalysis(_4324.BevelGearSetModalAnalysis):
    '''StraightBevelGearSetModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2291.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2291.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6686.StraightBevelGearSetLoadCase':
        '''StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6686.StraightBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2555.StraightBevelGearSetSystemDeflection':
        '''StraightBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2555.StraightBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def straight_bevel_gears_modal_analysis(self) -> 'List[_4422.StraightBevelGearModalAnalysis]':
        '''List[StraightBevelGearModalAnalysis]: 'StraightBevelGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsModalAnalysis, constructor.new(_4422.StraightBevelGearModalAnalysis))
        return value

    @property
    def straight_bevel_meshes_modal_analysis(self) -> 'List[_4421.StraightBevelGearMeshModalAnalysis]':
        '''List[StraightBevelGearMeshModalAnalysis]: 'StraightBevelMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesModalAnalysis, constructor.new(_4421.StraightBevelGearMeshModalAnalysis))
        return value
