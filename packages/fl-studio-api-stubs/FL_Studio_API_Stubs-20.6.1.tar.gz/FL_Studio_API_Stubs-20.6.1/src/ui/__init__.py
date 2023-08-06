"""User Interface Module (FL Studio built-in)

Allows you to control and interact with FL Studio's UI.

## WARNING:
* Many of the functions in this module will simply echo a hotkey into whatever
  application is active, meaning that actions can potentially be sent to the
  wrong application. Functions that have this behaviour are listed with a short
  warning saying so.

## HELP WANTED:
* What do the return values mean?
"""
from fl_model import since, keyEchoes


def jog(value: int) -> int:
    """Jog control. Used to map a jog wheel to selections.

    ## Args:
     * `value` (`int`): delta value (increment), for example
          * `1`: next

          * `-1`: previous

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def jog2(value: int) -> int:
    """Alternate jog control. Used to map a jog wheel to relocate.

    ## Args:
     * `value` (`int`): delta value (increment), for example
          * `1`: next

          * `-1`: previous

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def strip(value: int) -> int:
    """Used by touch-sensitive strip controls.

    ## HELP WANTED:
    * What controls does this apply to?

    ## Args:
     * `value` (`int`): ???

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def stripJog(value: int) -> int:
    """Touch-sensitive strip in jog mode.

    ## Args:
     * `value` (`int`): delta value (increment)

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def stripHold(value: int) -> int:
    """Touch-sensitive strip in hold mode

    ## Args:
     * `value` (`int`):
          * `0`: release

          * `1`: 1-finger centred mode

          * `2`: 2-fingers centred mode

          * `-1`: 1-finger jog mode

          * `-2`: 2-finger jog mode

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def previous() -> int:
    """Select to previous control:
     * in mixer: select previous track

     * in channel rack: select previous channel

     * in browser: scroll to previous item

     * in plugin: switch to previous preset (since API version 9)

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def next() -> int:
    """Select to next control:
     * in mixer: select next track

     * in channel rack: select next channel

     * in browser: scroll to next item

     * in plugin: switch to next preset

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def moveJog(value: int) -> int:
    """Used to relocate items with a jog control.

    ## HELP WANTED:
    * How does this differ from `jog2()`?

    ## Args:
     * `value` (`int`): delta value (increment)

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def up(value: int = 1) -> int:
    """Generic up control.

    ## WARNING:
    * This function echoes the up arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def down(value: int = 1) -> int:
    """Generic down control.

    ## WARNING:
    * This function echoes the down arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def left(value: int = 1) -> int:
    """Generic left control.

    ## WARNING:
    * This function echoes the left arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def right(value: int = 1) -> int:
    """Generic right control.

    ## WARNING:
    * This function echoes the right arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


def horZoom(value: int) -> int:
    """Zoom horizontally by `value`.

    ## Args:
     * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms in.
        Larger magnitudes zoom more, but the scale doesn't seem consistent.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def verZoom(value: int) -> int:
    """Zoom vertically by `value`.

    ## Args:
     * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms in.
        Larger magnitudes zoom more, but the scale doesn't seem consistent.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def snapOnOff() -> int:
    """Toggle whether snapping is enabled globally.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def cut() -> int:
    """Cut the selection.

    ## WARNING:
    * This function echoes the hotkey to cut, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def copy() -> int:
    """Copy the selection.

    ## WARNING:
    * This function echoes the hotkey to copy, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def paste() -> int:
    """Paste the selection.

    ## WARNING:
    * This function echoes the hotkey to paste, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def insert() -> int:
    """Press the insert key.

    ## WARNING:
    * This function echoes the insert key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def delete() -> int:
    """Press the delete key.

    ## WARNING:
    * This function echoes the delete key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def enter() -> int:
    """Press the enter key.

    ## WARNING:
    * This function echoes the enter key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def escape() -> int:
    """Press the escape key.

    ## WARNING:
    * This function echoes the escape key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def yes() -> int:
    """Press the y key.

    ## WARNING:
    * This function echoes the y key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def no() -> int:
    """Press the n key.

    ## WARNING:
    * This function echoes the n key, and thus will affect
      programs outside of FL Studio. Use with caution.

    * This function is listed in the official documentation as `not`,
      however this is incorrect, and will result in a syntax error since
      overriding core keywords (such as `if`, `def` and `not`) is not allowed.
      The function is actually named `no`, which is how this documentation
      lists it.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def getHintMsg() -> str:
    """Returns the current message in FL Studio's hint panel.

    ## Returns:
     * `str`: hint

    Included since API version 1
    """
    return ""


def setHintMsg(msg: str) -> None:
    """Sets the current hint message in FL Studio's hint panel to `msg`.

    ## Args:
     * `msg` (`str`): new message

    ## Usage:

    As well as setting basic info, scripts can use a variety of icons before
    their hint messages, which can be accessed by embedding `^c` at the start
    of the string, where `c` is a character from the list below:

    * `b`: record

    * `c`: yellow smiling face

    * `d`: mouse right click

    * `e`: red sad face

    * `f`: orange left-facing triangle

    * `g`: fast-forward icon

    * `h`: exclamation point in a red circle

    * `i`: clock

    * `j`: rewind icon

    * `k`: link icon

    * `l`: midi keyboard

    * `m`: F1 (help) key icon

    * `n`: Image-Line icon

    * `r`: plugin icon

    * `s`: file icon

    * `t`: eye

    * `u`: tempo tap icon

    * `v`: left-facing triangle

    * `w`: right-facing triangle

    * `x`: pencil

    * `y`: slice tool

    * `z`: brush tool icon

    For example, to display a tempo tap message with a relevant icon, the
    following code could be used:

    ```py
    ui.setHintMsg("^uTap tempo")
    ```

    Note that these icon codes are not returned by `getHintMsg()`.

    Included since API version 1
    """


def getHintValue(value: int, max: int) -> str:
    """Returns `value/max` as a percentage.

    Equivalent to:
    ```
    f"{value/max:.0%}"
    ```

    ## Args:
     * `value` (`int`): ???

     * `max` (`int`): ???

    ## Returns:
     * `str`: hint for `value`

    Included since API version 1
    """
    return f"{value/max:.0%}"


def getTimeDispMin() -> bool:
    """Returns `True` when the song position panel is displaying time, rather
    than bar and beat.

    ## Returns:
     * `bool`: whether song position is displaying time.

    Included since API version 1
    """
    return False


def setTimeDispMin() -> None:
    """Toggles whether the song position panel is displaying time or bar and
    beat.

    Included since API version 1
    """


def getVisible(index: int) -> bool:
    """Returns whether an FL Studio window is visible.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    ## Returns:
     * `bool`: whether it is visible

    Included since API version 1
    """
    return False


def showWindow(index: int) -> None:
    """Shows an FL Studio window specified by `index`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 1
    """


@since(5)
def hideWindow(index: int) -> None:
    """Hides an FL Studio window specified by `index`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 5
    """


def getFocused(index: int) -> bool:
    """Returns whether an FL Studio window is focused (meaning it is the
    currently selected Window in FL Studio).

    ## NOTE:
    * this doesn't necessarily mean that it is the currently selected window
      in the host operating system, so functions that rely on keypress emulation
      (such as `ui.copy()`) may not work as intended, even if this returns `True`.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

          * `widPlugin` (`5`): Plugin Window (note that this constant is only
            usable in this particular function).

          * `widPluginEffect` (`6`): Effect Plugin Window.

          * `widPluginGenerator` (`7`): Generator Plugin Window.

    ## Returns:
     * `bool`: whether it is visible

    Included since API version 1
    """
    return False


@since(2)
def setFocused(index: int) -> None:
    """Sets which FL Studio window should be focused (meaning it is the
    currently selected Window in FL Studio).

    ## NOTE:
    * This doesn't necessarily mean that it will be the currently selected
      window in the host operating system, so functions that rely on keypress
      emulation (such as `ui.copy()`) may not work as intended, even after calling
      this function.

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

    Included since API version 2
    """


def getFocusedFormCaption() -> str:
    """Returns the caption (title) of the focused FL Studio window. This isn't
    necessarily the same as the plugin's name.

    ## Returns:
     * `str`: window title

    Included since API version 1
    """
    return ""


@since(13)
def getFocusedFormID() -> int:
    """Returns ID of the focused window.

    Used to get the channel rack index or mixer plugin ID for plugins

    ## WARNING:
    * This can crash FL Studio's API if a plugin window is in the process of
      closing (until API v21).

    ## NOTE:
    * The official documentation says that this function returns a string,
      which is incorrect.

    ## Returns:
    * `int`: form ID:
          * Index in channel rack (zero indexed)

          * Plugin ID in mixer (track number * 4194304 + slot index * 65536,
            all zero indexed)

          * Window ID for mixer, channel rack, playlist, etc

          * `-1` for invalid plugin (eg. script output or settings window)

    Included since API version 13
    """
    return 0


@since(5)
def getFocusedPluginName() -> str:
    """Returns the plugin name for the active window if it is a plugin,
    otherwise an empty string.

    ## Returns:
     * `str`: plugin name

    Included since API version 5
    """
    return ""


@since(13)
def scrollWindow(index: int, value: int, directionFlag: int = 0) -> None:
    """Scrolls on the window specified by `index`. Value is index for whatever
    is contained on that window (eg channels for the Channel Rack or tracks for
    the Mixer).

    ## Args:
     * `index` (`int`): window index:
          * `widMixer` (`0`): Mixer

          * `widChannelRack` (`1`): Channel Rack

          * `widPlaylist` (`2`): Playlist

          * `widPianoRoll` (`3`): Piano Roll

          * `widBrowser` (`4`): Browser

     * `value` (`int`): index to scroll to:
          * on mixer: track number

          * on channel rack: channel number

          * on playlist: playlist track number

          * on playlist: bar number (when `directionFlag` is set to `1`)

    Included since API version 13
    """


def nextWindow() -> int:
    """Switch to the next window

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


@keyEchoes()
def selectWindow(shift: bool) -> int:
    """Switch to the next window by pressing the `Tab` key. If `shift` is
    `True`, switch to the previous window by pressing `Shift` and `Tab`.

    ## WARNING:
    * This function echoes the tab key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Args:
     * `shift` (`bool`): whether the shift key is pressed.

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


def launchAudioEditor(reuse: int, filename: str, index: int, preset: str,
                      presetGUID: str) -> int:
    """Launches an audio editor for track at `index` and returns the state of
    the editor. Set `reuse` to true (`1`) to reuse an already loaded audio
    editor.

    ## HELP WANTED:
    * How do I get this to work? I can only get it to open an empty window.

    ## Args:
     * `reuse` (`int`): whether to reuse an already open audio editor

     * `filename` (`str`): filename to open?

     * `index` (`int`): mixer track index to open on

     * `preset` (`str`): ???

     * `presetGUID` (`str`): ???

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


@since(9)
def openEventEditor(eventId: int, mode: int, newWindow: int = 0) -> int:
    """Launches an event editor for `eventId`.

    ## HELP WANTED:
    * Yuck REC events please help me.

    ## Args:
     * `eventId` (`int`): ???

     * `mode` (`int`): Refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#openEventEditorMode)

     * `newWindow` (`int`, optional): whether to open in a new window. Defaults
       to 0.

    ## Returns:
     * `int`: ???

    Included since API version 9
    """
    return 0


def isInPopupMenu() -> bool:
    """Returns `True` when a popup menu is open (for example a rick-click or
    drop-down menu).

    ## Returns:
      * `bool`: whether a popup menu is open

    Included since API version 1
    """
    return False


def closeActivePopupMenu() -> None:
    """Closes a currently-open popup menu (for example a rick-click or
    drop-down menu).

    Included since API version 1
    """


def isClosing() -> bool:
    """Returns `True` when FL Studio is closing

    ## Returns:
     * `bool`: is closing

    Included since API version 1
    """
    return False


def isMetronomeEnabled() -> bool:
    """Returns whether the metronome is enabled

    ## Returns:
     * `bool`: whether metronome is enabled

    Included since API version 1
    """
    return False


def isStartOnInputEnabled() -> bool:
    """Returns whether start on input is enabled

    ## Returns:
     * `bool`: whether start on input is enabled

    Included since API version 1
    """
    return False


def isPrecountEnabled() -> bool:
    """Returns whether precount is enabled

    ## Returns:
     * `bool`: whether precount is enabled

    Included since API version 1
    """
    return False


def isLoopRecEnabled() -> bool:
    """Returns whether loop recording is enabled

    ## Returns:
     * `bool`: whether loop recording is enabled

    Included since API version 1
    """
    return False


def getSnapMode() -> int:
    """Returns the current snap mode.

    Although the official documentation states that this takes an argument
    `value`, it does not. This stub reflects the actual behaviour.

    ## Returns:
     * `int`: index in the snap mode list:
          * `0`: Line

          * `1`: Cell

          * `2`: Unused (separator)

          * `3`: None

          * `4`: 1/6 step

          * `5`: 1/4 step

          * `6`: 1/3 step

          * `7`: 1/2 step

          * `8`: Step

          * `9`: 1/6 beat

          * `10`: 1/4 beat

          * `11`: 1/3 beat

          * `12`: 1/2 beat

          * `13`: Beat

          * `14`: bar

    Included since API version 1
    """
    return 0


def snapMode(value: int) -> int:
    """Changes the snap mode, by shifting it by `value` in the list of modes.
    Note that `2` (the unused value) is skipped.

    Also note that the usage for this function is truly painful. I am sorry.

    TODO: Add helper function to provide a better implementation to this
    documentation, so people can copy it into their code.

    ## Args:
     * `value` (`int`): increment (`1` for next, `-1` for previous)

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


def getProgTitle() -> str:
    """Returns the title of the FL Studio window

    ## Returns:
     * `str`: program title

    Included since API version 1
    """
    return ""


def getVersion(mode: int = 4) -> 'str | int':
    """Returns the version number of FL Studio

    ## Args:
     * `mode` (`int`, optional):
          * `VER_Major` (`0`): Major version number (as `int`)
            Eg: `20`

          * `VER_Minor` (`1`): Minor version number (as `int`)
            Eg: `8`

          * `VER_Release` (`2`): Release version number (as `int`)
            Eg: `4`

          * `VER_Build` (`3`): Program build number (as `int`)
            Eg: `2553`

          * `VER_VersionAndEdition` (`4`): Program version and edition (as `str`).
            Eg: `"Producer Edition v20.8.4 [build 2553]"`

          * `VER_FillVersionAndEdition` (`5`): Full version and edition (as `str`).
            Eg: `"Producer Edition v20.8.4 [build 2553] - Signature Bundle - 64Bit"`

          * `VER_ArchAndBuild` (`6`): Architecture and build number?

    Included since API version 1, with mode parameter since API version 7
    """
    return 0


def crDisplayRect(left: int, top: int, right: int, bottom: int, duration: int, flags: int = 0) -> None:
    """Displays a selection rectangle on the channel rack.

    This rectangle is anchored using the top left corner, and a width and
    height.

    Subsequent calls to this function will remove previously displaying
    rectangles.

    ## Args:
     * `left` (`int`): left position

     * `top` (`int`): top position

     * `width` (`int`): horizontal width

     * `height` (`int`): vertical height

     * `duration` (`int`): duration to display for (in ms). Or,
          * use `midi.MaxInt` to show indefinitely

          * use `0` to hide

     * `flags` (`int`, optional): a bitwise combination of:
          * `CR_HighlightChannels`: Display on channel list rather than on
            grid

          * `CR_ScrollToView`: Scroll channel rack to specified position

    Included since API version 1
    """


@since(13)
def miDisplayRect(start: int, end: int, duration: int, flags: int = 0) -> None:
    """Displays a selection rectangle on the mixer

    Subsequent calls to this function will remove previously displaying
    rectangles.

    ## Args:
     * `start` (`int`): start track index

     * `end` (`int`): end track index

     * `duration` (`int`): duration to display for (in ms). Or,
          * use `midi.MaxInt` to show indefinitely

          * use `0` to hide

     * `flags` (`int`, optional): unknown

    Included since API version 13
    """


@since(20)
def getFocusedNodeCaption() -> str:
    """
    Returns the filename associated with the currently selected item in the
    browser

    ## WARNING:
    * This function has no official documentation

    ## Returns:
    * `str`: node caption

    Included since API Version 20
    """
    return ""


@since(20)
def getFocusedNodeFileType() -> int:
    """
    Returns a value based on the type of the selected file in the browser

    ## WARNING:
    * This function has no official documentation

    ## Returns:
    * `int`: ???

    Included since API Version 20
    """
    return 0


@since(20)
def isBrowserAutoHide() -> bool:
    """
    Returns whether the browser is set to auto-hide

    ## WARNING:
    * This function has no official documentation

    ## Returns:
    * `bool`: auto-hide

    Included since API Version 20
    """
    return False


@since(20)
def setBrowserAutoHide(value: int):
    """
    Toggle whether the browser is set to auto-hide

    ## WARNING:
    * This function has no official documentation

    ## Args:
    * `value` (`int`): whether the browser should auto-hide (`1`) or not (`0`)

    Included since API Version 20
    """


@since(20)
def miDisplayDockRect(
    start: int,
    length: int,
    dock_side: int,
    time: int,
):
    """
    Display a red guide rectangle on the mixer, but contained to one side of
    the dock.

    Compare to: `miDisplayRect()`

    ## WARNING:
    * This function has no official documentation

    ## Args:
    * `start` (`int`): the index of the starting point, with `1` being the 1st
      track to be docked to that side, and `5` being the 5th track docked to
      that side

    * `length` (`int`): the length of the rectangle to display, for example `1`
      means the rectangle will be `1` track wide

    * `dock_side` (`int`): the dock side to show the rectangle on:
          * `0`: left

          * `1`: middle

          * `2`: right

    * `time` (`int`): the amount of time to display the rectangle for, or
      `midi.MAXINT` to display indefinitely and `0` to turn off.

    Included since API Version 20
    """


@since(20)
def navigateBrowserMenu(*args):
    """
    Navigate within the browser window???

    ## WARNING:
    * This function has no official documentation

    ## Args:
    * Unknown

    Included since API Version 20
    """


@since(20)
def previewBrowserMenuItem():
    """
    Preview the currently selected item in the browser

    ## WARNING:
    * This function has no official documentation

    Included since API Version 20
    """


@since(20)
def selectBrowserMenuItem():
    """
    ???

    ## WARNING:
    * This function has no official documentation

    Included since API Version 20
    """


@since(20)
def showNotification(val: int):
    """
    Show a notification to the user, which is chosen from a set of notification
    strings. This notification appears in the hint panel, much like with
    `ui.setHintMsg()`, except with less customization. Currently there is no
    apparent way to link these to the Script output window.

    ## WARNING:
    * This function has no official documentation

    * This function appears to cause FL Studio's scripting environment to crash
      when used under Wine on Linux

    ## Args:
    * `val` (`int`): Notification ID, the identifier of the notification string
      to send.
          * `0`: `"Now firmware is available for your MIDI device"`

          * `1`: `"New version of script is available"`

    Included since API Version 20
    """
