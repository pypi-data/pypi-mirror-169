﻿'''_2648.py

ZerolBevelGearSetCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2230
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2646, _2647, _2536
from mastapy.system_model.analyses_and_results.system_deflections import _2507
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ZerolBevelGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetCompoundSystemDeflection',)


class ZerolBevelGearSetCompoundSystemDeflection(_2536.BevelGearSetCompoundSystemDeflection):
    '''ZerolBevelGearSetCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2230.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2230.ZerolBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2230.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2230.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def zerol_bevel_gears_compound_system_deflection(self) -> 'List[_2646.ZerolBevelGearCompoundSystemDeflection]':
        '''List[ZerolBevelGearCompoundSystemDeflection]: 'ZerolBevelGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsCompoundSystemDeflection, constructor.new(_2646.ZerolBevelGearCompoundSystemDeflection))
        return value

    @property
    def zerol_bevel_meshes_compound_system_deflection(self) -> 'List[_2647.ZerolBevelGearMeshCompoundSystemDeflection]':
        '''List[ZerolBevelGearMeshCompoundSystemDeflection]: 'ZerolBevelMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesCompoundSystemDeflection, constructor.new(_2647.ZerolBevelGearMeshCompoundSystemDeflection))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2507.ZerolBevelGearSetSystemDeflection]':
        '''List[ZerolBevelGearSetSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2507.ZerolBevelGearSetSystemDeflection))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2507.ZerolBevelGearSetSystemDeflection]':
        '''List[ZerolBevelGearSetSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2507.ZerolBevelGearSetSystemDeflection))
        return value
