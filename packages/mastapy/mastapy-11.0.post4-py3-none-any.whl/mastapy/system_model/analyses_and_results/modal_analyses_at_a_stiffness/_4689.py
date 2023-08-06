﻿'''_4689.py

SpiralBevelGearModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.gears import _2286
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6675
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4605
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'SpiralBevelGearModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearModalAnalysisAtAStiffness',)


class SpiralBevelGearModalAnalysisAtAStiffness(_4605.BevelGearModalAnalysisAtAStiffness):
    '''SpiralBevelGearModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2286.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2286.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6675.SpiralBevelGearLoadCase':
        '''SpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6675.SpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
