'''_2892.py

CouplingConnectionCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2758
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _2919
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CouplingConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundSteadyStateSynchronousResponse',)


class CouplingConnectionCompoundSteadyStateSynchronousResponse(_2919.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse):
    '''CouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2758.CouplingConnectionSteadyStateSynchronousResponse]':
        '''List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2758.CouplingConnectionSteadyStateSynchronousResponse))
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2758.CouplingConnectionSteadyStateSynchronousResponse]':
        '''List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2758.CouplingConnectionSteadyStateSynchronousResponse))
        return value
