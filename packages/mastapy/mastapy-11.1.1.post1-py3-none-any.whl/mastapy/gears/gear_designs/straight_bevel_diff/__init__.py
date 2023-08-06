'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._923 import StraightBevelDiffGearDesign
    from ._924 import StraightBevelDiffGearMeshDesign
    from ._925 import StraightBevelDiffGearSetDesign
    from ._926 import StraightBevelDiffMeshedGearDesign
