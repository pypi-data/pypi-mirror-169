﻿'''_3840.py

KlingelnbergCycloPalloidHypoidGearSetPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6637
from mastapy.gears.rating.klingelnberg_hypoid import _377
from mastapy.system_model.analyses_and_results.power_flows import _3839, _3838, _3837
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'KlingelnbergCycloPalloidHypoidGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetPowerFlow',)


class KlingelnbergCycloPalloidHypoidGearSetPowerFlow(_3837.KlingelnbergCycloPalloidConicalGearSetPowerFlow):
    '''KlingelnbergCycloPalloidHypoidGearSetPowerFlow

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2282.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6637.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6637.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def rating(self) -> '_377.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_377.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_377.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_377.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def gears_power_flow(self) -> 'List[_3839.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsPowerFlow, constructor.new(_3839.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_power_flow(self) -> 'List[_3839.KlingelnbergCycloPalloidHypoidGearPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsPowerFlow, constructor.new(_3839.KlingelnbergCycloPalloidHypoidGearPowerFlow))
        return value

    @property
    def meshes_power_flow(self) -> 'List[_3838.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesPowerFlow, constructor.new(_3838.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_power_flow(self) -> 'List[_3838.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]: 'KlingelnbergCycloPalloidHypoidMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesPowerFlow, constructor.new(_3838.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow))
        return value
