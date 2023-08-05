import java.awt
import java.io
import java.net
import java.util
import javax.accessibility
import typing



class Applet(java.awt.Panel):
    def __init__(self): ...
    def destroy(self) -> None: ...
    def getAccessibleContext(self) -> javax.accessibility.AccessibleContext: ...
    def getAppletContext(self) -> 'AppletContext': ...
    def getAppletInfo(self) -> str: ...
    @typing.overload
    def getAudioClip(self, uRL: java.net.URL) -> 'AudioClip': ...
    @typing.overload
    def getAudioClip(self, uRL: java.net.URL, string: str) -> 'AudioClip': ...
    def getCodeBase(self) -> java.net.URL: ...
    def getDocumentBase(self) -> java.net.URL: ...
    @typing.overload
    def getImage(self, uRL: java.net.URL) -> java.awt.Image: ...
    @typing.overload
    def getImage(self, uRL: java.net.URL, string: str) -> java.awt.Image: ...
    def getLocale(self) -> java.util.Locale: ...
    def getParameter(self, string: str) -> str: ...
    def getParameterInfo(self) -> typing.List[typing.List[str]]: ...
    def init(self) -> None: ...
    def isActive(self) -> bool: ...
    def isValidateRoot(self) -> bool: ...
    @staticmethod
    def newAudioClip(uRL: java.net.URL) -> 'AudioClip': ...
    @typing.overload
    def play(self, uRL: java.net.URL) -> None: ...
    @typing.overload
    def play(self, uRL: java.net.URL, string: str) -> None: ...
    @typing.overload
    def resize(self, int: int, int2: int) -> None: ...
    @typing.overload
    def resize(self, dimension: java.awt.Dimension) -> None: ...
    def setStub(self, appletStub: 'AppletStub') -> None: ...
    def showStatus(self, string: str) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class AppletContext:
    def getApplet(self, string: str) -> Applet: ...
    def getApplets(self) -> java.util.Enumeration[Applet]: ...
    def getAudioClip(self, uRL: java.net.URL) -> 'AudioClip': ...
    def getImage(self, uRL: java.net.URL) -> java.awt.Image: ...
    def getStream(self, string: str) -> java.io.InputStream: ...
    def getStreamKeys(self) -> java.util.Iterator[str]: ...
    def setStream(self, string: str, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def showDocument(self, uRL: java.net.URL) -> None: ...
    @typing.overload
    def showDocument(self, uRL: java.net.URL, string: str) -> None: ...
    def showStatus(self, string: str) -> None: ...

class AppletStub:
    def appletResize(self, int: int, int2: int) -> None: ...
    def getAppletContext(self) -> AppletContext: ...
    def getCodeBase(self) -> java.net.URL: ...
    def getDocumentBase(self) -> java.net.URL: ...
    def getParameter(self, string: str) -> str: ...
    def isActive(self) -> bool: ...

class AudioClip:
    def loop(self) -> None: ...
    def play(self) -> None: ...
    def stop(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.applet")``.

    Applet: typing.Type[Applet]
    AppletContext: typing.Type[AppletContext]
    AppletStub: typing.Type[AppletStub]
    AudioClip: typing.Type[AudioClip]
