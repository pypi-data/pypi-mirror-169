﻿'''_3787.py

PowerLoadPowerFlow
'''


from mastapy.system_model.part_model import _2150
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6586
from mastapy.system_model.analyses_and_results.power_flows import _3823
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'PowerLoadPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadPowerFlow',)


class PowerLoadPowerFlow(_3823.VirtualComponentPowerFlow):
    '''PowerLoadPowerFlow

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2150.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2150.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6586.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6586.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
