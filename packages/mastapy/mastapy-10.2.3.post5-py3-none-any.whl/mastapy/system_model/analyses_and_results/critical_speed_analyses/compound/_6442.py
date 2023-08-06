﻿'''_6442.py

UnbalancedMassCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2155
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6313
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6443
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'UnbalancedMassCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundCriticalSpeedAnalysis',)


class UnbalancedMassCompoundCriticalSpeedAnalysis(_6443.VirtualComponentCompoundCriticalSpeedAnalysis):
    '''UnbalancedMassCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2155.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2155.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6313.UnbalancedMassCriticalSpeedAnalysis]':
        '''List[UnbalancedMassCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_6313.UnbalancedMassCriticalSpeedAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6313.UnbalancedMassCriticalSpeedAnalysis]':
        '''List[UnbalancedMassCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_6313.UnbalancedMassCriticalSpeedAnalysis))
        return value
