﻿'''_5161.py

FaceGearMeshMultibodyDynamicsAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _2056
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6603
from mastapy.system_model.analyses_and_results.mbd_analyses import _5166
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'FaceGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshMultibodyDynamicsAnalysis',)


class FaceGearMeshMultibodyDynamicsAnalysis(_5166.GearMeshMultibodyDynamicsAnalysis):
    '''FaceGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2056.FaceGearMesh':
        '''FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.FaceGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6603.FaceGearMeshLoadCase':
        '''FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6603.FaceGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
