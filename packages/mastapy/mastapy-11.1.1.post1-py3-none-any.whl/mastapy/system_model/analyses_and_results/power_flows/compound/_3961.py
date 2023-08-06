﻿'''_3961.py

GearSetCompoundPowerFlow
'''


from typing import List

from mastapy.gears.rating import _329
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _342
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _416
from mastapy.gears.rating.cylindrical import _428
from mastapy.gears.rating.conical import _502
from mastapy.gears.rating.concept import _513
from mastapy.system_model.analyses_and_results.power_flows import _3829
from mastapy.system_model.analyses_and_results.power_flows.compound import _3999
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundPowerFlow',)


class GearSetCompoundPowerFlow(_3999.SpecialisedAssemblyCompoundPowerFlow):
    '''GearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self) -> '_329.GearSetDutyCycleRating':
        '''GearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _329.GearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to GearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_worm_gear_set_duty_cycle_rating(self) -> '_342.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _342.WormGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to WormGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_face_gear_set_duty_cycle_rating(self) -> '_416.FaceGearSetDutyCycleRating':
        '''FaceGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _416.FaceGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to FaceGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_428.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _428.CylindricalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_conical_gear_set_duty_cycle_rating(self) -> '_502.ConicalGearSetDutyCycleRating':
        '''ConicalGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _502.ConicalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to ConicalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_concept_gear_set_duty_cycle_rating(self) -> '_513.ConceptGearSetDutyCycleRating':
        '''ConceptGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _513.ConceptGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to ConceptGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_3829.GearSetPowerFlow]':
        '''List[GearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3829.GearSetPowerFlow))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3829.GearSetPowerFlow]':
        '''List[GearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3829.GearSetPowerFlow))
        return value
