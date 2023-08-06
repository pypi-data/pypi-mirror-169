﻿'''_7146.py

BoltedJointCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _2188
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7013
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7224
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'BoltedJointCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointCompoundAdvancedSystemDeflection',)


class BoltedJointCompoundAdvancedSystemDeflection(_7224.SpecialisedAssemblyCompoundAdvancedSystemDeflection):
    '''BoltedJointCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2188.BoltedJoint':
        '''BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2188.BoltedJoint)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2188.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2188.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7013.BoltedJointAdvancedSystemDeflection]':
        '''List[BoltedJointAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_7013.BoltedJointAdvancedSystemDeflection))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7013.BoltedJointAdvancedSystemDeflection]':
        '''List[BoltedJointAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_7013.BoltedJointAdvancedSystemDeflection))
        return value
