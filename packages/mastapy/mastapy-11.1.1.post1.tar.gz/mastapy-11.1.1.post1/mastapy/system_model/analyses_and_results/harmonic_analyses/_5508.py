﻿'''_5508.py

MountableComponentHarmonicAnalysis
'''


from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4388, _4311, _4314, _4318,
    _4320, _4321, _4323, _4328,
    _4333, _4336, _4339, _4342,
    _4345, _4349, _4355, _4357,
    _4361, _4367, _4371, _4375,
    _4378, _4381, _4383, _4384,
    _4389, _4393, _4397, _4398,
    _4399, _4400, _4401, _4405,
    _4407, _4413, _4416, _4419,
    _4422, _4424, _4425, _4426,
    _4428, _4429, _4432, _4433,
    _4434, _4435, _4442, _4445
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model import (
    _2208, _2185, _2192, _2206,
    _2207, _2210, _2213, _2215,
    _2216, _2221, _2223
)
from mastapy.system_model.part_model.gears import (
    _2256, _2258, _2260, _2261,
    _2262, _2264, _2266, _2268,
    _2270, _2271, _2273, _2277,
    _2279, _2281, _2283, _2286,
    _2288, _2290, _2292, _2293,
    _2294, _2296
)
from mastapy.system_model.part_model.cycloidal import _2313
from mastapy.system_model.part_model.couplings import (
    _2322, _2325, _2327, _2330,
    _2332, _2333, _2339, _2341,
    _2344, _2347, _2348, _2349,
    _2351, _2353
)
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2520, _2434, _2436, _2441,
    _2442, _2443, _2446, _2450,
    _2456, _2460, _2464, _2466,
    _2468, _2471, _2483, _2484,
    _2485, _2488, _2494, _2499,
    _2503, _2508, _2511, _2514,
    _2517, _2518, _2522, _2525,
    _2528, _2529, _2530, _2531,
    _2532, _2537, _2539, _2547,
    _2549, _2553, _2556, _2557,
    _2558, _2559, _2560, _2561,
    _2567, _2569, _2572, _2573,
    _2576, _2579
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5433
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'MountableComponentHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentHarmonicAnalysis',)


class MountableComponentHarmonicAnalysis(_5433.ComponentHarmonicAnalysis):
    '''MountableComponentHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MountableComponentHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coupled_modal_analysis(self) -> '_4388.MountableComponentModalAnalysis':
        '''MountableComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4388.MountableComponentModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MountableComponentModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_agma_gleason_conical_gear_modal_analysis(self) -> '_4311.AGMAGleasonConicalGearModalAnalysis':
        '''AGMAGleasonConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4311.AGMAGleasonConicalGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to AGMAGleasonConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_bearing_modal_analysis(self) -> '_4314.BearingModalAnalysis':
        '''BearingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4314.BearingModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BearingModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_gear_modal_analysis(self) -> '_4318.BevelDifferentialGearModalAnalysis':
        '''BevelDifferentialGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4318.BevelDifferentialGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_planet_gear_modal_analysis(self) -> '_4320.BevelDifferentialPlanetGearModalAnalysis':
        '''BevelDifferentialPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4320.BevelDifferentialPlanetGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_differential_sun_gear_modal_analysis(self) -> '_4321.BevelDifferentialSunGearModalAnalysis':
        '''BevelDifferentialSunGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4321.BevelDifferentialSunGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelDifferentialSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_bevel_gear_modal_analysis(self) -> '_4323.BevelGearModalAnalysis':
        '''BevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4323.BevelGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to BevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_clutch_half_modal_analysis(self) -> '_4328.ClutchHalfModalAnalysis':
        '''ClutchHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4328.ClutchHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ClutchHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_coupling_half_modal_analysis(self) -> '_4333.ConceptCouplingHalfModalAnalysis':
        '''ConceptCouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4333.ConceptCouplingHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_concept_gear_modal_analysis(self) -> '_4336.ConceptGearModalAnalysis':
        '''ConceptGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4336.ConceptGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConceptGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_conical_gear_modal_analysis(self) -> '_4339.ConicalGearModalAnalysis':
        '''ConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4339.ConicalGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_connector_modal_analysis(self) -> '_4342.ConnectorModalAnalysis':
        '''ConnectorModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4342.ConnectorModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ConnectorModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_coupling_half_modal_analysis(self) -> '_4345.CouplingHalfModalAnalysis':
        '''CouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4345.CouplingHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_cvt_pulley_modal_analysis(self) -> '_4349.CVTPulleyModalAnalysis':
        '''CVTPulleyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4349.CVTPulleyModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CVTPulleyModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_cylindrical_gear_modal_analysis(self) -> '_4355.CylindricalGearModalAnalysis':
        '''CylindricalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4355.CylindricalGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CylindricalGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_cylindrical_planet_gear_modal_analysis(self) -> '_4357.CylindricalPlanetGearModalAnalysis':
        '''CylindricalPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4357.CylindricalPlanetGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to CylindricalPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_face_gear_modal_analysis(self) -> '_4361.FaceGearModalAnalysis':
        '''FaceGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4361.FaceGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to FaceGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_gear_modal_analysis(self) -> '_4367.GearModalAnalysis':
        '''GearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4367.GearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to GearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_hypoid_gear_modal_analysis(self) -> '_4371.HypoidGearModalAnalysis':
        '''HypoidGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4371.HypoidGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to HypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_conical_gear_modal_analysis(self) -> '_4375.KlingelnbergCycloPalloidConicalGearModalAnalysis':
        '''KlingelnbergCycloPalloidConicalGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4375.KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidConicalGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(self) -> '_4378.KlingelnbergCycloPalloidHypoidGearModalAnalysis':
        '''KlingelnbergCycloPalloidHypoidGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4378.KlingelnbergCycloPalloidHypoidGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidHypoidGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(self) -> '_4381.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis':
        '''KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4381.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_mass_disc_modal_analysis(self) -> '_4383.MassDiscModalAnalysis':
        '''MassDiscModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4383.MassDiscModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MassDiscModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_measurement_component_modal_analysis(self) -> '_4384.MeasurementComponentModalAnalysis':
        '''MeasurementComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4384.MeasurementComponentModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to MeasurementComponentModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_oil_seal_modal_analysis(self) -> '_4389.OilSealModalAnalysis':
        '''OilSealModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4389.OilSealModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to OilSealModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_part_to_part_shear_coupling_half_modal_analysis(self) -> '_4393.PartToPartShearCouplingHalfModalAnalysis':
        '''PartToPartShearCouplingHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4393.PartToPartShearCouplingHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PartToPartShearCouplingHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_planet_carrier_modal_analysis(self) -> '_4397.PlanetCarrierModalAnalysis':
        '''PlanetCarrierModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4397.PlanetCarrierModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PlanetCarrierModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_point_load_modal_analysis(self) -> '_4398.PointLoadModalAnalysis':
        '''PointLoadModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4398.PointLoadModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PointLoadModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_power_load_modal_analysis(self) -> '_4399.PowerLoadModalAnalysis':
        '''PowerLoadModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4399.PowerLoadModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PowerLoadModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_pulley_modal_analysis(self) -> '_4400.PulleyModalAnalysis':
        '''PulleyModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4400.PulleyModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to PulleyModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_ring_pins_modal_analysis(self) -> '_4401.RingPinsModalAnalysis':
        '''RingPinsModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4401.RingPinsModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RingPinsModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_rolling_ring_modal_analysis(self) -> '_4405.RollingRingModalAnalysis':
        '''RollingRingModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4405.RollingRingModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to RollingRingModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_shaft_hub_connection_modal_analysis(self) -> '_4407.ShaftHubConnectionModalAnalysis':
        '''ShaftHubConnectionModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4407.ShaftHubConnectionModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ShaftHubConnectionModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_spiral_bevel_gear_modal_analysis(self) -> '_4413.SpiralBevelGearModalAnalysis':
        '''SpiralBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4413.SpiralBevelGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpiralBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_spring_damper_half_modal_analysis(self) -> '_4416.SpringDamperHalfModalAnalysis':
        '''SpringDamperHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4416.SpringDamperHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SpringDamperHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_diff_gear_modal_analysis(self) -> '_4419.StraightBevelDiffGearModalAnalysis':
        '''StraightBevelDiffGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4419.StraightBevelDiffGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelDiffGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_gear_modal_analysis(self) -> '_4422.StraightBevelGearModalAnalysis':
        '''StraightBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4422.StraightBevelGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_planet_gear_modal_analysis(self) -> '_4424.StraightBevelPlanetGearModalAnalysis':
        '''StraightBevelPlanetGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4424.StraightBevelPlanetGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelPlanetGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_straight_bevel_sun_gear_modal_analysis(self) -> '_4425.StraightBevelSunGearModalAnalysis':
        '''StraightBevelSunGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4425.StraightBevelSunGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to StraightBevelSunGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_half_modal_analysis(self) -> '_4426.SynchroniserHalfModalAnalysis':
        '''SynchroniserHalfModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4426.SynchroniserHalfModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserHalfModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_part_modal_analysis(self) -> '_4428.SynchroniserPartModalAnalysis':
        '''SynchroniserPartModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4428.SynchroniserPartModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserPartModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_synchroniser_sleeve_modal_analysis(self) -> '_4429.SynchroniserSleeveModalAnalysis':
        '''SynchroniserSleeveModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4429.SynchroniserSleeveModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to SynchroniserSleeveModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_torque_converter_pump_modal_analysis(self) -> '_4432.TorqueConverterPumpModalAnalysis':
        '''TorqueConverterPumpModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4432.TorqueConverterPumpModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to TorqueConverterPumpModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_torque_converter_turbine_modal_analysis(self) -> '_4433.TorqueConverterTurbineModalAnalysis':
        '''TorqueConverterTurbineModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4433.TorqueConverterTurbineModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to TorqueConverterTurbineModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_unbalanced_mass_modal_analysis(self) -> '_4434.UnbalancedMassModalAnalysis':
        '''UnbalancedMassModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4434.UnbalancedMassModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to UnbalancedMassModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_virtual_component_modal_analysis(self) -> '_4435.VirtualComponentModalAnalysis':
        '''VirtualComponentModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4435.VirtualComponentModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to VirtualComponentModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_worm_gear_modal_analysis(self) -> '_4442.WormGearModalAnalysis':
        '''WormGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4442.WormGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to WormGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def coupled_modal_analysis_of_type_zerol_bevel_gear_modal_analysis(self) -> '_4445.ZerolBevelGearModalAnalysis':
        '''ZerolBevelGearModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4445.ZerolBevelGearModalAnalysis.TYPE not in self.wrapped.CoupledModalAnalysis.__class__.__mro__:
            raise CastException('Failed to cast coupled_modal_analysis to ZerolBevelGearModalAnalysis. Expected: {}.'.format(self.wrapped.CoupledModalAnalysis.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CoupledModalAnalysis.__class__)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def component_design(self) -> '_2208.MountableComponent':
        '''MountableComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.MountableComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MountableComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2185.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2185.Bearing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_connector(self) -> '_2192.Connector':
        '''Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.Connector.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_mass_disc(self) -> '_2206.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2206.MassDisc.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MassDisc. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_measurement_component(self) -> '_2207.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2207.MeasurementComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to MeasurementComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2210.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2210.OilSeal.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_planet_carrier(self) -> '_2213.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2213.PlanetCarrier.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PlanetCarrier. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_point_load(self) -> '_2215.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2215.PointLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PointLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_power_load(self) -> '_2216.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2216.PowerLoad.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PowerLoad. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_unbalanced_mass(self) -> '_2221.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2221.UnbalancedMass.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to UnbalancedMass. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_virtual_component(self) -> '_2223.VirtualComponent':
        '''VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2223.VirtualComponent.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to VirtualComponent. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_agma_gleason_conical_gear(self) -> '_2256.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2256.AGMAGleasonConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_gear(self) -> '_2258.BevelDifferentialGear':
        '''BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2258.BevelDifferentialGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_planet_gear(self) -> '_2260.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2260.BevelDifferentialPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_differential_sun_gear(self) -> '_2261.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2261.BevelDifferentialSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_bevel_gear(self) -> '_2262.BevelGear':
        '''BevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2262.BevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_gear(self) -> '_2264.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2264.ConceptGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_conical_gear(self) -> '_2266.ConicalGear':
        '''ConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2266.ConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cylindrical_gear(self) -> '_2268.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2268.CylindricalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cylindrical_planet_gear(self) -> '_2270.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2270.CylindricalPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_face_gear(self) -> '_2271.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2271.FaceGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to FaceGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_gear(self) -> '_2273.Gear':
        '''Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2273.Gear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Gear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_hypoid_gear(self) -> '_2277.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2277.HypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to HypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2279.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2279.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2281.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2281.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2283.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2283.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spiral_bevel_gear(self) -> '_2286.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2286.SpiralBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpiralBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_diff_gear(self) -> '_2288.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2288.StraightBevelDiffGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_gear(self) -> '_2290.StraightBevelGear':
        '''StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2290.StraightBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_planet_gear(self) -> '_2292.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2292.StraightBevelPlanetGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_straight_bevel_sun_gear(self) -> '_2293.StraightBevelSunGear':
        '''StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2293.StraightBevelSunGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_worm_gear(self) -> '_2294.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2294.WormGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to WormGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_zerol_bevel_gear(self) -> '_2296.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2296.ZerolBevelGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ZerolBevelGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_ring_pins(self) -> '_2313.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.RingPins.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RingPins. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_clutch_half(self) -> '_2322.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2322.ClutchHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ClutchHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_concept_coupling_half(self) -> '_2325.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.ConceptCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_coupling_half(self) -> '_2327.CouplingHalf':
        '''CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.CouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_cvt_pulley(self) -> '_2330.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.CVTPulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CVTPulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_part_to_part_shear_coupling_half(self) -> '_2332.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.PartToPartShearCouplingHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_pulley(self) -> '_2333.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.Pulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_rolling_ring(self) -> '_2339.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2339.RollingRing.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to RollingRing. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2341.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2341.ShaftHubConnection.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_spring_damper_half(self) -> '_2344.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2344.SpringDamperHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SpringDamperHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_half(self) -> '_2347.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2347.SynchroniserHalf.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserHalf. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_part(self) -> '_2348.SynchroniserPart':
        '''SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2348.SynchroniserPart.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserPart. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_synchroniser_sleeve(self) -> '_2349.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2349.SynchroniserSleeve.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_torque_converter_pump(self) -> '_2351.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2351.TorqueConverterPump.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterPump. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_design_of_type_torque_converter_turbine(self) -> '_2353.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2353.TorqueConverterTurbine.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def system_deflection_results(self) -> '_2520.MountableComponentSystemDeflection':
        '''MountableComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2520.MountableComponentSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MountableComponentSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2434.AGMAGleasonConicalGearSystemDeflection':
        '''AGMAGleasonConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2434.AGMAGleasonConicalGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_bearing_system_deflection(self) -> '_2436.BearingSystemDeflection':
        '''BearingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2436.BearingSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BearingSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_gear_system_deflection(self) -> '_2441.BevelDifferentialGearSystemDeflection':
        '''BevelDifferentialGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2441.BevelDifferentialGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2442.BevelDifferentialPlanetGearSystemDeflection':
        '''BevelDifferentialPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2442.BevelDifferentialPlanetGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2443.BevelDifferentialSunGearSystemDeflection':
        '''BevelDifferentialSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2443.BevelDifferentialSunGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_bevel_gear_system_deflection(self) -> '_2446.BevelGearSystemDeflection':
        '''BevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2446.BevelGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to BevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_clutch_half_system_deflection(self) -> '_2450.ClutchHalfSystemDeflection':
        '''ClutchHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2450.ClutchHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ClutchHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_concept_coupling_half_system_deflection(self) -> '_2456.ConceptCouplingHalfSystemDeflection':
        '''ConceptCouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2456.ConceptCouplingHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptCouplingHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_concept_gear_system_deflection(self) -> '_2460.ConceptGearSystemDeflection':
        '''ConceptGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2460.ConceptGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConceptGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_conical_gear_system_deflection(self) -> '_2464.ConicalGearSystemDeflection':
        '''ConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2464.ConicalGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_connector_system_deflection(self) -> '_2466.ConnectorSystemDeflection':
        '''ConnectorSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2466.ConnectorSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ConnectorSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_coupling_half_system_deflection(self) -> '_2468.CouplingHalfSystemDeflection':
        '''CouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2468.CouplingHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CouplingHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cvt_pulley_system_deflection(self) -> '_2471.CVTPulleySystemDeflection':
        '''CVTPulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2471.CVTPulleySystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CVTPulleySystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection(self) -> '_2483.CylindricalGearSystemDeflection':
        '''CylindricalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2483.CylindricalGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2484.CylindricalGearSystemDeflectionTimestep':
        '''CylindricalGearSystemDeflectionTimestep: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2484.CylindricalGearSystemDeflectionTimestep.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2485.CylindricalGearSystemDeflectionWithLTCAResults':
        '''CylindricalGearSystemDeflectionWithLTCAResults: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2485.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2488.CylindricalPlanetGearSystemDeflection':
        '''CylindricalPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2488.CylindricalPlanetGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_face_gear_system_deflection(self) -> '_2494.FaceGearSystemDeflection':
        '''FaceGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2494.FaceGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to FaceGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_gear_system_deflection(self) -> '_2499.GearSystemDeflection':
        '''GearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2499.GearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to GearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_hypoid_gear_system_deflection(self) -> '_2503.HypoidGearSystemDeflection':
        '''HypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2503.HypoidGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to HypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2508.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2508.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2511.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2511.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2514.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2514.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_mass_disc_system_deflection(self) -> '_2517.MassDiscSystemDeflection':
        '''MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2517.MassDiscSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MassDiscSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_measurement_component_system_deflection(self) -> '_2518.MeasurementComponentSystemDeflection':
        '''MeasurementComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2518.MeasurementComponentSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to MeasurementComponentSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_oil_seal_system_deflection(self) -> '_2522.OilSealSystemDeflection':
        '''OilSealSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2522.OilSealSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to OilSealSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_part_to_part_shear_coupling_half_system_deflection(self) -> '_2525.PartToPartShearCouplingHalfSystemDeflection':
        '''PartToPartShearCouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2525.PartToPartShearCouplingHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PartToPartShearCouplingHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_planet_carrier_system_deflection(self) -> '_2528.PlanetCarrierSystemDeflection':
        '''PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2528.PlanetCarrierSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PlanetCarrierSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_point_load_system_deflection(self) -> '_2529.PointLoadSystemDeflection':
        '''PointLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2529.PointLoadSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PointLoadSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_power_load_system_deflection(self) -> '_2530.PowerLoadSystemDeflection':
        '''PowerLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2530.PowerLoadSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PowerLoadSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_pulley_system_deflection(self) -> '_2531.PulleySystemDeflection':
        '''PulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2531.PulleySystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to PulleySystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_ring_pins_system_deflection(self) -> '_2532.RingPinsSystemDeflection':
        '''RingPinsSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2532.RingPinsSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RingPinsSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_rolling_ring_system_deflection(self) -> '_2537.RollingRingSystemDeflection':
        '''RollingRingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2537.RollingRingSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to RollingRingSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_shaft_hub_connection_system_deflection(self) -> '_2539.ShaftHubConnectionSystemDeflection':
        '''ShaftHubConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2539.ShaftHubConnectionSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ShaftHubConnectionSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_spiral_bevel_gear_system_deflection(self) -> '_2547.SpiralBevelGearSystemDeflection':
        '''SpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2547.SpiralBevelGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_spring_damper_half_system_deflection(self) -> '_2549.SpringDamperHalfSystemDeflection':
        '''SpringDamperHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2549.SpringDamperHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SpringDamperHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2553.StraightBevelDiffGearSystemDeflection':
        '''StraightBevelDiffGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2553.StraightBevelDiffGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_gear_system_deflection(self) -> '_2556.StraightBevelGearSystemDeflection':
        '''StraightBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2556.StraightBevelGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2557.StraightBevelPlanetGearSystemDeflection':
        '''StraightBevelPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2557.StraightBevelPlanetGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2558.StraightBevelSunGearSystemDeflection':
        '''StraightBevelSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2558.StraightBevelSunGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_half_system_deflection(self) -> '_2559.SynchroniserHalfSystemDeflection':
        '''SynchroniserHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2559.SynchroniserHalfSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserHalfSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_part_system_deflection(self) -> '_2560.SynchroniserPartSystemDeflection':
        '''SynchroniserPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2560.SynchroniserPartSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserPartSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_synchroniser_sleeve_system_deflection(self) -> '_2561.SynchroniserSleeveSystemDeflection':
        '''SynchroniserSleeveSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2561.SynchroniserSleeveSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to SynchroniserSleeveSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_torque_converter_pump_system_deflection(self) -> '_2567.TorqueConverterPumpSystemDeflection':
        '''TorqueConverterPumpSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2567.TorqueConverterPumpSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to TorqueConverterPumpSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_torque_converter_turbine_system_deflection(self) -> '_2569.TorqueConverterTurbineSystemDeflection':
        '''TorqueConverterTurbineSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2569.TorqueConverterTurbineSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to TorqueConverterTurbineSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_unbalanced_mass_system_deflection(self) -> '_2572.UnbalancedMassSystemDeflection':
        '''UnbalancedMassSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2572.UnbalancedMassSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to UnbalancedMassSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_virtual_component_system_deflection(self) -> '_2573.VirtualComponentSystemDeflection':
        '''VirtualComponentSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2573.VirtualComponentSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to VirtualComponentSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_worm_gear_system_deflection(self) -> '_2576.WormGearSystemDeflection':
        '''WormGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2576.WormGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to WormGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def system_deflection_results_of_type_zerol_bevel_gear_system_deflection(self) -> '_2579.ZerolBevelGearSystemDeflection':
        '''ZerolBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2579.ZerolBevelGearSystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to ZerolBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
