﻿'''_2259.py

BevelDifferentialGearSet
'''


from typing import List

from mastapy.gears.gear_designs.bevel import _1131
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.zerol_bevel import _912
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _921
from mastapy.gears.gear_designs.straight_bevel_diff import _925
from mastapy.gears.gear_designs.spiral_bevel import _929
from mastapy.system_model.part_model.gears import _2262, _2263
from mastapy.system_model.connections_and_sockets.gears import _2048
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSet',)


class BevelDifferentialGearSet(_2263.BevelGearSet):
    '''BevelDifferentialGearSet

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_1131.BevelGearSetDesign':
        '''BevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1131.BevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearSetDesign.__class__)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def conical_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_912.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _912.ZerolBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearSetDesign.__class__)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_921.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _921.StraightBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearSetDesign.__class__)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_925.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _925.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearSetDesign.__class__)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def conical_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_929.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _929.SpiralBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ConicalGearSetDesign.__class__)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign is not None else None

    @property
    def bevel_gear_set_design(self) -> '_1131.BevelGearSetDesign':
        '''BevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1131.BevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BevelGearSetDesign.__class__)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign is not None else None

    @property
    def bevel_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_912.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _912.ZerolBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BevelGearSetDesign.__class__)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign is not None else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_921.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _921.StraightBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BevelGearSetDesign.__class__)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign is not None else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_925.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _925.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BevelGearSetDesign.__class__)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign is not None else None

    @property
    def bevel_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_929.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _929.SpiralBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.BevelGearSetDesign.__class__)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign is not None else None

    @property
    def bevel_gears(self) -> 'List[_2262.BevelGear]':
        '''List[BevelGear]: 'BevelGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelGears, constructor.new(_2262.BevelGear))
        return value

    @property
    def bevel_meshes(self) -> 'List[_2048.BevelGearMesh]':
        '''List[BevelGearMesh]: 'BevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelMeshes, constructor.new(_2048.BevelGearMesh))
        return value
