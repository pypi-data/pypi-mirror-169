import java.awt
import java.awt.font
import java.awt.im.spi
import java.lang
import java.text
import java.util
import typing



class InputContext:
    def dispatchEvent(self, aWTEvent: java.awt.AWTEvent) -> None: ...
    def dispose(self) -> None: ...
    def endComposition(self) -> None: ...
    def getInputMethodControlObject(self) -> typing.Any: ...
    @staticmethod
    def getInstance() -> 'InputContext': ...
    def getLocale(self) -> java.util.Locale: ...
    def isCompositionEnabled(self) -> bool: ...
    def reconvert(self) -> None: ...
    def removeNotify(self, component: java.awt.Component) -> None: ...
    def selectInputMethod(self, locale: java.util.Locale) -> bool: ...
    def setCharacterSubsets(self, subsetArray: typing.List[java.lang.Character.Subset]) -> None: ...
    def setCompositionEnabled(self, boolean: bool) -> None: ...

class InputMethodHighlight:
    RAW_TEXT: typing.ClassVar[int] = ...
    CONVERTED_TEXT: typing.ClassVar[int] = ...
    UNSELECTED_RAW_TEXT_HIGHLIGHT: typing.ClassVar['InputMethodHighlight'] = ...
    SELECTED_RAW_TEXT_HIGHLIGHT: typing.ClassVar['InputMethodHighlight'] = ...
    UNSELECTED_CONVERTED_TEXT_HIGHLIGHT: typing.ClassVar['InputMethodHighlight'] = ...
    SELECTED_CONVERTED_TEXT_HIGHLIGHT: typing.ClassVar['InputMethodHighlight'] = ...
    @typing.overload
    def __init__(self, boolean: bool, int: int): ...
    @typing.overload
    def __init__(self, boolean: bool, int: int, int2: int): ...
    @typing.overload
    def __init__(self, boolean: bool, int: int, int2: int, map: typing.Union[java.util.Map[java.awt.font.TextAttribute, typing.Any], typing.Mapping[java.awt.font.TextAttribute, typing.Any]]): ...
    def getState(self) -> int: ...
    def getStyle(self) -> java.util.Map[java.awt.font.TextAttribute, typing.Any]: ...
    def getVariation(self) -> int: ...
    def isSelected(self) -> bool: ...

class InputMethodRequests:
    def cancelLatestCommittedText(self, attributeArray: typing.List[java.text.AttributedCharacterIterator.Attribute]) -> java.text.AttributedCharacterIterator: ...
    def getCommittedText(self, int: int, int2: int, attributeArray: typing.List[java.text.AttributedCharacterIterator.Attribute]) -> java.text.AttributedCharacterIterator: ...
    def getCommittedTextLength(self) -> int: ...
    def getInsertPositionOffset(self) -> int: ...
    def getLocationOffset(self, int: int, int2: int) -> java.awt.font.TextHitInfo: ...
    def getSelectedText(self, attributeArray: typing.List[java.text.AttributedCharacterIterator.Attribute]) -> java.text.AttributedCharacterIterator: ...
    def getTextLocation(self, textHitInfo: java.awt.font.TextHitInfo) -> java.awt.Rectangle: ...

class InputSubset(java.lang.Character.Subset):
    LATIN: typing.ClassVar['InputSubset'] = ...
    LATIN_DIGITS: typing.ClassVar['InputSubset'] = ...
    TRADITIONAL_HANZI: typing.ClassVar['InputSubset'] = ...
    SIMPLIFIED_HANZI: typing.ClassVar['InputSubset'] = ...
    KANJI: typing.ClassVar['InputSubset'] = ...
    HANJA: typing.ClassVar['InputSubset'] = ...
    HALFWIDTH_KATAKANA: typing.ClassVar['InputSubset'] = ...
    FULLWIDTH_LATIN: typing.ClassVar['InputSubset'] = ...
    FULLWIDTH_DIGITS: typing.ClassVar['InputSubset'] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.im")``.

    InputContext: typing.Type[InputContext]
    InputMethodHighlight: typing.Type[InputMethodHighlight]
    InputMethodRequests: typing.Type[InputMethodRequests]
    InputSubset: typing.Type[InputSubset]
    spi: java.awt.im.spi.__module_protocol__
