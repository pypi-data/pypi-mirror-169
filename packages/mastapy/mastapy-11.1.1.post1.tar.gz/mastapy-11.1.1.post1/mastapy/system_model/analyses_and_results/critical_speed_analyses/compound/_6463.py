﻿'''_6463.py

KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6461, _6462, _6460
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6334
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis(_6460.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2282.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2282.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_critical_speed_analysis(self) -> 'List[_6461.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundCriticalSpeedAnalysis, constructor.new(_6461.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_critical_speed_analysis(self) -> 'List[_6462.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundCriticalSpeedAnalysis, constructor.new(_6462.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6334.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_6334.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6334.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_6334.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis))
        return value
