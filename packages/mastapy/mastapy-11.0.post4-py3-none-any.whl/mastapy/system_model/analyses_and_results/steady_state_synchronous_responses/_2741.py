﻿'''_2741.py

BoltSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model import _2187
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6549
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2746
from mastapy._internal.python_net import python_net_import

_BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'BoltSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltSteadyStateSynchronousResponse',)


class BoltSteadyStateSynchronousResponse(_2746.ComponentSteadyStateSynchronousResponse):
    '''BoltSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _BOLT_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2187.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2187.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6549.BoltLoadCase':
        '''BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6549.BoltLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
