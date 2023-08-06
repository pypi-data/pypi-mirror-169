﻿'''_6382.py

TorqueConverterPumpCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model.couplings import _2351
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6696
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6300
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'TorqueConverterPumpCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCriticalSpeedAnalysis',)


class TorqueConverterPumpCriticalSpeedAnalysis(_6300.CouplingHalfCriticalSpeedAnalysis):
    '''TorqueConverterPumpCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2351.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2351.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6696.TorqueConverterPumpLoadCase':
        '''TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6696.TorqueConverterPumpLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
