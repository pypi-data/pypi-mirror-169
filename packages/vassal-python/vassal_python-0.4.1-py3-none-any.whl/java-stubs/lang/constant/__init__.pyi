import java.lang
import java.lang.invoke
import java.util
import typing



class Constable:
    def describeConstable(self) -> java.util.Optional['ConstantDesc']: ...

class ConstantDesc:
    def resolveConstantDesc(self, lookup: java.lang.invoke.MethodHandles.Lookup) -> typing.Any: ...

class ConstantDescs:
    DEFAULT_NAME: typing.ClassVar[str] = ...
    CD_Object: typing.ClassVar['ClassDesc'] = ...
    CD_String: typing.ClassVar['ClassDesc'] = ...
    CD_Class: typing.ClassVar['ClassDesc'] = ...
    CD_Number: typing.ClassVar['ClassDesc'] = ...
    CD_Integer: typing.ClassVar['ClassDesc'] = ...
    CD_Long: typing.ClassVar['ClassDesc'] = ...
    CD_Float: typing.ClassVar['ClassDesc'] = ...
    CD_Double: typing.ClassVar['ClassDesc'] = ...
    CD_Short: typing.ClassVar['ClassDesc'] = ...
    CD_Byte: typing.ClassVar['ClassDesc'] = ...
    CD_Character: typing.ClassVar['ClassDesc'] = ...
    CD_Boolean: typing.ClassVar['ClassDesc'] = ...
    CD_Void: typing.ClassVar['ClassDesc'] = ...
    CD_Throwable: typing.ClassVar['ClassDesc'] = ...
    CD_Exception: typing.ClassVar['ClassDesc'] = ...
    CD_Enum: typing.ClassVar['ClassDesc'] = ...
    CD_VarHandle: typing.ClassVar['ClassDesc'] = ...
    CD_MethodHandles: typing.ClassVar['ClassDesc'] = ...
    CD_MethodHandles_Lookup: typing.ClassVar['ClassDesc'] = ...
    CD_MethodHandle: typing.ClassVar['ClassDesc'] = ...
    CD_MethodType: typing.ClassVar['ClassDesc'] = ...
    CD_CallSite: typing.ClassVar['ClassDesc'] = ...
    CD_Collection: typing.ClassVar['ClassDesc'] = ...
    CD_List: typing.ClassVar['ClassDesc'] = ...
    CD_Set: typing.ClassVar['ClassDesc'] = ...
    CD_Map: typing.ClassVar['ClassDesc'] = ...
    CD_ConstantDesc: typing.ClassVar['ClassDesc'] = ...
    CD_ClassDesc: typing.ClassVar['ClassDesc'] = ...
    CD_EnumDesc: typing.ClassVar['ClassDesc'] = ...
    CD_MethodTypeDesc: typing.ClassVar['ClassDesc'] = ...
    CD_MethodHandleDesc: typing.ClassVar['ClassDesc'] = ...
    CD_DirectMethodHandleDesc: typing.ClassVar['ClassDesc'] = ...
    CD_VarHandleDesc: typing.ClassVar['ClassDesc'] = ...
    CD_MethodHandleDesc_Kind: typing.ClassVar['ClassDesc'] = ...
    CD_DynamicConstantDesc: typing.ClassVar['ClassDesc'] = ...
    CD_DynamicCallSiteDesc: typing.ClassVar['ClassDesc'] = ...
    CD_ConstantBootstraps: typing.ClassVar['ClassDesc'] = ...
    BSM_PRIMITIVE_CLASS: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_ENUM_CONSTANT: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_NULL_CONSTANT: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_VARHANDLE_FIELD: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_VARHANDLE_STATIC_FIELD: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_VARHANDLE_ARRAY: typing.ClassVar['DirectMethodHandleDesc'] = ...
    BSM_INVOKE: typing.ClassVar['DirectMethodHandleDesc'] = ...
    CD_int: typing.ClassVar['ClassDesc'] = ...
    CD_long: typing.ClassVar['ClassDesc'] = ...
    CD_float: typing.ClassVar['ClassDesc'] = ...
    CD_double: typing.ClassVar['ClassDesc'] = ...
    CD_short: typing.ClassVar['ClassDesc'] = ...
    CD_byte: typing.ClassVar['ClassDesc'] = ...
    CD_char: typing.ClassVar['ClassDesc'] = ...
    CD_boolean: typing.ClassVar['ClassDesc'] = ...
    CD_void: typing.ClassVar['ClassDesc'] = ...
    NULL: typing.ClassVar[ConstantDesc] = ...
    @staticmethod
    def ofCallsiteBootstrap(classDesc: 'ClassDesc', string: str, classDesc2: 'ClassDesc', *classDesc3: 'ClassDesc') -> 'DirectMethodHandleDesc': ...
    @staticmethod
    def ofConstantBootstrap(classDesc: 'ClassDesc', string: str, classDesc2: 'ClassDesc', *classDesc3: 'ClassDesc') -> 'DirectMethodHandleDesc': ...

class DynamicCallSiteDesc:
    def bootstrapArgs(self) -> typing.List[ConstantDesc]: ...
    def bootstrapMethod(self) -> 'MethodHandleDesc': ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def invocationName(self) -> str: ...
    def invocationType(self) -> 'MethodTypeDesc': ...
    @typing.overload
    @staticmethod
    def of(directMethodHandleDesc: 'DirectMethodHandleDesc', string: str, methodTypeDesc: 'MethodTypeDesc') -> 'DynamicCallSiteDesc': ...
    @typing.overload
    @staticmethod
    def of(directMethodHandleDesc: 'DirectMethodHandleDesc', string: str, methodTypeDesc: 'MethodTypeDesc', *constantDesc: ConstantDesc) -> 'DynamicCallSiteDesc': ...
    @typing.overload
    @staticmethod
    def of(directMethodHandleDesc: 'DirectMethodHandleDesc', methodTypeDesc: 'MethodTypeDesc') -> 'DynamicCallSiteDesc': ...
    def resolveCallSiteDesc(self, lookup: java.lang.invoke.MethodHandles.Lookup) -> java.lang.invoke.CallSite: ...
    def toString(self) -> str: ...
    def withArgs(self, *constantDesc: ConstantDesc) -> 'DynamicCallSiteDesc': ...
    def withNameAndType(self, string: str, methodTypeDesc: 'MethodTypeDesc') -> 'DynamicCallSiteDesc': ...

class ClassDesc(ConstantDesc, java.lang.invoke.TypeDescriptor.OfField['ClassDesc']):
    @typing.overload
    def arrayType(self) -> 'ClassDesc': ...
    @typing.overload
    def arrayType(self, int: int) -> 'ClassDesc': ...
    def componentType(self) -> 'ClassDesc': ...
    def descriptorString(self) -> str: ...
    def displayName(self) -> str: ...
    def equals(self, object: typing.Any) -> bool: ...
    def isArray(self) -> bool: ...
    def isClassOrInterface(self) -> bool: ...
    def isPrimitive(self) -> bool: ...
    @typing.overload
    def nested(self, string: str) -> 'ClassDesc': ...
    @typing.overload
    def nested(self, string: str, *string2: str) -> 'ClassDesc': ...
    @typing.overload
    @staticmethod
    def of(string: str) -> 'ClassDesc': ...
    @typing.overload
    @staticmethod
    def of(string: str, string2: str) -> 'ClassDesc': ...
    @staticmethod
    def ofDescriptor(string: str) -> 'ClassDesc': ...
    def packageName(self) -> str: ...

_DynamicConstantDesc__T = typing.TypeVar('_DynamicConstantDesc__T')  # <T>
class DynamicConstantDesc(ConstantDesc, typing.Generic[_DynamicConstantDesc__T]):
    def bootstrapArgs(self) -> typing.List[ConstantDesc]: ...
    def bootstrapArgsList(self) -> java.util.List[ConstantDesc]: ...
    def bootstrapMethod(self) -> 'DirectMethodHandleDesc': ...
    def constantName(self) -> str: ...
    def constantType(self) -> ClassDesc: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    _of_0__T = typing.TypeVar('_of_0__T')  # <T>
    _of_1__T = typing.TypeVar('_of_1__T')  # <T>
    @typing.overload
    @staticmethod
    def of(directMethodHandleDesc: 'DirectMethodHandleDesc') -> 'DynamicConstantDesc'[_of_0__T]: ...
    @typing.overload
    @staticmethod
    def of(directMethodHandleDesc: 'DirectMethodHandleDesc', *constantDesc: ConstantDesc) -> 'DynamicConstantDesc'[_of_1__T]: ...
    _ofCanonical__T = typing.TypeVar('_ofCanonical__T')  # <T>
    @staticmethod
    def ofCanonical(directMethodHandleDesc: 'DirectMethodHandleDesc', string: str, classDesc: ClassDesc, constantDescArray: typing.List[ConstantDesc]) -> ConstantDesc: ...
    _ofNamed__T = typing.TypeVar('_ofNamed__T')  # <T>
    @staticmethod
    def ofNamed(directMethodHandleDesc: 'DirectMethodHandleDesc', string: str, classDesc: ClassDesc, *constantDesc: ConstantDesc) -> 'DynamicConstantDesc'[_ofNamed__T]: ...
    def resolveConstantDesc(self, lookup: java.lang.invoke.MethodHandles.Lookup) -> _DynamicConstantDesc__T: ...
    def toString(self) -> str: ...

class MethodHandleDesc(ConstantDesc):
    def asType(self, methodTypeDesc: 'MethodTypeDesc') -> 'MethodHandleDesc': ...
    def equals(self, object: typing.Any) -> bool: ...
    def invocationType(self) -> 'MethodTypeDesc': ...
    @staticmethod
    def of(kind: 'DirectMethodHandleDesc.Kind', classDesc: ClassDesc, string: str, string2: str) -> 'DirectMethodHandleDesc': ...
    @staticmethod
    def ofConstructor(classDesc: ClassDesc, *classDesc2: ClassDesc) -> 'DirectMethodHandleDesc': ...
    @staticmethod
    def ofField(kind: 'DirectMethodHandleDesc.Kind', classDesc: ClassDesc, string: str, classDesc2: ClassDesc) -> 'DirectMethodHandleDesc': ...
    @staticmethod
    def ofMethod(kind: 'DirectMethodHandleDesc.Kind', classDesc: ClassDesc, string: str, methodTypeDesc: 'MethodTypeDesc') -> 'DirectMethodHandleDesc': ...

class MethodTypeDesc(ConstantDesc, java.lang.invoke.TypeDescriptor.OfMethod[ClassDesc, 'MethodTypeDesc']):
    def changeParameterType(self, int: int, classDesc: ClassDesc) -> 'MethodTypeDesc': ...
    def changeReturnType(self, classDesc: ClassDesc) -> 'MethodTypeDesc': ...
    def descriptorString(self) -> str: ...
    def displayDescriptor(self) -> str: ...
    def dropParameterTypes(self, int: int, int2: int) -> 'MethodTypeDesc': ...
    def equals(self, object: typing.Any) -> bool: ...
    def insertParameterTypes(self, int: int, *classDesc: ClassDesc) -> 'MethodTypeDesc': ...
    @staticmethod
    def of(classDesc: ClassDesc, *classDesc2: ClassDesc) -> 'MethodTypeDesc': ...
    @staticmethod
    def ofDescriptor(string: str) -> 'MethodTypeDesc': ...
    def parameterArray(self) -> typing.List[ClassDesc]: ...
    def parameterCount(self) -> int: ...
    def parameterList(self) -> java.util.List[ClassDesc]: ...
    def parameterType(self, int: int) -> ClassDesc: ...
    def returnType(self) -> ClassDesc: ...

class DirectMethodHandleDesc(MethodHandleDesc):
    def equals(self, object: typing.Any) -> bool: ...
    def isOwnerInterface(self) -> bool: ...
    def kind(self) -> 'DirectMethodHandleDesc.Kind': ...
    def lookupDescriptor(self) -> str: ...
    def methodName(self) -> str: ...
    def owner(self) -> ClassDesc: ...
    def refKind(self) -> int: ...
    class Kind(java.lang.Enum['DirectMethodHandleDesc.Kind']):
        STATIC: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        INTERFACE_STATIC: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        VIRTUAL: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        INTERFACE_VIRTUAL: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        SPECIAL: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        INTERFACE_SPECIAL: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        CONSTRUCTOR: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        GETTER: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        SETTER: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        STATIC_GETTER: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        STATIC_SETTER: typing.ClassVar['DirectMethodHandleDesc.Kind'] = ...
        refKind: int = ...
        isInterface: bool = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(int: int) -> 'DirectMethodHandleDesc.Kind': ...
        @typing.overload
        @staticmethod
        def valueOf(int: int, boolean: bool) -> 'DirectMethodHandleDesc.Kind': ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DirectMethodHandleDesc.Kind': ...
        @staticmethod
        def values() -> typing.List['DirectMethodHandleDesc.Kind']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.constant")``.

    ClassDesc: typing.Type[ClassDesc]
    Constable: typing.Type[Constable]
    ConstantDesc: typing.Type[ConstantDesc]
    ConstantDescs: typing.Type[ConstantDescs]
    DirectMethodHandleDesc: typing.Type[DirectMethodHandleDesc]
    DynamicCallSiteDesc: typing.Type[DynamicCallSiteDesc]
    DynamicConstantDesc: typing.Type[DynamicConstantDesc]
    MethodHandleDesc: typing.Type[MethodHandleDesc]
    MethodTypeDesc: typing.Type[MethodTypeDesc]
