﻿'''_5130.py

ClutchMultibodyDynamicsAnalysis
'''


from mastapy.system_model.part_model.couplings import _2321
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6552
from mastapy.system_model.analyses_and_results.mbd_analyses import _5128, _5147
from mastapy._internal.python_net import python_net_import

_CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchMultibodyDynamicsAnalysis',)


class ClutchMultibodyDynamicsAnalysis(_5147.CouplingMultibodyDynamicsAnalysis):
    '''ClutchMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2321.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2321.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6552.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6552.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def clutch_connection(self) -> '_5128.ClutchConnectionMultibodyDynamicsAnalysis':
        '''ClutchConnectionMultibodyDynamicsAnalysis: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5128.ClutchConnectionMultibodyDynamicsAnalysis)(self.wrapped.ClutchConnection) if self.wrapped.ClutchConnection is not None else None
