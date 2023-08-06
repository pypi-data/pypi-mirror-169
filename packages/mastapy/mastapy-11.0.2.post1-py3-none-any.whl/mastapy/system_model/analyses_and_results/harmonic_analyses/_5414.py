'''_5414.py

AssemblyHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6536, _6669
from mastapy.system_model.analyses_and_results.system_deflections import _2435, _2538
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5484, _5415, _5417, _5420,
    _5427, _5426, _5430, _5436,
    _5439, _5449, _5451, _5453,
    _5457, _5475, _5476, _5477,
    _5495, _5502, _5505, _5506,
    _5507, _5509, _5513, _5517,
    _5518, _5519, _5528, _5521,
    _5523, _5527, _5535, _5538,
    _5541, _5544, _5548, _5552,
    _5556, _5560, _5563, _5406
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AssemblyHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyHarmonicAnalysis',)


class AssemblyHarmonicAnalysis(_5406.AbstractAssemblyHarmonicAnalysis):
    '''AssemblyHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2179.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6536.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6536.AssemblyLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to AssemblyLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2435.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2435.AssemblySystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AssemblySystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def loaded_gear_sets(self) -> 'List[_5484.GearSetHarmonicAnalysis]':
        '''List[GearSetHarmonicAnalysis]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadedGearSets, constructor.new(_5484.GearSetHarmonicAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5415.BearingHarmonicAnalysis]':
        '''List[BearingHarmonicAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5415.BearingHarmonicAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5417.BeltDriveHarmonicAnalysis]':
        '''List[BeltDriveHarmonicAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5417.BeltDriveHarmonicAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5420.BevelDifferentialGearSetHarmonicAnalysis]':
        '''List[BevelDifferentialGearSetHarmonicAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5420.BevelDifferentialGearSetHarmonicAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5427.BoltHarmonicAnalysis]':
        '''List[BoltHarmonicAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5427.BoltHarmonicAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5426.BoltedJointHarmonicAnalysis]':
        '''List[BoltedJointHarmonicAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5426.BoltedJointHarmonicAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5430.ClutchHarmonicAnalysis]':
        '''List[ClutchHarmonicAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5430.ClutchHarmonicAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5436.ConceptCouplingHarmonicAnalysis]':
        '''List[ConceptCouplingHarmonicAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5436.ConceptCouplingHarmonicAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5439.ConceptGearSetHarmonicAnalysis]':
        '''List[ConceptGearSetHarmonicAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5439.ConceptGearSetHarmonicAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5449.CVTHarmonicAnalysis]':
        '''List[CVTHarmonicAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5449.CVTHarmonicAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5451.CycloidalAssemblyHarmonicAnalysis]':
        '''List[CycloidalAssemblyHarmonicAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_5451.CycloidalAssemblyHarmonicAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5453.CycloidalDiscHarmonicAnalysis]':
        '''List[CycloidalDiscHarmonicAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_5453.CycloidalDiscHarmonicAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5457.CylindricalGearSetHarmonicAnalysis]':
        '''List[CylindricalGearSetHarmonicAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5457.CylindricalGearSetHarmonicAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5475.FaceGearSetHarmonicAnalysis]':
        '''List[FaceGearSetHarmonicAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5475.FaceGearSetHarmonicAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_5476.FEPartHarmonicAnalysis]':
        '''List[FEPartHarmonicAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5476.FEPartHarmonicAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5477.FlexiblePinAssemblyHarmonicAnalysis]':
        '''List[FlexiblePinAssemblyHarmonicAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5477.FlexiblePinAssemblyHarmonicAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5495.HypoidGearSetHarmonicAnalysis]':
        '''List[HypoidGearSetHarmonicAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5495.HypoidGearSetHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5502.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5502.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5505.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5505.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5506.MassDiscHarmonicAnalysis]':
        '''List[MassDiscHarmonicAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5506.MassDiscHarmonicAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5507.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5507.MeasurementComponentHarmonicAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5509.OilSealHarmonicAnalysis]':
        '''List[OilSealHarmonicAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5509.OilSealHarmonicAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5513.PartToPartShearCouplingHarmonicAnalysis]':
        '''List[PartToPartShearCouplingHarmonicAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5513.PartToPartShearCouplingHarmonicAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5517.PlanetCarrierHarmonicAnalysis]':
        '''List[PlanetCarrierHarmonicAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5517.PlanetCarrierHarmonicAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5518.PointLoadHarmonicAnalysis]':
        '''List[PointLoadHarmonicAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5518.PointLoadHarmonicAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5519.PowerLoadHarmonicAnalysis]':
        '''List[PowerLoadHarmonicAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5519.PowerLoadHarmonicAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5528.ShaftHubConnectionHarmonicAnalysis]':
        '''List[ShaftHubConnectionHarmonicAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5528.ShaftHubConnectionHarmonicAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_5521.RingPinsHarmonicAnalysis]':
        '''List[RingPinsHarmonicAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5521.RingPinsHarmonicAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5523.RollingRingAssemblyHarmonicAnalysis]':
        '''List[RollingRingAssemblyHarmonicAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5523.RollingRingAssemblyHarmonicAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5527.ShaftHarmonicAnalysis]':
        '''List[ShaftHarmonicAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5527.ShaftHarmonicAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5535.SpiralBevelGearSetHarmonicAnalysis]':
        '''List[SpiralBevelGearSetHarmonicAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5535.SpiralBevelGearSetHarmonicAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5538.SpringDamperHarmonicAnalysis]':
        '''List[SpringDamperHarmonicAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5538.SpringDamperHarmonicAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5541.StraightBevelDiffGearSetHarmonicAnalysis]':
        '''List[StraightBevelDiffGearSetHarmonicAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5541.StraightBevelDiffGearSetHarmonicAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5544.StraightBevelGearSetHarmonicAnalysis]':
        '''List[StraightBevelGearSetHarmonicAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5544.StraightBevelGearSetHarmonicAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5548.SynchroniserHarmonicAnalysis]':
        '''List[SynchroniserHarmonicAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5548.SynchroniserHarmonicAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5552.TorqueConverterHarmonicAnalysis]':
        '''List[TorqueConverterHarmonicAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5552.TorqueConverterHarmonicAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5556.UnbalancedMassHarmonicAnalysis]':
        '''List[UnbalancedMassHarmonicAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5556.UnbalancedMassHarmonicAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5560.WormGearSetHarmonicAnalysis]':
        '''List[WormGearSetHarmonicAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5560.WormGearSetHarmonicAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5563.ZerolBevelGearSetHarmonicAnalysis]':
        '''List[ZerolBevelGearSetHarmonicAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5563.ZerolBevelGearSetHarmonicAnalysis))
        return value
