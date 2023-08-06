'''_5095.py

TorqueConverterPumpCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2351
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4966
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5015
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'TorqueConverterPumpCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCompoundModalAnalysisAtASpeed',)


class TorqueConverterPumpCompoundModalAnalysisAtASpeed(_5015.CouplingHalfCompoundModalAnalysisAtASpeed):
    '''TorqueConverterPumpCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCompoundModalAnalysisAtASpeed.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_4966.TorqueConverterPumpModalAnalysisAtASpeed]':
        '''List[TorqueConverterPumpModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4966.TorqueConverterPumpModalAnalysisAtASpeed))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4966.TorqueConverterPumpModalAnalysisAtASpeed]':
        '''List[TorqueConverterPumpModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4966.TorqueConverterPumpModalAnalysisAtASpeed))
        return value
