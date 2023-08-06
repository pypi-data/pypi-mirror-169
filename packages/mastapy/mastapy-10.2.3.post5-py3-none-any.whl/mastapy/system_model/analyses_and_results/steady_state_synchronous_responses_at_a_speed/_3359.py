﻿'''_3359.py

SynchroniserSteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model.couplings import _2345
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6690
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3340
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'SynchroniserSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSteadyStateSynchronousResponseAtASpeed',)


class SynchroniserSteadyStateSynchronousResponseAtASpeed(_3340.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed):
    '''SynchroniserSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2345.Synchroniser':
        '''Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2345.Synchroniser)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6690.SynchroniserLoadCase':
        '''SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6690.SynchroniserLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
