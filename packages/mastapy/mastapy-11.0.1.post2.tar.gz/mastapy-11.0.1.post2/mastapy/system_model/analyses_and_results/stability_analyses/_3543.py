﻿'''_3543.py

StraightBevelGearStabilityAnalysis
'''


from mastapy.system_model.part_model.gears import _2223
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6611
from mastapy.system_model.analyses_and_results.stability_analyses import _3448
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'StraightBevelGearStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearStabilityAnalysis',)


class StraightBevelGearStabilityAnalysis(_3448.BevelGearStabilityAnalysis):
    '''StraightBevelGearStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2223.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2223.StraightBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6611.StraightBevelGearLoadCase':
        '''StraightBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6611.StraightBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
