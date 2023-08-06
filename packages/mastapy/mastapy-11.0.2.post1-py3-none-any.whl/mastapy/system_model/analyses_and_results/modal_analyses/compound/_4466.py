'''_4466.py

AssemblyCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.modal_analyses import _4313
from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
    _4467, _4469, _4472, _4478,
    _4479, _4480, _4485, _4490,
    _4500, _4502, _4504, _4508,
    _4514, _4515, _4516, _4523,
    _4530, _4533, _4534, _4535,
    _4537, _4539, _4544, _4545,
    _4546, _4555, _4548, _4550,
    _4554, _4560, _4561, _4566,
    _4569, _4572, _4576, _4580,
    _4584, _4587, _4459
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AssemblyCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysis',)


class AssemblyCompoundModalAnalysis(_4459.AbstractAssemblyCompoundModalAnalysis):
    '''AssemblyCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2179.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_4313.AssemblyModalAnalysis]':
        '''List[AssemblyModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4313.AssemblyModalAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_4467.BearingCompoundModalAnalysis]':
        '''List[BearingCompoundModalAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4467.BearingCompoundModalAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_4469.BeltDriveCompoundModalAnalysis]':
        '''List[BeltDriveCompoundModalAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4469.BeltDriveCompoundModalAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4472.BevelDifferentialGearSetCompoundModalAnalysis]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4472.BevelDifferentialGearSetCompoundModalAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_4478.BoltCompoundModalAnalysis]':
        '''List[BoltCompoundModalAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4478.BoltCompoundModalAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_4479.BoltedJointCompoundModalAnalysis]':
        '''List[BoltedJointCompoundModalAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4479.BoltedJointCompoundModalAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_4480.ClutchCompoundModalAnalysis]':
        '''List[ClutchCompoundModalAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4480.ClutchCompoundModalAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_4485.ConceptCouplingCompoundModalAnalysis]':
        '''List[ConceptCouplingCompoundModalAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4485.ConceptCouplingCompoundModalAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4490.ConceptGearSetCompoundModalAnalysis]':
        '''List[ConceptGearSetCompoundModalAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4490.ConceptGearSetCompoundModalAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_4500.CVTCompoundModalAnalysis]':
        '''List[CVTCompoundModalAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4500.CVTCompoundModalAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_4502.CycloidalAssemblyCompoundModalAnalysis]':
        '''List[CycloidalAssemblyCompoundModalAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_4502.CycloidalAssemblyCompoundModalAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_4504.CycloidalDiscCompoundModalAnalysis]':
        '''List[CycloidalDiscCompoundModalAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_4504.CycloidalDiscCompoundModalAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4508.CylindricalGearSetCompoundModalAnalysis]':
        '''List[CylindricalGearSetCompoundModalAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4508.CylindricalGearSetCompoundModalAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4514.FaceGearSetCompoundModalAnalysis]':
        '''List[FaceGearSetCompoundModalAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4514.FaceGearSetCompoundModalAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_4515.FEPartCompoundModalAnalysis]':
        '''List[FEPartCompoundModalAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_4515.FEPartCompoundModalAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4516.FlexiblePinAssemblyCompoundModalAnalysis]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4516.FlexiblePinAssemblyCompoundModalAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4523.HypoidGearSetCompoundModalAnalysis]':
        '''List[HypoidGearSetCompoundModalAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4523.HypoidGearSetCompoundModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4530.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4530.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4533.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4533.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_4534.MassDiscCompoundModalAnalysis]':
        '''List[MassDiscCompoundModalAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4534.MassDiscCompoundModalAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_4535.MeasurementComponentCompoundModalAnalysis]':
        '''List[MeasurementComponentCompoundModalAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4535.MeasurementComponentCompoundModalAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_4537.OilSealCompoundModalAnalysis]':
        '''List[OilSealCompoundModalAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4537.OilSealCompoundModalAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4539.PartToPartShearCouplingCompoundModalAnalysis]':
        '''List[PartToPartShearCouplingCompoundModalAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4539.PartToPartShearCouplingCompoundModalAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_4544.PlanetCarrierCompoundModalAnalysis]':
        '''List[PlanetCarrierCompoundModalAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4544.PlanetCarrierCompoundModalAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_4545.PointLoadCompoundModalAnalysis]':
        '''List[PointLoadCompoundModalAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4545.PointLoadCompoundModalAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_4546.PowerLoadCompoundModalAnalysis]':
        '''List[PowerLoadCompoundModalAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4546.PowerLoadCompoundModalAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4555.ShaftHubConnectionCompoundModalAnalysis]':
        '''List[ShaftHubConnectionCompoundModalAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4555.ShaftHubConnectionCompoundModalAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_4548.RingPinsCompoundModalAnalysis]':
        '''List[RingPinsCompoundModalAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_4548.RingPinsCompoundModalAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4550.RollingRingAssemblyCompoundModalAnalysis]':
        '''List[RollingRingAssemblyCompoundModalAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4550.RollingRingAssemblyCompoundModalAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_4554.ShaftCompoundModalAnalysis]':
        '''List[ShaftCompoundModalAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4554.ShaftCompoundModalAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4560.SpiralBevelGearSetCompoundModalAnalysis]':
        '''List[SpiralBevelGearSetCompoundModalAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4560.SpiralBevelGearSetCompoundModalAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_4561.SpringDamperCompoundModalAnalysis]':
        '''List[SpringDamperCompoundModalAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4561.SpringDamperCompoundModalAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4566.StraightBevelDiffGearSetCompoundModalAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4566.StraightBevelDiffGearSetCompoundModalAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4569.StraightBevelGearSetCompoundModalAnalysis]':
        '''List[StraightBevelGearSetCompoundModalAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4569.StraightBevelGearSetCompoundModalAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_4572.SynchroniserCompoundModalAnalysis]':
        '''List[SynchroniserCompoundModalAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4572.SynchroniserCompoundModalAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_4576.TorqueConverterCompoundModalAnalysis]':
        '''List[TorqueConverterCompoundModalAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4576.TorqueConverterCompoundModalAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4580.UnbalancedMassCompoundModalAnalysis]':
        '''List[UnbalancedMassCompoundModalAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4580.UnbalancedMassCompoundModalAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4584.WormGearSetCompoundModalAnalysis]':
        '''List[WormGearSetCompoundModalAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4584.WormGearSetCompoundModalAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4587.ZerolBevelGearSetCompoundModalAnalysis]':
        '''List[ZerolBevelGearSetCompoundModalAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4587.ZerolBevelGearSetCompoundModalAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4313.AssemblyModalAnalysis]':
        '''List[AssemblyModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4313.AssemblyModalAnalysis))
        return value
