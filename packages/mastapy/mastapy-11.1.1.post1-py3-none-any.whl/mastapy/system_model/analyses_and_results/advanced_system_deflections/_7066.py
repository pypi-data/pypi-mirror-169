﻿'''_7066.py

KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6637
from mastapy.gears.rating.klingelnberg_hypoid import _377
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7064, _7065, _7063
from mastapy.system_model.analyses_and_results.system_deflections import _2510
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection',)


class KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection(_7063.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection):
    '''KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection.TYPE'):
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
    def klingelnberg_cyclo_palloid_hypoid_gears_advanced_system_deflection(self) -> 'List[_7064.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection, constructor.new(_7064.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_advanced_system_deflection(self) -> 'List[_7065.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection, constructor.new(_7065.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2510.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2510.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection))
        return value
