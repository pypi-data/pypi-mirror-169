﻿'''_6350.py

PowerLoadCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model import _2216
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6660
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6385
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PowerLoadCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadCriticalSpeedAnalysis',)


class PowerLoadCriticalSpeedAnalysis(_6385.VirtualComponentCriticalSpeedAnalysis):
    '''PowerLoadCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2216.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2216.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6660.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6660.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
