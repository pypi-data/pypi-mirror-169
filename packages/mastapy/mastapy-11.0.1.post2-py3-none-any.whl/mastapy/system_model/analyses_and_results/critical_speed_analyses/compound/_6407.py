﻿'''_6407.py

PointLoadCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2149
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6278
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6443
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'PointLoadCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundCriticalSpeedAnalysis',)


class PointLoadCompoundCriticalSpeedAnalysis(_6443.VirtualComponentCompoundCriticalSpeedAnalysis):
    '''PointLoadCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2149.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2149.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6278.PointLoadCriticalSpeedAnalysis]':
        '''List[PointLoadCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_6278.PointLoadCriticalSpeedAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6278.PointLoadCriticalSpeedAnalysis]':
        '''List[PointLoadCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_6278.PointLoadCriticalSpeedAnalysis))
        return value
