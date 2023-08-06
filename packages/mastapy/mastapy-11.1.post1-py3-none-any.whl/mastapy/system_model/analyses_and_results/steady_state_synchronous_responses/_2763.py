﻿'''_2763.py

CVTSteadyStateSynchronousResponse
'''


from mastapy.system_model.part_model.couplings import _2329
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2731
from mastapy._internal.python_net import python_net_import

_CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CVTSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTSteadyStateSynchronousResponse',)


class CVTSteadyStateSynchronousResponse(_2731.BeltDriveSteadyStateSynchronousResponse):
    '''CVTSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2329.CVT':
        '''CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2329.CVT)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None
