﻿'''_2125.py

ConnectedSockets
'''


from mastapy.system_model.connections_and_sockets import (
    _1977, _1947, _1948, _1955,
    _1957, _1959, _1960, _1961,
    _1963, _1964, _1965, _1966,
    _1967, _1969, _1970, _1971,
    _1974, _1975, _1953, _1946,
    _1949, _1950, _1954, _1962,
    _1968, _1973, _1976
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _1981, _1983, _1985, _1987,
    _1989, _1991, _1993, _1995,
    _1997, _1998, _2002, _2003,
    _2005, _2007, _2009, _2011,
    _2013, _1980, _1982, _1984,
    _1986, _1988, _1990, _1992,
    _1994, _1996, _1999, _2000,
    _2001, _2004, _2006, _2008,
    _2010, _2012
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2014, _2015, _2017, _2018,
    _2020, _2021, _2016, _2019,
    _2022
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2024, _2026, _2028, _2030,
    _2032, _2034, _2035, _2023,
    _2025, _2027, _2029, _2031,
    _2033
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ConnectedSockets')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectedSockets',)


class ConnectedSockets(_0.APIBase):
    '''ConnectedSockets

    This is a mastapy class.
    '''

    TYPE = _CONNECTED_SOCKETS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectedSockets.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def socket_a(self) -> '_1977.Socket':
        '''Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1977.Socket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to Socket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bearing_inner_socket(self) -> '_1947.BearingInnerSocket':
        '''BearingInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1947.BearingInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bearing_outer_socket(self) -> '_1948.BearingOuterSocket':
        '''BearingOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1948.BearingOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cvt_pulley_socket(self) -> '_1955.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1955.CVTPulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_socket(self) -> '_1957.CylindricalSocket':
        '''CylindricalSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1957.CylindricalSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_electric_machine_stator_socket(self) -> '_1959.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1959.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_socket(self) -> '_1960.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1960.InnerShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_inner_shaft_socket_base(self) -> '_1961.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1961.InnerShaftSocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_mountable_component_inner_socket(self) -> '_1963.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1963.MountableComponentInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_mountable_component_outer_socket(self) -> '_1964.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1964.MountableComponentOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_mountable_component_socket(self) -> '_1965.MountableComponentSocket':
        '''MountableComponentSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1965.MountableComponentSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_socket(self) -> '_1966.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1966.OuterShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_outer_shaft_socket_base(self) -> '_1967.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1967.OuterShaftSocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_planetary_socket(self) -> '_1969.PlanetarySocket':
        '''PlanetarySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1969.PlanetarySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_planetary_socket_base(self) -> '_1970.PlanetarySocketBase':
        '''PlanetarySocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1970.PlanetarySocketBase.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_pulley_socket(self) -> '_1971.PulleySocket':
        '''PulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1971.PulleySocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PulleySocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_rolling_ring_socket(self) -> '_1974.RollingRingSocket':
        '''RollingRingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1974.RollingRingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_shaft_socket(self) -> '_1975.ShaftSocket':
        '''ShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1975.ShaftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1981.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1981.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_differential_gear_teeth_socket(self) -> '_1983.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1983.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_bevel_gear_teeth_socket(self) -> '_1985.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1985.BevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_gear_teeth_socket(self) -> '_1987.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1987.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_conical_gear_teeth_socket(self) -> '_1989.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1989.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cylindrical_gear_teeth_socket(self) -> '_1991.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1991.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_face_gear_teeth_socket(self) -> '_1993.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1993.FaceGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_gear_teeth_socket(self) -> '_1995.GearTeethSocket':
        '''GearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1995.GearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_hypoid_gear_teeth_socket(self) -> '_1997.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1997.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1998.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1998.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2002.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2002.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2003.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2003.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2005.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2005.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2007.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2007.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_straight_bevel_gear_teeth_socket(self) -> '_2009.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2009.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_worm_gear_teeth_socket(self) -> '_2011.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2011.WormGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2013.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2013.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_left_socket(self) -> '_2014.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2014.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_right_socket(self) -> '_2015.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2015.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cycloidal_disc_inner_socket(self) -> '_2017.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2017.CycloidalDiscInnerSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cycloidal_disc_outer_socket(self) -> '_2018.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2018.CycloidalDiscOuterSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2020.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2020.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_ring_pins_socket(self) -> '_2021.RingPinsSocket':
        '''RingPinsSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2021.RingPinsSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RingPinsSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_clutch_socket(self) -> '_2024.ClutchSocket':
        '''ClutchSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2024.ClutchSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_concept_coupling_socket(self) -> '_2026.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2026.ConceptCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_coupling_socket(self) -> '_2028.CouplingSocket':
        '''CouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.CouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_part_to_part_shear_coupling_socket(self) -> '_2030.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2030.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_spring_damper_socket(self) -> '_2032.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2032.SpringDamperSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_pump_socket(self) -> '_2034.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2034.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_a_of_type_torque_converter_turbine_socket(self) -> '_2035.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2035.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketA.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketA.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketA.__class__)(self.wrapped.SocketA) if self.wrapped.SocketA else None

    @property
    def socket_b(self) -> '_1977.Socket':
        '''Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1977.Socket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to Socket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bearing_inner_socket(self) -> '_1947.BearingInnerSocket':
        '''BearingInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1947.BearingInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bearing_outer_socket(self) -> '_1948.BearingOuterSocket':
        '''BearingOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1948.BearingOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cvt_pulley_socket(self) -> '_1955.CVTPulleySocket':
        '''CVTPulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1955.CVTPulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CVTPulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_socket(self) -> '_1957.CylindricalSocket':
        '''CylindricalSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1957.CylindricalSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_electric_machine_stator_socket(self) -> '_1959.ElectricMachineStatorSocket':
        '''ElectricMachineStatorSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1959.ElectricMachineStatorSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ElectricMachineStatorSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_socket(self) -> '_1960.InnerShaftSocket':
        '''InnerShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1960.InnerShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_inner_shaft_socket_base(self) -> '_1961.InnerShaftSocketBase':
        '''InnerShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1961.InnerShaftSocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_mountable_component_inner_socket(self) -> '_1963.MountableComponentInnerSocket':
        '''MountableComponentInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1963.MountableComponentInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_mountable_component_outer_socket(self) -> '_1964.MountableComponentOuterSocket':
        '''MountableComponentOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1964.MountableComponentOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_mountable_component_socket(self) -> '_1965.MountableComponentSocket':
        '''MountableComponentSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1965.MountableComponentSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_socket(self) -> '_1966.OuterShaftSocket':
        '''OuterShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1966.OuterShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_outer_shaft_socket_base(self) -> '_1967.OuterShaftSocketBase':
        '''OuterShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1967.OuterShaftSocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_planetary_socket(self) -> '_1969.PlanetarySocket':
        '''PlanetarySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1969.PlanetarySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_planetary_socket_base(self) -> '_1970.PlanetarySocketBase':
        '''PlanetarySocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1970.PlanetarySocketBase.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocketBase. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_pulley_socket(self) -> '_1971.PulleySocket':
        '''PulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1971.PulleySocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PulleySocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_rolling_ring_socket(self) -> '_1974.RollingRingSocket':
        '''RollingRingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1974.RollingRingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RollingRingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_shaft_socket(self) -> '_1975.ShaftSocket':
        '''ShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1975.ShaftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_1981.AGMAGleasonConicalGearTeethSocket':
        '''AGMAGleasonConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1981.AGMAGleasonConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_differential_gear_teeth_socket(self) -> '_1983.BevelDifferentialGearTeethSocket':
        '''BevelDifferentialGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1983.BevelDifferentialGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelDifferentialGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_bevel_gear_teeth_socket(self) -> '_1985.BevelGearTeethSocket':
        '''BevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1985.BevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_gear_teeth_socket(self) -> '_1987.ConceptGearTeethSocket':
        '''ConceptGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1987.ConceptGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_conical_gear_teeth_socket(self) -> '_1989.ConicalGearTeethSocket':
        '''ConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1989.ConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cylindrical_gear_teeth_socket(self) -> '_1991.CylindricalGearTeethSocket':
        '''CylindricalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1991.CylindricalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_face_gear_teeth_socket(self) -> '_1993.FaceGearTeethSocket':
        '''FaceGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1993.FaceGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to FaceGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_gear_teeth_socket(self) -> '_1995.GearTeethSocket':
        '''GearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1995.GearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to GearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_hypoid_gear_teeth_socket(self) -> '_1997.HypoidGearTeethSocket':
        '''HypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1997.HypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to HypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_1998.KlingelnbergConicalGearTeethSocket':
        '''KlingelnbergConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1998.KlingelnbergConicalGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2002.KlingelnbergHypoidGearTeethSocket':
        '''KlingelnbergHypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2002.KlingelnbergHypoidGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2003.KlingelnbergSpiralBevelGearTeethSocket':
        '''KlingelnbergSpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2003.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2005.SpiralBevelGearTeethSocket':
        '''SpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2005.SpiralBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpiralBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2007.StraightBevelDiffGearTeethSocket':
        '''StraightBevelDiffGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2007.StraightBevelDiffGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_straight_bevel_gear_teeth_socket(self) -> '_2009.StraightBevelGearTeethSocket':
        '''StraightBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2009.StraightBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_worm_gear_teeth_socket(self) -> '_2011.WormGearTeethSocket':
        '''WormGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2011.WormGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to WormGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2013.ZerolBevelGearTeethSocket':
        '''ZerolBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2013.ZerolBevelGearTeethSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ZerolBevelGearTeethSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_left_socket(self) -> '_2014.CycloidalDiscAxialLeftSocket':
        '''CycloidalDiscAxialLeftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2014.CycloidalDiscAxialLeftSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_right_socket(self) -> '_2015.CycloidalDiscAxialRightSocket':
        '''CycloidalDiscAxialRightSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2015.CycloidalDiscAxialRightSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialRightSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cycloidal_disc_inner_socket(self) -> '_2017.CycloidalDiscInnerSocket':
        '''CycloidalDiscInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2017.CycloidalDiscInnerSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscInnerSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cycloidal_disc_outer_socket(self) -> '_2018.CycloidalDiscOuterSocket':
        '''CycloidalDiscOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2018.CycloidalDiscOuterSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscOuterSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2020.CycloidalDiscPlanetaryBearingSocket':
        '''CycloidalDiscPlanetaryBearingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2020.CycloidalDiscPlanetaryBearingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_ring_pins_socket(self) -> '_2021.RingPinsSocket':
        '''RingPinsSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2021.RingPinsSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RingPinsSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_clutch_socket(self) -> '_2024.ClutchSocket':
        '''ClutchSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2024.ClutchSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ClutchSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_concept_coupling_socket(self) -> '_2026.ConceptCouplingSocket':
        '''ConceptCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2026.ConceptCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_coupling_socket(self) -> '_2028.CouplingSocket':
        '''CouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2028.CouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_part_to_part_shear_coupling_socket(self) -> '_2030.PartToPartShearCouplingSocket':
        '''PartToPartShearCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2030.PartToPartShearCouplingSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PartToPartShearCouplingSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_spring_damper_socket(self) -> '_2032.SpringDamperSocket':
        '''SpringDamperSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2032.SpringDamperSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpringDamperSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_pump_socket(self) -> '_2034.TorqueConverterPumpSocket':
        '''TorqueConverterPumpSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2034.TorqueConverterPumpSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterPumpSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def socket_b_of_type_torque_converter_turbine_socket(self) -> '_2035.TorqueConverterTurbineSocket':
        '''TorqueConverterTurbineSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2035.TorqueConverterTurbineSocket.TYPE not in self.wrapped.SocketB.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterTurbineSocket. Expected: {}.'.format(self.wrapped.SocketB.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SocketB.__class__)(self.wrapped.SocketB) if self.wrapped.SocketB else None

    @property
    def connection(self) -> '_1953.Connection':
        '''Connection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1953.Connection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to Connection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_1946.AbstractShaftToMountableComponentConnection':
        '''AbstractShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1946.AbstractShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_belt_connection(self) -> '_1949.BeltConnection':
        '''BeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1949.BeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coaxial_connection(self) -> '_1950.CoaxialConnection':
        '''CoaxialConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1950.CoaxialConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CoaxialConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cvt_belt_connection(self) -> '_1954.CVTBeltConnection':
        '''CVTBeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1954.CVTBeltConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CVTBeltConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_inter_mountable_component_connection(self) -> '_1962.InterMountableComponentConnection':
        '''InterMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1962.InterMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to InterMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_planetary_connection(self) -> '_1968.PlanetaryConnection':
        '''PlanetaryConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1968.PlanetaryConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PlanetaryConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_rolling_ring_connection(self) -> '_1973.RollingRingConnection':
        '''RollingRingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1973.RollingRingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RollingRingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_shaft_to_mountable_component_connection(self) -> '_1976.ShaftToMountableComponentConnection':
        '''ShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1976.ShaftToMountableComponentConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ShaftToMountableComponentConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_1980.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1980.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_differential_gear_mesh(self) -> '_1982.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1982.BevelDifferentialGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_bevel_gear_mesh(self) -> '_1984.BevelGearMesh':
        '''BevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1984.BevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_gear_mesh(self) -> '_1986.ConceptGearMesh':
        '''ConceptGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1986.ConceptGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_conical_gear_mesh(self) -> '_1988.ConicalGearMesh':
        '''ConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1988.ConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cylindrical_gear_mesh(self) -> '_1990.CylindricalGearMesh':
        '''CylindricalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1990.CylindricalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CylindricalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_face_gear_mesh(self) -> '_1992.FaceGearMesh':
        '''FaceGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1992.FaceGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to FaceGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_gear_mesh(self) -> '_1994.GearMesh':
        '''GearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1994.GearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to GearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_hypoid_gear_mesh(self) -> '_1996.HypoidGearMesh':
        '''HypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1996.HypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to HypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1999.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1999.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2000.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2000.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2001.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2001.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spiral_bevel_gear_mesh(self) -> '_2004.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2004.SpiralBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2006.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2006.StraightBevelDiffGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_straight_bevel_gear_mesh(self) -> '_2008.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2008.StraightBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_worm_gear_mesh(self) -> '_2010.WormGearMesh':
        '''WormGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2010.WormGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to WormGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_zerol_bevel_gear_mesh(self) -> '_2012.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2012.ZerolBevelGearMesh.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2016.CycloidalDiscCentralBearingConnection':
        '''CycloidalDiscCentralBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2016.CycloidalDiscCentralBearingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2019.CycloidalDiscPlanetaryBearingConnection':
        '''CycloidalDiscPlanetaryBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2019.CycloidalDiscPlanetaryBearingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_ring_pins_to_disc_connection(self) -> '_2022.RingPinsToDiscConnection':
        '''RingPinsToDiscConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2022.RingPinsToDiscConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to RingPinsToDiscConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_clutch_connection(self) -> '_2023.ClutchConnection':
        '''ClutchConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2023.ClutchConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ClutchConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_concept_coupling_connection(self) -> '_2025.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2025.ConceptCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_coupling_connection(self) -> '_2027.CouplingConnection':
        '''CouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2027.CouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to CouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2029.PartToPartShearCouplingConnection':
        '''PartToPartShearCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2029.PartToPartShearCouplingConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to PartToPartShearCouplingConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_spring_damper_connection(self) -> '_2031.SpringDamperConnection':
        '''SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2031.SpringDamperConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to SpringDamperConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None

    @property
    def connection_of_type_torque_converter_connection(self) -> '_2033.TorqueConverterConnection':
        '''TorqueConverterConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2033.TorqueConverterConnection.TYPE not in self.wrapped.Connection.__class__.__mro__:
            raise CastException('Failed to cast connection to TorqueConverterConnection. Expected: {}.'.format(self.wrapped.Connection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Connection.__class__)(self.wrapped.Connection) if self.wrapped.Connection else None
