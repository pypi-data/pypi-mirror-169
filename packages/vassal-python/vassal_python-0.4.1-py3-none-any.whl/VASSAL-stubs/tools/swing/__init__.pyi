import VASSAL.tools
import VASSAL.tools.concurrent
import java.awt
import java.awt.dnd
import java.awt.event
import java.awt.geom
import java.awt.image
import java.lang
import java.net
import java.util
import java.util.concurrent
import javax.swing
import javax.swing.event
import javax.swing.text
import javax.swing.text.html
import typing



class AboutWindow(javax.swing.JWindow):
    def __init__(self, window: java.awt.Window, bufferedImage: java.awt.image.BufferedImage, string: str): ...

class DataArchiveHTMLEditorKit(javax.swing.text.html.HTMLEditorKit):
    def __init__(self, dataArchive: VASSAL.tools.DataArchive): ...
    def getViewFactory(self) -> javax.swing.text.ViewFactory: ...

class DetailsButton(javax.swing.JButton):
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, component: java.awt.Component): ...
    @typing.overload
    def __init__(self, string: str, string2: str, component: java.awt.Component, component2: java.awt.Component): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def setBuddy(self, component: java.awt.Component) -> None: ...
    def setButtonHideText(self, string: str) -> None: ...
    def setButtonShowText(self, string: str) -> None: ...
    def setExpanded(self, boolean: bool) -> None: ...
    def setExpander(self, component: java.awt.Component) -> None: ...

class DetailsDialog:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    @staticmethod
    def showDialog(component: java.awt.Component, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, int: int, object: typing.Any) -> None: ...

class Dialogs:
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    @typing.overload
    @staticmethod
    def showConfirmDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def showConfirmDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int, int2: int, object: typing.Any, string4: str) -> int: ...
    @typing.overload
    @staticmethod
    def showConfirmDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int, icon: javax.swing.Icon, int2: int, object: typing.Any, string4: str) -> int: ...
    @staticmethod
    def showDialog(component: java.awt.Component, string: str, component2: java.awt.Component, int: int, icon: javax.swing.Icon, int2: int, objectArray: typing.List[typing.Any], object2: typing.Any, object3: typing.Any, string2: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def showMessageDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def showMessageDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int, object: typing.Any, string4: str) -> None: ...
    @typing.overload
    @staticmethod
    def showMessageDialog(component: java.awt.Component, string: str, string2: str, string3: str, int: int, icon: javax.swing.Icon, object: typing.Any, string4: str) -> None: ...

class EDT:
    @staticmethod
    def execute(runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    @staticmethod
    def getInstance() -> java.util.concurrent.ExecutorService: ...
    _submit_0__T = typing.TypeVar('_submit_0__T')  # <T>
    _submit_2__T = typing.TypeVar('_submit_2__T')  # <T>
    _submit_3__T = typing.TypeVar('_submit_3__T')  # <T>
    @typing.overload
    @staticmethod
    def submit(eDTRunnableFuture: 'EDTRunnableFuture'[_submit_0__T]) -> 'EDTRunnableFuture'[_submit_0__T]: ...
    @typing.overload
    @staticmethod
    def submit(runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> java.util.concurrent.Future[typing.Any]: ...
    @typing.overload
    @staticmethod
    def submit(runnable: typing.Union[java.lang.Runnable, typing.Callable], t: _submit_2__T) -> java.util.concurrent.Future[_submit_2__T]: ...
    @typing.overload
    @staticmethod
    def submit(callable: typing.Union[java.util.concurrent.Callable[_submit_3__T], typing.Callable[[], _submit_3__T]]) -> java.util.concurrent.Future[_submit_3__T]: ...

class EDTExecutorService(java.util.concurrent.AbstractExecutorService):
    def __init__(self): ...
    def awaitTermination(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def execute(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    def isShutdown(self) -> bool: ...
    def isTerminated(self) -> bool: ...
    def shutdown(self) -> None: ...
    def shutdownNow(self) -> java.util.List[java.lang.Runnable]: ...
    _submit_0__T = typing.TypeVar('_submit_0__T')  # <T>
    _submit_2__T = typing.TypeVar('_submit_2__T')  # <T>
    _submit_3__T = typing.TypeVar('_submit_3__T')  # <T>
    @typing.overload
    def submit(self, eDTRunnableFuture: 'EDTRunnableFuture'[_submit_0__T]) -> 'EDTRunnableFuture'[_submit_0__T]: ...
    @typing.overload
    def submit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> java.util.concurrent.Future[typing.Any]: ...
    @typing.overload
    def submit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], t: _submit_2__T) -> java.util.concurrent.Future[_submit_2__T]: ...
    @typing.overload
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit_3__T], typing.Callable[[], _submit_3__T]]) -> java.util.concurrent.Future[_submit_3__T]: ...

_EDTRunnableFuture__V = typing.TypeVar('_EDTRunnableFuture__V')  # <V>
class EDTRunnableFuture(VASSAL.tools.concurrent.SimpleRunnableFuture[_EDTRunnableFuture__V], typing.Generic[_EDTRunnableFuture__V]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, v: _EDTRunnableFuture__V): ...
    def run(self) -> None: ...

class FlowLabel(javax.swing.JTextPane):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def setText(self, string: str) -> None: ...

class HTMLWindowHelper(javax.swing.event.HyperlinkListener):
    def __init__(self): ...
    def hyperlinkUpdate(self, hyperlinkEvent: javax.swing.event.HyperlinkEvent) -> None: ...
    def setup(self, window: java.awt.Window, uRL: java.net.URL) -> None: ...
    def update(self, uRL: java.net.URL) -> None: ...

class ProgressDialog(javax.swing.JDialog):
    def __init__(self, frame: java.awt.Frame, string: str, string2: str): ...
    def addActionListener(self, actionListener: java.awt.event.ActionListener) -> None: ...
    @staticmethod
    def createOnEDT(frame: java.awt.Frame, string: str, string2: str) -> 'ProgressDialog': ...
    def getActionListeners(self) -> typing.List[java.awt.event.ActionListener]: ...
    def getLabel(self) -> str: ...
    def getProgress(self) -> int: ...
    def isIndeterminate(self) -> bool: ...
    def isStringPainted(self) -> bool: ...
    def removeActionListener(self, actionListener: java.awt.event.ActionListener) -> None: ...
    def setIndeterminate(self, boolean: bool) -> None: ...
    def setLabel(self, string: str) -> None: ...
    def setProgress(self, int: int) -> None: ...
    def setStringPainted(self, boolean: bool) -> None: ...

class Progressor(VASSAL.tools.concurrent.RangedRunnable[int]):
    def __init__(self, int: int, int2: int): ...
    def add(self, int: int) -> None: ...
    def get(self) -> int: ...
    def getPct(self) -> int: ...
    def increment(self) -> None: ...
    def set(self, int: int) -> None: ...
    def setPct(self, int: int) -> None: ...

class SplitPane(javax.swing.JSplitPane):
    def __init__(self, int: int, component: java.awt.Component, component2: java.awt.Component): ...
    def hideBottom(self) -> None: ...
    def hideLeft(self) -> None: ...
    def hideRight(self) -> None: ...
    def hideTop(self) -> None: ...
    def isBottomVisible(self) -> bool: ...
    def isLeftVisible(self) -> bool: ...
    def isRightVisible(self) -> bool: ...
    def isTopVisible(self) -> bool: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def setBottomVisible(self, boolean: bool) -> None: ...
    def setLeftVisible(self, boolean: bool) -> None: ...
    def setRightVisible(self, boolean: bool) -> None: ...
    def setTopVisible(self, boolean: bool) -> None: ...
    def showBottom(self) -> None: ...
    def showLeft(self) -> None: ...
    def showRight(self) -> None: ...
    def showTop(self) -> None: ...
    def toggleBottom(self) -> None: ...
    def toggleLeft(self) -> None: ...
    def toggleRight(self) -> None: ...
    def toggleTop(self) -> None: ...

class SwingUtils:
    FONT_HINTS: typing.ClassVar[java.util.Map] = ...
    def __init__(self): ...
    @staticmethod
    def convertKeyEvent(keyEvent: java.awt.event.KeyEvent) -> java.awt.event.KeyEvent: ...
    @staticmethod
    def descaleTransform(affineTransform: java.awt.geom.AffineTransform) -> java.awt.geom.AffineTransform: ...
    @staticmethod
    def ensureOnScreen(window: java.awt.Window) -> None: ...
    @staticmethod
    def genericToSystem(keyStroke: javax.swing.KeyStroke) -> javax.swing.KeyStroke: ...
    @staticmethod
    def getIndexInParent(component: java.awt.Component, container: java.awt.Container) -> int: ...
    @staticmethod
    def getKeyStrokeForEvent(keyEvent: java.awt.event.KeyEvent) -> javax.swing.KeyStroke: ...
    @staticmethod
    def getScreenBounds(component: java.awt.Component) -> java.awt.Rectangle: ...
    @staticmethod
    def getScreenInsets(component: java.awt.Component) -> java.awt.Insets: ...
    @staticmethod
    def getScreenSize() -> java.awt.Dimension: ...
    @staticmethod
    def isContextMouseButtonDown(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @staticmethod
    def isControlDown(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @staticmethod
    def isDragTrigger(dragGestureEvent: java.awt.dnd.DragGestureEvent) -> bool: ...
    @staticmethod
    def isLeftMouseButton(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @staticmethod
    def isMacLegacy() -> bool: ...
    @staticmethod
    def isMainMouseButtonDown(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @staticmethod
    def isModifierKeyDown(keyEvent: java.awt.event.KeyEvent) -> bool: ...
    @staticmethod
    def isRightMouseButton(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @staticmethod
    def isSelectionToggle(mouseEvent: java.awt.event.MouseEvent) -> bool: ...
    @typing.overload
    @staticmethod
    def repack(component: java.awt.Component) -> None: ...
    @typing.overload
    @staticmethod
    def repack(window: java.awt.Window) -> None: ...
    @typing.overload
    @staticmethod
    def repack(window: java.awt.Window, boolean: bool) -> None: ...
    @staticmethod
    def setMacLegacy(boolean: bool) -> None: ...
    @staticmethod
    def systemToGeneric(keyStroke: javax.swing.KeyStroke) -> javax.swing.KeyStroke: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.tools.swing")``.

    AboutWindow: typing.Type[AboutWindow]
    DataArchiveHTMLEditorKit: typing.Type[DataArchiveHTMLEditorKit]
    DetailsButton: typing.Type[DetailsButton]
    DetailsDialog: typing.Type[DetailsDialog]
    Dialogs: typing.Type[Dialogs]
    EDT: typing.Type[EDT]
    EDTExecutorService: typing.Type[EDTExecutorService]
    EDTRunnableFuture: typing.Type[EDTRunnableFuture]
    FlowLabel: typing.Type[FlowLabel]
    HTMLWindowHelper: typing.Type[HTMLWindowHelper]
    ProgressDialog: typing.Type[ProgressDialog]
    Progressor: typing.Type[Progressor]
    SplitPane: typing.Type[SplitPane]
    SwingUtils: typing.Type[SwingUtils]
