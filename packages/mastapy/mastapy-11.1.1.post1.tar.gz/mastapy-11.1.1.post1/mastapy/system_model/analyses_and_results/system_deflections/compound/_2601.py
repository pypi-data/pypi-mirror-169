﻿'''_2601.py

BevelDifferentialGearMeshCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2046
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2439
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2606
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BevelDifferentialGearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshCompoundSystemDeflection',)


class BevelDifferentialGearMeshCompoundSystemDeflection(_2606.BevelGearMeshCompoundSystemDeflection):
    '''BevelDifferentialGearMeshCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2046.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2046.BevelDifferentialGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2046.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2046.BevelDifferentialGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2439.BevelDifferentialGearMeshSystemDeflection]':
        '''List[BevelDifferentialGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_2439.BevelDifferentialGearMeshSystemDeflection))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2439.BevelDifferentialGearMeshSystemDeflection]':
        '''List[BevelDifferentialGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_2439.BevelDifferentialGearMeshSystemDeflection))
        return value
