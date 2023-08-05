import VASSAL.build
import VASSAL.chat
import VASSAL.chat.messageboard
import java.awt
import java.awt.event
import java.net
import javax.swing
import javax.swing.event
import javax.swing.tree
import typing



class ChatControlsInitializer:
    def initializeControls(self, chatServerControls: 'ChatServerControls') -> None: ...
    def uninitializeControls(self, chatServerControls: 'ChatServerControls') -> None: ...

class ChatServerControls(VASSAL.build.AbstractBuildable):
    def __init__(self): ...
    def addExtendedNewRoomHandler(self, actionListener: java.awt.event.ActionListener) -> None: ...
    def addTo(self, buildable: VASSAL.build.Buildable) -> None: ...
    def getAttributeNames(self) -> typing.List[str]: ...
    def getAttributeValueString(self, string: str) -> str: ...
    def getClient(self) -> VASSAL.chat.ChatServerConnection: ...
    def getControls(self) -> javax.swing.JPanel: ...
    def getCurrentRoom(self) -> 'RoomTree': ...
    def getExtendedControls(self) -> java.awt.Component: ...
    def getNewRoom(self) -> javax.swing.JTextField: ...
    def getRoomTree(self) -> 'RoomTree': ...
    def getToolbar(self) -> javax.swing.JToolBar: ...
    def removeExtendedNewRoomHandler(self, actionListener: java.awt.event.ActionListener) -> None: ...
    def setAttribute(self, string: str, object: typing.Any) -> None: ...
    def setClient(self, chatServerConnection: VASSAL.chat.ChatServerConnection) -> None: ...
    def setRoomControlsVisible(self, boolean: bool) -> None: ...
    def toggleVisible(self) -> None: ...
    def updateClientDisplay(self, icon: javax.swing.Icon, string: str) -> None: ...

class CurrentRoomActions:
    def buildPopupForPlayer(self, simplePlayer: VASSAL.chat.SimplePlayer, jTree: javax.swing.JTree) -> javax.swing.JPopupMenu: ...

class InviteAction(javax.swing.AbstractAction):
    def __init__(self, lockableChatServerConnection: VASSAL.chat.LockableChatServerConnection, simplePlayer: VASSAL.chat.SimplePlayer): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory(lockableChatServerConnection: VASSAL.chat.LockableChatServerConnection) -> 'PlayerActionFactory': ...

class JoinRoomAction(javax.swing.AbstractAction):
    def __init__(self, room: VASSAL.chat.Room, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory(chatServerConnection: VASSAL.chat.ChatServerConnection) -> 'RoomActionFactory': ...

class KickAction(javax.swing.AbstractAction):
    def __init__(self, lockableChatServerConnection: VASSAL.chat.LockableChatServerConnection, simplePlayer: VASSAL.chat.SimplePlayer): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory(lockableChatServerConnection: VASSAL.chat.LockableChatServerConnection) -> 'PlayerActionFactory': ...

class PlayerActionFactory:
    def getAction(self, simplePlayer: VASSAL.chat.SimplePlayer, jTree: javax.swing.JTree) -> javax.swing.Action: ...

class PrivateMessageAction(javax.swing.AbstractAction):
    def __init__(self, player: VASSAL.chat.Player, chatServerConnection: VASSAL.chat.ChatServerConnection, privateChatManager: VASSAL.chat.PrivateChatManager): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory(chatServerConnection: VASSAL.chat.ChatServerConnection, privateChatManager: VASSAL.chat.PrivateChatManager) -> PlayerActionFactory: ...

class RoomActionFactory:
    def getAction(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> javax.swing.Action: ...

class RoomTree(javax.swing.JTree):
    def __init__(self): ...
    def setRooms(self, roomArray: typing.List[VASSAL.chat.Room]) -> None: ...

class RoomTreeRenderer(javax.swing.tree.DefaultTreeCellRenderer):
    def __init__(self): ...
    def getTreeCellRendererComponent(self, jTree: javax.swing.JTree, object: typing.Any, boolean: bool, boolean2: bool, boolean3: bool, int: int, boolean4: bool) -> java.awt.Component: ...

class SendSoundAction(javax.swing.AbstractAction):
    def __init__(self, string: str, chatServerConnection: VASSAL.chat.ChatServerConnection, string2: str, player: VASSAL.chat.Player): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory(chatServerConnection: VASSAL.chat.ChatServerConnection, string: str, string2: str, string3: str) -> PlayerActionFactory: ...

class ServerStatusView(javax.swing.JTabbedPane, javax.swing.event.ChangeListener, javax.swing.event.TreeSelectionListener):
    SELECTION_PROPERTY: typing.ClassVar[str] = ...
    def __init__(self, serverStatus: VASSAL.chat.ServerStatus): ...
    def refresh(self) -> None: ...
    def setStatusServer(self, serverStatus: VASSAL.chat.ServerStatus) -> None: ...
    def stateChanged(self, changeEvent: javax.swing.event.ChangeEvent) -> None: ...
    def valueChanged(self, treeSelectionEvent: javax.swing.event.TreeSelectionEvent) -> None: ...
    class Render(javax.swing.tree.DefaultTreeCellRenderer):
        def __init__(self): ...
        def getTreeCellRendererComponent(self, jTree: javax.swing.JTree, object: typing.Any, boolean: bool, boolean2: bool, boolean3: bool, int: int, boolean4: bool) -> java.awt.Component: ...

class ShowProfileAction(javax.swing.AbstractAction):
    def __init__(self, simplePlayer: VASSAL.chat.SimplePlayer, frame: java.awt.Frame): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def factory() -> PlayerActionFactory: ...

class ShowServerStatusAction(javax.swing.AbstractAction):
    @typing.overload
    def __init__(self, serverStatus: VASSAL.chat.ServerStatus, uRL: java.net.URL): ...
    @typing.overload
    def __init__(self, serverStatus: VASSAL.chat.ServerStatus, uRL: java.net.URL, boolean: bool): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...

class SynchAction(javax.swing.AbstractAction):
    def __init__(self, player: VASSAL.chat.Player, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def actionPerformed(self, actionEvent: java.awt.event.ActionEvent) -> None: ...
    @staticmethod
    def clearSynchRoom() -> None: ...
    @staticmethod
    def factory(chatServerConnection: VASSAL.chat.ChatServerConnection) -> PlayerActionFactory: ...

class BasicChatControlsInitializer(ChatControlsInitializer):
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def initializeControls(self, chatServerControls: ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: ChatServerControls) -> None: ...

class LockableRoomTreeRenderer(RoomTreeRenderer):
    def __init__(self): ...
    def getTreeCellRendererComponent(self, jTree: javax.swing.JTree, object: typing.Any, boolean: bool, boolean2: bool, boolean3: bool, int: int, boolean4: bool) -> java.awt.Component: ...

class MessageBoardControlsInitializer(ChatControlsInitializer):
    def __init__(self, string: str, messageBoard: VASSAL.chat.messageboard.MessageBoard): ...
    def initializeControls(self, chatServerControls: ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: ChatServerControls) -> None: ...

class RoomInteractionControlsInitializer(ChatControlsInitializer):
    POPUP_MENU_FONT: typing.ClassVar[java.awt.Font] = ...
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def addPlayerActionFactory(self, playerActionFactory: typing.Union[PlayerActionFactory, typing.Callable]) -> None: ...
    def addRoomActionFactory(self, roomActionFactory: typing.Union[RoomActionFactory, typing.Callable]) -> None: ...
    def buildPopupForPlayer(self, simplePlayer: VASSAL.chat.SimplePlayer, jTree: javax.swing.JTree) -> javax.swing.JPopupMenu: ...
    def buildPopupForRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> javax.swing.JPopupMenu: ...
    def doubleClickRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> None: ...
    def initializeControls(self, chatServerControls: ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: ChatServerControls) -> None: ...

class ServerStatusControlsInitializer(ChatControlsInitializer):
    def __init__(self, serverStatus: VASSAL.chat.ServerStatus): ...
    def initializeControls(self, chatServerControls: ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: ChatServerControls) -> None: ...

class ServerWindowActions(CurrentRoomActions):
    def buildPopupForRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> javax.swing.JPopupMenu: ...
    def createRoom(self, string: str) -> None: ...
    def doubleClickRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> None: ...

class SimpleStatusControlsInitializer(ChatControlsInitializer):
    @typing.overload
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    @typing.overload
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection, boolean: bool): ...
    def initializeControls(self, chatServerControls: ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: ChatServerControls) -> None: ...

class LockableRoomControls(RoomInteractionControlsInitializer):
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def buildPopupForRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> javax.swing.JPopupMenu: ...
    def doubleClickRoom(self, room: VASSAL.chat.Room, jTree: javax.swing.JTree) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.chat.ui")``.

    BasicChatControlsInitializer: typing.Type[BasicChatControlsInitializer]
    ChatControlsInitializer: typing.Type[ChatControlsInitializer]
    ChatServerControls: typing.Type[ChatServerControls]
    CurrentRoomActions: typing.Type[CurrentRoomActions]
    InviteAction: typing.Type[InviteAction]
    JoinRoomAction: typing.Type[JoinRoomAction]
    KickAction: typing.Type[KickAction]
    LockableRoomControls: typing.Type[LockableRoomControls]
    LockableRoomTreeRenderer: typing.Type[LockableRoomTreeRenderer]
    MessageBoardControlsInitializer: typing.Type[MessageBoardControlsInitializer]
    PlayerActionFactory: typing.Type[PlayerActionFactory]
    PrivateMessageAction: typing.Type[PrivateMessageAction]
    RoomActionFactory: typing.Type[RoomActionFactory]
    RoomInteractionControlsInitializer: typing.Type[RoomInteractionControlsInitializer]
    RoomTree: typing.Type[RoomTree]
    RoomTreeRenderer: typing.Type[RoomTreeRenderer]
    SendSoundAction: typing.Type[SendSoundAction]
    ServerStatusControlsInitializer: typing.Type[ServerStatusControlsInitializer]
    ServerStatusView: typing.Type[ServerStatusView]
    ServerWindowActions: typing.Type[ServerWindowActions]
    ShowProfileAction: typing.Type[ShowProfileAction]
    ShowServerStatusAction: typing.Type[ShowServerStatusAction]
    SimpleStatusControlsInitializer: typing.Type[SimpleStatusControlsInitializer]
    SynchAction: typing.Type[SynchAction]
