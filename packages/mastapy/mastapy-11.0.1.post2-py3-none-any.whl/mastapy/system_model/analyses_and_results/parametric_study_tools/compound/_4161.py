﻿'''_4161.py

FaceGearSetCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2205
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4159, _4160, _4166
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4021
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'FaceGearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundParametricStudyTool',)


class FaceGearSetCompoundParametricStudyTool(_4166.GearSetCompoundParametricStudyTool):
    '''FaceGearSetCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2205.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2205.FaceGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2205.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2205.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def face_gears_compound_parametric_study_tool(self) -> 'List[_4159.FaceGearCompoundParametricStudyTool]':
        '''List[FaceGearCompoundParametricStudyTool]: 'FaceGearsCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsCompoundParametricStudyTool, constructor.new(_4159.FaceGearCompoundParametricStudyTool))
        return value

    @property
    def face_meshes_compound_parametric_study_tool(self) -> 'List[_4160.FaceGearMeshCompoundParametricStudyTool]':
        '''List[FaceGearMeshCompoundParametricStudyTool]: 'FaceMeshesCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesCompoundParametricStudyTool, constructor.new(_4160.FaceGearMeshCompoundParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4021.FaceGearSetParametricStudyTool]':
        '''List[FaceGearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4021.FaceGearSetParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4021.FaceGearSetParametricStudyTool]':
        '''List[FaceGearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4021.FaceGearSetParametricStudyTool))
        return value
