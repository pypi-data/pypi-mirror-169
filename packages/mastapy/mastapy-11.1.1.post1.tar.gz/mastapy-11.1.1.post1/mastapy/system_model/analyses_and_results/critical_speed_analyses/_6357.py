﻿'''_6357.py

RootAssemblyCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model import _2218
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _2368, _6268
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'RootAssemblyCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCriticalSpeedAnalysis',)


class RootAssemblyCriticalSpeedAnalysis(_6268.AssemblyCriticalSpeedAnalysis):
    '''RootAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2218.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2218.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def critical_speed_analysis_inputs(self) -> '_2368.CriticalSpeedAnalysis':
        '''CriticalSpeedAnalysis: 'CriticalSpeedAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2368.CriticalSpeedAnalysis)(self.wrapped.CriticalSpeedAnalysisInputs) if self.wrapped.CriticalSpeedAnalysisInputs is not None else None
