﻿'''_5120.py

BevelDifferentialGearSetMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2259
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6542
from mastapy.system_model.analyses_and_results.mbd_analyses import _5119, _5118, _5125
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BevelDifferentialGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetMultibodyDynamicsAnalysis',)


class BevelDifferentialGearSetMultibodyDynamicsAnalysis(_5125.BevelGearSetMultibodyDynamicsAnalysis):
    '''BevelDifferentialGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2259.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2259.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6542.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6542.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def gears(self) -> 'List[_5119.BevelDifferentialGearMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_5119.BevelDifferentialGearMultibodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_gears_multibody_dynamics_analysis(self) -> 'List[_5119.BevelDifferentialGearMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearMultibodyDynamicsAnalysis]: 'BevelDifferentialGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsMultibodyDynamicsAnalysis, constructor.new(_5119.BevelDifferentialGearMultibodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_meshes_multibody_dynamics_analysis(self) -> 'List[_5118.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearMeshMultibodyDynamicsAnalysis]: 'BevelDifferentialMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesMultibodyDynamicsAnalysis, constructor.new(_5118.BevelDifferentialGearMeshMultibodyDynamicsAnalysis))
        return value
