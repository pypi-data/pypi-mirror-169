'''_2972.py

TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2097
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2842
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _2892
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'TorqueConverterConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionCompoundSteadyStateSynchronousResponse',)


class TorqueConverterConnectionCompoundSteadyStateSynchronousResponse(_2892.CouplingConnectionCompoundSteadyStateSynchronousResponse):
    '''TorqueConverterConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2097.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2097.TorqueConverterConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2097.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2097.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2842.TorqueConverterConnectionSteadyStateSynchronousResponse]':
        '''List[TorqueConverterConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2842.TorqueConverterConnectionSteadyStateSynchronousResponse))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2842.TorqueConverterConnectionSteadyStateSynchronousResponse]':
        '''List[TorqueConverterConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2842.TorqueConverterConnectionSteadyStateSynchronousResponse))
        return value
