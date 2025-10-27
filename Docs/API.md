<a id="phardwareitk"></a>

# phardwareitk

Pheonix Hardware Interface Tool Kit -
PHardwareITK

<a id="phardwareitk.GUI.gui_sdl"></a>

# phardwareitk.GUI.gui\_sdl

GUI Library using SDL.

NOTE: Still under development.

<a id="phardwareitk.GUI.gui_sdl.ext"></a>

## ext

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.os"></a>

## os

<a id="phardwareitk.GUI.gui_sdl.sys"></a>

## sys

<a id="phardwareitk.GUI.gui_sdl.ctypes"></a>

## ctypes

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.*"></a>

## \*

<a id="phardwareitk.GUI.gui_sdl.DWMWA_USE_IMMERSIVE_DARK_MODE"></a>

#### DWMWA\_USE\_IMMERSIVE\_DARK\_MODE

<a id="phardwareitk.GUI.gui_sdl.WM_SETICON"></a>

#### WM\_SETICON

<a id="phardwareitk.GUI.gui_sdl.ICON_SMALL"></a>

#### ICON\_SMALL

<a id="phardwareitk.GUI.gui_sdl.ICON_BIG"></a>

#### ICON\_BIG

<a id="phardwareitk.GUI.gui_sdl.PError"></a>

#### PError

<a id="phardwareitk.GUI.gui_sdl.title"></a>

#### title

<a id="phardwareitk.GUI.gui_sdl.taskbarWindowedIds"></a>

#### taskbarWindowedIds

<a id="phardwareitk.GUI.gui_sdl.SafeExitSDL"></a>

#### SafeExitSDL

```python
def SafeExitSDL(msg: Optional[Union[str, int, dict, bool, list, tuple]],
                DestroyFunc: object, DestroyFuncParams: tuple) -> None
```

Safe Exit for SDL.

**Arguments**:

- `msg` _Optional[Union[str, int, dict, bool, list, tuple]]_ - Message.
- `DestroyFunc` _object_ - The DestroyFunc in gui_sdl.py.
- `DestroyFuncParams` _tuple_ - The DestroyFunc Parameters in gui_sdl.py.

<a id="phardwareitk.GUI.gui_sdl.WidgetPack"></a>

## WidgetPack Objects

```python
class WidgetPack()
```

A type for a single PACKED Widget.

<a id="phardwareitk.GUI.gui_sdl.WidgetPack.__init__"></a>

#### \_\_init\_\_

```python
def __init__(Widget: PWidget, MainFunc: object, MainFuncParams: list) -> None
```

INITALIZE func.

**Arguments**:

- `Widget` _PWidget_ - The Widget class.
- `MainFunc` _function_ - The main function of the widget.
- `MainFuncParams` _list_ - The parameters of the main function.

<a id="phardwareitk.GUI.gui_sdl.InitializePError"></a>

#### InitializePError

```python
def InitializePError() -> None
```

Initializes Pheonix/Print Error.

<a id="phardwareitk.GUI.gui_sdl.DeinitializePError"></a>

#### DeinitializePError

```python
def DeinitializePError() -> None
```

Deinitializes Pheonix/Print Error.

<a id="phardwareitk.GUI.gui_sdl.initialize"></a>

#### initialize

```python
def initialize() -> None
```

Initializes the SDL and PHardware GUI.

**Raises**:

- `PheonixException` - Incase SDL does not initialize properly.

<a id="phardwareitk.GUI.gui_sdl.ExtensionsInit"></a>

#### ExtensionsInit

```python
def ExtensionsInit(video: bool = True,
                   audio: bool = False,
                   timer: bool = False,
                   joystick: bool = False,
                   controller: bool = False,
                   haptic: bool = False,
                   sensor: bool = False,
                   events: bool = True) -> None
```

Initializes the SDL2 Extensions.

**Arguments**:

- `video` _bool, optional_ - Video. Defaults to True.
- `audio` _bool, optional_ - Audio. Defaults to False.
- `timer` _bool, optional_ - Timer. Defaults to False.
- `joystick` _bool, optional_ - Joystick. Defaults to False.
- `controller` _bool, optional_ - Controller. Defaults to False.
- `haptic` _bool, optional_ - Haptic. Defaults to False.
- `sensor` _bool, optional_ - Sensor. Defaults to False.
- `events` _bool, optional_ - Events. Defaults to True.

<a id="phardwareitk.GUI.gui_sdl.GetHwnd"></a>

#### GetHwnd

```python
def GetHwnd(Title: Optional[str] = None) -> Optional[Any]
```

Returns the windows handle for the specific window with the specified title.

**Arguments**:

- `Title` _Optional[str], optional_ - The title of the created window, If None uses the title of the latest window. Defaults to None.
  

**Returns**:

- `Optional[Any]` - Windows Handle, used in Windows OS, OR None incase of error. HWND.

<a id="phardwareitk.GUI.gui_sdl.LoadHIcon"></a>

#### LoadHIcon

```python
def LoadHIcon(icon: PIcon, Title: Optional[str] = None) -> Any
```

Loads the windows handle icon for the specific window with the specified title.

**Arguments**:

- `icon` _PIcon_ - The icon for the HWnd. NOTE: Can use 'exe' format too, it will fetch the icon of the 'exe' file.
- `Title` _Optional[str], optional_ - The title of the created window, If None uses the title of the latest window. Defaults to None.
  

**Returns**:

  The loaded HIcon

<a id="phardwareitk.GUI.gui_sdl.GetNSWindow"></a>

#### GetNSWindow

```python
def GetNSWindow() -> None
```

Returns the native macOS window object. Gets the latest opened window.

<a id="phardwareitk.GUI.gui_sdl.SetBackgroundColor"></a>

#### SetBackgroundColor

```python
def SetBackgroundColor(window: Any, color: Color = Color("white")) -> None
```

Sets the background color of the specified window.

**Arguments**:

- `window` _Any_ - The window
- `color` _Color, optional_ - The color. [phardwareitk.Extensions.Color]. Defaults to Color("white").

<a id="phardwareitk.GUI.gui_sdl.SetSurfaceBackgroundColor"></a>

#### SetSurfaceBackgroundColor

```python
def SetSurfaceBackgroundColor(
    surface: Any, color: Color = Color("white")) -> None
```

Sets the background color of the specified surface.

**Arguments**:

- `surface` _Any_ - The surface
- `color` _Color, optional_ - The color. [phardwareitk.Extensions.Color]. Defaults to Color("white").

<a id="phardwareitk.GUI.gui_sdl.AddIcon"></a>

#### AddIcon

```python
def AddIcon(window: Any,
            icon: PIcon,
            taskbarIncluded: bool = True,
            Title: Optional[str] = None) -> None
```

Adds an icon to the window.

**Arguments**:

- `window` _Any_ - Window.
- `icon` _PIcon_ - Icon. [phardwareitk.Extensions.PIcon]
- `taskbarIncluded` _bool, optional_ - If True, depending on Os, the taskbar window icon will change from python to the specified icon with the icon on the window. Defaults to True.
- `Title` _Optional[str], optional_ - The title of the window, If 'None' the title of the latest window will be used. Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.WindowSurface"></a>

#### WindowSurface

```python
def WindowSurface(window: Any) -> Any
```

Returns the SDL2 window surface.

**Arguments**:

- `window` _Any_ - The window returned by 'CreateWindow' Function.
  

**Returns**:

- `Any` - Window surface.

<a id="phardwareitk.GUI.gui_sdl.LoadBMP"></a>

#### LoadBMP

```python
def LoadBMP(image: str = "") -> Any
```

Loads the specified BMP image.

**Arguments**:

- `image` _str, optional_ - The image path in string. Defaults to "".
  

**Returns**:

- `Any` - The returned value of SDL2.'LoadBMP' Function.

<a id="phardwareitk.GUI.gui_sdl.UpdateWindow"></a>

#### UpdateWindow

```python
def UpdateWindow(window: Any) -> None
```

Updates the window.

**Arguments**:

- `window` _Any_ - The window.

<a id="phardwareitk.GUI.gui_sdl.BlitSurfaceScaled"></a>

#### BlitSurfaceScaled

```python
def BlitSurfaceScaled(src: Any, srcrect: Any, dst: Any, dstrect: Any,
                      scaleMode: Any) -> bool
```

_summary_

**Arguments**:

- `src` _Any_ - the SDL_Surface structure to be copied from.
- `srcrect` _Any_ - the SDL_Rect structure representing the rectangle to be copied, or NULL to copy the entire surface.
- `dst` _Any_ - the SDL_Surface structure that is the blit target.
- `dstrect` _Any_ - the SDL_Rect structure representing the target rectangle in the destination surface, or NULL to fill the entire destination surface.
- `scaleMode` _Any_ - the SDL_ScaleMode to be used.

<a id="phardwareitk.GUI.gui_sdl.BlitSurface"></a>

#### BlitSurface

```python
def BlitSurface(src: Any, srcrect: Any, dst: Any, dstrect: Any) -> bool
```

Same as SDL2.BlitSurface.

**Arguments**:

- `src` _Any_ - the SDL_Surface structure to be copied from.
- `srcrect` _Any_ - the SDL_Rect structure representing the rectangle to be copied, or NULL to copy the entire surface.
- `dst` _Any_ - the SDL_Surface structure that is the blit target.
- `dstrect` _Any_ - the SDL_Rect structure representing the x and y position in the destination surface, or NULL for (0,0). The width and height are ignored, and are copied from srcrect. If you want a specific width and height, you should use BlitSurfaceScaled().

<a id="phardwareitk.GUI.gui_sdl.FreeSurface"></a>

#### FreeSurface

```python
def FreeSurface(image: Any) -> None
```

Frees the specified BMP image.

**Arguments**:

- `image` _Any_ - The image returned from 'LoadBMP' function.

<a id="phardwareitk.GUI.gui_sdl.CreateWindow"></a>

#### CreateWindow

```python
def CreateWindow(name: str = "PHardware GUI",
                 width: int = 800,
                 height: int = 400,
                 WindowPos: Union[None, Any] = SDL_WINDOWPOS_CENTERED,
                 WindowType: Optional[Any] = None,
                 x: int = 0,
                 y: int = 0) -> Any
```

Creates a window.

**Arguments**:

- `name` _str, optional_ - The Title of the window. Defaults to "PHardware GUI".
- `width` _int, optional_ - The width of the window. Defaults to 800.
- `height` _int, optional_ - The height of the window. Defaults to 400.
- `WindowPos` _Union[None, Any], optional_ - The position of the window. Only accept SDL_WINDOWPOS_[Something]. Defaults to SDL_WINDOWPOS_CENTERED
- `WindowType` _Optional[Any], optional_ - If not NONE, The provided SDL_WINDOW_[type] will be used for the window type. Example -> SDL_WINDOW_FULLSCREEN or SDL_WINDOW_BORDERLESS. None for normal. Defaults to None
- `x` _int_ - If WindowType is not None, this will be used as the X position. Defaults to 0.
- `y` _int_ - If WindowType is not None, this will be used as the Y position. Defaults to 0.
  

**Raises**:

- `PheonixException` - Incase window creation failed.
  

**Returns**:

- `Any` - Window Handle

<a id="phardwareitk.GUI.gui_sdl.Quit"></a>

#### Quit

```python
def Quit() -> None
```

Quits the Window.

<a id="phardwareitk.GUI.gui_sdl.DestroyWindow"></a>

#### DestroyWindow

```python
def DestroyWindow(window: Any,
                  icon: Optional[PIcon] = None,
                  renderer: Optional[SDL_Renderer] = None) -> None
```

Destroys the Window and any remaining resources.

**Arguments**:

- `window` _Any_ - The Window.
- `icon` _Optional[PIcon], optional_ - If any, The icon used. Defaults to None.
- `renderer` _Optional[SDL_Renderer], optional_ - If any, the renderer used. Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.EventLoop"></a>

#### EventLoop

```python
def EventLoop(quit_OnMessage: bool = False,
              window: Any = None,
              WidgetPacks: Optional[list[WidgetPack]] = None,
              icon: Optional[PIcon] = None,
              renderer: Optional[SDL_Renderer] = None,
              SafeExitOnError: bool = True) -> Union[bool, SDL_Event]
```

Checks if any events are in event queue and reteives the next event.

**Arguments**:

- `quit_OnMessage` _bool, optional_ - If set to True, will run loop (Button and such widgets will not work), upon receiving Quit event (e.g. On Window Quit) the program will destroy the window. Else False. Defaults to False
- `window` _Any, optional_ - If quit_OnMessage set to true, the provide the window
- `WidgetPacks` _Optional[list[WidgetPack]]_ - If any, the program will provide events to the widget.
- `....` - Parameter to DestroyWindow.
  

**Returns**:

  Union[bool, SDL_Event]: True for Quit, otherwise the event.

<a id="phardwareitk.GUI.gui_sdl.MakeRenderer"></a>

#### MakeRenderer

```python
def MakeRenderer(window: Any,
                 index: int = -1,
                 flags: Union[0, Any] = SDL_RENDERER_ACCELERATED) -> Any
```

Returns a renderer.

**Arguments**:

- `window` _Any_ - The Window.
- `index` _int, optional_ - The index of the rendering device to activate. -1 for default. Defaults to -1.
- `flags` _Any, optional_ - The flags for Renderer.
  

**Returns**:

- `Any` - The renderer.

<a id="phardwareitk.GUI.gui_sdl.RenderText"></a>

#### RenderText

```python
def RenderText(renderer: SDL_Renderer,
               widget_rect: SDL_Rect,
               text: str,
               font: TextFont = TextFont(font_color=Color("black")),
               fontFile: Optional[str] = None) -> Union[SDL_Renderer, bytes]
```

Renders text.

**Arguments**:

- `renderer` _SDL_Renderer_ - The renderer to use.
- `widget_rect` _SDL_Rect_ - The rectangle inside which the text should be rendered. (RECT will be invisible)
- `text` _str_ - The text to be rendered.
- `font` _TextFont_ - The text font to be rendered.
- `fontFile` _Optional[str], optional_ - The Font file, if not present -> None. Defaults to None._

<a id="phardwareitk.GUI.gui_sdl.Delay"></a>

#### Delay

```python
def Delay(time: int) -> None
```

Creates a delay of specified seconds, in that time, all the processes will be paused. Since, it is a window, normal time.sleep doesn't work.

**Arguments**:

- `time` _int_ - The time to delay in seconds.

<a id="phardwareitk.GUI.gui_sdl.TitleBarWindows"></a>

#### TitleBarWindows

```python
def TitleBarWindows(
    Title: Optional[str] = None,
    mode: Optional[str] = None,
    color: Color = Color("white")) -> None
```

Modifies the orignal titleBar, to the specified color or mode. WINDOWS SPECIFIC

**Arguments**:

- `Title` _Optional[str]_ - the title of the window, that needs to be modified, If 'None', uses the title of the main window. Defaults to None
- `mode` _Optional[str], optional_ - The mode to use. Available -> dark, light, None (Default). Defaults to None.
- `color` _Color, optional_ - The color of the titleBar, used incase 'mode' is set to None. Defaults to Color("black").

<a id="phardwareitk.GUI.gui_sdl.TitleBarMacOS"></a>

#### TitleBarMacOS

```python
def TitleBarMacOS(mode: Optional[str] = None) -> None
```

Modifies the orignal titleBar, to the specified color or mode. MACOS SPECIFIC. DOESN't SUPPORT COLOR!

**Arguments**:

- `mode` _Optional[str], optional_ - The mode to use. Available -> dark, light, None (Default). Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.TitleBar"></a>

## TitleBar Objects

```python
class TitleBar(PWidget)
```

A title bar class. Allows you to create custom title bars. To use this keep window creation to SDL_Window_BORDERLESS.

NOTE: Still Under development, hence some bugs might occur.

NOTE: The main action buttons do not work! please use with care! (Under Development)

<a id="phardwareitk.GUI.gui_sdl.TitleBar.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    window: Any,
    width: Optional[int] = None,
    height: int = 50,
    title: str = "PHardwareITK",
    bgcolor: Color = Color("black")) -> None
```

Init func of TitleBar Class.

NOTE: Still Under development, hence some bugs might occur.

NOTE: The main action buttons do not work! please use with care! (Under Development)

**Arguments**:

- `window` _Any_ - The window to draw the titleBar on.
- `width` _Optional[int], optional_ - The width of the title bar, None for using Window Size Width. Defaults to None.
- `height` _int, optional_ - The height of the title bar. Defaults to 50.
- `title` _str, optional_ - The title text. Defaults to "PHardwareITK".
- `bgcolor` _Color, optional_ - The background color of the title bar. Defaults to Color("black").

<a id="phardwareitk.GUI.gui_sdl.TitleBar.SetBackgroundColor"></a>

#### SetBackgroundColor

```python
def SetBackgroundColor(color: Color) -> None
```

Changes the orignal background color of the title bar.

**Arguments**:

- `color` _Color_ - The color.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.DisableTitle"></a>

#### DisableTitle

```python
def DisableTitle() -> None
```

Disables the title from the title bar

<a id="phardwareitk.GUI.gui_sdl.TitleBar.SetTitle"></a>

#### SetTitle

```python
def SetTitle(
    title: str = "PHardwareITK",
    font: TextFont = TextFont(font_size=16)) -> None
```

Changes the orignal title of the title bar.

**Arguments**:

- `title` _str, optional_ - The title. Defaults to "PHardwareITK".
- `font` _TextFont, optional_ - The font of the title. Defaults to TextFont(font_size=16).

<a id="phardwareitk.GUI.gui_sdl.TitleBar.AddText"></a>

#### AddText

```python
def AddText(name: str,
            text: str,
            font: TextFont = TextFont(font_size=16),
            x: int = 0,
            y: int = 0,
            enabled: bool = True) -> None
```

Adds a new text to the title bar at the specified locations.

**Arguments**:

- `name` _str_ - The name of the object. (should be Unique and not previously used)
- `text` _str_ - The text of the object.
- `font` _TextFont, optional_ - The font of the object. Defaults to TextFont(font_size=16).
- `x` _int, optional_ - The X coordinate (in the titlebar). Defaults to 0.
- `y` _int, optional_ - The X coordinate (in the titlebar)The X coordinate (in the titlebar). Defaults to 0.
- `enabled` _bool, optional_ - Wether to enable it or not for the time being. Defaults to True.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.ModifyTitle"></a>

#### ModifyTitle

```python
def ModifyTitle(text: Optional[str] = None,
                font: Optional[TextFont] = None,
                x: Optional[int] = None,
                y: Optional[int] = None,
                enabled: Optional[bool] = None) -> None
```

Modifies the Title of the title bar.

Set parameter to 'None' to define no change.

**Arguments**:

- `text` _Optional[str], optional_ - Text. Defaults to None.
- `font` _Optional[TextFont], optional_ - Font. Defaults to None.
- `x` _Optional[int], optional_ - X coordinate. (of the titlebar). Defaults to None.
- `y` _Optional[int], optional_ - Y coordinate. (of the titlebar). Defaults to None.
- `enabled` _Optional[bool], optional_ - Wether it is enabled or not. Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.ModifyText"></a>

#### ModifyText

```python
def ModifyText(name: str,
               text: Optional[str] = None,
               font: Optional[TextFont] = None,
               x: Optional[int] = None,
               y: Optional[int] = None,
               enabled: Optional[bool] = None) -> None
```

Modifies the specified Text object of the title bar.

Set parameter to 'None' to define no change.

**Arguments**:

- `name` _str_ - The name of the object.
- `text` _Optional[str], optional_ - Text. Defaults to None.
- `font` _Optional[TextFont], optional_ - Font. Defaults to None.
- `x` _Optional[int], optional_ - X coordinate. (of the titlebar). Defaults to None.
- `y` _Optional[int], optional_ - Y coordinate. (of the titlebar). Defaults to None.
- `enabled` _Optional[bool], optional_ - Wether it is enabled or not. Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.EnableText"></a>

#### EnableText

```python
def EnableText(name: str) -> None
```

Enables the specified text object in the title bar.

**Arguments**:

- `name` _str_ - The name of the object.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.EnableTitle"></a>

#### EnableTitle

```python
def EnableTitle() -> None
```

Enables the title in the title bar.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.SetIcon"></a>

#### SetIcon

```python
def SetIcon(name: str, icon: PIcon) -> None
```

Adds a new icon to the title bar at the specified x, y coordinates.

**Arguments**:

- `name` _str_ - The name of the icon object. (Should be Unique and not previously used)
- `icon` _PIcon_ - The icon itself.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.RemoveIcon"></a>

#### RemoveIcon

```python
def RemoveIcon(name: str) -> None
```

Removes the specified icon from the title bar.

**Arguments**:

- `name` _str_ - The name of the icon to remove.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.ModifyInteractivityOptions"></a>

#### ModifyInteractivityOptions

```python
def ModifyInteractivityOptions(draggable: Optional[bool] = None,
                               close_action: Optional[bool] = None,
                               on_click: Optional[bool] = None) -> None
```

Modifies the pre-made options for the titlebar.

NOTE: Use 'None' to define no change.

NOTE: Be Careful while using this, incase you set close_action to 'False', try to use some kind of program like task manager to kill the python process.

**Arguments**:

- `draggable` _Optional[bool], optional_ - Is it draggable. Defaults to None.
- `close_action` _Optional[bool], optional_ - Can it be closed. Defaults to None.
- `on_click` _Optional[bool], optional_ - Is it clickable. Defaults to None.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.LoadIcons"></a>

#### LoadIcons

```python
def LoadIcons(renderer: SDL_Renderer)
```

Loads the icons for drawing.

<a id="phardwareitk.GUI.gui_sdl.TitleBar.Draw"></a>

#### Draw

```python
def Draw(renderer: SDL_Renderer) -> WidgetPack
```

Draws the title bar based on the information.

**Arguments**:

- `renderer` _SDL_Renderer_ - The renderer to use.
  

**Returns**:

- `WidgetPack` - Pass it as a list into the EventLoop.

<a id="phardwareitk.GUI.gui_sdl.Button"></a>

## Button Objects

```python
class Button(PWidget)
```

A Button widget

**Arguments**:

- `PWidget` _PWidget_ - phardwareitk.Extensions.PWidget

<a id="phardwareitk.GUI.gui_sdl.Button.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    x: int,
    y: int,
    width: int,
    height: int,
    label: str = "ClickMe",
    bg_color: Color = Color("gray"),
    Font: TextFont = TextFont()
) -> None
```

Initialize the Button.

**Arguments**:

- `x` _int_ - X coordinate.
- `y` _int_ - Y coordinate.
- `width` _int_ - Width.
- `height` _int_ - Height.
- `label` _str, optional_ - Label for the button. Defaults to "Button".
- `bg_color` _Color, optional_ - Background-Color. Defaults to Color("gray").
- `Font` _TextFont, optional_ - Font for the label. Defaults to TextFont().

<a id="phardwareitk.GUI.gui_sdl.Button.Draw"></a>

#### Draw

```python
def Draw(window: Any) -> SDL_Renderer
```

Draws the button widget.

**Arguments**:

- `window` _Any_ - The window to draw the widget.

<a id="phardwareitk.GUI.gui_sdl.Button.onClick"></a>

#### onClick

```python
def onClick(callback: object, params: Optional[tuple] = None) -> WidgetPack
```

Runs the following function if Mouse is clicked upon the button.

**Arguments**:

- `callback` _object_ - The callback function.
- `params` _Optional[tuple], optional_ - If any, parameters for the callback. Defaults to None.
  

**Returns**:

- `WidgetPack` - Use it inside the EventLoop.

<a id="phardwareitk.GUI.gui_sdl.Label"></a>

## Label Objects

```python
class Label(PWidget)
```

Creates a label.

<a id="phardwareitk.GUI.gui_sdl.Label.__init__"></a>

#### \_\_init\_\_

```python
def __init__(label: str,
             x: int = 0,
             y: int = 0,
             width: int = 5,
             height: int = 5,
             font: TextFont = TextFont()) -> None
```

INIT Function for Label class.

**Arguments**:

- `label` _str_ - The Text.
- `x` _int, optional_ - The X coordinate. Defaults to 0.
- `y` _int, optional_ - The Y coordinate. Defaults to 0.
- `width` _int, optional_ - The width of the label. Defaults to 5.
- `height` _int, optional_ - The height of the label. Defaults to 5.
- `font` _TextFont, optional_ - The font of the label. Defaults to TextFont().

<a id="phardwareitk.GUI.gui_sdl.Label.Draw"></a>

#### Draw

```python
def Draw(window: Any) -> SDL_Renderer
```

Draws the label on the screen.

**Arguments**:

- `window` _Any_ - The window to draw on.
  

**Returns**:

- `SDL_Renderer` - The renderer object. Should be passed onto the list of renderers in DestroyWindow function.

<a id="phardwareitk.GUI.gui_sdl.Quadrilateral"></a>

## Quadrilateral Objects

```python
class Quadrilateral(PWidget)
```

Creates a Quadrilateral.

<a id="phardwareitk.GUI.gui_sdl.Quadrilateral.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int = 5,
             height: int = 8,
             x: int = 0,
             y: int = 0,
             color: Color = Color("white")) -> None
```

INIT function of Quadrilateral class.

**Arguments**:

- `width` _int, optional_ - The width of the quadrilateral. Defaults to 5.
- `height` _int, optional_ - The height of the quadrilateral. Defaults to 8.
- `x` _int, optional_ - The X coordinate. Defaults to 0.
- `y` _int, optional_ - The Y coordinate. Defaults to 0.
- `color` _Color, optional_ - The color of the quadrilateral. Defaults to Color("white").

<a id="phardwareitk.GUI.gui_sdl.Quadrilateral.Draw"></a>

#### Draw

```python
def Draw(window: Any) -> None
```

Draws the quadrilateral.

**Arguments**:

- `window` _Any_ - The window to draw the quadrilateral.

<a id="phardwareitk.GUI.gui_sdl.Shape"></a>

## Shape Objects

```python
class Shape(PWidget)
```

Creates a shape.

<a id="phardwareitk.GUI.gui_sdl.Shape.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    vertex: tuple,
    x: int = 0,
    y: int = 0,
    wireframe: bool = False,
    bgcolor: Color = Color("white"),
    color: Color = Color("white")
) -> None
```

INIT function of Shape Class.

**Arguments**:

- `vertex` _tuple_ - The vertexes of the shape.
- `x` _int, optional_ - X coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
- `y` _int, optional_ - Y coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
- `wireframe` _bool, optional_ - If True, the shape will be a wireframe shape. Defaults to False.
- `bgcolor` _Color, optional_ - The background color of the shape. Defaults to Color("white").
- `color` _Color, optional_ - The color of the lines. Defaults to Color("white").

<a id="phardwareitk.GUI.gui_sdl.Shape.Draw"></a>

#### Draw

```python
def Draw(renderer: SDL_Renderer) -> SDL_Renderer
```

Draws the Shape.

**Arguments**:

- `renderer` _SDL_Renderer_ - The renderer to use.
  

**Returns**:

- `SDL_Renderer` - The renderer of the shape.

<a id="phardwareitk.GUI.gui_sdl.AdvQuadrilateral"></a>

## AdvQuadrilateral Objects

```python
class AdvQuadrilateral(PWidget)
```

Creates a Advanced Quadrilateral.

<a id="phardwareitk.GUI.gui_sdl.AdvQuadrilateral.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    p1: int,
    p1w: int,
    p2: int,
    p2w: int,
    p3: int,
    p3w: int,
    p4: int,
    p4w: int,
    x: int = 0,
    y: int = 0,
    wireframe: bool = False,
    bgcolor: Color = Color("white"),
    color: Color = Color("white")
) -> None
```

INIT function of AdvQuadrilateral Class.

**Arguments**:

- `p1` _int_ - Vertex X.
- `p1w` _int_ - Vertex Y.
  ....... Continued
- `x` _int, optional_ - X coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
- `y` _int, optional_ - Y coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
- `wireframe` _bool, optional_ - Whether to make the shape wireframe. Defaults to False.
- `bgcolor` _Color, optional_ - The background color of the shape. Defaults to Color("white").
- `color` _Color, optional_ - The color. Defaults to Color("white").

<a id="phardwareitk.GUI.gui_sdl.AdvQuadrilateral.Draw"></a>

#### Draw

```python
def Draw(renderer: SDL_Renderer) -> SDL_Renderer
```

Draws the shape

**Arguments**:

- `renderer` _SDL_Renderer_ - The renderer to draw using.
  

**Returns**:

- `SDL_Renderer` - The renderer of the shape.

<a id="phardwareitk.GUI.PheonixIon.win32"></a>

# phardwareitk.GUI.PheonixIon.win32

<a id="phardwareitk.GUI.PheonixIon.win32.ctypes"></a>

## ctypes

<a id="phardwareitk.GUI.PheonixIon.win32.wintypes"></a>

## wintypes

<a id="phardwareitk.GUI.PheonixIon.win32.Optional"></a>

## Optional

<a id="phardwareitk.GUI.PheonixIon.win32.user32"></a>

#### user32

<a id="phardwareitk.GUI.PheonixIon.win32.kernel32"></a>

#### kernel32

<a id="phardwareitk.GUI.PheonixIon.win32.gdi32"></a>

#### gdi32

<a id="phardwareitk.GUI.PheonixIon.win32.*"></a>

## \*

<a id="phardwareitk.GUI.PheonixIon.win32.GPU_API"></a>

## GPU\_API

<a id="phardwareitk.GUI.PheonixIon.win32.PIonContext"></a>

## PIonContext

<a id="phardwareitk.GUI.PheonixIon.win32.*"></a>

## \*

<a id="phardwareitk.GUI.PheonixIon.win32.BaseGPUD"></a>

## BaseGPUD

<a id="phardwareitk.GUI.PheonixIon.win32.PIWin32Flags"></a>

## PIWin32Flags Objects

```python
class PIWin32Flags()
```

<a id="phardwareitk.GUI.PheonixIon.win32.PIWin32Flags.__init__"></a>

#### \_\_init\_\_

```python
def __init__(exStyle: int = 0,
             className="PheonixIonWindow",
             windowName="Pheonix Ion",
             style: int = WS_OVERLAPPEDWINDOW,
             x: int = 100,
             y: int = 100,
             width: int = 800,
             height: int = 600,
             parent: Optional[HWND] = None,
             menu: Optional[HMENU] = None,
             instance: Optional[HINSTANCE] = None,
             param: Optional[LPVOID] = None) -> None
```

<a id="phardwareitk.GUI.PheonixIon.win32.PIWin32Flags.to_c"></a>

#### to\_c

```python
def to_c()
```

<a id="phardwareitk.GUI.PheonixIon.win32.create_window"></a>

#### create\_window

```python
def create_window(title: str = "Pheonix Ion",
                  width: int = 800,
                  height: int = 600,
                  flags: PIWin32Flags = None) -> HWND
```

Create a Win32 window and return its handle.

<a id="phardwareitk.GUI.PheonixIon.win32.show_window"></a>

#### show\_window

```python
def show_window(hwnd: HWND) -> None
```

<a id="phardwareitk.GUI.PheonixIon.win32.hide_window"></a>

#### hide\_window

```python
def hide_window(hwnd: HWND) -> None
```

<a id="phardwareitk.GUI.PheonixIon.win32.set_window_title"></a>

#### set\_window\_title

```python
def set_window_title(hwnd: HWND, title: str) -> None
```

<a id="phardwareitk.GUI.PheonixIon.win32.destroy_window"></a>

#### destroy\_window

```python
def destroy_window(hwnd: HWND) -> None
```

<a id="phardwareitk.GUI.PheonixIon.win32.poll_events"></a>

#### poll\_events

```python
def poll_events(hwnd: HWND)
```

<a id="phardwareitk.GUI.PheonixIon.win32.is_window_alive"></a>

#### is\_window\_alive

```python
def is_window_alive(hwnd: HWND) -> bool
```

<a id="phardwareitk.GUI.PheonixIon.win32.get_gpu"></a>

#### get\_gpu

```python
def get_gpu(hwnd: HWND, api: Optional[str],
            driver: Optional[BaseGPUD]) -> GPU_API
```

<a id="phardwareitk.GUI.PheonixIon.win32.attach_gpu"></a>

#### attach\_gpu

```python
def attach_gpu(hwnd: HWND, gpu: GPU_API) -> PIonContext
```

<a id="phardwareitk.GUI.PheonixIon.x11"></a>

# phardwareitk.GUI.PheonixIon.x11

<a id="phardwareitk.GUI.PheonixIon.x11.ctypes"></a>

## ctypes

<a id="phardwareitk.GUI.PheonixIon.x11.os"></a>

## os

<a id="phardwareitk.GUI.PheonixIon.x11.c_int"></a>

## c\_int

<a id="phardwareitk.GUI.PheonixIon.x11.c_ulong"></a>

## c\_ulong

<a id="phardwareitk.GUI.PheonixIon.x11.c_char_p"></a>

## c\_char\_p

<a id="phardwareitk.GUI.PheonixIon.x11.c_void_p"></a>

## c\_void\_p

<a id="phardwareitk.GUI.PheonixIon.x11.POINTER"></a>

## POINTER

<a id="phardwareitk.GUI.PheonixIon.x11.c_long"></a>

## c\_long

<a id="phardwareitk.GUI.PheonixIon.x11.c_uint"></a>

## c\_uint

<a id="phardwareitk.GUI.PheonixIon.x11.cdll"></a>

## cdll

<a id="phardwareitk.GUI.PheonixIon.x11.BaseGPUD"></a>

## BaseGPUD

<a id="phardwareitk.GUI.PheonixIon.x11.*"></a>

## \*

<a id="phardwareitk.GUI.PheonixIon.x11.GPU_API"></a>

## GPU\_API

<a id="phardwareitk.GUI.PheonixIon.x11.PIonContext"></a>

## PIonContext

<a id="phardwareitk.GUI.PheonixIon.x11.libX11"></a>

#### libX11

<a id="phardwareitk.GUI.PheonixIon.x11.Display"></a>

#### Display

<a id="phardwareitk.GUI.PheonixIon.x11.Window"></a>

#### Window

<a id="phardwareitk.GUI.PheonixIon.x11.Atom"></a>

#### Atom

<a id="phardwareitk.GUI.PheonixIon.x11.Window"></a>

#### Window

<a id="phardwareitk.GUI.PheonixIon.x11.Drawable"></a>

#### Drawable

<a id="phardwareitk.GUI.PheonixIon.x11.Time"></a>

#### Time

<a id="phardwareitk.GUI.PheonixIon.x11.XPointer"></a>

#### XPointer

<a id="phardwareitk.GUI.PheonixIon.x11.Bool"></a>

#### Bool

<a id="phardwareitk.GUI.PheonixIon.x11.Colormap"></a>

#### Colormap

<a id="phardwareitk.GUI.PheonixIon.x11.VisualID"></a>

#### VisualID

<a id="phardwareitk.GUI.PheonixIon.x11.XSetWindowAttributes"></a>

## XSetWindowAttributes Objects

```python
class XSetWindowAttributes(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XSetWindowAttributes._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XWindowAttributes"></a>

## XWindowAttributes Objects

```python
class XWindowAttributes(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XWindowAttributes._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XVisualInfo"></a>

## XVisualInfo Objects

```python
class XVisualInfo(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XVisualInfo._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XAnyEvent"></a>

## XAnyEvent Objects

```python
class XAnyEvent(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XAnyEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XKeyEvent"></a>

## XKeyEvent Objects

```python
class XKeyEvent(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XKeyEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XButtonEvent"></a>

## XButtonEvent Objects

```python
class XButtonEvent(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XButtonEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XConfigureEvent"></a>

## XConfigureEvent Objects

```python
class XConfigureEvent(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XConfigureEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XEvent"></a>

## XEvent Objects

```python
class XEvent(ctypes.Union)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.XErrorEvent"></a>

## XErrorEvent Objects

```python
class XErrorEvent(ctypes.Structure)
```

<a id="phardwareitk.GUI.PheonixIon.x11.XErrorEvent._fields_"></a>

#### \_fields\_

<a id="phardwareitk.GUI.PheonixIon.x11.X_EVENT_MASKS"></a>

#### X\_EVENT\_MASKS

<a id="phardwareitk.GUI.PheonixIon.x11.X_EVENT_MASK"></a>

#### X\_EVENT\_MASK

<a id="phardwareitk.GUI.PheonixIon.x11.CWBackPixel"></a>

#### CWBackPixel

<a id="phardwareitk.GUI.PheonixIon.x11.CWBorderPixel"></a>

#### CWBorderPixel

<a id="phardwareitk.GUI.PheonixIon.x11.CWEventMask"></a>

#### CWEventMask

<a id="phardwareitk.GUI.PheonixIon.x11.CWColormap"></a>

#### CWColormap

<a id="phardwareitk.GUI.PheonixIon.x11.VALUEMASK"></a>

#### VALUEMASK

<a id="phardwareitk.GUI.PheonixIon.x11.INPUT_OUTPUT"></a>

#### INPUT\_OUTPUT

<a id="phardwareitk.GUI.PheonixIon.x11.x_error_handler"></a>

#### x\_error\_handler

```python
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(XErrorEvent))
def x_error_handler(error_event_ptr)
```

<a id="phardwareitk.GUI.PheonixIon.x11.PIX11Flags"></a>

## PIX11Flags Objects

```python
class PIX11Flags()
```

<a id="phardwareitk.GUI.PheonixIon.x11.PIX11Flags.__init__"></a>

#### \_\_init\_\_

```python
def __init__(x=100,
             y=100,
             width=800,
             height=600,
             border=1,
             border_color=0,
             background=0)
```

<a id="phardwareitk.GUI.PheonixIon.x11.create_window"></a>

#### create\_window

```python
def create_window(title: str = "Pheonix Ion",
                  width: int = 800,
                  height: int = 600,
                  flags: PIX11Flags = None)
```

<a id="phardwareitk.GUI.PheonixIon.x11.show_window"></a>

#### show\_window

```python
def show_window(window_tuple)
```

<a id="phardwareitk.GUI.PheonixIon.x11.hide_window"></a>

#### hide\_window

```python
def hide_window(window_tuple)
```

<a id="phardwareitk.GUI.PheonixIon.x11.set_window_title"></a>

#### set\_window\_title

```python
def set_window_title(window_tuple, title)
```

<a id="phardwareitk.GUI.PheonixIon.x11.destroy_window"></a>

#### destroy\_window

```python
def destroy_window(window_tuple)
```

<a id="phardwareitk.GUI.PheonixIon.x11.poll_events"></a>

#### poll\_events

```python
def poll_events(window_tuple)
```

<a id="phardwareitk.GUI.PheonixIon.x11.is_window_alive"></a>

#### is\_window\_alive

```python
def is_window_alive(window_tuple) -> bool
```

<a id="phardwareitk.GUI.PheonixIon.x11.get_gpu"></a>

#### get\_gpu

```python
def get_gpu(window_tuple,
            api: Optional[str] = None,
            driver: Optional[BaseGPUD] = None) -> GPU_API
```

<a id="phardwareitk.GUI.PheonixIon.x11.attach_gpu"></a>

#### attach\_gpu

```python
def attach_gpu(window_tuple, gpu: GPU_API) -> None
```

<a id="phardwareitk.GUI.PheonixIon"></a>

# phardwareitk.GUI.PheonixIon

Pheonix Ion is the native GUI system for PHardwareITK

<a id="phardwareitk.GUI.PheonixIon.types"></a>

# phardwareitk.GUI.PheonixIon.types

<a id="phardwareitk.GUI.PheonixIon.types.os"></a>

## os

<a id="phardwareitk.GUI.PheonixIon.types.platform"></a>

## platform

<a id="phardwareitk.GUI.PheonixIon.types.*"></a>

## \*

<a id="phardwareitk.GUI.PheonixIon.types.PIenum"></a>

## PIenum Objects

```python
class PIenum()
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = None) -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.create_enum"></a>

#### create\_enum

```python
def create_enum(entries: list[str], start_value: int = 0) -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.access"></a>

#### access

```python
def access(name: str) -> int
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.reverse_access"></a>

#### reverse\_access

```python
def reverse_access(val: int) -> str
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(item: Union[str, int]) -> Any
```

<a id="phardwareitk.GUI.PheonixIon.types.PIenum.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.GUI.PheonixIon.types.PIint"></a>

## PIint Objects

```python
class PIint(int)
```

<a id="phardwareitk.GUI.PheonixIon.types.PIint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIint.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.GUI.PheonixIon.types.PIuint"></a>

## PIuint Objects

```python
class PIuint(int)
```

<a id="phardwareitk.GUI.PheonixIon.types.PIuint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIuint.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.GUI.PheonixIon.types.PIstring"></a>

## PIstring Objects

```python
class PIstring(str)
```

<a id="phardwareitk.GUI.PheonixIon.types.PIstring.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: str = "") -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIstring.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.GUI.PheonixIon.types.PIonEvent_Types"></a>

#### PIonEvent\_Types

<a id="phardwareitk.GUI.PheonixIon.types.PIonEvent"></a>

## PIonEvent Objects

```python
class PIonEvent()
```

Pheonix Ion Event Class

<a id="phardwareitk.GUI.PheonixIon.types.PIonEvent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(typ: Union[int, str], **kwargs) -> None
```

<a id="phardwareitk.GUI.PheonixIon.types.PIonEvent.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.GUI"></a>

# phardwareitk.GUI

Graphical User Interface Backends and SubModules

<a id="phardwareitk.GUI.platform"></a>

## platform

<a id="phardwareitk.GUI.sys"></a>

## sys

<a id="phardwareitk.GUI.os"></a>

## os

<a id="phardwareitk.GUI.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.GUI.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.GUI.HyperOut"></a>

## HyperOut

<a id="phardwareitk.GUI.Extensions"></a>

## Extensions

<a id="phardwareitk.GUI.*"></a>

## \*

<a id="phardwareitk.GUI.get_platform"></a>

#### get\_platform

```python
def get_platform() -> str
```

<a id="phardwareitk.GUI.OS"></a>

#### OS

<a id="phardwareitk.GUI.Linux"></a>

#### Linux

<a id="phardwareitk.GUI.Windows"></a>

#### Windows

<a id="phardwareitk.GUI.Darwin"></a>

#### Darwin

<a id="phardwareitk.GUI.Unix"></a>

#### Unix

<a id="phardwareitk.GUI.Unknown_os"></a>

#### Unknown\_os

<a id="phardwareitk.GUI.QUIT"></a>

#### QUIT

SDL_QUIT

<a id="phardwareitk.GUI.WM_DESTROY"></a>

#### WM\_DESTROY

<a id="phardwareitk.GUI.WM_PAINT"></a>

#### WM\_PAINT

<a id="phardwareitk.GUI.pheonix_ion"></a>

# phardwareitk.GUI.pheonix\_ion

GUI Library, from PHardwareITK itself

<a id="phardwareitk.GUI.pheonix_ion.platform"></a>

## platform

<a id="phardwareitk.GUI.pheonix_ion.os"></a>

## os

<a id="phardwareitk.GUI.pheonix_ion.sys"></a>

## sys

<a id="phardwareitk.GUI.pheonix_ion.ctypes"></a>

## ctypes

<a id="phardwareitk.GUI.pheonix_ion.*"></a>

## \*

<a id="phardwareitk.GUI.pheonix_ion.BaseGPUD"></a>

## BaseGPUD

<a id="phardwareitk.GUI.pheonix_ion.*"></a>

## \*

<a id="phardwareitk.GUI.pheonix_ion.NoCompatibleGraphicsAPIFound"></a>

## NoCompatibleGraphicsAPIFound Objects

```python
class NoCompatibleGraphicsAPIFound(Exception)
```

<a id="phardwareitk.GUI.pheonix_ion.NoCompatibleGraphicsAPIFound.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message="No compatible graphics API found")
```

<a id="phardwareitk.GUI.pheonix_ion.UnsupportedPlatform"></a>

## UnsupportedPlatform Objects

```python
class UnsupportedPlatform(Exception)
```

<a id="phardwareitk.GUI.pheonix_ion.UnsupportedPlatform.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message="Unsupported platform for window creation")
```

<a id="phardwareitk.GUI.pheonix_ion.SYSTEM"></a>

#### SYSTEM

<a id="phardwareitk.GUI.pheonix_ion.try_load_library"></a>

#### try\_load\_library

```python
def try_load_library(lib_names: list)
```

Try to load a list of library names; return first that succeeds.

<a id="phardwareitk.GUI.pheonix_ion.PIonWindow"></a>

## PIonWindow Objects

```python
class PIonWindow()
```

A Pheonix Ion Window Instance

<a id="phardwareitk.GUI.pheonix_ion.PIonWindow.__init__"></a>

#### \_\_init\_\_

```python
def __init__(title: str,
             width: int,
             height: int,
             flags=None,
             handle=None) -> None
```

<a id="phardwareitk.GUI.pheonix_ion.GPU_API"></a>

## GPU\_API Objects

```python
class GPU_API()
```

Pheonix Ion GPU API, use the driver attribute to access functions like -
```python
    mygpu = GPU_API() # This is a simplification, the PheonixIon Class will return the GPU_API initialized.
    # Initialize
    mygpu.driver.init(mydisplay, mywin)
    # Clear screen
    mygpu.driver.clear(255, 0, 0, 255) # rgba
    # Destroy
    mygpu.driver.shutdown()
```

<a id="phardwareitk.GUI.pheonix_ion.GPU_API.__init__"></a>

#### \_\_init\_\_

```python
def __init__(api: str = None, driver: Any = None) -> None
```

<a id="phardwareitk.GUI.pheonix_ion.PIonContext"></a>

## PIonContext Objects

```python
class PIonContext()
```

<a id="phardwareitk.GUI.pheonix_ion.PIonContext.__init__"></a>

#### \_\_init\_\_

```python
def __init__(api_name: str,
             native_handle: object,
             lib_path: str,
             metadata: dict = None)
```

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon"></a>

## PheonixIon Objects

```python
class PheonixIon()
```

The Main Pheonix Ion Multi-Window System, using one instance a user can create 1, 2, 3, ..., 50+ windows if they wanted.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.create_window"></a>

#### create\_window

```python
def create_window(title: str = "Pheonix Ion",
                  width: int = 800,
                  height: int = 600,
                  flags=None) -> PIonWindow
```

Create a window with specified parameters.

**Arguments**:

- `title` _str_ - Title of the window.
- `width` _int_ - Width of the window.
- `height` _int_ - Height of the window.
- `backend` _str or PIenum_ - Backend to use for window creation. If None, auto-detects based on platform.
- `flags` - Additional flags for window creation (backend-specific), For example PIWin32Flags for Win32 backend.

**Returns**:

- `PIonWindow` - The created window object.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.poll_events"></a>

#### poll\_events

```python
def poll_events(win: Union[int, PIonWindow]) -> list
```

Poll events for the created window.

**Arguments**:

- `win` _int | PIonWindow_ - The window index or the PIonWindow class instance
  

**Returns**:

- `list` - A List of PIonEvent from PheonixIon.types

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.destroy_window"></a>

#### destroy\_window

```python
def destroy_window(win: Union[int, PIonWindow])
```

Destroy a window and release its resources.

**Arguments**:

- `win` _int | PIonWindow_ - Window index or PIonWindow instance.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.hide_window"></a>

#### hide\_window

```python
def hide_window(win: Union[int, PIonWindow])
```

Hide a window (make it invisible but not destroyed).

**Arguments**:

- `win` _int | PIonWindow_ - Window index or PIonWindow instance.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.show_window"></a>

#### show\_window

```python
def show_window(win: Union[int, PIonWindow])
```

Show a previously hidden window.

**Arguments**:

- `win` _int | PIonWindow_ - Window index or PIonWindow instance.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.set_window_title"></a>

#### set\_window\_title

```python
def set_window_title(win: Union[int, PIonWindow], title: str)
```

Change the title of a window.

**Arguments**:

- `win` _int | PIonWindow_ - Window index or PIonWindow instance.
- `title` _str_ - New window title.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.is_window_alive"></a>

#### is\_window\_alive

```python
def is_window_alive(win: Union[int, PIonWindow]) -> bool
```

Check if a window is still alive (not closed/destroyed).

**Arguments**:

- `win` _int | PIonWindow_ - Window index or PIonWindow instance.
  

**Returns**:

- `bool` - True if the window is alive, False otherwise.

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.get_window"></a>

#### get\_window

```python
def get_window(win: Union[int, PIonWindow],
               throw_err=False) -> Optional[PIonWindow]
```

Gets the PIonWindow based of its index, or class

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.get_native_handle"></a>

#### get\_native\_handle

```python
def get_native_handle(win: Union[int, PIonWindow]) -> Any
```

Return OS-specific window handle (HWND on Win, X11 tuple, NSWindow on Mac).

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.get_gpu"></a>

#### get\_gpu

```python
def get_gpu(win: Union[int, PIonWindow],
            api: Optional[str] = None,
            driver: Optional[BaseGPUD] = None) -> Optional[GPU_API]
```

Returns the GPU context in form of GPU_API class

<a id="phardwareitk.GUI.pheonix_ion.PheonixIon.attach_gpu"></a>

#### attach\_gpu

```python
def attach_gpu(win: Union[int, PIonWindow], gpu: GPU_API) -> None
```

<a id="phardwareitk.GUI.gui"></a>

# phardwareitk.GUI.gui

Under Development. The provided functions in gui_sdl and renderGUI are just for making the gui process simple.
You can use this file to use SDL and OpenGL functions to create whatever you want.

NOTES:
1. Uses SDL2 (Simple DirectMedia Layer) and OpenGL (Open Graphics Library)

2. Both SDL2 and OpenGL are cross-platform.

3. OpenGL may vary depending on graphics card.

4. To use OpenGL follow the steps below ->

 a. Change the directory to phardwareitk Folder.

 b. Do - '''pip install cython'''


 c. Do - '''cythonize -i GUI/renderGUI.pyx'''


 d. Download GCC


 e. Run - '''gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/[Path to Main Python Folder] -o GUI/renderGUI.[so in linux and pyd in windows] GUI/renderGUI.c'''


 f. The functions from renderGUI will be imported as OpenGUI.[functions]

5. SDL2 Only supports 2d and provides more simple functions. Whereas OpenGL is known for its complexity and performance. OpenGL directly communicates with the GPU and hence needs to be written in C. OpenGL supports both 2D and 3D and complex shapes.

6. Better to import phardwareitk.Extensions, for classes like PIcon, PWidget, Color, TextFont, it also provides HyperIn and HyperOut files, including better versions of python buitins

<a id="phardwareitk.GUI.gui.*"></a>

## \*

<a id="phardwareitk.GUI.gui.*"></a>

## \*

<a id="phardwareitk.GUI.gui.*"></a>

## \*

<a id="phardwareitk.GUI.gui.sdl2"></a>

## sdl2

<a id="phardwareitk.GUI.gui.GL"></a>

## GL

<a id="phardwareitk.GUI.gui.*"></a>

## \*

<a id="phardwareitk.GUI.gui.sys"></a>

## sys

<a id="phardwareitk.GUI.gui.os"></a>

## os

<a id="phardwareitk.GUI.gui.*"></a>

## \*

<a id="phardwareitk.GUI.gui.LIB"></a>

## LIB

<a id="phardwareitk.GUI.gui.Errors"></a>

## Errors

<a id="phardwareitk.GUI.gui.ToStandaloneApplication"></a>

## ToStandaloneApplication Objects

```python
class ToStandaloneApplication()
```

Convert the GUI app to a standalone application. [.EXE/.ELF/...]

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.__init__"></a>

#### \_\_init\_\_

```python
def __init__(getRequirements: bool,
             icon: Optional[str],
             file: str,
             windowed: bool = False) -> None
```

Initialize function of ToStandaloneApplication.

**Arguments**:

- `getRequirements` _bool_ - Download the requirements?
- `icon` _Optional[str]_ - The icon to be used. Leave for default.
- `file` _str_ - The main .py file.
- `windowed` _bool_ - Whether to run the app inside a window. NOTE: If the app is a GUI application then it is recommended to Set this to False.

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.runCmds1"></a>

#### runCmds1

```python
def runCmds1()
```

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.makeCmd"></a>

#### makeCmd

```python
def makeCmd()
```

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.addWIN"></a>

#### addWIN

```python
def addWIN()
```

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.addIcon"></a>

#### addIcon

```python
def addIcon()
```

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.getReq"></a>

#### getReq

```python
def getReq()
```

<a id="phardwareitk.GUI.gui.ToStandaloneApplication.MakeStandaloneApplication"></a>

#### MakeStandaloneApplication

```python
def MakeStandaloneApplication()
```

Makes a standalone application.

<a id="phardwareitk.PENV.framebuffer"></a>

# phardwareitk.PENV.framebuffer

<a id="phardwareitk.PENV.framebuffer.os"></a>

## os

<a id="phardwareitk.PENV.framebuffer.sys"></a>

## sys

<a id="phardwareitk.PENV.framebuffer.module_path"></a>

#### module\_path

<a id="phardwareitk.PENV.framebuffer.*"></a>

## \*

<a id="phardwareitk.PENV.framebuffer.*"></a>

## \*

<a id="phardwareitk.PENV.framebuffer.Framebuffer"></a>

## Framebuffer Objects

```python
class Framebuffer()
```

Bro i lost my mind building this

<a id="phardwareitk.PENV.framebuffer.Framebuffer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int,
             height: int,
             depth: int = 3,
             classNameWin32: str = "Static",
             winNameWin32: str = "Framebuffer") -> None
```

Initialize the framebuffer with specified dimensions and depth.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.write_pixel"></a>

#### write\_pixel

```python
def write_pixel(x=0, y=0, r=0, g=0, b=0) -> None
```

Write a pixel to the framebuffer at the specified coordinates with the given RGB color.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.clear"></a>

#### clear

```python
def clear(r=0, g=0, b=0) -> None
```

Clear the framebuffer with the specified RGB color.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.flush"></a>

#### flush

```python
def flush() -> None
```

Flush the framebuffer to the display.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.handle_events"></a>

#### handle\_events

```python
def handle_events() -> None
```

Handle events for the framebuffer driver.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.lserialize"></a>

#### lserialize

```python
def lserialize() -> list
```

Serialize the framebuffer dimensions into a list.

<a id="phardwareitk.PENV.framebuffer.Framebuffer.delete"></a>

#### delete

```python
def delete() -> None
```

Delete the framebuffer and clean up resources.

<a id="phardwareitk.PENV.PBFS"></a>

# phardwareitk.PENV.PBFS

<a id="phardwareitk.PENV.PBFS.os"></a>

## os

<a id="phardwareitk.PENV.PBFS.sys"></a>

## sys

<a id="phardwareitk.PENV.PBFS.time"></a>

## time

<a id="phardwareitk.PENV.PBFS.struct"></a>

## struct

<a id="phardwareitk.PENV.PBFS.MPATH"></a>

#### MPATH

<a id="phardwareitk.PENV.PBFS.C"></a>

## C

<a id="phardwareitk.PENV.PBFS.stdlib"></a>

## stdlib

<a id="phardwareitk.PENV.PBFS.stdio"></a>

## stdio

<a id="phardwareitk.PENV.PBFS.stdint"></a>

## stdint

<a id="phardwareitk.PENV.PBFS.PBFS_HEADER"></a>

#### PBFS\_HEADER

typedef struct {
	char Magic[6]; // PBFS  
	uint32_t Block_Size; // 512 bytes by default (BIOS BLOCK SIZE)
	uint32_t Total_Blocks;  // 2048 blocks for 1MB
	char Disk_Name[24]; // Just the name of the disk for the os
	uint64_t Timestamp; // Timestamp
	uint32_t Version; // Version
	uint64_t First_Boot_Timestamp; // First boot timestamp
	uint16_t OS_BootMode; // Again optional but there for furture use!
	uint32_t FileTableOffset; // Offset of the file table (first data block)
	uint32_t Entries; // Number of entries in the file table
} __attribute__((packed)) PBFS_Header; // Total = 68 bytes

<a id="phardwareitk.PENV.PBFS.PBFS_FILE_TABLE_ENTRY"></a>

#### PBFS\_FILE\_TABLE\_ENTRY

typedef struct {
	char Name[150]; // Name of the file
	uint64_t File_Data_Offset; // File data offset
	uint64_t Permission_Table_Offset; // Permission table offset
	uint64_t Block_Span; // File Block Span
} __attribute__((packed)) PBFS_FileTableEntry; // Total = 24 bytes

<a id="phardwareitk.PENV.PBFS.PBFS_PERMISSION_TABLE_ENTRY"></a>

#### PBFS\_PERMISSION\_TABLE\_ENTRY

typedef struct {
	uint16_t Read; // Read Permission
	uint16_t Write; // Write Permission
	uint16_t Executable; // Executable Permission
	uint16_t Listable; // Listable Permission
	uint16_t Hidden; // Hidden Permission
	uint16_t Full_Control; // System File Permission
	uint16_t Delete; // Delete Permission
	uint16_t Special_Access; // Special Access
	uint32_t File_Tree_Offset; // Offset of the file tree
} __attribute__((packed)) PBFS_PermissionTableEntry; // Total = 20 bytes

<a id="phardwareitk.PENV.PBFS.PBFS_FILE_TREE_ENTRY"></a>

#### PBFS\_FILE\_TREE\_ENTRY

typedef struct {
	char Name[20]; // Name of the file (unique id is also accepted, it is 20 bytes because the file paths are not used here but rather the unique id is used).
} __attribute__((packed)) PBFS_FileTreeEntry; // Total = 20 bytes

<a id="phardwareitk.PENV.PBFS.PBFS_DAP"></a>

#### PBFS\_DAP

typedef struct {
	uint8_t size;
	uint8_t reserved;
	uint16_t sector_count;
	uint16_t offset;
	uint16_t segment;
	uint64_t lba;
} __attribute__((packed)) PBFS_DAP;

<a id="phardwareitk.PENV.PBFS.PBFS_PERMISSIONS"></a>

#### PBFS\_PERMISSIONS

typedef struct {
	uint16_t Read; // Read Permission
	uint16_t Write; // Write Permission
	uint16_t Executable; // Executable Permission
	uint16_t Listable; // Listable Permission
	uint16_t Hidden; // Hidden Permission
	uint16_t Full_Control; // System File Permission
	uint16_t Delete; // Delete Permission
	uint16_t Special_Access; // Special Access
} __attribute__((packed)) PBFS_Permissions; // Total = 16 bytes

<a id="phardwareitk.PENV.PBFS.PBFS_LAYOUT"></a>

#### PBFS\_LAYOUT

typedef struct {
	uint64_t Header_Start;
	uint64_t Header_End;
	uint64_t Header_BlockSpan;
	uint64_t Bitmap_Start;
	uint64_t Bitmap_BlockSpan;
	uint64_t Bitmap_End;
	uint64_t Data_Start;
} __attribute__((packed)) PBFS_Layout;

<a id="phardwareitk.PENV.PBFS.DRIVE_PARAMETERS"></a>

#### DRIVE\_PARAMETERS

typedef struct {
	uint16_t size;              // 0x00 - Must be 0x1E (30)
	uint16_t flags;             // 0x02
	uint32_t cylinders;         // 0x04 - reserved or zero
	uint32_t heads;             // 0x08 - reserved or zero
	uint32_t sectors_per_track; // 0x0C - reserved or zero
	uint64_t total_sectors;     // 0x10 - important!
	uint16_t bytes_per_sector;  // 0x18 - important!
	uint8_t  reserved[6];       // 0x1A - reserved
} __attribute__((packed)) DriveParameters;

<a id="phardwareitk.PENV.PBFS.PBFS_FILE_LIST_ENTRY"></a>

#### PBFS\_FILE\_LIST\_ENTRY

typedef struct {
	char* name;
	uint64_t lba;
} PBFS_FileListEntry;

<a id="phardwareitk.PENV.PBFS.memsize"></a>

#### memsize

<a id="phardwareitk.PENV.PBFS.round_up_to_block"></a>

#### round\_up\_to\_block

```python
def round_up_to_block(size: int, block_size: int = 512) -> int
```

<a id="phardwareitk.PENV.PBFS.validate_disk"></a>

#### validate\_disk

```python
def validate_disk(path: str, block_size: int = 512) -> bool
```

Validates the Drive

<a id="phardwareitk.PENV.PBFS.format_disk"></a>

#### format\_disk

```python
def format_disk(path: str,
                total_blocks: int = 2048,
                block_size: int = 512,
                disk_name: bytes = b"SSD-PBFS-VIRTUAL") -> int
```

Formates the Drive

<a id="phardwareitk.PENV.PBFS.increase_memsize"></a>

#### increase\_memsize

```python
def increase_memsize(size_: int)
```

Increase the default memory size for this file

<a id="phardwareitk.PENV.PBFS.initialize_pbfs"></a>

#### initialize\_pbfs

```python
def initialize_pbfs(size_: int)
```

<a id="phardwareitk.PENV.PBFS.PBFS"></a>

## PBFS Objects

```python
class PBFS()
```

Python Block File System / Pheonix Block File System

<a id="phardwareitk.PENV.PBFS.PBFS.__init__"></a>

#### \_\_init\_\_

```python
def __init__(drive: str,
             block_size: int = 512,
             total_blocks: int = 2048) -> None
```

<a id="phardwareitk.PENV.shared"></a>

# phardwareitk.PENV.shared

<a id="phardwareitk.PENV.shared.os"></a>

## os

<a id="phardwareitk.PENV.shared.platform"></a>

## platform

<a id="phardwareitk.PENV.shared.json"></a>

## json

<a id="phardwareitk.PENV.shared.mem"></a>

#### mem

<a id="phardwareitk.PENV.shared.vga"></a>

#### vga

<a id="phardwareitk.PENV.shared.framebuffer"></a>

#### framebuffer

<a id="phardwareitk.PENV.shared.disk_data"></a>

#### disk\_data

<a id="phardwareitk.PENV.shared.sys_data"></a>

#### sys\_data

<a id="phardwareitk.PENV.shared.posix_os"></a>

#### posix\_os

<a id="phardwareitk.PENV.shared.PenvInturruptReturn"></a>

## PenvInturruptReturn Objects

```python
class PenvInturruptReturn(Exception)
```

<a id="phardwareitk.PENV.shared.PenvInturruptReturn.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*values)
```

<a id="phardwareitk.PENV.shared.PenvInturruptReturn.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="phardwareitk.PENV.shared.PenvInturruptReturn.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.PENV.shared.set_mem"></a>

#### set\_mem

```python
def set_mem(memory: object) -> None
```

<a id="phardwareitk.PENV.shared.set_vga"></a>

#### set\_vga

```python
def set_vga(vga_: object) -> None
```

<a id="phardwareitk.PENV.shared.set_framebuffer"></a>

#### set\_framebuffer

```python
def set_framebuffer(framebuffer_: object) -> None
```

<a id="phardwareitk.PENV.shared.set_disk_data"></a>

#### set\_disk\_data

```python
def set_disk_data(disk_data_: object) -> None
```

<a id="phardwareitk.PENV.shared.set_sys_data"></a>

#### set\_sys\_data

```python
def set_sys_data(sys_data_: object) -> None
```

<a id="phardwareitk.PENV.shared.interrupt"></a>

#### interrupt

```python
def interrupt(code: int, *args)
```

<a id="phardwareitk.PENV.shared.ddh_key"></a>

#### ddh\_key

```python
def ddh_key(dict_: dict, key: str) -> bool
```

<a id="phardwareitk.PENV.shared.get_os"></a>

#### get\_os

```python
def get_os() -> tuple[bool, bool, bool, str]
```

<a id="phardwareitk.PENV.AOS_PENV.AOS_FHD"></a>

# phardwareitk.PENV.AOS\_PENV.AOS\_FHD

<a id="phardwareitk.PENV.AOS_PENV.AOS_FHD.json"></a>

## json

<a id="phardwareitk.PENV.AOS_PENV.AOS_FHD.setup_dir_tree"></a>

#### setup\_dir\_tree

```python
def setup_dir_tree(_file_manager: object, _cd_: str,
                   _user: str) -> tuple[str, str]
```

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel"></a>

# phardwareitk.PENV.AOS\_PENV.AOS\_Kernel

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.os"></a>

## os

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.sys"></a>

## sys

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.time"></a>

## time

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.json"></a>

## json

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.platform"></a>

## platform

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.threading"></a>

## threading

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.gc"></a>

## gc

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.os_files"></a>

#### os\_files

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.path"></a>

#### path

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.*"></a>

## \*

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.PBFS_DriveData"></a>

## PBFS\_DriveData

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.setup_dir_tree"></a>

## setup\_dir\_tree

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel._cd_"></a>

#### \_cd\_

Current directory

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.base_mode"></a>

#### base\_mode

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.x"></a>

#### x

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.y"></a>

#### y

<a id="phardwareitk.PENV.AOS_PENV.AOS_Kernel.cmd"></a>

#### cmd

<a id="phardwareitk.PENV.AOS_PENV.boot"></a>

# phardwareitk.PENV.AOS\_PENV.boot

<a id="phardwareitk.PENV.AOS_PENV.boot.__sys_info__"></a>

#### \_\_sys\_info\_\_

type:ignore

<a id="phardwareitk.PENV.AOS_PENV.boot.__drive_info__"></a>

#### \_\_drive\_info\_\_

type:ignore

<a id="phardwareitk.PENV.AOS_PENV.boot.table"></a>

#### table

<a id="phardwareitk.PENV.AOS_PENV.aoshelp"></a>

# phardwareitk.PENV.AOS\_PENV.aoshelp

<a id="phardwareitk.PENV.AOS_PENV.aoshelp.*"></a>

## \*

<a id="phardwareitk.PENV.AOS_PENV.aoshelp.cmd_aos_help"></a>

#### cmd\_aos\_help

```python
def cmd_aos_help(print_: bool,
                 flush: bool = False,
                 endl: str = "\n") -> Optional[None, str]
```

AOS cmd help func

<a id="phardwareitk.PENV.Drivers.display"></a>

# phardwareitk.PENV.Drivers.display

<a id="phardwareitk.PENV.Drivers.display.os"></a>

## os

<a id="phardwareitk.PENV.Drivers.display.sys"></a>

## sys

<a id="phardwareitk.PENV.Drivers.display.platform"></a>

## platform

<a id="phardwareitk.PENV.Drivers.display.module_path"></a>

#### module\_path

<a id="phardwareitk.PENV"></a>

# phardwareitk.PENV

DO NOT USE YET!

PENV stands for Pheonix Environment, it is a full virtual machine requiring no dependencies, it is capable of loading multiple OS made in either .py (python) or .vasm (Virtual Assembly). (NOTE: Learn more about .vasm from PVCpu)

It has a BIOS, it is capable of loading a 512-byte or less .vasm/.py file with AA55 signature. If it is a .py file it is run in complete restriction and can call the BIOS via -
```python
__int__(code:int)
```

PENV also has GUI capabilites and Driver support. (NOTE: Currently remapping the entire FileSystem so please wait till it is ready!)

PENV provides AOS:PENV by default, it is an OS that uses CLI and can run .aosf (AOS Executable File) and .caosf (Compressed AOS Executable File).

You can upgrade to AOS++:PENV for free but it will use more resources. It will provide GUI support and even Extension support.

<a id="phardwareitk.PENV.os"></a>

## os

<a id="phardwareitk.PENV.sys"></a>

## sys

<a id="phardwareitk.PENV.subprocess"></a>

## subprocess

<a id="phardwareitk.PENV.base_path"></a>

#### base\_path

<a id="phardwareitk.PENV.module_path"></a>

#### module\_path

<a id="phardwareitk.PENV.memory"></a>

## memory

<a id="phardwareitk.PENV.*"></a>

## \*

<a id="phardwareitk.PENV.*"></a>

## \*

<a id="phardwareitk.PENV.*"></a>

## \*

<a id="phardwareitk.PENV.*"></a>

## \*

<a id="phardwareitk.PENV.*"></a>

## \*

<a id="phardwareitk.PENV.PBFS_DISK"></a>

#### PBFS\_DISK

<a id="phardwareitk.PENV.force_os"></a>

#### force\_os

```python
def force_os(_os: str, posix_based_os: bool = False) -> None
```

Forces a OS so that the script will follow that specific os

**Arguments**:

- `_os` _str_ - The OS you want to force.

<a id="phardwareitk.PENV.copy_folder_to_pbfs"></a>

#### copy\_folder\_to\_pbfs

```python
def copy_folder_to_pbfs(pbfs,
                        folder_path: str,
                        reserved_size: int = 0,
                        permissions: tuple = (1, 1, 1, 1, 0, 0, 1, 0))
```

Recursively copies a folder into PBFS.

**Arguments**:

- `pbfs` _PBFS_ - The mounted PBFS instance.
- `folder_path` _str_ - Path to the folder to copy.
- `reserved_size` _int_ - Extra space to reserve per file.
- `permissions` _tuple_ - Permissions to apply to all files.

<a id="phardwareitk.PENV.start_penv"></a>

#### start\_penv

```python
def start_penv(max_ram_bytes: int = 2 * 1000000,
               process_ram_size: int = 1 * 1000000,
               command_py: str = "python",
               bheight: int = 500,
               bwidth: int = 800,
               bdepth: int = 3,
               total_blocks: int = 2048,
               block_size: int = 512,
               disk_name: str = "PheonixSSD",
               include_uefi: bool = True,
               format_drive: bool = False,
               os: str = "") -> None
```

Starts Pheonix Virtual Environment

<a id="phardwareitk.PENV.bios"></a>

# phardwareitk.PENV.bios

<a id="phardwareitk.PENV.bios.os"></a>

## os

<a id="phardwareitk.PENV.bios.sys"></a>

## sys

<a id="phardwareitk.PENV.bios.struct"></a>

## struct

<a id="phardwareitk.PENV.bios.*"></a>

## \*

<a id="phardwareitk.PENV.bios.PBFS_HEADER"></a>

## PBFS\_HEADER

<a id="phardwareitk.PENV.bios.Mem"></a>

## Mem

<a id="phardwareitk.PENV.bios.*"></a>

## \*

<a id="phardwareitk.PENV.bios.Framebuffer"></a>

## Framebuffer

<a id="phardwareitk.PENV.bios.PBFS"></a>

## PBFS

<a id="phardwareitk.PENV.bios.SystemData"></a>

#### SystemData

<a id="phardwareitk.PENV.bios.drive_data"></a>

#### drive\_data

<a id="phardwareitk.PENV.bios.DRIVE_PATH"></a>

#### DRIVE\_PATH

<a id="phardwareitk.PENV.bios.DRIVE_FOLDER"></a>

#### DRIVE\_FOLDER

<a id="phardwareitk.PENV.bios.GetSystemInfoBIOS"></a>

#### GetSystemInfoBIOS

```python
def GetSystemInfoBIOS() -> None
```

Gets System Info

<a id="phardwareitk.PENV.bios.get_drive_data"></a>

#### get\_drive\_data

```python
def get_drive_data() -> int
```

<a id="phardwareitk.PENV.bios.search_for_bootloader"></a>

#### search\_for\_bootloader

```python
def search_for_bootloader() -> str
```

Searches for the bootloader in the drive data directory.

<a id="phardwareitk.PENV.bios.run_bootloader"></a>

#### run\_bootloader

```python
def run_bootloader(file_path: str, mem: Mem.Memory, bios_ram_start_addr: int,
                   fb: Framebuffer) -> tuple
```

<a id="phardwareitk.PENV.bios.start"></a>

#### start

```python
def start() -> str
```

<a id="phardwareitk.Memory._platform._win32"></a>

# phardwareitk.Memory.\_platform.\_win32

<a id="phardwareitk.Memory._platform._win32.sys"></a>

## sys

<a id="phardwareitk.Memory._platform._win32.threading"></a>

## threading

<a id="phardwareitk.Memory._platform._win32.inspect"></a>

## inspect

<a id="phardwareitk.Memory._platform._win32.queue"></a>

## queue

<a id="phardwareitk.Memory._platform._win32.socket"></a>

## socket

<a id="phardwareitk.Memory._platform._win32.MemBlock"></a>

## MemBlock Objects

```python
class MemBlock()
```

A Memory Block class used to define protected sections of RAM (Virtual RAM)

<a id="phardwareitk.Memory._platform._win32.MemBlock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int, access: list[str], name: str = "BLOCK", seek: int = 0)
```

Init func

**Arguments**:

- `size` _int_ - The size of the protected region in bytes.
- `access` _str_ - The __file__ variable of the file that can access this region.
- `name` _str, optional_ - Name of the region. Defaults to "BLOCK".
- `seek` _int, optional_ - Address where the region starts. Defaults to 0.

<a id="phardwareitk.Memory._platform._win32.Process_Data"></a>

## Process\_Data Objects

```python
class Process_Data()
```

A Class for VRam Mapping Data for processes

<a id="phardwareitk.Memory._platform._win32.Process_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(Pid: int, process: object, *params)
```

The init func

**Arguments**:

- `Pid` _int_ - The Unique ID given to every func (Process ID).
- `process` _object_ - The function to run as a process.
- `*params` - Params to the process.

<a id="phardwareitk.Memory._platform._win32.Execution_Data"></a>

## Execution\_Data Objects

```python
class Execution_Data()
```

Execution Data Class

<a id="phardwareitk.Memory._platform._win32.Execution_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(heap_size: int = 6,
             stack_size: int = 6,
             heap_reserve: int = 1,
             stack_reserve: int = 1,
             data_size: int = 8) -> None
```

Init func

**Arguments**:

- `heap_size` _int, optional_ - MAX Heap size including Heap Reserve in bytes. Defaults to 6.
- `stack_size` _int, optional_ - MAX Stack size including Stack Reserve in bytes. Defaults to 6.
- `heap_reserve` _int, optional_ - Reserved Heap in bytes. Defaults to 1.
- `stack_reserve` _int, optional_ - Reserved Stack in bytes. Defaults to 1.
- `data_size` _int, optional_ - Size of initialized data in bytes. Defaults to 8.

<a id="phardwareitk.Memory._platform._win32.Memory"></a>

## Memory Objects

```python
class Memory()
```

A Memory Class.

Memory Layout ->

System Memory -> 64 bytes (Blocked)

Process Memory -> User-Defined, Default 64 bytes (Open)

-- Program Memory (Virtual Memory) -> Per Process , User - Defined (Blocked)

Rest of the Memory -> User-Defined (Open)

<a id="phardwareitk.Memory._platform._win32.Memory.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int,
             proc_sector_size: int = 64,
             Block: list[MemBlock] = None,
             debug: bool = False) -> None
```

Initialization function.
NOTE: RAM in this class refers to a part of mapped RAM known as Virtual Memory that every program has.

**Arguments**:

- `size` _int_ - The size of RAM in bytes.
- `proc_sector_size` _int_ - The size of RAM dedicated to processes in bytes. Defaults to 64.
- `Block` _list[MemBlock]_ - The protected regions if any. Defaults to None.

<a id="phardwareitk.Memory._platform._win32.Memory.write_ram"></a>

#### write\_ram

```python
def write_ram(data: bytes, addr: int = None, size: int = 0) -> bool
```

Writes data to a address. If addr is None, writes data at current addr. Size argument if present just appends data with 0

<a id="phardwareitk.Memory._platform._win32.Memory.get_ram"></a>

#### get\_ram

```python
def get_ram(size: int, addr: int = None) -> bytes
```

Gets data from a part of RAM

**Arguments**:

- `size` _int_ - The size of data to get
- `addr` _int, optional_ - The address of data (start). If None, uses current address. Defaults to None.
  

**Returns**:

- `bytes` - The retrieved data

<a id="phardwareitk.Memory._platform._win32.serialize"></a>

#### serialize

```python
def serialize(self) -> str
```

<a id="phardwareitk.Memory._platform._win32.Process"></a>

## Process Objects

```python
class Process()
```

A Class for the Proc Handling (DO NOT USE!)

<a id="phardwareitk.Memory._platform._win32.Process.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory,
             exec_data: Execution_Data,
             ProcessData: Process_Data,
             addr: int = 0) -> None
```

Init func

<a id="phardwareitk.Memory._platform._win32.Process.__setattr__"></a>

#### \_\_setattr\_\_

```python
def __setattr__(name: str, value: int)
```

<a id="phardwareitk.Memory._platform._win32.Process.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

<a id="phardwareitk.Memory._platform._win32.Process_Manager"></a>

## Process\_Manager Objects

```python
class Process_Manager()
```

Process Handling with Scheduling

<a id="phardwareitk.Memory._platform._win32.Process_Manager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory)
```

<a id="phardwareitk.Memory._platform._win32.Process_Manager.add_proc"></a>

#### add\_proc

```python
def add_proc(exec_data: Execution_Data, process_data: Process_Data) -> None
```

Create and Add a New Process

<a id="phardwareitk.Memory._platform._win32.Process_Manager.run_next"></a>

#### run\_next

```python
def run_next() -> None
```

Execute Next Process in Queue

<a id="phardwareitk.Memory._platform._win32.Process_Manager.stop_proc"></a>

#### stop\_proc

```python
def stop_proc(pid: int)
```

Stop Running process

<a id="phardwareitk.Memory._platform._win32.Process_Manager.start_debug_server"></a>

#### start\_debug\_server

```python
def start_debug_server(host: str = "127.0.0.1", port: int = 65432) -> None
```

Start a TCP server in a background thread to serve debug commands.

<a id="phardwareitk.Memory._platform._posix"></a>

# phardwareitk.Memory.\_platform.\_posix

<a id="phardwareitk.Memory._platform._posix.sys"></a>

## sys

<a id="phardwareitk.Memory._platform._posix.threading"></a>

## threading

<a id="phardwareitk.Memory._platform._posix.inspect"></a>

## inspect

<a id="phardwareitk.Memory._platform._posix.queue"></a>

## queue

<a id="phardwareitk.Memory._platform._posix.socket"></a>

## socket

<a id="phardwareitk.Memory._platform._posix.MemBlock"></a>

## MemBlock Objects

```python
class MemBlock()
```

A Memory Block class used to define protected sections of RAM (Virtual RAM)

<a id="phardwareitk.Memory._platform._posix.MemBlock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int, access: list[str], name: str = "BLOCK", seek: int = 0)
```

Init func

**Arguments**:

- `size` _int_ - The size of the protected region in bytes.
- `access` _str_ - The __file__ variable of the file that can access this region.
- `name` _str, optional_ - Name of the region. Defaults to "BLOCK".
- `seek` _int, optional_ - Address where the region starts. Defaults to 0.

<a id="phardwareitk.Memory._platform._posix.Process_Data"></a>

## Process\_Data Objects

```python
class Process_Data()
```

A Class for VRam Mapping Data for processes

<a id="phardwareitk.Memory._platform._posix.Process_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(Pid: int, process: object, *params)
```

The init func

**Arguments**:

- `Pid` _int_ - The Unique ID given to every func (Process ID).
- `process` _object_ - The function to run as a process.
- `*params` - Params to the process.

<a id="phardwareitk.Memory._platform._posix.Execution_Data"></a>

## Execution\_Data Objects

```python
class Execution_Data()
```

Execution Data Class

<a id="phardwareitk.Memory._platform._posix.Execution_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(heap_size: int = 6,
             stack_size: int = 6,
             heap_reserve: int = 1,
             stack_reserve: int = 1,
             data_size: int = 8) -> None
```

Init func

**Arguments**:

- `heap_size` _int, optional_ - MAX Heap size including Heap Reserve in bytes. Defaults to 6.
- `stack_size` _int, optional_ - MAX Stack size including Stack Reserve in bytes. Defaults to 6.
- `heap_reserve` _int, optional_ - Reserved Heap in bytes. Defaults to 1.
- `stack_reserve` _int, optional_ - Reserved Stack in bytes. Defaults to 1.
- `data_size` _int, optional_ - Size of initialized data in bytes. Defaults to 8.

<a id="phardwareitk.Memory._platform._posix.Memory"></a>

## Memory Objects

```python
class Memory()
```

A Memory Class.

Memory Layout ->

System Memory -> 64 bytes (Blocked)

Process Memory -> User-Defined, Default 64 bytes (Open)

-- Program Memory (Virtual Memory) -> Per Process , User - Defined (Blocked)

Rest of the Memory -> User-Defined (Open)

<a id="phardwareitk.Memory._platform._posix.Memory.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int,
             proc_sector_size: int = 64,
             Block: list[MemBlock] = None,
             debug: bool = False) -> None
```

Initialization function.
NOTE: RAM in this class refers to a part of mapped RAM known as Virtual Memory that every program has.

**Arguments**:

- `size` _int_ - The size of RAM in bytes.
- `proc_sector_size` _int_ - The size of RAM dedicated to processes in bytes. Defaults to 64.
- `Block` _list[MemBlock]_ - The protected regions if any. Defaults to None.

<a id="phardwareitk.Memory._platform._posix.Memory.write_ram"></a>

#### write\_ram

```python
def write_ram(data: bytes, addr: int = None, size: int = 0) -> bool
```

Writes data to a address. If addr is None, writes data at current addr. Size argument if present just appends data with 0

<a id="phardwareitk.Memory._platform._posix.Memory.get_ram"></a>

#### get\_ram

```python
def get_ram(size: int, addr: int = None) -> bytes
```

Gets data from a part of RAM

**Arguments**:

- `size` _int_ - The size of data to get
- `addr` _int, optional_ - The address of data (start). If None, uses current address. Defaults to None.
  

**Returns**:

- `bytes` - The retrieved data

<a id="phardwareitk.Memory._platform._posix.Memory.serialize"></a>

#### serialize

```python
def serialize() -> str
```

<a id="phardwareitk.Memory._platform._posix.Process"></a>

## Process Objects

```python
class Process()
```

A Class for the Proc Handling (DO NOT USE!)

<a id="phardwareitk.Memory._platform._posix.Process.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory,
             exec_data: Execution_Data,
             ProcessData: Process_Data,
             addr: int = 0) -> None
```

Init func

<a id="phardwareitk.Memory._platform._posix.Process.__setattr__"></a>

#### \_\_setattr\_\_

```python
def __setattr__(name: str, value: int)
```

<a id="phardwareitk.Memory._platform._posix.Process.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

<a id="phardwareitk.Memory._platform._posix.Process_Manager"></a>

## Process\_Manager Objects

```python
class Process_Manager()
```

Process Handling with Scheduling

<a id="phardwareitk.Memory._platform._posix.Process_Manager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory)
```

<a id="phardwareitk.Memory._platform._posix.Process_Manager.add_proc"></a>

#### add\_proc

```python
def add_proc(exec_data: Execution_Data, process_data: Process_Data) -> None
```

Create and Add a New Process

<a id="phardwareitk.Memory._platform._posix.Process_Manager.run_next"></a>

#### run\_next

```python
def run_next() -> None
```

Execute Next Process in Queue

<a id="phardwareitk.Memory._platform._posix.Process_Manager.stop_proc"></a>

#### stop\_proc

```python
def stop_proc(pid: int)
```

Stop Running process

<a id="phardwareitk.Memory._platform._posix.Process_Manager.start_debug_server"></a>

#### start\_debug\_server

```python
def start_debug_server(host: str = "127.0.0.1", port: int = 65432) -> None
```

Start a TCP server in a background thread to serve debug commands.

<a id="phardwareitk.Memory._platform"></a>

# phardwareitk.Memory.\_platform

This is a backend area of the module, DO NOT USE!

<a id="phardwareitk.Memory"></a>

# phardwareitk.Memory

Memory Allocation and such functions for python.

<a id="phardwareitk.Memory.platform"></a>

## platform

<a id="phardwareitk.Memory.os"></a>

## os

<a id="phardwareitk.Memory.sys"></a>

## sys

<a id="phardwareitk.Memory.module_path"></a>

#### module\_path

<a id="phardwareitk.Memory.os_"></a>

#### os\_

<a id="phardwareitk.Memory.os_"></a>

#### os\_

<a id="phardwareitk.Memory.win32"></a>

#### win32

<a id="phardwareitk.Memory.posix"></a>

#### posix

<a id="phardwareitk.Memory.unknown"></a>

#### unknown

<a id="phardwareitk.Memory.posix_os"></a>

#### posix\_os

<a id="phardwareitk.Memory.force_os"></a>

#### force\_os

```python
def force_os(_os: str, posix_based_os: bool = False) -> None
```

Forces a OS so that the script will follow that specific os

**Arguments**:

- `_os` _str_ - The OS you want to force.

<a id="phardwareitk.Memory.Memory"></a>

# phardwareitk.Memory.Memory

<a id="phardwareitk.Memory.Memory.sys"></a>

## sys

<a id="phardwareitk.Memory.Memory.threading"></a>

## threading

<a id="phardwareitk.Memory.Memory.inspect"></a>

## inspect

<a id="phardwareitk.Memory.Memory.queue"></a>

## queue

<a id="phardwareitk.Memory.Memory.socket"></a>

## socket

<a id="phardwareitk.Memory.Memory.MemBlock"></a>

## MemBlock Objects

```python
class MemBlock()
```

A Memory Block class used to define protected sections of RAM (Virtual RAM)

<a id="phardwareitk.Memory.Memory.MemBlock.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int, access: list[str], name: str = "BLOCK", seek: int = 0)
```

Init func

**Arguments**:

- `size` _int_ - The size of the protected region in bytes.
- `access` _str_ - The __file__ variable of the file that can access this region.
- `name` _str, optional_ - Name of the region. Defaults to "BLOCK".
- `seek` _int, optional_ - Address where the region starts. Defaults to 0.

<a id="phardwareitk.Memory.Memory.Process_Data"></a>

## Process\_Data Objects

```python
class Process_Data()
```

A Class for VRam Mapping Data for processes

<a id="phardwareitk.Memory.Memory.Process_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(Pid: int, process: object, *params)
```

The init func

**Arguments**:

- `Pid` _int_ - The Unique ID given to every func (Process ID).
- `process` _object_ - The function to run as a process.
- `*params` - Params to the process.

<a id="phardwareitk.Memory.Memory.Execution_Data"></a>

## Execution\_Data Objects

```python
class Execution_Data()
```

Execution Data Class

<a id="phardwareitk.Memory.Memory.Execution_Data.__init__"></a>

#### \_\_init\_\_

```python
def __init__(heap_size: int = 6,
             stack_size: int = 6,
             heap_reserve: int = 1,
             stack_reserve: int = 1,
             data_size: int = 8) -> None
```

Init func

**Arguments**:

- `heap_size` _int, optional_ - MAX Heap size including Heap Reserve in bytes. Defaults to 6.
- `stack_size` _int, optional_ - MAX Stack size including Stack Reserve in bytes. Defaults to 6.
- `heap_reserve` _int, optional_ - Reserved Heap in bytes. Defaults to 1.
- `stack_reserve` _int, optional_ - Reserved Stack in bytes. Defaults to 1.
- `data_size` _int, optional_ - Size of initialized data in bytes. Defaults to 8.

<a id="phardwareitk.Memory.Memory.Memory"></a>

## Memory Objects

```python
class Memory()
```

A Memory Class.

Memory Layout ->

System Memory -> 64 bytes (Blocked)

Process Memory -> User-Defined, Default 64 bytes (Open)

-- Program Memory (Virtual Memory) -> Per Process , User - Defined (Blocked)

Rest of the Memory -> User-Defined (Open)

<a id="phardwareitk.Memory.Memory.Memory.__init__"></a>

#### \_\_init\_\_

```python
def __init__(size: int,
             proc_sector_size: int = 64,
             Block: list[MemBlock] = None,
             debug: bool = False,
             system_size: int = 64) -> None
```

Initialization function.
NOTE: RAM in this class refers to a part of mapped RAM known as Virtual Memory that every program has.

**Arguments**:

- `size` _int_ - The size of RAM in bytes.
- `proc_sector_size` _int_ - The size of RAM dedicated to processes in bytes. Defaults to 64.
- `Block` _list[MemBlock]_ - The protected regions if any. Defaults to None.

<a id="phardwareitk.Memory.Memory.Memory.write_ram"></a>

#### write\_ram

```python
def write_ram(data: bytes, addr: int = None, size: int = 0) -> bool
```

Writes data to a address. If addr is None, writes data at current addr. Size argument if present just appends data with 0

<a id="phardwareitk.Memory.Memory.Memory.get_ram"></a>

#### get\_ram

```python
def get_ram(size: int, addr: int = None) -> bytes
```

Gets data from a part of RAM

**Arguments**:

- `size` _int_ - The size of data to get
- `addr` _int, optional_ - The address of data (start). If None, uses current address. Defaults to None.
  

**Returns**:

- `bytes` - The retrieved data

<a id="phardwareitk.Memory.Memory.Memory.serialize"></a>

#### serialize

```python
def serialize() -> str
```

<a id="phardwareitk.Memory.Memory.Process"></a>

## Process Objects

```python
class Process()
```

A Class for the Proc Handling (DO NOT USE!)

<a id="phardwareitk.Memory.Memory.Process.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory,
             exec_data: Execution_Data,
             ProcessData: Process_Data,
             addr: int = 0) -> None
```

Init func

<a id="phardwareitk.Memory.Memory.Process.__setattr__"></a>

#### \_\_setattr\_\_

```python
def __setattr__(name: str, value: int)
```

<a id="phardwareitk.Memory.Memory.Process.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

<a id="phardwareitk.Memory.Memory.Process_Manager"></a>

## Process\_Manager Objects

```python
class Process_Manager()
```

Process Handling with Scheduling

<a id="phardwareitk.Memory.Memory.Process_Manager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mem: Memory)
```

<a id="phardwareitk.Memory.Memory.Process_Manager.add_proc"></a>

#### add\_proc

```python
def add_proc(exec_data: Execution_Data, process_data: Process_Data) -> None
```

Create and Add a New Process

<a id="phardwareitk.Memory.Memory.Process_Manager.run_next"></a>

#### run\_next

```python
def run_next() -> None
```

Execute Next Process in Queue

<a id="phardwareitk.Memory.Memory.Process_Manager.stop_proc"></a>

#### stop\_proc

```python
def stop_proc(pid: int)
```

Stop Running process

<a id="phardwareitk.Memory.Memory.Process_Manager.start_debug_server"></a>

#### start\_debug\_server

```python
def start_debug_server(host: str = "127.0.0.1", port: int = 65432) -> None
```

Start a TCP server in a background thread to serve debug commands.

<a id="phardwareitk.ErrorSystem.ErrorSystem"></a>

# phardwareitk.ErrorSystem.ErrorSystem

<a id="phardwareitk.ErrorSystem.ErrorSystem.*"></a>

## \*

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITKException"></a>

## PHardwareITKException Objects

```python
class PHardwareITKException(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITKException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_RuntimeError"></a>

## PHardwareITK\_RuntimeError Objects

```python
class PHardwareITK_RuntimeError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_RuntimeError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_NotSupportedError"></a>

## PHardwareITK\_NotSupportedError Objects

```python
class PHardwareITK_NotSupportedError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_NotSupportedError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_ValueError"></a>

## PHardwareITK\_ValueError Objects

```python
class PHardwareITK_ValueError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_ValueError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_ParserError"></a>

## PHardwareITK\_ParserError Objects

```python
class PHardwareITK_ParserError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_ParserError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_SettingsError"></a>

## PHardwareITK\_SettingsError Objects

```python
class PHardwareITK_SettingsError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_SettingsError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_FileError"></a>

## PHardwareITK\_FileError Objects

```python
class PHardwareITK_FileError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_FileError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_FileNotFoundError"></a>

## PHardwareITK\_FileNotFoundError Objects

```python
class PHardwareITK_FileNotFoundError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_FileNotFoundError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_IOError"></a>

## PHardwareITK\_IOError Objects

```python
class PHardwareITK_IOError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PHardwareITK_IOError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixException"></a>

## PheonixException Objects

```python
class PheonixException(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixException.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixFileNotFoundError"></a>

## PheonixFileNotFoundError Objects

```python
class PheonixFileNotFoundError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixFileNotFoundError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixInternalError"></a>

## PheonixInternalError Objects

```python
class PheonixInternalError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixInternalError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixValuerError"></a>

## PheonixValuerError Objects

```python
class PheonixValuerError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixValuerError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixArgumentError"></a>

## PheonixArgumentError Objects

```python
class PheonixArgumentError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixArgumentError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixSettingsError"></a>

## PheonixSettingsError Objects

```python
class PheonixSettingsError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixSettingsError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixObjectError"></a>

## PheonixObjectError Objects

```python
class PheonixObjectError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixObjectError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixOsError"></a>

## PheonixOsError Objects

```python
class PheonixOsError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixOsError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixOsVersionError"></a>

## PheonixOsVersionError Objects

```python
class PheonixOsVersionError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixOsVersionError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixVersionNotSupported"></a>

## PheonixVersionNotSupported Objects

```python
class PheonixVersionNotSupported(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixVersionNotSupported.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixUnknownVersion"></a>

## PheonixUnknownVersion Objects

```python
class PheonixUnknownVersion(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixUnknownVersion.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixUnknownSetting"></a>

## PheonixUnknownSetting Objects

```python
class PheonixUnknownSetting(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixUnknownSetting.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixIOError"></a>

## PheonixIOError Objects

```python
class PheonixIOError(Exception)
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.PheonixIOError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.CustomError"></a>

## CustomError Objects

```python
class CustomError(Exception)
```

Custom Error

**Arguments**:

- `name` _str_ - The name of the Exception.
- `message` _str_ - The message displayed.
- `*args` _Any_ - Other Arguments.
  
  Calls:
  Exception

<a id="phardwareitk.ErrorSystem.ErrorSystem.CustomError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.CustomError.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="phardwareitk.ErrorSystem.ErrorSystem.RunCustomError"></a>

## RunCustomError Objects

```python
class RunCustomError()
```

Run Custom Error

**Arguments**:

- `name` _str_ - The name of the Exception.
- `message` _str_ - The message displayed.
- `*args` _Any_ - Other Arguments.
  
  Calls:
  CustomError -> Exception
  
- `NOTE` - Same as Custom Error.

<a id="phardwareitk.ErrorSystem.ErrorSystem.RunCustomError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, message: str = "", *args) -> None
```

<a id="phardwareitk.ErrorSystem"></a>

# phardwareitk.ErrorSystem

Many Prebuilt and Custom Errors (You can create one using this also)

<a id="phardwareitk.ErrorSystem.os"></a>

## os

<a id="phardwareitk.ErrorSystem.sys"></a>

## sys

<a id="phardwareitk.ErrorSystem.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.ErrorSystem.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.FileSystem.FileSystem"></a>

# phardwareitk.FileSystem.FileSystem

<a id="phardwareitk.FileSystem.FileSystem.os"></a>

## os

<a id="phardwareitk.FileSystem.FileSystem.sys"></a>

## sys

<a id="phardwareitk.FileSystem.FileSystem.binascii"></a>

## binascii

<a id="phardwareitk.FileSystem.FileSystem.json"></a>

## json

<a id="phardwareitk.FileSystem.FileSystem.Cipher"></a>

## Cipher

<a id="phardwareitk.FileSystem.FileSystem.algorithms"></a>

## algorithms

<a id="phardwareitk.FileSystem.FileSystem.modes"></a>

## modes

<a id="phardwareitk.FileSystem.FileSystem.padding"></a>

## padding

<a id="phardwareitk.FileSystem.FileSystem.default_backend"></a>

## default\_backend

<a id="phardwareitk.FileSystem.FileSystem.*"></a>

## \*

<a id="phardwareitk.FileSystem.FileSystem.LIB"></a>

## LIB

<a id="phardwareitk.FileSystem.FileSystem.ES"></a>

## ES

<a id="phardwareitk.FileSystem.FileSystem.*"></a>

## \*

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem"></a>

## BasicFileSystem Objects

```python
class BasicFileSystem()
```

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.CreateFile"></a>

#### CreateFile

```python
@staticmethod
def CreateFile(filePath: str, data: Union[str, dict, int]) -> tuple[bool, str]
```

Creates a new file with the provided data.

**Arguments**:

- `filePath` _str_ - The path to the file to be created.
  date (Union[str, dict, int]) : The data to be inserted into the file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The Error if success was False.
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during creation.
- `PheonixIOError` - If an Input/Output Error occurs during creation.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.AppendFile"></a>

#### AppendFile

```python
@staticmethod
def AppendFile(filePath: str,
               data: Union[str, int, dict],
               seek: Union[None, int] = None) -> tuple[bool, str]
```

Appends the data to the given filePath

**Arguments**:

- `filePath` _str_ - The path to the file to append.
- `data` _Union[str, int, dict]_ - The data to append in the file.
  seek (Optional) (Union[None, int]): The seek position. 'None' means to append at the end of the file. Defaults to None.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The Error if success was False
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during creation.
- `PheonixIOError` - If an Input/Output Error occurs during creation.
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.ReadFile"></a>

#### ReadFile

```python
@staticmethod
def ReadFile(filePath: str) -> tuple[bool, Union[str, None]]
```

Reads the content of the file.

**Arguments**:

- `filePath` _str_ - The path to the file to read.
  

**Returns**:

  tuple[bool, Union[str, None]] ->
- `bool` - True if successful, False otherwise.
- `str` - The content of the file if successful, or error message if not.
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during reading.
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.DeleteFile"></a>

#### DeleteFile

```python
@staticmethod
def DeleteFile(filePath: str) -> tuple[bool, str]
```

Deletes the specified file.

**Arguments**:

- `filePath` _str_ - The path to the file to delete.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.RenameFile"></a>

#### RenameFile

```python
@staticmethod
def RenameFile(oldPath: str, newPath: str) -> tuple[bool, str]
```

Renames a file from `oldPath` to `newPath`.

**Arguments**:

- `oldPath` _str_ - The current path of the file to rename.
- `newPath` _str_ - The new name/path of the file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.FileExists"></a>

#### FileExists

```python
@staticmethod
def FileExists(filePath: str) -> tuple[bool, str]
```

Checks if the file exists at the specified path.

**Arguments**:

- `filePath` _str_ - The path to check.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if the file exists, False otherwise.
- `str` - An appropriate message.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.GetFileSize"></a>

#### GetFileSize

```python
@staticmethod
def GetFileSize(filePath: str) -> tuple[bool, Union[int, str]]
```

Returns the size of the specified file.

**Arguments**:

- `filePath` _str_ - The path to the file.
  

**Returns**:

  tuple[bool, Union[int, str]] ->
- `bool` - True if successful, False otherwise.
- `int` - The size of the file in bytes if successful.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.CopyFile"></a>

#### CopyFile

```python
@staticmethod
def CopyFile(srcPath: str, destPath: str) -> tuple[bool, str]
```

Copies a file from the source path to the destination path.

**Arguments**:

- `srcPath` _str_ - The source file path.
- `destPath` _str_ - The destination file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the source file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.MoveFile"></a>

#### MoveFile

```python
@staticmethod
def MoveFile(srcPath: str, destPath: str) -> tuple[bool, str]
```

Moves a file from the source path to the destination path.

**Arguments**:

- `srcPath` _str_ - The source file path.
- `destPath` _str_ - The destination file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the source file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.BasicFileSystem.CreateDirectory"></a>

#### CreateDirectory

```python
@staticmethod
def CreateDirectory(dirPath: str) -> tuple[bool, str]
```

Creates a directory at the specified path.

**Arguments**:

- `dirPath` _str_ - The path where the directory will be created.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem"></a>

## JsonFileSystem Objects

```python
class JsonFileSystem()
```

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.CreateJsonFile"></a>

#### CreateJsonFile

```python
@staticmethod
def CreateJsonFile(filePath: str, data: Union[dict, list]) -> tuple[bool, str]
```

Creates a new JSON file with the provided data.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be created.
- `data` _Union[dict, list]_ - The data to be inserted into the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixException` - If an unknown error occurs during file creation.
- `PheonixIOError` - If there is an input/output error during file creation.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.AppendJsonData"></a>

#### AppendJsonData

```python
@staticmethod
def AppendJsonData(filePath: str, data: Union[dict, list]) -> tuple[bool, str]
```

Appends data to an existing JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to append data.
- `data` _Union[dict, list]_ - The data to be appended.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the file is not found.
- `PheonixIOError` - If an input/output error occurs.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.ReadJsonFile"></a>

#### ReadJsonFile

```python
@staticmethod
def ReadJsonFile(filePath: str) -> tuple[bool, Union[dict, list, str]]
```

Reads data from a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[dict, list, str]] ->
- `bool` - True if successful, False otherwise.
- `dict/list` - The contents of the file if successful, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file not found.
- `PheonixIOError` - If an input/output error occurs.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.DeleteJsonFile"></a>

#### DeleteJsonFile

```python
@staticmethod
def DeleteJsonFile(filePath: str) -> tuple[bool, str]
```

Deletes a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be deleted.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.FileExists"></a>

#### FileExists

```python
@staticmethod
def FileExists(filePath: str) -> bool
```

Checks if the JSON file exists.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

- `bool` - True if the file exists, False otherwise.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.GetJsonKeys"></a>

#### GetJsonKeys

```python
@staticmethod
def GetJsonKeys(filePath: str) -> tuple[bool, Union[list, str]]
```

Returns all keys in a JSON file (if it is a JSON object).

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[list, str]] ->
- `bool` - True if successful, False otherwise.
- `list` - List of keys if file is a dictionary, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.GetJsonFileSize"></a>

#### GetJsonFileSize

```python
@staticmethod
def GetJsonFileSize(filePath: str) -> tuple[bool, Union[int, str]]
```

Returns the size of the JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[int, str]] ->
- `bool` - True if successful, False otherwise.
- `int` - File size in bytes if successful, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.UpdateJsonKey"></a>

#### UpdateJsonKey

```python
@staticmethod
def UpdateJsonKey(filePath: str, key: str,
                  new_value: Union[str, int, dict, list]) -> tuple[bool, str]
```

Updates the value of a specific key in a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
- `key` _str_ - The key whose value needs to be updated.
- `new_value` _Union[str, int, dict, list]_ - The new value to update.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.ValidateJson"></a>

#### ValidateJson

```python
@staticmethod
def ValidateJson(filePath: str) -> tuple[bool, str]
```

Validates if a file is a valid JSON.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if valid, False otherwise.
- `str` - The error message if invalid.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file not found.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.GetJsonFileExtension"></a>

#### GetJsonFileExtension

```python
@staticmethod
def GetJsonFileExtension(filePath: str) -> tuple[bool, str]
```

Gets the file extension of a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The file extension ('.json') if successful, error message if not.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.MergeJsonFiles"></a>

#### MergeJsonFiles

```python
@staticmethod
def MergeJsonFiles(srcPath: str, destPath: str) -> tuple[bool, str]
```

Merges two JSON files.

**Arguments**:

- `srcPath` _str_ - The source JSON file path.
- `destPath` _str_ - The destination JSON file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If any file is not found.

<a id="phardwareitk.FileSystem.FileSystem.JsonFileSystem.CreateJsonBackup"></a>

#### CreateJsonBackup

```python
@staticmethod
def CreateJsonBackup(filePath: str) -> tuple[bool, str]
```

Creates a backup of a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be backed up.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem"></a>

## LowFileSystem Objects

```python
class LowFileSystem()
```

NOTE: For using majority of the functions in this class, please install GCC, LD, and NASM (Mingw64 or Msys2 UCRT64).
If you cannot install it. Please use PLTEC via Command Line Interface to convert any language syntax defined in a json file to Assembly or even Object (Undergoing development). But before making such a file please understand the file's syntax ->
    1. Include the convertion Os (ALL CAPS) and mode at the start of the json. Like -> 'ELF': '', 'x86': ''
    2. define a json inside the file with the key as 'SET'. Like -> '{'ELF': '', 'x86': '', 'SET': {}}'. The set is the point where all the syntax will go.
    3. NOTE: The syntax will work with the pre-made funcs in the DEF_LanguageSET.json. The syntax will have to be understood by the you if you want to add more funcs in it.
    4. Each Key in the 'SET' will have to have these required notes ->
        i. No spaces are allowed in the key
        ii. Include /S at the end of the key. And after the /S please include a sperator that will be used to seperate the key. Commomly used -> ' '.
        iii. Here are some important definitions ->
            a. /*DNAME: Specifies that at the specific location the user must type in the name of [something].
            b. /*DVALUE: Specifies that at the specific location the user must type in the value of [something].
            c. /*DSIZE: Specifies that at the specific location the user must type in the size of [something]. NOTE: DSIZE is a must in input function
    5. Inside the 'SET' please include a key:value pair with the value as 'includeFuncs'. This ensures all the neccarry functions will be imported if the user wrote the specific key.
    6. After that include whatever key you want as to be working with the syntax but please remember the 4.iii section. The definitions act as a parameter to the funcs and please openUP DEF_LanguageSET to see the parameters and funcs
    7. In the Value input the func you want to call if the specified key is displayed.

    EXAMPLE Lang.json -> '
    {
        "ELF": "",
        "x86": "",
        "SET": {
            "`include`:/*DVALUE/INCLUDEINS/S ": "includeFuncs",
            "BasicIO/INCLUDE": {
                "print:/*DVALUE/*DNAME/S ": "printINS",
                "input:/*DNAME/*DSIZE/S ": "inputINS",
                "clean:/S": "cleanupINS",
                "return:/*DVALUE/S ": "returnINS"
            }
        }
    }'

    Example Test.txt -> '
    `include`: BasicIO

    print: helloWorld HelloVariable
    clean:
    return: 0'

    Converted Assembly -> '
    section .data
    HelloVariable_pri db "helloWorld"
    HelloVariable_pri_LEN equ $ - HelloVariable_pri

    section .text
    global _start

    _start:
    mov ecx, HelloVariable_pri
    mov edx, HelloVariable_pri_LEN
    call print
    call cleanup32
    mov ebx, 0
    call return

    print:
    mov eax, 4
    mov ebx, 1
    int 80h

    input:
    mov eax, 3
    mov ebx, 1
    int 80h

    return:
    mov eax, 1
    int 80h

    cleanup32:
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
    xor esi, esi
    xor ebp, ebp
    ret
    '

    PLTEC has been updated and some changes in the DEF_lang.json might not bee understood. so please try using a AI to understand via the example provided.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CreateAsmFile"></a>

#### CreateAsmFile

```python
@staticmethod
def CreateAsmFile(filePath: str, asmContent: str) -> tuple[bool, str]
```

Creates a new ASM file with the provided ASM content.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.ReadAsmFile"></a>

#### ReadAsmFile

```python
@staticmethod
def ReadAsmFile(filePath: str) -> tuple[bool, str]
```

Reads content from an ASM file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CompileAsmToObject"></a>

#### CompileAsmToObject

```python
@staticmethod
def CompileAsmToObject(filePath: str) -> tuple[bool, str]
```

Compiles an ASM file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.DisassembleAsmFile"></a>

#### DisassembleAsmFile

```python
@staticmethod
def DisassembleAsmFile(filePath: str) -> tuple[bool, str]
```

Disassembles an ASM file to inspect the assembly instructions.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CreateAsmFromString"></a>

#### CreateAsmFromString

```python
@staticmethod
def CreateAsmFromString(asmCode: str, outputFile: str) -> tuple[bool, str]
```

Creates an ASM file from a string of ASM code.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CreateObjectFile"></a>

#### CreateObjectFile

```python
@staticmethod
def CreateObjectFile(filePath: str) -> tuple[bool, str]
```

Creates an object (.o) file from a C/C++ file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.LinkObjectFiles"></a>

#### LinkObjectFiles

```python
@staticmethod
def LinkObjectFiles(objFiles: list[str], outputFile: str) -> tuple[bool, str]
```

Links multiple object (.o) files into an executable.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.DisassembleObjectFile"></a>

#### DisassembleObjectFile

```python
@staticmethod
def DisassembleObjectFile(objFilePath: str) -> tuple[bool, str]
```

Disassembles an object file to inspect the assembly instructions.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CreateCFile"></a>

#### CreateCFile

```python
@staticmethod
def CreateCFile(filePath: str, cContent: str) -> tuple[bool, str]
```

Creates a new C file with the provided C code.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CompileCToObject"></a>

#### CompileCToObject

```python
@staticmethod
def CompileCToObject(filePath: str) -> tuple[bool, str]
```

Compiles a C file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CreateCppFile"></a>

#### CreateCppFile

```python
@staticmethod
def CreateCppFile(filePath: str, cppContent: str) -> tuple[bool, str]
```

Creates a new C++ file with the provided C++ code.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CompileCppToObject"></a>

#### CompileCppToObject

```python
@staticmethod
def CompileCppToObject(filePath: str) -> tuple[bool, str]
```

Compiles a C++ file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.CompileCPlusPlusFile"></a>

#### CompileCPlusPlusFile

```python
@staticmethod
def CompileCPlusPlusFile(filePath: str) -> tuple[bool, str]
```

Compiles a C++ file into an executable.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.ReadBinaryFile"></a>

#### ReadBinaryFile

```python
@staticmethod
def ReadBinaryFile(filePath: str) -> tuple[bool, bytes]
```

Reads data from a binary file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.WriteBinaryFile"></a>

#### WriteBinaryFile

```python
@staticmethod
def WriteBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]
```

Writes data to a binary file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.AppendBinaryFile"></a>

#### AppendBinaryFile

```python
@staticmethod
def AppendBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]
```

Appends data to a binary file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.GetBinaryFileSize"></a>

#### GetBinaryFileSize

```python
@staticmethod
def GetBinaryFileSize(filePath: str) -> tuple[bool, int]
```

Returns the size of a binary file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.EncryptFile"></a>

#### EncryptFile

```python
@staticmethod
def EncryptFile(filePath: str, key: bytes) -> tuple[bool, str]
```

Encrypts the content of a file using AES encryption.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.DecryptFile"></a>

#### DecryptFile

```python
@staticmethod
def DecryptFile(filePath: str, key: bytes) -> tuple[bool, str]
```

Decrypts an encrypted file.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.Base64EncodeFile"></a>

#### Base64EncodeFile

```python
@staticmethod
def Base64EncodeFile(filePath: str) -> tuple[bool, str]
```

Encodes a file in Base64 format.

<a id="phardwareitk.FileSystem.FileSystem.LowFileSystem.Base64DecodeFile"></a>

#### Base64DecodeFile

```python
@staticmethod
def Base64DecodeFile(filePath: str) -> tuple[bool, str]
```

Decodes a Base64 encoded file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem"></a>

## FileSystem Objects

```python
class FileSystem(BasicFileSystem, JsonFileSystem, LowFileSystem)
```

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateFile"></a>

#### CreateFile

```python
@staticmethod
def CreateFile(filePath: str, data: str) -> tuple[bool, str]
```

Creates a new file with the provided data.

**Arguments**:

- `filePath` _str_ - The path to the file to be created.
  date (Union[str, dict, int]) : The data to be inserted into the file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The Error if success was False.
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during creation.
- `PheonixIOError` - If an Input/Output Error occurs during creation.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.AppendFile"></a>

#### AppendFile

```python
@staticmethod
def AppendFile(filePath: str,
               data: Union[str, int, dict],
               seek: Optional[Union[None, int]] = None) -> tuple[bool, str]
```

Appends the data to the given filePath.

**Arguments**:

- `filePath` _str_ - The path to the file to append.
- `data` _Union[str, int, dict]_ - The data to append in the file.
  seek (Optional) (Union[None, int]): The seek position. 'None' means to append at the end of the file. Defaults to None.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The Error if success was False
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during creation.
- `PheonixIOError` - If an Input/Output Error occurs during creation.
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ReadFile"></a>

#### ReadFile

```python
@staticmethod
def ReadFile(filePath: str) -> tuple[bool, Union[str, None]]
```

Reads the content of the file.

**Arguments**:

- `filePath` _str_ - The path to the file to read.
  

**Returns**:

  tuple[bool, Union[str, None]] ->
- `bool` - True if successful, False otherwise.
- `str` - The content of the file if successful, or error message if not.
  
  Calls (Without raising):
- `PheonixException` - If an Unknown Error occurs during reading.
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.DeleteFile"></a>

#### DeleteFile

```python
@staticmethod
def DeleteFile(filePath: str) -> tuple[bool, str]
```

Deletes the specified file.

**Arguments**:

- `filePath` _str_ - The path to the file to delete.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.RenameFile"></a>

#### RenameFile

```python
@staticmethod
def RenameFile(oldPath: str, newPath: str) -> tuple[bool, str]
```

Renames a file from `oldPath` to `newPath`.

**Arguments**:

- `oldPath` _str_ - The current path of the file to rename.
- `newPath` _str_ - The new name/path of the file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.FileExists"></a>

#### FileExists

```python
@staticmethod
def FileExists(filePath: str) -> tuple[bool, str]
```

Checks if the file exists at the specified path.

**Arguments**:

- `filePath` _str_ - The path to check.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if the file exists, False otherwise.
- `str` - An appropriate message.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetFileSize"></a>

#### GetFileSize

```python
@staticmethod
def GetFileSize(filePath: str) -> tuple[bool, Union[int, str]]
```

Returns the size of the specified file.

**Arguments**:

- `filePath` _str_ - The path to the file.
  

**Returns**:

  tuple[bool, Union[int, str]] ->
- `bool` - True if successful, False otherwise.
- `int` - The size of the file in bytes if successful.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file was not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CopyFile"></a>

#### CopyFile

```python
@staticmethod
def CopyFile(srcPath: str, destPath: str) -> tuple[bool, str]
```

Copies a file from the source path to the destination path.

**Arguments**:

- `srcPath` _str_ - The source file path.
- `destPath` _str_ - The destination file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the source file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.MoveFile"></a>

#### MoveFile

```python
@staticmethod
def MoveFile(srcPath: str, destPath: str) -> tuple[bool, str]
```

Moves a file from the source path to the destination path.

**Arguments**:

- `srcPath` _str_ - The source file path.
- `destPath` _str_ - The destination file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the source file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateDirectory"></a>

#### CreateDirectory

```python
@staticmethod
def CreateDirectory(dirPath: str) -> tuple[bool, str]
```

Creates a directory at the specified path.

**Arguments**:

- `dirPath` _str_ - The path where the directory will be created.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateJsonFile"></a>

#### CreateJsonFile

```python
@staticmethod
def CreateJsonFile(filePath: str, data: Union[dict, list]) -> tuple[bool, str]
```

Creates a new JSON file with the provided data.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be created.
- `data` _Union[dict, list]_ - The data to be inserted into the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixException` - If an unknown error occurs during file creation.
- `PheonixIOError` - If there is an input/output error during file creation.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.AppendJsonData"></a>

#### AppendJsonData

```python
@staticmethod
def AppendJsonData(filePath: str, data: Union[dict, list]) -> tuple[bool, str]
```

Appends data to an existing JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to append data.
- `data` _Union[dict, list]_ - The data to be appended.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - Error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If the file is not found.
- `PheonixIOError` - If an input/output error occurs.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ReadJsonFile"></a>

#### ReadJsonFile

```python
@staticmethod
def ReadJsonFile(filePath: str) -> tuple[bool, Union[dict, list, str]]
```

Reads data from a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[dict, list, str]] ->
- `bool` - True if successful, False otherwise.
- `dict/list` - The contents of the file if successful, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file not found.
- `PheonixIOError` - If an input/output error occurs.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.DeleteJsonFile"></a>

#### DeleteJsonFile

```python
@staticmethod
def DeleteJsonFile(filePath: str) -> tuple[bool, str]
```

Deletes a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be deleted.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.FileExists"></a>

#### FileExists

```python
@staticmethod
def FileExists(filePath: str) -> bool
```

Checks if the JSON file exists.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

- `bool` - True if the file exists, False otherwise.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetJsonKeys"></a>

#### GetJsonKeys

```python
@staticmethod
def GetJsonKeys(filePath: str) -> tuple[bool, Union[list, str]]
```

Returns all keys in a JSON file (if it is a JSON object).

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[list, str]] ->
- `bool` - True if successful, False otherwise.
- `list` - List of keys if file is a dictionary, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetJsonFileSize"></a>

#### GetJsonFileSize

```python
@staticmethod
def GetJsonFileSize(filePath: str) -> tuple[bool, Union[int, str]]
```

Returns the size of the JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, Union[int, str]] ->
- `bool` - True if successful, False otherwise.
- `int` - File size in bytes if successful, error message if not.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.UpdateJsonKey"></a>

#### UpdateJsonKey

```python
@staticmethod
def UpdateJsonKey(filePath: str, key: str,
                  new_value: Union[str, int, dict, list]) -> tuple[bool, str]
```

Updates the value of a specific key in a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
- `key` _str_ - The key whose value needs to be updated.
- `new_value` _Union[str, int, dict, list]_ - The new value to update.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file does not exist.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ValidateJson"></a>

#### ValidateJson

```python
@staticmethod
def ValidateJson(filePath: str) -> tuple[bool, str]
```

Validates if a file is a valid JSON.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if valid, False otherwise.
- `str` - The error message if invalid.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If file not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetJsonFileExtension"></a>

#### GetJsonFileExtension

```python
@staticmethod
def GetJsonFileExtension(filePath: str) -> tuple[bool, str]
```

Gets the file extension of a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The file extension ('.json') if successful, error message if not.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.MergeJsonFiles"></a>

#### MergeJsonFiles

```python
@staticmethod
def MergeJsonFiles(srcPath: str, destPath: str) -> tuple[bool, str]
```

Merges two JSON files.

**Arguments**:

- `srcPath` _str_ - The source JSON file path.
- `destPath` _str_ - The destination JSON file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.
  
  Calls (Without raising):
- `PheonixFileNotFoundError` - If any file is not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateJsonBackup"></a>

#### CreateJsonBackup

```python
@staticmethod
def CreateJsonBackup(filePath: str) -> tuple[bool, str]
```

Creates a backup of a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file to be backed up.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.RenameJsonFile"></a>

#### RenameJsonFile

```python
@staticmethod
def RenameJsonFile(filePath: str, new_name: str) -> tuple[bool, str]
```

Renames an existing JSON file.

**Arguments**:

- `filePath` _str_ - The path to the existing JSON file.
- `new_name` _str_ - The new name for the file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetJsonFileInfo"></a>

#### GetJsonFileInfo

```python
@staticmethod
def GetJsonFileInfo(filePath: str) -> tuple[bool, str]
```

Gets the basic information (size, keys) about a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ReadJsonKey"></a>

#### ReadJsonKey

```python
@staticmethod
def ReadJsonKey(filePath: str,
                key: str) -> tuple[bool, Union[str, dict, list]]
```

Reads the value of a specific key from a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
- `key` _str_ - The key whose value needs to be read.
  

**Returns**:

  tuple[bool, Union[str, dict, list]] ->
- `bool` - True if successful, False otherwise.
- `str/dict/list` - The value of the key, or error message if not found.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.SetJsonKey"></a>

#### SetJsonKey

```python
@staticmethod
def SetJsonKey(filePath: str, key: str,
               value: Union[str, int, dict, list]) -> tuple[bool, str]
```

Sets the value of a specific key in a JSON file.

**Arguments**:

- `filePath` _str_ - The path to the JSON file.
- `key` _str_ - The key whose value needs to be set.
- `value` _Union[str, int, dict, list]_ - The value to set for the key.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateEmptyJson"></a>

#### CreateEmptyJson

```python
@staticmethod
def CreateEmptyJson(filePath: str) -> tuple[bool, str]
```

Creates an empty JSON file.

**Arguments**:

- `filePath` _str_ - The path where the empty JSON file will be created.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CopyJsonFile"></a>

#### CopyJsonFile

```python
@staticmethod
def CopyJsonFile(srcPath: str, destPath: str) -> tuple[bool, str]
```

Copies a JSON file to a new location.

**Arguments**:

- `srcPath` _str_ - The source JSON file path.
- `destPath` _str_ - The destination file path.
  

**Returns**:

  tuple[bool, str] ->
- `bool` - True if successful, False otherwise.
- `str` - The error message if unsuccessful.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateAsmFile"></a>

#### CreateAsmFile

```python
@staticmethod
def CreateAsmFile(filePath: str, asmContent: str) -> tuple[bool, str]
```

Creates a new ASM file with the provided ASM content.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ReadAsmFile"></a>

#### ReadAsmFile

```python
@staticmethod
def ReadAsmFile(filePath: str) -> tuple[bool, str]
```

Reads content from an ASM file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CompileAsmToObject"></a>

#### CompileAsmToObject

```python
@staticmethod
def CompileAsmToObject(filePath: str) -> tuple[bool, str]
```

Compiles an ASM file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.DisassembleAsmFile"></a>

#### DisassembleAsmFile

```python
@staticmethod
def DisassembleAsmFile(filePath: str) -> tuple[bool, str]
```

Disassembles an ASM file to inspect the assembly instructions.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateAsmFromString"></a>

#### CreateAsmFromString

```python
@staticmethod
def CreateAsmFromString(asmCode: str, outputFile: str) -> tuple[bool, str]
```

Creates an ASM file from a string of ASM code.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateObjectFile"></a>

#### CreateObjectFile

```python
@staticmethod
def CreateObjectFile(filePath: str) -> tuple[bool, str]
```

Creates an object (.o) file from a C/C++ file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.LinkObjectFiles"></a>

#### LinkObjectFiles

```python
@staticmethod
def LinkObjectFiles(objFiles: list[str], outputFile: str) -> tuple[bool, str]
```

Links multiple object (.o) files into an executable.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.DisassembleObjectFile"></a>

#### DisassembleObjectFile

```python
@staticmethod
def DisassembleObjectFile(objFilePath: str) -> tuple[bool, str]
```

Disassembles an object file to inspect the assembly instructions.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateCFile"></a>

#### CreateCFile

```python
@staticmethod
def CreateCFile(filePath: str, cContent: str) -> tuple[bool, str]
```

Creates a new C file with the provided C code.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CompileCToObject"></a>

#### CompileCToObject

```python
@staticmethod
def CompileCToObject(filePath: str) -> tuple[bool, str]
```

Compiles a C file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CreateCppFile"></a>

#### CreateCppFile

```python
@staticmethod
def CreateCppFile(filePath: str, cppContent: str) -> tuple[bool, str]
```

Creates a new C++ file with the provided C++ code.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CompileCppToObject"></a>

#### CompileCppToObject

```python
@staticmethod
def CompileCppToObject(filePath: str) -> tuple[bool, str]
```

Compiles a C++ file to an object (.o) file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.CompileCPlusPlusFile"></a>

#### CompileCPlusPlusFile

```python
@staticmethod
def CompileCPlusPlusFile(filePath: str) -> tuple[bool, str]
```

Compiles a C++ file into an executable.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.ReadBinaryFile"></a>

#### ReadBinaryFile

```python
@staticmethod
def ReadBinaryFile(filePath: str) -> tuple[bool, bytes]
```

Reads data from a binary file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.WriteBinaryFile"></a>

#### WriteBinaryFile

```python
@staticmethod
def WriteBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]
```

Writes data to a binary file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.AppendBinaryFile"></a>

#### AppendBinaryFile

```python
@staticmethod
def AppendBinaryFile(filePath: str, data: bytes) -> tuple[bool, str]
```

Appends data to a binary file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.GetBinaryFileSize"></a>

#### GetBinaryFileSize

```python
@staticmethod
def GetBinaryFileSize(filePath: str) -> tuple[bool, int]
```

Returns the size of a binary file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.EncryptFile"></a>

#### EncryptFile

```python
@staticmethod
def EncryptFile(filePath: str, key: bytes) -> tuple[bool, str]
```

Encrypts the content of a file using AES encryption.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.DecryptFile"></a>

#### DecryptFile

```python
@staticmethod
def DecryptFile(filePath: str, key: bytes) -> tuple[bool, str]
```

Decrypts an encrypted file.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.Base64EncodeFile"></a>

#### Base64EncodeFile

```python
@staticmethod
def Base64EncodeFile(filePath: str) -> tuple[bool, str]
```

Encodes a file in Base64 format.

<a id="phardwareitk.FileSystem.FileSystem.FileSystem.Base64DecodeFile"></a>

#### Base64DecodeFile

```python
@staticmethod
def Base64DecodeFile(filePath: str) -> tuple[bool, str]
```

Decodes a Base64 encoded file.

<a id="phardwareitk.FileSystem"></a>

# phardwareitk.FileSystem

Allows working with many types of Files

<a id="phardwareitk.FileSystem.os"></a>

## os

<a id="phardwareitk.FileSystem.sys"></a>

## sys

<a id="phardwareitk.FileSystem.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.FileSystem.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.LIB"></a>

# phardwareitk.LIB

Provides almost all file paths in the module

<a id="phardwareitk.LIB.os"></a>

## os

<a id="phardwareitk.LIB.Paths"></a>

## Paths Objects

```python
class Paths()
```

File Paths and Folder paths

<a id="phardwareitk.LIB.Paths.phardwareitk"></a>

#### phardwareitk

<a id="phardwareitk.LIB.Paths.ErrorSystem"></a>

#### ErrorSystem

<a id="phardwareitk.LIB.Paths.Extensions"></a>

#### Extensions

<a id="phardwareitk.LIB.Paths.FileSystem"></a>

#### FileSystem

<a id="phardwareitk.LIB.Paths.GUI"></a>

#### GUI

<a id="phardwareitk.LIB.Paths.HGame"></a>

#### HGame

<a id="phardwareitk.LIB.Paths.ModuleController"></a>

#### ModuleController

<a id="phardwareitk.LIB.Paths.PLTEC"></a>

#### PLTEC

<a id="phardwareitk.LIB.Paths.System"></a>

#### System

<a id="phardwareitk.LIB.Paths.CLI"></a>

#### CLI

<a id="phardwareitk.LIB.Paths.C"></a>

#### C

<a id="phardwareitk.LIB.Paths.defrunSettingsNOEXT"></a>

#### defrunSettingsNOEXT

<a id="phardwareitk.LIB.Paths.DependenciesPY_phardwareitk"></a>

#### DependenciesPY\_phardwareitk

<a id="phardwareitk.LIB.Paths.cliToolKitPY_CLI"></a>

#### cliToolKitPY\_CLI

<a id="phardwareitk.LIB.Paths.ErrorSystemPY_ErrorSystem"></a>

#### ErrorSystemPY\_ErrorSystem

<a id="phardwareitk.LIB.Paths.HyperOutPY_Extensions"></a>

#### HyperOutPY\_Extensions

<a id="phardwareitk.LIB.Paths.HyperInPY_Extensions"></a>

#### HyperInPY\_Extensions

<a id="phardwareitk.LIB.Paths.FileSystemPY_FileSystem"></a>

#### FileSystemPY\_FileSystem

<a id="phardwareitk.LIB.Paths.guiPY_GUI"></a>

#### guiPY\_GUI

<a id="phardwareitk.LIB.Paths.gui_sdlPY_GUI"></a>

#### gui\_sdlPY\_GUI

<a id="phardwareitk.LIB.Paths.renderGUIPYX_GUI"></a>

#### renderGUIPYX\_GUI

<a id="phardwareitk.LIB.Paths.renderGUIPYD_GUI"></a>

#### renderGUIPYD\_GUI

<a id="phardwareitk.LIB.Paths.renderGUISO_GUI"></a>

#### renderGUISO\_GUI

<a id="phardwareitk.LIB.Paths.mainPY_ModuleController"></a>

#### mainPY\_ModuleController

<a id="phardwareitk.LIB.Paths.anayzerPY_PLTEC"></a>

#### anayzerPY\_PLTEC

<a id="phardwareitk.LIB.Paths.ASMPY_PLTEC"></a>

#### ASMPY\_PLTEC

<a id="phardwareitk.LIB.Paths.CheckerPY_PLTEC"></a>

#### CheckerPY\_PLTEC

<a id="phardwareitk.LIB.Paths.DEF_langJSON_PLTEC"></a>

#### DEF\_langJSON\_PLTEC

<a id="phardwareitk.LIB.Paths.DEF_LanguageSETJSON_PLTEC"></a>

#### DEF\_LanguageSETJSON\_PLTEC

<a id="phardwareitk.LIB.Paths.LinkerPY_PLTEC"></a>

#### LinkerPY\_PLTEC

<a id="phardwareitk.LIB.Paths.LoggerPY_PLTEC"></a>

#### LoggerPY\_PLTEC

<a id="phardwareitk.LIB.Paths.mainPY_PLTEC"></a>

#### mainPY\_PLTEC

<a id="phardwareitk.LIB.Paths.OBJECTPY_PLTEC"></a>

#### OBJECTPY\_PLTEC

<a id="phardwareitk.LIB.Paths.ReaderPY_PLTEC"></a>

#### ReaderPY\_PLTEC

<a id="phardwareitk.LIB.Paths.SysUsagePY_System"></a>

#### SysUsagePY\_System

<a id="phardwareitk.System.CSpectre"></a>

# phardwareitk.System.CSpectre

C-Spectre is a ctypes like library offering auto-resolving, object-oriented, simpler-interface, library-auto-loading, auto-function-resolving and more features while being fully compatible with ctypes

<a id="phardwareitk.System.CSpectre.ctypes"></a>

## ctypes

<a id="phardwareitk.System.CSpectre.os"></a>

## os

<a id="phardwareitk.System.CSpectre.sys"></a>

## sys

<a id="phardwareitk.System.CSpectre.*"></a>

## \*

<a id="phardwareitk.System.CSpectre.NULL"></a>

#### NULL

<a id="phardwareitk.System.CSpectre.CInt"></a>

## CInt Objects

```python
class CInt()
```

Base Int class providing all functions

<a id="phardwareitk.System.CSpectre.CInt.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0)
```

<a id="phardwareitk.System.CSpectre.CInt.__int__"></a>

#### \_\_int\_\_

```python
def __int__()
```

<a id="phardwareitk.System.CSpectre.CInt.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.System.CSpectre.CInt.__add__"></a>

#### \_\_add\_\_

```python
def __add__(val: int)
```

<a id="phardwareitk.System.CSpectre.CInt.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(val: int)
```

<a id="phardwareitk.System.CSpectre.CInt.__mul__"></a>

#### \_\_mul\_\_

```python
def __mul__(val: int)
```

<a id="phardwareitk.System.CSpectre.CInt.__div__"></a>

#### \_\_div\_\_

```python
def __div__(val: int)
```

<a id="phardwareitk.System.CSpectre.CInt.to_ctypes"></a>

#### to\_ctypes

```python
def to_ctypes()
```

Returns CTypes compatible instance.

<a id="phardwareitk.System.CSpectre.CUint"></a>

## CUint Objects

```python
class CUint(CInt)
```

Base Unsigned int class providing all functions

<a id="phardwareitk.System.CSpectre.CUint.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CUint8"></a>

## CUint8 Objects

```python
class CUint8(CUint)
```

Unsigned Int8 (uint8_t)

<a id="phardwareitk.System.CSpectre.CUint8.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CUint16"></a>

## CUint16 Objects

```python
class CUint16(CUint)
```

Unsigned int16 (uint16_t)

<a id="phardwareitk.System.CSpectre.CUint16.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CUint32"></a>

## CUint32 Objects

```python
class CUint32(CUint)
```

Unsigned int32 (uint32_t)

<a id="phardwareitk.System.CSpectre.CUint32.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CUint64"></a>

## CUint64 Objects

```python
class CUint64(CUint)
```

Unsigned int64 (uint64_t)

<a id="phardwareitk.System.CSpectre.CUint64.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CInt8"></a>

## CInt8 Objects

```python
class CInt8(CInt)
```

Int8 (int8_t)

<a id="phardwareitk.System.CSpectre.CInt8.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CInt16"></a>

## CInt16 Objects

```python
class CInt16(CInt)
```

Int16 (int16_t)

<a id="phardwareitk.System.CSpectre.CInt16.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CInt32"></a>

## CInt32 Objects

```python
class CInt32(CInt)
```

Int32 (int32_t)

<a id="phardwareitk.System.CSpectre.CInt32.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.CInt64"></a>

## CInt64 Objects

```python
class CInt64(CInt)
```

Int64 (int64_t)

<a id="phardwareitk.System.CSpectre.CInt64.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.System.CSpectre.Void"></a>

## Void Objects

```python
class Void()
```

Void (void)

<a id="phardwareitk.System.CSpectre.Void.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="phardwareitk.System.CSpectre.Void.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.System.CSpectre.Void.to_ctypes"></a>

#### to\_ctypes

```python
def to_ctypes()
```

Returns CTypes compatible instance.

<a id="phardwareitk.System.CSpectre.Pointer"></a>

## Pointer Objects

```python
class Pointer()
```

A pointer (*)

<a id="phardwareitk.System.CSpectre.Pointer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(base_type, value=None)
```

<a id="phardwareitk.System.CSpectre.Pointer.deref"></a>

#### deref

```python
def deref()
```

Dereferences the pointer (&ptr)

<a id="phardwareitk.System.CSpectre.Pointer.set"></a>

#### set

```python
def set(value)
```

Sets a value

<a id="phardwareitk.System.CSpectre.Pointer.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.System.CSpectre.Pointer.to_ctypes"></a>

#### to\_ctypes

```python
def to_ctypes()
```

Returns CTypes compatible instance.

<a id="phardwareitk.System.CSpectre.VoidPointer"></a>

## VoidPointer Objects

```python
class VoidPointer(Pointer)
```

A Void Pointer (void*)

<a id="phardwareitk.System.CSpectre.VoidPointer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value=None)
```

<a id="phardwareitk.System.CSpectre.CPrebuilt"></a>

## CPrebuilt Objects

```python
class CPrebuilt()
```

<a id="phardwareitk.System.CSpectre.CPrebuilt.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="phardwareitk.System.CSpectre.CPrebuilt.include"></a>

#### include

```python
def include(path: str,
            include_dirs: Union[str, list] = "",
            ignore_includes: bool = False)
```

Includes a header file and auto resolves all dependencies, functions, macros and conditionals

**Arguments**:

- `path` _str_ - Path to the file to be resolved. Path can be absolute or relative to cwd or relative to any of the paths in include_dirs (NOTE: INCLUDE_DIRS ARE SAVED PER INSTANCE).
- `include_dirs` _str | list_ - Either a single path to any include directory or a list containing multiple include directory paths. Defaults to ''
- `ignore_includes` _bool_ - Wether to ignore include statements. Defaults to False.

<a id="phardwareitk.System.CSpectre.CPrebuilt.parse"></a>

#### parse

```python
def parse(text: str, ignore_includes: bool = False)
```

Parse C header text for functions, macros, and conditionals

**Arguments**:

- `text` _str_ - The data to parse.
- `ignore_includes` _bool_ - Wether to ignore include statements. Defaults to False.

<a id="phardwareitk.System.CSpectre.CPrebuilt.get_function"></a>

#### get\_function

```python
def get_function(name: str) -> dict
```

Gets a function from the resolved functions

<a id="phardwareitk.System.CSpectre.CPrebuilt.resolved_macros"></a>

#### resolved\_macros

```python
@property
def resolved_macros()
```

<a id="phardwareitk.System.CSpectre.CPrebuilt.conditional_stack"></a>

#### conditional\_stack

```python
@property
def conditional_stack()
```

<a id="phardwareitk.System.CSpectre.CPrebuilt.resolved_functions"></a>

#### resolved\_functions

```python
@property
def resolved_functions()
```

<a id="phardwareitk.System.CSpectre.CPrebuilt.resolved_typedefs"></a>

#### resolved\_typedefs

```python
@property
def resolved_typedefs()
```

<a id="phardwareitk.System.CSpectre.LibraryWrapper"></a>

## LibraryWrapper Objects

```python
class LibraryWrapper()
```

<a id="phardwareitk.System.CSpectre.LibraryWrapper.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path)
```

<a id="phardwareitk.System.CSpectre.LibraryWrapper.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name)
```

<a id="phardwareitk.System.SysUsage"></a>

# phardwareitk.System.SysUsage

<a id="phardwareitk.System.SysUsage.psutil"></a>

## psutil

<a id="phardwareitk.System.SysUsage.*"></a>

## \*

<a id="phardwareitk.System.SysUsage.os"></a>

## os

<a id="phardwareitk.System.SysUsage.*"></a>

## \*

<a id="phardwareitk.System.SysUsage.subprocess"></a>

## subprocess

<a id="phardwareitk.System.SysUsage.platform"></a>

## platform

<a id="phardwareitk.System.SysUsage.socket"></a>

## socket

<a id="phardwareitk.System.SysUsage.SYSTEM"></a>

#### SYSTEM

<a id="phardwareitk.System.SysUsage.CPU"></a>

## CPU Objects

```python
class CPU()
```

<a id="phardwareitk.System.SysUsage.CPU.CpuUsage"></a>

#### CpuUsage

```python
@staticmethod
def CpuUsage(interval: Union[None, float] = 1.0) -> float
```

This function calculates the CPU usage via the given interval and returns the CPU usage.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.
  

**Returns**:

- `float` - The Cpu usage.

<a id="phardwareitk.System.SysUsage.CPU.CpuUsageDetails"></a>

#### CpuUsageDetails

```python
@staticmethod
def CpuUsageDetails()
```

This function returns the following details about the CPU usage ->

user: This represents the time spent by normal processes executing in the user mode.
system: This represents the time spent by processes executing in the kernel mode.
idle: This represents the time when the system is idle.
nice: This represents the time spent by priority processes executing in the user mode.
iowait: This represents the time spent waiting for I/O to complete.
irq: This represents the time spent for servicing hardware interrupts.
softirq: This represents the time spent for servicing software interrupts.
steal: Represents the time spent by other operating systems running in a virtualized environment
guest: This represents the time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.

WINDOWS ONLY:
interrupt: This represents the time spent for servicing hardware interrupts.
dpc: This represents the time spent servicing deferred procedure calls (DPCs).

**Returns**:

- `Any` - Return type -> psutil._ps[Your OS].scputimes

<a id="phardwareitk.System.SysUsage.CPU.CpuUsageTimesDetails"></a>

#### CpuUsageTimesDetails

```python
@staticmethod
def CpuUsageTimesDetails(interval: Union[float, None] = 1.0)
```

Same as CpuUsage but returns like CpuUsageDetails.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.
  

**Returns**:

- `Any` - Return Type -> psutil._ps[Your OS].scputimes.

<a id="phardwareitk.System.SysUsage.CPU.CpuCount"></a>

#### CpuCount

```python
@staticmethod
def CpuCount(logical: bool = False) -> int
```

Returns the number of Cpu Cores in System.

**Arguments**:

- `logical` _bool, optional_ - If set to true returned value will be [Number of Physical Cores + Hyper Threading]. Defaults to False.
  

**Returns**:

- `int` - The number of Cpu Physical Cores [+ Hyper Threading if [logical] is True].

<a id="phardwareitk.System.SysUsage.CPU.CpuStats"></a>

#### CpuStats

```python
@staticmethod
def CpuStats()
```

Returns detailed CPU statistics such as context switches, interrupts, and soft interrupts.

**Returns**:

- `Any` - Object containing detailed statistics about the CPU.

<a id="phardwareitk.System.SysUsage.CPU.CpuFreq"></a>

#### CpuFreq

```python
@staticmethod
def CpuFreq()
```

Returns the current frequency of the CPU, in MHz.

**Returns**:

- `Any` - A scpufreq object that contains the current frequency of the CPU.

<a id="phardwareitk.System.SysUsage.CPU.CpuFreqPerCore"></a>

#### CpuFreqPerCore

```python
@staticmethod
def CpuFreqPerCore() -> list
```

Returns the current frequency per CPU core, in MHz.

**Returns**:

- `list` - A list of scpufreq objects, one per CPU core.

<a id="phardwareitk.System.SysUsage.CPU.CpuLoadAvg"></a>

#### CpuLoadAvg

```python
@staticmethod
def CpuLoadAvg() -> list
```

Returns the 1, 5, and 15 minute load averages for the CPU system.

**Returns**:

- `list` - list of 3 floats representing the load averages over 1, 5, and 15 minutes.

<a id="phardwareitk.System.SysUsage.CPU.CpuAffinity"></a>

#### CpuAffinity

```python
@staticmethod
def CpuAffinity(pid: int = None) -> Union[list, None]
```

Returns a list of CPU cores the given process (or current process if no PID is specified) is allowed to run on.

**Arguments**:

- `pid` _int, optional_ - The process ID. If None, the current process is used. Defaults to None.
  

**Returns**:

  Union[list, None]: A list of CPU cores the process is allowed to use, or None if the process is not found.

<a id="phardwareitk.System.SysUsage.CPU.CpuTimesPerCore"></a>

#### CpuTimesPerCore

```python
@staticmethod
def CpuTimesPerCore() -> list
```

Returns the CPU times per core in the system.

**Returns**:

- `list` - A list of scputimes objects per CPU core.

<a id="phardwareitk.System.SysUsage.CPU.CpuUsagePerCore"></a>

#### CpuUsagePerCore

```python
@staticmethod
def CpuUsagePerCore(interval: Union[None, float] = 1.0) -> list
```

Returns the CPU usage per core over the given interval.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval for calculating the usage. Defaults to 1.0.
  

**Returns**:

- `list` - list of CPU usage percentages per core.

<a id="phardwareitk.System.SysUsage.Battery"></a>

## Battery Objects

```python
class Battery()
```

<a id="phardwareitk.System.SysUsage.Battery.BatteryStatus"></a>

#### BatteryStatus

```python
@staticmethod
def BatteryStatus() -> str
```

Returns the status of the battery (e.g., 'charging', 'discharging', 'full', or 'not present').

**Returns**:

- `str` - The battery status.

<a id="phardwareitk.System.SysUsage.Battery.BatteryPercentage"></a>

#### BatteryPercentage

```python
@staticmethod
def BatteryPercentage() -> float
```

Returns the current battery percentage.

**Returns**:

- `float` - The battery percentage.

<a id="phardwareitk.System.SysUsage.Battery.BatteryTimeLeft"></a>

#### BatteryTimeLeft

```python
@staticmethod
def BatteryTimeLeft() -> str
```

Returns the estimated time left on the battery in minutes. If plugged in, returns 'Charging'.

**Returns**:

- `str` - Time left + Time Period (Minutes/Hours/Seconds/Days/Months/Years/Centuries), or 'Charging' if plugged in.

<a id="phardwareitk.System.SysUsage.Battery.BatteryPlugged"></a>

#### BatteryPlugged

```python
@staticmethod
def BatteryPlugged() -> bool
```

Returns True if the battery is currently plugged in (charging), otherwise False.

**Returns**:

- `bool` - True if the battery is plugged in, else False.

<a id="phardwareitk.System.SysUsage.Battery.BatterySecsLeft"></a>

#### BatterySecsLeft

```python
@staticmethod
def BatterySecsLeft() -> Union[int, None]
```

Returns the remaining seconds of battery life. Returns None if the time left is unknown.

**Returns**:

  Union[int, None]: Remaining time in seconds or None if unknown.

<a id="phardwareitk.System.SysUsage.Battery.BatteryPluggedTime"></a>

#### BatteryPluggedTime

```python
@staticmethod
def BatteryPluggedTime() -> float
```

Returns the time in seconds that the battery has been plugged in.

**Returns**:

- `float` - The time in seconds the battery has been plugged in.

<a id="phardwareitk.System.SysUsage.Battery.BatteryIsCharging"></a>

#### BatteryIsCharging

```python
@staticmethod
def BatteryIsCharging() -> bool
```

Returns True if the battery is currently charging, False otherwise.

**Returns**:

- `bool` - True if the battery is charging, False otherwise.

<a id="phardwareitk.System.SysUsage.Battery.BatteryTimeToFullCharge"></a>

#### BatteryTimeToFullCharge

```python
@staticmethod
def BatteryTimeToFullCharge() -> Union[str, float]
```

Returns the estimated time in minutes for the battery to be fully charged. Returns 'Charging' if plugged in.

**Returns**:

  Union[str, float]: Time to full charge in minutes or 'Charging' if plugged in.

<a id="phardwareitk.System.SysUsage.Battery.BatteryDetails"></a>

#### BatteryDetails

```python
@staticmethod
def BatteryDetails() -> Union[str, dict]
```

Returns detailed information about the battery, including percent, time left, and charging status.

**Returns**:

  Union[str, dict]: A dictionary with detailed battery information or 'Battery not present'.

<a id="phardwareitk.System.SysUsage.Battery.BatteryStatusDetails"></a>

#### BatteryStatusDetails

```python
@staticmethod
def BatteryStatusDetails() -> Union[str, dict]
```

Returns detailed battery status information, including charging status and percent.

**Returns**:

  Union[str, dict]: A dictionary with battery status details or 'Battery not present'.

<a id="phardwareitk.System.SysUsage.Battery.BatteryType"></a>

#### BatteryType

```python
@staticmethod
def BatteryType() -> str
```

Returns the battery type (e.g., 'Li-ion', 'NiMH', etc.) if available.

**Returns**:

- `str` - The battery type or 'Unknown' if the information is unavailable.

<a id="phardwareitk.System.SysUsage.Temperature"></a>

## Temperature Objects

```python
class Temperature()
```

Linux Only

<a id="phardwareitk.System.SysUsage.Temperature.CpuTemp"></a>

#### CpuTemp

```python
@staticmethod
def CpuTemp() -> float
```

Returns the current temperature of the CPU in Celsius.

**Returns**:

- `float` - The current CPU temperature in Celsius.

<a id="phardwareitk.System.SysUsage.Temperature.GpuTemp"></a>

#### GpuTemp

```python
@staticmethod
def GpuTemp() -> float
```

Returns the current temperature of the GPU in Celsius.

**Returns**:

- `float` - The current GPU temperature in Celsius.

<a id="phardwareitk.System.SysUsage.Temperature.TempSensors"></a>

#### TempSensors

```python
@staticmethod
def TempSensors() -> dict
```

Returns a dictionary of available temperature sensors and their values.

**Returns**:

- `dict` - A dictionary where keys are sensor names, and values are lists of sensor readings.

<a id="phardwareitk.System.SysUsage.Temperature.TempMax"></a>

#### TempMax

```python
@staticmethod
def TempMax() -> float
```

Returns the maximum temperature of the CPU in Celsius.

**Returns**:

- `float` - The maximum CPU temperature.

<a id="phardwareitk.System.SysUsage.Temperature.TempMin"></a>

#### TempMin

```python
@staticmethod
def TempMin() -> float
```

Returns the minimum temperature of the CPU in Celsius.

**Returns**:

- `float` - The minimum CPU temperature.

<a id="phardwareitk.System.SysUsage.Temperature.TempAveraged"></a>

#### TempAveraged

```python
@staticmethod
def TempAveraged() -> float
```

Returns the average temperature of the CPU in Celsius.

**Returns**:

- `float` - The average CPU temperature.

<a id="phardwareitk.System.SysUsage.Temperature.CpuTempPerCore"></a>

#### CpuTempPerCore

```python
@staticmethod
def CpuTempPerCore() -> list
```

Returns the temperature of each CPU core in Celsius.

**Returns**:

- `list` - A list of CPU temperatures for each core.

<a id="phardwareitk.System.SysUsage.Temperature.GpuTempPerCore"></a>

#### GpuTempPerCore

```python
@staticmethod
def GpuTempPerCore() -> list
```

Returns the temperature of each GPU core in Celsius.

**Returns**:

- `list` - A list of GPU temperatures for each core.

<a id="phardwareitk.System.SysUsage.Temperature.TempCritical"></a>

#### TempCritical

```python
@staticmethod
def TempCritical() -> float
```

Returns the critical temperature threshold for the CPU in Celsius.

**Returns**:

- `float` - The critical temperature threshold.

<a id="phardwareitk.System.SysUsage.Temperature.TempWarning"></a>

#### TempWarning

```python
@staticmethod
def TempWarning() -> float
```

Returns the warning temperature threshold for the CPU in Celsius.

**Returns**:

- `float` - The warning temperature threshold.

<a id="phardwareitk.System.SysUsage.Temperature.TempStatus"></a>

#### TempStatus

```python
@staticmethod
def TempStatus() -> dict
```

Returns a dictionary of temperature status (e.g., current, critical, warning) for each sensor.

**Returns**:

- `dict` - A dictionary with temperature status.

<a id="phardwareitk.System.SysUsage.Temperature.GpuTempStatus"></a>

#### GpuTempStatus

```python
@staticmethod
def GpuTempStatus() -> dict
```

Returns the temperature status for the GPU.

**Returns**:

- `dict` - A dictionary with GPU temperature status.

<a id="phardwareitk.System.SysUsage.Temperature.CpuTempStatus"></a>

#### CpuTempStatus

```python
@staticmethod
def CpuTempStatus() -> dict
```

Returns the temperature status for the CPU.

**Returns**:

- `dict` - A dictionary with CPU temperature status.

<a id="phardwareitk.System.SysUsage.Temperature.MaxTempThreshold"></a>

#### MaxTempThreshold

```python
@staticmethod
def MaxTempThreshold() -> float
```

Returns the maximum temperature threshold for all sensors.

**Returns**:

- `float` - The maximum temperature threshold across all sensors.

<a id="phardwareitk.System.SysUsage.Temperature.MinTempThreshold"></a>

#### MinTempThreshold

```python
@staticmethod
def MinTempThreshold() -> float
```

Returns the minimum temperature threshold for all sensors.

**Returns**:

- `float` - The minimum temperature threshold across all sensors.

<a id="phardwareitk.System.SysUsage.Temperature.TemperatureTrends"></a>

#### TemperatureTrends

```python
@staticmethod
def TemperatureTrends() -> dict
```

Returns the temperature trends (current, max, min) for each sensor.

**Returns**:

- `dict` - A dictionary with temperature trends for each sensor.

<a id="phardwareitk.System.SysUsage.Temperature.TempInFahrenheit"></a>

#### TempInFahrenheit

```python
@staticmethod
def TempInFahrenheit() -> dict
```

Returns all temperature readings in Fahrenheit.

**Returns**:

- `dict` - A dictionary with temperature readings in Fahrenheit.

<a id="phardwareitk.System.SysUsage.Temperature.TempInKelvin"></a>

#### TempInKelvin

```python
@staticmethod
def TempInKelvin() -> dict
```

Returns all temperature readings in Kelvin.

**Returns**:

- `dict` - A dictionary with temperature readings in Kelvin.

<a id="phardwareitk.System.SysUsage.Temperature.TempForProcesses"></a>

#### TempForProcesses

```python
@staticmethod
def TempForProcesses(pid: int) -> dict
```

Returns the temperature readings for processes, if available.

**Arguments**:

- `pid` _int_ - The process ID.
  

**Returns**:

- `dict` - A dictionary with temperature readings for the given process.

<a id="phardwareitk.System.SysUsage.Disk"></a>

## Disk Objects

```python
class Disk()
```

<a id="phardwareitk.System.SysUsage.Disk.DiskUsage"></a>

#### DiskUsage

```python
@staticmethod
def DiskUsage(path: str = '/') -> dict
```

Returns the disk usage (free, used, total, percent).
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskPartitions"></a>

#### DiskPartitions

```python
@staticmethod
def DiskPartitions() -> list
```

Returns a list of partitions on the system.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskFree"></a>

#### DiskFree

```python
@staticmethod
def DiskFree(path: str = '/') -> float
```

Returns the free space of a partition in bytes.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskUsed"></a>

#### DiskUsed

```python
@staticmethod
def DiskUsed(path: str = '/') -> float
```

Returns the used space of a partition in bytes.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskTotal"></a>

#### DiskTotal

```python
@staticmethod
def DiskTotal(path: str = '/') -> float
```

Returns the total space of a partition in bytes.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskReadBytes"></a>

#### DiskReadBytes

```python
@staticmethod
def DiskReadBytes() -> int
```

Returns the total number of bytes read from all disks.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskWriteBytes"></a>

#### DiskWriteBytes

```python
@staticmethod
def DiskWriteBytes() -> int
```

Returns the total number of bytes written to all disks.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskReads"></a>

#### DiskReads

```python
@staticmethod
def DiskReads() -> int
```

Returns the total number of read operations performed on all disks.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskWrites"></a>

#### DiskWrites

```python
@staticmethod
def DiskWrites() -> int
```

Returns the total number of write operations performed on all disks.
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskReadTime"></a>

#### DiskReadTime

```python
@staticmethod
def DiskReadTime() -> int
```

Returns the total time spent reading from the disk (in milliseconds).
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskWriteTime"></a>

#### DiskWriteTime

```python
@staticmethod
def DiskWriteTime() -> int
```

Returns the total time spent writing to the disk (in milliseconds).
Works cross-platform (Linux, Windows, macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskIOMerges"></a>

#### DiskIOMerges

```python
@staticmethod
def DiskIOMerges() -> int
```

Returns the total number of merged I/O operations.
Works on Linux (Not available on Windows/macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskQueueDepth"></a>

#### DiskQueueDepth

```python
@staticmethod
def DiskQueueDepth() -> int
```

Returns the current disk I/O queue depth.
Works on Linux (Not available on Windows/macOS)

<a id="phardwareitk.System.SysUsage.Disk.DiskHealth"></a>

#### DiskHealth

```python
@staticmethod
def DiskHealth(device: str) -> dict
```

Returns the SMART health status of a disk.
Works on Linux (using smartmontools), Windows (using OpenHardwareMonitor), macOS (via system commands)

<a id="phardwareitk.System.SysUsage.Disk.DiskTemp"></a>

#### DiskTemp

```python
@staticmethod
def DiskTemp(device: str) -> float
```

Returns the temperature of the disk (if supported).
Works on Linux (using smartmontools), Windows (using OpenHardwareMonitor), macOS (via system commands)

<a id="phardwareitk.System.SysUsage.Memory"></a>

## Memory Objects

```python
class Memory()
```

<a id="phardwareitk.System.SysUsage.Memory.RAMInfo"></a>

#### RAMInfo

```python
@staticmethod
def RAMInfo() -> dict
```

Returns overall system RAM information (total, available, used, percent).

<a id="phardwareitk.System.SysUsage.Memory.RAMTotal"></a>

#### RAMTotal

```python
@staticmethod
def RAMTotal() -> float
```

Returns total RAM in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMAvailable"></a>

#### RAMAvailable

```python
@staticmethod
def RAMAvailable() -> float
```

Returns available RAM in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMUsed"></a>

#### RAMUsed

```python
@staticmethod
def RAMUsed() -> float
```

Returns used RAM in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMPercent"></a>

#### RAMPercent

```python
@staticmethod
def RAMPercent() -> float
```

Returns percentage of RAM used.

<a id="phardwareitk.System.SysUsage.Memory.RAMActive"></a>

#### RAMActive

```python
@staticmethod
def RAMActive() -> float
```

Returns active RAM in bytes (used for active processes).

<a id="phardwareitk.System.SysUsage.Memory.RAMBuffered"></a>

#### RAMBuffered

```python
@staticmethod
def RAMBuffered() -> float
```

Returns buffered RAM in bytes (used for temporary caching).

<a id="phardwareitk.System.SysUsage.Memory.RAMShared"></a>

#### RAMShared

```python
@staticmethod
def RAMShared() -> float
```

Returns shared RAM in bytes (used by multiple processes).

<a id="phardwareitk.System.SysUsage.Memory.RAMSlab"></a>

#### RAMSlab

```python
@staticmethod
def RAMSlab() -> float
```

Returns slab memory in bytes (kernel memory used to cache objects).

<a id="phardwareitk.System.SysUsage.Memory.RAMFree"></a>

#### RAMFree

```python
@staticmethod
def RAMFree() -> float
```

Returns free RAM in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMUsedByProcesses"></a>

#### RAMUsedByProcesses

```python
@staticmethod
def RAMUsedByProcesses() -> list
```

Returns memory used by processes in a list of dictionaries.

<a id="phardwareitk.System.SysUsage.Memory.RAMSwapTotal"></a>

#### RAMSwapTotal

```python
@staticmethod
def RAMSwapTotal() -> float
```

Returns total swap memory used for RAM overflow (if applicable).

<a id="phardwareitk.System.SysUsage.Memory.RAMSwapUsed"></a>

#### RAMSwapUsed

```python
@staticmethod
def RAMSwapUsed() -> float
```

Returns used swap memory in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMSwapFree"></a>

#### RAMSwapFree

```python
@staticmethod
def RAMSwapFree() -> float
```

Returns free swap memory in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMSwapPercent"></a>

#### RAMSwapPercent

```python
@staticmethod
def RAMSwapPercent() -> float
```

Returns swap memory usage percentage.

<a id="phardwareitk.System.SysUsage.Memory.RAMSwapInUse"></a>

#### RAMSwapInUse

```python
@staticmethod
def RAMSwapInUse() -> bool
```

Returns True if swap memory is in use, otherwise False.

<a id="phardwareitk.System.SysUsage.Memory.RAMBufferInfo"></a>

#### RAMBufferInfo

```python
@staticmethod
def RAMBufferInfo() -> dict
```

Returns detailed memory buffer information.

<a id="phardwareitk.System.SysUsage.Memory.RAMPhysicalMemory"></a>

#### RAMPhysicalMemory

```python
@staticmethod
def RAMPhysicalMemory() -> float
```

Returns total physical memory (RAM) in bytes.

<a id="phardwareitk.System.SysUsage.Memory.RAMActiveProcessMemory"></a>

#### RAMActiveProcessMemory

```python
@staticmethod
def RAMActiveProcessMemory(pid: int) -> float
```

Returns memory used by a specific process (pid).

<a id="phardwareitk.System.SysUsage.Fan"></a>

## Fan Objects

```python
class Fan()
```

Linux Only

<a id="phardwareitk.System.SysUsage.Fan.FansInfo"></a>

#### FansInfo

```python
@staticmethod
def FansInfo() -> dict
```

Returns detailed information about all fans, including fan ID and speed (RPM).

<a id="phardwareitk.System.SysUsage.Fan.FansCount"></a>

#### FansCount

```python
@staticmethod
def FansCount() -> int
```

Returns the number of fans in the system.

<a id="phardwareitk.System.SysUsage.Fan.FanSpeed"></a>

#### FanSpeed

```python
@staticmethod
def FanSpeed(fan_id: int) -> Union[int, None]
```

Returns the speed of a specific fan by fan ID (RPM).

<a id="phardwareitk.System.SysUsage.Fan.AllFanSpeeds"></a>

#### AllFanSpeeds

```python
@staticmethod
def AllFanSpeeds() -> dict
```

Returns a dictionary of fan speeds (RPM) for all fans.

<a id="phardwareitk.System.SysUsage.Fan.FanInfoById"></a>

#### FanInfoById

```python
@staticmethod
def FanInfoById(fan_id: int) -> Union[dict, None]
```

Returns detailed information about a specific fan (by fan ID).

<a id="phardwareitk.System.SysUsage.Network"></a>

## Network Objects

```python
class Network()
```

<a id="phardwareitk.System.SysUsage.Network.Interfaces"></a>

#### Interfaces

```python
@staticmethod
def Interfaces() -> Union[dict[str, dict], str]
```

Returns a dictionary of network interfaces, their addresses, and stats. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.InterfaceStats"></a>

#### InterfaceStats

```python
@staticmethod
def InterfaceStats() -> Union[dict[str, dict], str]
```

Returns the stats (bytes, packets, errors, drops, etc.) for each network interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.NetworkConnections"></a>

#### NetworkConnections

```python
@staticmethod
def NetworkConnections(kind: str = 'inet') -> Union[list, str]
```

Returns a list of network connections of the specified type (TCP, UDP, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.NetworkStats"></a>

#### NetworkStats

```python
@staticmethod
def NetworkStats() -> Union[dict[str, Union[int, float]], str]
```

Returns global network statistics like bytes sent, received, errors, etc. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.InterfaceNetworkStats"></a>

#### InterfaceNetworkStats

```python
@staticmethod
def InterfaceNetworkStats(interface: str) -> Union[dict, str]
```

Returns per-interface network stats (bytes sent, received, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.DefaultGateway"></a>

#### DefaultGateway

```python
@staticmethod
def DefaultGateway() -> Union[dict[str, str], str]
```

Returns the default gateway for the system. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.DNSConfig"></a>

#### DNSConfig

```python
@staticmethod
def DNSConfig() -> Union[dict[str, list], str]
```

Returns DNS configuration for the system (DNS servers). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.IPAddress"></a>

#### IPAddress

```python
@staticmethod
def IPAddress(interface: str) -> Union[str, str]
```

Returns the IP address of a given interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.MACAddress"></a>

#### MACAddress

```python
@staticmethod
def MACAddress(interface: str) -> Union[str, str]
```

Returns the MAC address of a given interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.Hostname"></a>

#### Hostname

```python
@staticmethod
def Hostname() -> Union[str, str]
```

Returns the hostname of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.FQDN"></a>

#### FQDN

```python
@staticmethod
def FQDN() -> Union[str, str]
```

Returns the fully qualified domain name (FQDN) of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.LocalIPAddress"></a>

#### LocalIPAddress

```python
@staticmethod
def LocalIPAddress() -> Union[str, str]
```

Returns the local IP address of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.InterfaceState"></a>

#### InterfaceState

```python
@staticmethod
def InterfaceState(interface: str) -> Union[str, str]
```

Returns the current state (UP/DOWN) of the network interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.IsInterfaceUp"></a>

#### IsInterfaceUp

```python
@staticmethod
def IsInterfaceUp(interface: str) -> Union[bool, str]
```

Returns True if the network interface is up, False otherwise. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.NetworkConnectionsByPID"></a>

#### NetworkConnectionsByPID

```python
@staticmethod
def NetworkConnectionsByPID(pid: int) -> Union[list, str]
```

Returns network connections by the process ID (PID). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.LocalPortsInUse"></a>

#### LocalPortsInUse

```python
@staticmethod
def LocalPortsInUse() -> Union[list, str]
```

Returns a list of local ports in use. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.ExternalIPAddress"></a>

#### ExternalIPAddress

```python
@staticmethod
def ExternalIPAddress() -> Union[str, str]
```

Returns the external IP address of the system (if available).

<a id="phardwareitk.System.SysUsage.Network.InterfaceType"></a>

#### InterfaceType

```python
@staticmethod
def InterfaceType(interface: str) -> Union[str, str]
```

Returns the type of a network interface (e.g., ethernet, wifi). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.ConnectionStatus"></a>

#### ConnectionStatus

```python
@staticmethod
def ConnectionStatus(connection) -> Union[str, str]
```

Returns the status of a network connection (ESTABLISHED, LISTEN, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.Network.Netmask"></a>

#### Netmask

```python
@staticmethod
def Netmask(interface: str) -> Union[str, str]
```

Returns the netmask of the given network interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System"></a>

## System Objects

```python
class System(CPU, Battery, Temperature, Disk, Memory, Fan, Network)
```

<a id="phardwareitk.System.SysUsage.System.CpuUsage"></a>

#### CpuUsage

```python
@classmethod
def CpuUsage(cls, interval: Union[None, float] = 1.0) -> float
```

This function calculates the CPU usage via the given interval and returns the CPU usage.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.
  

**Returns**:

- `float` - The Cpu usage.

<a id="phardwareitk.System.SysUsage.System.CpuUsageDetails"></a>

#### CpuUsageDetails

```python
@classmethod
def CpuUsageDetails(cls)
```

This function returns the following details about the CPU usage ->

user: This represents the time spent by normal processes executing in the user mode.
system: This represents the time spent by processes executing in the kernel mode.
idle: This represents the time when the system is idle.
nice: This represents the time spent by priority processes executing in the user mode.
iowait: This represents the time spent waiting for I/O to complete.
irq: This represents the time spent for servicing hardware interrupts.
softirq: This represents the time spent for servicing software interrupts.
steal: Represents the time spent by other operating systems running in a virtualized environment
guest: This represents the time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.

WINDOWS ONLY:
interrupt: This represents the time spent for servicing hardware interrupts.
dpc: This represents the time spent servicing deferred procedure calls (DPCs).

**Returns**:

- `Any` - Return type -> psutil._ps[Your OS].scputimes

<a id="phardwareitk.System.SysUsage.System.CpuUsageTimesDetails"></a>

#### CpuUsageTimesDetails

```python
@classmethod
def CpuUsageTimesDetails(cls, interval: Union[float, None] = 1.0)
```

Same as CpuUsage but returns like CpuUsageDetails.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval defines time used to calculate the CPU usage. None defines the time from module import. Defaults to 1.0.
  

**Returns**:

- `Any` - Return Type -> psutil._ps[Your OS].scputimes.

<a id="phardwareitk.System.SysUsage.System.CpuCount"></a>

#### CpuCount

```python
@classmethod
def CpuCount(cls, logical: bool = False) -> int
```

Returns the number of Cpu Cores in System.

**Arguments**:

- `logical` _bool, optional_ - If set to true returned value will be [Number of Physical Cores + Hyper Threading]. Defaults to False.
  

**Returns**:

- `int` - The number of Cpu Physical Cores [+ Hyper Threading if [logical] is True].

<a id="phardwareitk.System.SysUsage.System.CpuStats"></a>

#### CpuStats

```python
@classmethod
def CpuStats(cls)
```

Returns detailed CPU statistics such as context switches, interrupts, and soft interrupts.

**Returns**:

- `Any` - Object containing detailed statistics about the CPU.

<a id="phardwareitk.System.SysUsage.System.CpuFreq"></a>

#### CpuFreq

```python
@classmethod
def CpuFreq(cls)
```

Returns the current frequency of the CPU, in MHz.

**Returns**:

- `Any` - A scpufreq object that contains the current frequency of the CPU.

<a id="phardwareitk.System.SysUsage.System.CpuFreqPerCore"></a>

#### CpuFreqPerCore

```python
@classmethod
def CpuFreqPerCore(cls) -> list
```

Returns the current frequency per CPU core, in MHz.

**Returns**:

- `list` - A list of scpufreq objects, one per CPU core.

<a id="phardwareitk.System.SysUsage.System.CpuLoadAvg"></a>

#### CpuLoadAvg

```python
@classmethod
def CpuLoadAvg(cls) -> list
```

Returns the 1, 5, and 15 minute load averages for the CPU system.

**Returns**:

- `list` - list of 3 floats representing the load averages over 1, 5, and 15 minutes.

<a id="phardwareitk.System.SysUsage.System.CpuAffinity"></a>

#### CpuAffinity

```python
@classmethod
def CpuAffinity(cls, pid: int = None) -> Union[list, None]
```

Returns a list of CPU cores the given process (or current process if no PID is specified) is allowed to run on.

**Arguments**:

- `pid` _int, optional_ - The process ID. If None, the current process is used. Defaults to None.
  

**Returns**:

  Union[list, None]: A list of CPU cores the process is allowed to use, or None if the process is not found.

<a id="phardwareitk.System.SysUsage.System.CpuTimesPerCore"></a>

#### CpuTimesPerCore

```python
@classmethod
def CpuTimesPerCore(cls) -> list
```

Returns the CPU times per core in the system.

**Returns**:

- `list` - A list of scputimes objects per CPU core.

<a id="phardwareitk.System.SysUsage.System.CpuUsagePerCore"></a>

#### CpuUsagePerCore

```python
@classmethod
def CpuUsagePerCore(cls, interval: Union[None, float] = 1.0) -> list
```

Returns the CPU usage per core over the given interval.

**Arguments**:

- `interval` _Union[None, float], optional_ - Interval for calculating the usage. Defaults to 1.0.
  

**Returns**:

- `list` - list of CPU usage percentages per core.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryStatus"></a>

#### SystemBatteryStatus

```python
@classmethod
def SystemBatteryStatus(cls) -> str
```

Returns the battery status using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryPercentage"></a>

#### SystemBatteryPercentage

```python
@classmethod
def SystemBatteryPercentage(cls) -> float
```

Returns the battery percentage using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryTimeLeft"></a>

#### SystemBatteryTimeLeft

```python
@classmethod
def SystemBatteryTimeLeft(cls) -> str
```

Returns the estimated time left on the battery using the Battery class.

**Returns**:

- `str` - Time left + Time Period (Minutes/Hours/Seconds/Days/Months/Years/Centuries), or 'Charging' if plugged in.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryPlugged"></a>

#### SystemBatteryPlugged

```python
@classmethod
def SystemBatteryPlugged(cls) -> bool
```

Returns whether the battery is plugged in (charging) using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatterySecsLeft"></a>

#### SystemBatterySecsLeft

```python
@classmethod
def SystemBatterySecsLeft(cls) -> Union[int, None]
```

Returns the remaining battery life in seconds using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryPluggedTime"></a>

#### SystemBatteryPluggedTime

```python
@classmethod
def SystemBatteryPluggedTime(cls) -> float
```

Returns the time the battery has been plugged in using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryIsCharging"></a>

#### SystemBatteryIsCharging

```python
@classmethod
def SystemBatteryIsCharging(cls) -> bool
```

Returns whether the battery is charging using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryTimeToFullCharge"></a>

#### SystemBatteryTimeToFullCharge

```python
@classmethod
def SystemBatteryTimeToFullCharge(cls) -> Union[str, float]
```

Returns the estimated time to full charge using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryDetails"></a>

#### SystemBatteryDetails

```python
@classmethod
def SystemBatteryDetails(cls) -> Union[str, dict]
```

Returns detailed battery information using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryStatusDetails"></a>

#### SystemBatteryStatusDetails

```python
@classmethod
def SystemBatteryStatusDetails(cls) -> Union[str, dict]
```

Returns detailed battery status information using the Battery class.

<a id="phardwareitk.System.SysUsage.System.SystemBatteryType"></a>

#### SystemBatteryType

```python
@classmethod
def SystemBatteryType(cls) -> str
```

Returns the battery type using the Battery class.

<a id="phardwareitk.System.SysUsage.System.DiskUsage"></a>

#### DiskUsage

```python
@classmethod
def DiskUsage(cls, path: str = '/') -> dict
```

Returns the disk usage (free, used, total, percent).
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskPartitions"></a>

#### DiskPartitions

```python
@classmethod
def DiskPartitions(cls) -> list
```

Returns a list of partitions on the system.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskFree"></a>

#### DiskFree

```python
@classmethod
def DiskFree(cls, path: str = '/') -> float
```

Returns the free space of a partition in bytes.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskUsed"></a>

#### DiskUsed

```python
@classmethod
def DiskUsed(cls, path: str = '/') -> float
```

Returns the used space of a partition in bytes.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskTotal"></a>

#### DiskTotal

```python
@classmethod
def DiskTotal(cls, path: str = '/') -> float
```

Returns the total space of a partition in bytes.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskReadBytes"></a>

#### DiskReadBytes

```python
@classmethod
def DiskReadBytes(cls) -> int
```

Returns the total number of bytes read from all disks.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskWriteBytes"></a>

#### DiskWriteBytes

```python
@classmethod
def DiskWriteBytes(cls) -> int
```

Returns the total number of bytes written to all disks.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskReads"></a>

#### DiskReads

```python
@classmethod
def DiskReads(cls) -> int
```

Returns the total number of read operations performed on all disks.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskWrites"></a>

#### DiskWrites

```python
@classmethod
def DiskWrites(cls) -> int
```

Returns the total number of write operations performed on all disks.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskReadTime"></a>

#### DiskReadTime

```python
@classmethod
def DiskReadTime(cls) -> int
```

Returns the total time spent reading from the disk (in milliseconds).
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskWriteTime"></a>

#### DiskWriteTime

```python
@classmethod
def DiskWriteTime(cls) -> int
```

Returns the total time spent writing to the disk (in milliseconds).
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskIOMerges"></a>

#### DiskIOMerges

```python
@classmethod
def DiskIOMerges(cls) -> int
```

Returns the total number of merged I/O operations.
Delegates to the Disk class methods (Linux only).

<a id="phardwareitk.System.SysUsage.System.DiskQueueDepth"></a>

#### DiskQueueDepth

```python
@classmethod
def DiskQueueDepth(cls) -> int
```

Returns the current disk I/O queue depth.
Delegates to the Disk class methods (Linux only).

<a id="phardwareitk.System.SysUsage.System.DiskHealth"></a>

#### DiskHealth

```python
@classmethod
def DiskHealth(cls, device: str) -> dict
```

Returns the SMART health status of a disk.
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.DiskTemp"></a>

#### DiskTemp

```python
@classmethod
def DiskTemp(cls, device: str) -> float
```

Returns the temperature of the disk (if supported).
Delegates to the Disk class methods.

<a id="phardwareitk.System.SysUsage.System.RAMInfo"></a>

#### RAMInfo

```python
@classmethod
def RAMInfo(cls) -> dict
```

Returns overall system RAM information (total, available, used, percent).

<a id="phardwareitk.System.SysUsage.System.RAMTotal"></a>

#### RAMTotal

```python
@classmethod
def RAMTotal(cls) -> float
```

Returns total RAM in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMAvailable"></a>

#### RAMAvailable

```python
@classmethod
def RAMAvailable(cls) -> float
```

Returns available RAM in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMUsed"></a>

#### RAMUsed

```python
@classmethod
def RAMUsed(cls) -> float
```

Returns used RAM in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMPercent"></a>

#### RAMPercent

```python
@classmethod
def RAMPercent(cls) -> float
```

Returns percentage of RAM used.

<a id="phardwareitk.System.SysUsage.System.RAMActive"></a>

#### RAMActive

```python
@classmethod
def RAMActive(cls) -> float
```

Returns active RAM in bytes (used for active processes).

<a id="phardwareitk.System.SysUsage.System.RAMBuffered"></a>

#### RAMBuffered

```python
@classmethod
def RAMBuffered(cls) -> float
```

Returns buffered RAM in bytes (used for temporary caching).

<a id="phardwareitk.System.SysUsage.System.RAMShared"></a>

#### RAMShared

```python
@classmethod
def RAMShared(cls) -> float
```

Returns shared RAM in bytes (used by multiple processes).

<a id="phardwareitk.System.SysUsage.System.RAMSlab"></a>

#### RAMSlab

```python
@classmethod
def RAMSlab(cls) -> float
```

Returns slab memory in bytes (kernel memory used to cache objects).

<a id="phardwareitk.System.SysUsage.System.RAMFree"></a>

#### RAMFree

```python
@classmethod
def RAMFree(cls) -> float
```

Returns free RAM in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMUsedByProcesses"></a>

#### RAMUsedByProcesses

```python
@classmethod
def RAMUsedByProcesses(cls) -> list
```

Returns memory used by processes in a list of dictionaries.

<a id="phardwareitk.System.SysUsage.System.RAMSwapTotal"></a>

#### RAMSwapTotal

```python
@classmethod
def RAMSwapTotal(cls) -> float
```

Returns total swap memory used for RAM overflow (if applicable).

<a id="phardwareitk.System.SysUsage.System.RAMSwapUsed"></a>

#### RAMSwapUsed

```python
@classmethod
def RAMSwapUsed(cls) -> float
```

Returns used swap memory in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMSwapFree"></a>

#### RAMSwapFree

```python
@classmethod
def RAMSwapFree(cls) -> float
```

Returns free swap memory in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMSwapPercent"></a>

#### RAMSwapPercent

```python
@classmethod
def RAMSwapPercent(cls) -> float
```

Returns swap memory usage percentage.

<a id="phardwareitk.System.SysUsage.System.RAMSwapInUse"></a>

#### RAMSwapInUse

```python
@classmethod
def RAMSwapInUse(cls) -> bool
```

Returns True if swap memory is in use, otherwise False.

<a id="phardwareitk.System.SysUsage.System.RAMBufferInfo"></a>

#### RAMBufferInfo

```python
@classmethod
def RAMBufferInfo(cls) -> dict
```

Returns detailed memory buffer information.

<a id="phardwareitk.System.SysUsage.System.RAMPhysicalMemory"></a>

#### RAMPhysicalMemory

```python
@classmethod
def RAMPhysicalMemory(cls) -> float
```

Returns total physical memory (RAM) in bytes.

<a id="phardwareitk.System.SysUsage.System.RAMActiveProcessMemory"></a>

#### RAMActiveProcessMemory

```python
@classmethod
def RAMActiveProcessMemory(cls, pid: int) -> float
```

Returns memory used by a specific process (pid).

<a id="phardwareitk.System.SysUsage.System.Interfaces"></a>

#### Interfaces

```python
@classmethod
def Interfaces(cls) -> Union[dict[str, dict], str]
```

Returns a dictionary of network interfaces, their addresses, and stats. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.InterfaceStats"></a>

#### InterfaceStats

```python
@classmethod
def InterfaceStats(cls) -> Union[dict[str, dict], str]
```

Returns the stats (bytes, packets, errors, drops, etc.) for each network interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.NetworkConnections"></a>

#### NetworkConnections

```python
@classmethod
def NetworkConnections(cls, kind: str = 'inet') -> Union[list, str]
```

Returns a list of network connections of the specified type (TCP, UDP, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.NetworkStats"></a>

#### NetworkStats

```python
@classmethod
def NetworkStats(cls) -> Union[dict[str, Union[int, float]], str]
```

Returns global network statistics like bytes sent, received, errors, etc. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.InterfaceNetworkStats"></a>

#### InterfaceNetworkStats

```python
@classmethod
def InterfaceNetworkStats(cls, interface: str) -> Union[dict, str]
```

Returns per-interface network stats (bytes sent, received, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.DefaultGateway"></a>

#### DefaultGateway

```python
@classmethod
def DefaultGateway(cls) -> Union[dict[str, str], str]
```

Returns the default gateway for the system. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.DNSConfig"></a>

#### DNSConfig

```python
@classmethod
def DNSConfig(cls) -> Union[dict[str, list], str]
```

Returns DNS configuration for the system (DNS servers). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.IPAddress"></a>

#### IPAddress

```python
@classmethod
def IPAddress(cls, interface: str) -> Union[str, str]
```

Returns the IP address of a given interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.MACAddress"></a>

#### MACAddress

```python
@classmethod
def MACAddress(cls, interface: str) -> Union[str, str]
```

Returns the MAC address of a given interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.Hostname"></a>

#### Hostname

```python
@classmethod
def Hostname(cls) -> Union[str, str]
```

Returns the hostname of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.FQDN"></a>

#### FQDN

```python
@classmethod
def FQDN(cls) -> Union[str, str]
```

Returns the fully qualified domain name (FQDN) of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.LocalIPAddress"></a>

#### LocalIPAddress

```python
@classmethod
def LocalIPAddress(cls) -> Union[str, str]
```

Returns the local IP address of the machine. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.InterfaceState"></a>

#### InterfaceState

```python
@classmethod
def InterfaceState(cls, interface: str) -> Union[str, str]
```

Returns the current state (UP/DOWN) of the network interface. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.IsInterfaceUp"></a>

#### IsInterfaceUp

```python
@classmethod
def IsInterfaceUp(cls, interface: str) -> Union[bool, str]
```

Returns True if the network interface is up, False otherwise. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.NetworkConnectionsByPID"></a>

#### NetworkConnectionsByPID

```python
@classmethod
def NetworkConnectionsByPID(cls, pid: int) -> Union[list, str]
```

Returns network connections by the process ID (PID). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.LocalPortsInUse"></a>

#### LocalPortsInUse

```python
@classmethod
def LocalPortsInUse(cls) -> Union[list, str]
```

Returns a list of local ports in use. (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.ExternalIPAddress"></a>

#### ExternalIPAddress

```python
@classmethod
def ExternalIPAddress(cls) -> Union[str, str]
```

Returns the external IP address of the system (if available).

<a id="phardwareitk.System.SysUsage.System.InterfaceType"></a>

#### InterfaceType

```python
@classmethod
def InterfaceType(cls, interface: str) -> Union[str, str]
```

Returns the type of a network interface (e.g., ethernet, wifi). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.ConnectionStatus"></a>

#### ConnectionStatus

```python
@classmethod
def ConnectionStatus(cls, connection) -> Union[str, str]
```

Returns the status of a network connection (ESTABLISHED, LISTEN, etc.). (Linux, Windows only)

<a id="phardwareitk.System.SysUsage.System.Netmask"></a>

#### Netmask

```python
@classmethod
def Netmask(cls, interface: str) -> Union[str, str]
```

Returns the netmask of the given network interface. (Linux, Windows only)

<a id="phardwareitk.System"></a>

# phardwareitk.System

Provides System Functionality

<a id="phardwareitk.System.os"></a>

## os

<a id="phardwareitk.System.sys"></a>

## sys

<a id="phardwareitk.System.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.System.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.Dependencies"></a>

# phardwareitk.Dependencies

Allows to dynamically download any PHardwareITK used dependency (NOTE: These dependencies are not required to be downloaded)

<a id="phardwareitk.Dependencies.*"></a>

## \*

<a id="phardwareitk.Dependencies.os"></a>

## os

<a id="phardwareitk.Dependencies.Requirements"></a>

## Requirements Objects

```python
class Requirements()
```

<a id="phardwareitk.Dependencies.Requirements.Modules"></a>

#### Modules

```python
@staticmethod
def Modules(mode: Union[str, None, list] = None) -> Union[str, list, None]
```

**Arguments**:

- `mode` _Union[str, None, list]_ - This argument allows the program to understand the specified mode. modes ->
- `str` - Returns the string representation of the required modules seperated via ' '.
- `list` - Returns the list representation of the required modules.
- `None` - Downloads the required modules.
  

**Returns**:

  Union[str, list, None]: Returned Type will be the mode type.

<a id="phardwareitk.ModuleController.main"></a>

# phardwareitk.ModuleController.main

<a id="phardwareitk.ModuleController.main.os"></a>

## os

<a id="phardwareitk.ModuleController.main.sys"></a>

## sys

<a id="phardwareitk.ModuleController.main.*"></a>

## \*

<a id="phardwareitk.ModuleController.main.LIB"></a>

## LIB

<a id="phardwareitk.ModuleController.main.CompilerOptions"></a>

## CompilerOptions Objects

```python
class CompilerOptions()
```

NOTE: Encryption is only supported in PHITKfile format.

<a id="phardwareitk.ModuleController.main.CompilerOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(format_: str = "COMPILER_pheonix$phardwareitk$v0001",
             output_format_: str = "PHITKfile",
             encrypt: bool = True) -> None
```

NOTE: Encryption is only supported in PHITKfile format.

<a id="phardwareitk.ModuleController.main.Compiler"></a>

## Compiler Objects

```python
class Compiler()
```

Main Module Handler Compiler for phardwareitk

<a id="phardwareitk.ModuleController.main.Compiler.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    path: str = LIB.Paths.defrunSettingsNOEXT,
    compilerOptions: CompilerOptions = CompilerOptions()
) -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.encrypt"></a>

#### encrypt

```python
def encrypt(data: str) -> bytes
```

<a id="phardwareitk.ModuleController.main.Compiler.decrypt"></a>

#### decrypt

```python
def decrypt(data: bytes) -> str
```

<a id="phardwareitk.ModuleController.main.Compiler.get"></a>

#### get

```python
def get(name: str, section: Union[None, str] = None) -> str
```

<a id="phardwareitk.ModuleController.main.Compiler.set"></a>

#### set

```python
def set(name: str,
        value: Union[int, str, dict],
        section: Union[None, str] = None) -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.makeSection"></a>

#### makeSection

```python
def makeSection(section: str) -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.decompile_v0001"></a>

#### decompile\_v0001

```python
def decompile_v0001() -> dict
```

<a id="phardwareitk.ModuleController.main.Compiler.decompile_v0002"></a>

#### decompile\_v0002

```python
def decompile_v0002() -> dict
```

<a id="phardwareitk.ModuleController.main.Compiler.load"></a>

#### load

```python
def load() -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.getFromFile"></a>

#### getFromFile

```python
def getFromFile() -> str
```

<a id="phardwareitk.ModuleController.main.Compiler.Clear"></a>

#### Clear

```python
def Clear() -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.finalize_v0001"></a>

#### finalize\_v0001

```python
def finalize_v0001() -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.finalize_v0002"></a>

#### finalize\_v0002

```python
def finalize_v0002() -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.finalize"></a>

#### finalize

```python
def finalize() -> None
```

<a id="phardwareitk.ModuleController.main.Compiler.saveToFile"></a>

#### saveToFile

```python
def saveToFile(clearAfterSave: bool = True) -> None
```

<a id="phardwareitk.ModuleController.main.PHardwareITK"></a>

## PHardwareITK Objects

```python
class PHardwareITK()
```

<a id="phardwareitk.ModuleController.main.PHardwareITK.check_file"></a>

#### check\_file

```python
@staticmethod
def check_file(filename: str = LIB.Paths.defrunSettingsNOEXT) -> bool
```

<a id="phardwareitk.ModuleController"></a>

# phardwareitk.ModuleController

Pretty much not useful for many unless finished

<a id="phardwareitk.ModuleController.os"></a>

## os

<a id="phardwareitk.ModuleController.sys"></a>

## sys

<a id="phardwareitk.ModuleController.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.ModuleController.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.CLI.cliToolKit"></a>

# phardwareitk.CLI.cliToolKit

<a id="phardwareitk.CLI.cliToolKit.sys"></a>

## sys

<a id="phardwareitk.CLI.cliToolKit.os"></a>

## os

<a id="phardwareitk.CLI.cliToolKit.*"></a>

## \*

<a id="phardwareitk.CLI.cliToolKit.*"></a>

## \*

<a id="phardwareitk.CLI.cliToolKit.HyperIn"></a>

## HyperIn

<a id="phardwareitk.CLI.cliToolKit.HyperOut"></a>

## HyperOut

<a id="phardwareitk.CLI.cliToolKit.Extensions"></a>

## Extensions

<a id="phardwareitk.CLI.cliToolKit.Cursor"></a>

## Cursor Objects

```python
class Cursor()
```

A Class dedicated to cursor operations in command line.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorX"></a>

#### MoveCursorX

```python
@staticmethod
def MoveCursorX(x: int) -> None
```

Moves the cursor to the specified X postion.

**Arguments**:

- `x` _int_ - X coordinate.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursor"></a>

#### MoveCursor

```python
@staticmethod
def MoveCursor(x: int, y: int) -> None
```

Move Cursor to specified position.

**Arguments**:

- `x` _int_ - The X coordinate.
- `y` _int_ - the Y coordinate.

<a id="phardwareitk.CLI.cliToolKit.Cursor.HideCursor"></a>

#### HideCursor

```python
@staticmethod
def HideCursor() -> None
```

Hide the cursor.

<a id="phardwareitk.CLI.cliToolKit.Cursor.ShowCusor"></a>

#### ShowCusor

```python
@staticmethod
def ShowCusor() -> None
```

Show the cursor.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorUp"></a>

#### MoveCursorUp

```python
@staticmethod
def MoveCursorUp(n: int) -> None
```

Move cursor up by n lines.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorDown"></a>

#### MoveCursorDown

```python
@staticmethod
def MoveCursorDown(n: int) -> None
```

Move cursor down by n lines.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorRight"></a>

#### MoveCursorRight

```python
@staticmethod
def MoveCursorRight(n: int) -> None
```

Move cursor right by n columns.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorLeft"></a>

#### MoveCursorLeft

```python
@staticmethod
def MoveCursorLeft(n: int) -> None
```

Move cursor left by n columns.

<a id="phardwareitk.CLI.cliToolKit.Cursor.SaveCursorPosition"></a>

#### SaveCursorPosition

```python
@staticmethod
def SaveCursorPosition() -> None
```

Save the current cursor position.

<a id="phardwareitk.CLI.cliToolKit.Cursor.RestoreCursorPosition"></a>

#### RestoreCursorPosition

```python
@staticmethod
def RestoreCursorPosition() -> None
```

Restore the cursor to its last saved position.

<a id="phardwareitk.CLI.cliToolKit.Cursor.SetCursorToBeginningOfLine"></a>

#### SetCursorToBeginningOfLine

```python
@staticmethod
def SetCursorToBeginningOfLine() -> None
```

Move the cursor to the beginning of the current line.

<a id="phardwareitk.CLI.cliToolKit.Cursor.SetCursorToEndOfLine"></a>

#### SetCursorToEndOfLine

```python
@staticmethod
def SetCursorToEndOfLine() -> None
```

Move the cursor to the end of the current line.

<a id="phardwareitk.CLI.cliToolKit.Cursor.HideCursorTemporarily"></a>

#### HideCursorTemporarily

```python
@staticmethod
def HideCursorTemporarily() -> None
```

Temporarily hide the cursor (until next action).

<a id="phardwareitk.CLI.cliToolKit.Cursor.ShowCursorTemporarily"></a>

#### ShowCursorTemporarily

```python
@staticmethod
def ShowCursorTemporarily() -> None
```

Temporarily show the cursor again after it was hidden.

<a id="phardwareitk.CLI.cliToolKit.Cursor.SetCursorPositionToHome"></a>

#### SetCursorPositionToHome

```python
@staticmethod
def SetCursorPositionToHome() -> None
```

Set the cursor to the top left corner (1, 1).

<a id="phardwareitk.CLI.cliToolKit.Cursor.SetCursorPositionToEnd"></a>

#### SetCursorPositionToEnd

```python
@staticmethod
def SetCursorPositionToEnd() -> None
```

Set the cursor to the bottom right corner of the terminal.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveToNextWord"></a>

#### MoveToNextWord

```python
@staticmethod
def MoveToNextWord() -> None
```

Move the cursor to the next word.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveToPreviousWord"></a>

#### MoveToPreviousWord

```python
@staticmethod
def MoveToPreviousWord() -> None
```

Move the cursor to the previous word.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorToTop"></a>

#### MoveCursorToTop

```python
@staticmethod
def MoveCursorToTop() -> None
```

Move the cursor to the top of the terminal.

<a id="phardwareitk.CLI.cliToolKit.Cursor.MoveCursorToBottom"></a>

#### MoveCursorToBottom

```python
@staticmethod
def MoveCursorToBottom() -> None
```

Move the cursor to the bottom of the terminal.

<a id="phardwareitk.CLI.cliToolKit.Cursor.SetCursorVisibility"></a>

#### SetCursorVisibility

```python
@staticmethod
def SetCursorVisibility(is_visible: bool) -> None
```

Set the cursor visibility.

<a id="phardwareitk.CLI.cliToolKit.Cursor.CurrentCursorPosition"></a>

#### CurrentCursorPosition

```python
@staticmethod
def CurrentCursorPosition() -> tuple
```

Get the current cursor position using BLOCKING. (row(y), column(x)).

<a id="phardwareitk.CLI.cliToolKit.Screen"></a>

## Screen Objects

```python
class Screen()
```

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearCurrentLine"></a>

#### ClearCurrentLine

```python
@staticmethod
def ClearCurrentLine() -> None
```

Clear the current line.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearLine"></a>

#### ClearLine

```python
@staticmethod
def ClearLine(y: int) -> None
```

Clear a specified line.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearScreen"></a>

#### ClearScreen

```python
@staticmethod
def ClearScreen() -> None
```

Clear the entire screen.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearScreenFromCursorDown"></a>

#### ClearScreenFromCursorDown

```python
@staticmethod
def ClearScreenFromCursorDown() -> None
```

Clear the screen from the cursor's current position to the bottom.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearScreenFromCursorUp"></a>

#### ClearScreenFromCursorUp

```python
@staticmethod
def ClearScreenFromCursorUp() -> None
```

Clear the screen from the cursor's current position to the top.

<a id="phardwareitk.CLI.cliToolKit.Screen.SetScreenBackgroundColor"></a>

#### SetScreenBackgroundColor

```python
@staticmethod
def SetScreenBackgroundColor(color: str) -> None
```

Set the background color of the terminal.

<a id="phardwareitk.CLI.cliToolKit.Screen.SetScreenForegroundColor"></a>

#### SetScreenForegroundColor

```python
@staticmethod
def SetScreenForegroundColor(color: str) -> None
```

Set the foreground color of the terminal.

<a id="phardwareitk.CLI.cliToolKit.Screen.SetScreenColorReset"></a>

#### SetScreenColorReset

```python
@staticmethod
def SetScreenColorReset() -> None
```

Reset the screen's colors to default.

<a id="phardwareitk.CLI.cliToolKit.Screen.HideScreenCursor"></a>

#### HideScreenCursor

```python
@staticmethod
def HideScreenCursor() -> None
```

Hide the terminal cursor.

<a id="phardwareitk.CLI.cliToolKit.Screen.ShowScreenCursor"></a>

#### ShowScreenCursor

```python
@staticmethod
def ShowScreenCursor() -> None
```

Show the terminal cursor.

<a id="phardwareitk.CLI.cliToolKit.Screen.GetTerminalSize"></a>

#### GetTerminalSize

```python
@staticmethod
def GetTerminalSize() -> tuple
```

Get the current terminal size (rows, columns).

<a id="phardwareitk.CLI.cliToolKit.Screen.SetTerminalSize"></a>

#### SetTerminalSize

```python
@staticmethod
def SetTerminalSize(rows: int, cols: int) -> None
```

Set the terminal size.

<a id="phardwareitk.CLI.cliToolKit.Screen.EnableAlternateScreenBuffer"></a>

#### EnableAlternateScreenBuffer

```python
@staticmethod
def EnableAlternateScreenBuffer() -> None
```

Enable the alternate screen buffer.

<a id="phardwareitk.CLI.cliToolKit.Screen.DisableAlternateScreenBuffer"></a>

#### DisableAlternateScreenBuffer

```python
@staticmethod
def DisableAlternateScreenBuffer() -> None
```

Disable the alternate screen buffer.

<a id="phardwareitk.CLI.cliToolKit.Screen.ScrollUp"></a>

#### ScrollUp

```python
@staticmethod
def ScrollUp(n: int) -> None
```

Scroll up n lines in the terminal.

<a id="phardwareitk.CLI.cliToolKit.Screen.ScrollDown"></a>

#### ScrollDown

```python
@staticmethod
def ScrollDown(n: int) -> None
```

Scroll down n lines in the terminal.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearTabs"></a>

#### ClearTabs

```python
@staticmethod
def ClearTabs() -> None
```

Clear all tab stops in the terminal.

<a id="phardwareitk.CLI.cliToolKit.Screen.SetTab"></a>

#### SetTab

```python
@staticmethod
def SetTab() -> None
```

Set a tab stop at the current cursor position.

<a id="phardwareitk.CLI.cliToolKit.Screen.ResetTerminal"></a>

#### ResetTerminal

```python
@staticmethod
def ResetTerminal() -> None
```

Reset the terminal to its default state.

<a id="phardwareitk.CLI.cliToolKit.Screen.SetCursorStyle"></a>

#### SetCursorStyle

```python
@staticmethod
def SetCursorStyle(style: int) -> None
```

Set the cursor style (0: block, 1: underline, 2: bar).

<a id="phardwareitk.CLI.cliToolKit.Screen.EnableRawMode"></a>

#### EnableRawMode

```python
@staticmethod
def EnableRawMode() -> None
```

Enable raw mode (no input processing).

<a id="phardwareitk.CLI.cliToolKit.Screen.DisableRawMode"></a>

#### DisableRawMode

```python
@staticmethod
def DisableRawMode() -> None
```

Disable raw mode.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearFromCursorToTop"></a>

#### ClearFromCursorToTop

```python
@staticmethod
def ClearFromCursorToTop() -> None
```

Clear The Screen from the cursor to the top of the screen.

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearFromCursorToBottom"></a>

#### ClearFromCursorToBottom

```python
@staticmethod
def ClearFromCursorToBottom() -> None
```

Clear The Screen from the cursor to the bottom of the screen

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearFromCursorToEndOfLine"></a>

#### ClearFromCursorToEndOfLine

```python
@staticmethod
def ClearFromCursorToEndOfLine() -> None
```

Clear The Screen from the cursor to the end of the line

<a id="phardwareitk.CLI.cliToolKit.Screen.ClearCharacter"></a>

#### ClearCharacter

```python
@staticmethod
def ClearCharacter(x: int, y: int) -> None
```

Clear the character at the specified location (x, y).

<a id="phardwareitk.CLI.cliToolKit.Text"></a>

## Text Objects

```python
class Text()
```

<a id="phardwareitk.CLI.cliToolKit.Text.WriteText"></a>

#### WriteText

```python
@staticmethod
def WriteText(
    *values: object,
    seperator: Union[str, None] = " ",
    endl: Union[str, None] = "",
    File: Union[str, None] = None,
    Flush: bool = False,
    backgroundColorEnabled: bool = False,
    FontEnabled: bool = False,
    Font: Extensions.TextFont = Extensions.TextFont()
) -> None
```

Writes the specified text. (USES phardwareitk.Extensions.HyperOut.printH)

**Arguments**:

- `seperator` _Union[str, None], optional_ - Seperator between values in [*values]. Defaults to " ".
- `endl` _Union[str, None], optional_ - The ending string to include at the end of the values. None is don't want. Defaults to "
  ".
- `File` _Union[str, None], optional_ - Wether to save the print contents in a file before printing in console. Defaults to None.
- `Flush` _bool, optional_ - Wether to use Flush during printing. Defaults to False.
- `backgroundColorEnabled` _bool, optional_ - Wether to enable background-color. Defaults to None.
- `FontEnabled` _bool, optional_ - Wether to enable custom font. Defaults to False.
- `Font` _Extensions.TextFont, optional_ - The font. Defaults to Extensions.TextFont().

<a id="phardwareitk.CLI.cliToolKit.Text.InputText"></a>

#### InputText

```python
def InputText(
    *values: object,
    seperator: Union[str, None] = " ",
    endl: Union[str, None] = "\n",
    backgroundColorEnabled: bool = False,
    FontEnabled: bool = False,
    Font: Extensions.TextFont = Extensions.TextFont()
) -> str
```

Returns the entered user data from input. (USES phardwareitk.Extensions.HyperIn.inputH)

**Arguments**:

- `seperator` _Union[str, None], optional_ - Seperator between values in [*values]. Defaults to " ".
- `endl` _Union[str, None], optional_ - The ending string to include at the end of the values. None is don't want. Defaults to "
  ".
- `backgroundColorEnabled` _bool, optional_ - Wether to enable background-color. Defaults to False.
- `FontEnabled` _bool, optional_ - Wether to enable custom font. Defaults to False.
- `Font` _Extensions.TextFont, optional_ - The font. Defaults to Extensions.TextFont().
  

**Returns**:

- `str` - The user inputted string.

<a id="phardwareitk.CLI.cliToolKit.Text.DeleteChar"></a>

#### DeleteChar

```python
@staticmethod
def DeleteChar() -> None
```

Simulates Delete Key in terminal.

<a id="phardwareitk.CLI.cliToolKit.Text.BackSpaceChar"></a>

#### BackSpaceChar

```python
@staticmethod
def BackSpaceChar() -> None
```

Simulates Backspace in terminal.

<a id="phardwareitk.CLI"></a>

# phardwareitk.CLI

Provides Command Line Interface Tools

<a id="phardwareitk.CLI.os"></a>

## os

<a id="phardwareitk.CLI.sys"></a>

## sys

<a id="phardwareitk.CLI.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.CLI.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.HGame"></a>

# phardwareitk.HGame

Hardware Hyper Game (HGame).

To Use, pass parameters in **HGame_Settings**. Also no need to save it, as it has a automated system, to provide all functions with every parameter needed. Check file for code. And then the stage is yours!

<a id="phardwareitk.HGame.os"></a>

## os

<a id="phardwareitk.HGame.sys"></a>

## sys

<a id="phardwareitk.HGame.platform"></a>

## platform

<a id="phardwareitk.HGame.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.HGame.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.HGame.*"></a>

## \*

<a id="phardwareitk.HGame.HOut"></a>

## HOut

<a id="phardwareitk.HGame.HGame_OUT"></a>

## HGame\_OUT Objects

```python
class HGame_OUT()
```

This class defined **Output** locations available for HGame.

<a id="phardwareitk.HGame.HGame_OUT.console"></a>

#### console

```python
@staticmethod
def console() -> int
```

<a id="phardwareitk.HGame.HGame_OUT.stdout"></a>

#### stdout

```python
@staticmethod
def stdout() -> int
```

<a id="phardwareitk.HGame.HGame_OUT.messagebox"></a>

#### messagebox

```python
@staticmethod
def messagebox() -> int
```

<a id="phardwareitk.HGame.HGame_OUT.file"></a>

#### file

```python
@staticmethod
def file() -> int
```

<a id="phardwareitk.HGame.HGame_Settings"></a>

## HGame\_Settings Objects

```python
class HGame_Settings()
```

This class offers the settings for using HGame.

**Arguments**:

  output [HGame_OUT]: Defined where errors and logs will be displayed. Defaults to **HGame_OUT.stdout**
  debug [bool]: If true, Debug mode will be used. Defaults to False.
  filesystem_encrypt [bool]: If true, Creation of files via HGame_FileManager will be encrypted. Defaults to False.

<a id="phardwareitk.HGame.HGame_Settings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(output: HGame_OUT = HGame_OUT.stdout,
             debug: bool = False,
             filesystem_encrypt: bool = False) -> None
```

<a id="phardwareitk.HGame.HGame_Settings.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls)
```

<a id="phardwareitk.HGame.HGame_Settings.output_"></a>

#### output\_

```python
@property
def output_() -> int
```

<a id="phardwareitk.HGame.HGame_Settings.debug_"></a>

#### debug\_

```python
@property
def debug_() -> bool
```

<a id="phardwareitk.HGame.HGame_Settings.filesystem_encrypt_"></a>

#### filesystem\_encrypt\_

```python
@property
def filesystem_encrypt_() -> bool
```

<a id="phardwareitk.HGame.HGame_Settings.get_first_instance"></a>

#### get\_first\_instance

```python
@classmethod
def get_first_instance(cls)
```

<a id="phardwareitk.HGame.HGame_Settings.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="phardwareitk.HGame.HGame_Settings.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.HGame.gui"></a>

## gui

<a id="phardwareitk.HGame.GameObject"></a>

## GameObject Objects

```python
class GameObject()
```

Represents an entity within the game world.

**Attributes**:

- `name` _str_ - The name of the GameObject.
- `position` _tuple_ - The (x, y) coordinates of the GameObject.
- `components` _list_ - A list of Component objects attached to the GameObject.

<a id="phardwareitk.HGame.GameObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name="GameObject", position=(0, 0))
```

Initializes a new GameObject.

**Arguments**:

- `name` _str, optional_ - The name of the GameObject. Defaults to "GameObject".
- `position` _tuple, optional_ - The (x, y) coordinates. Defaults to (0, 0).

<a id="phardwareitk.HGame.GameObject.add_component"></a>

#### add\_component

```python
def add_component(component)
```

Adds a Component to the GameObject.

**Arguments**:

- `component` _Component_ - The Component object to add.

<a id="phardwareitk.HGame.GameObject.get_component"></a>

#### get\_component

```python
def get_component(component_type)
```

Retrieves a Component of a specific type.

**Arguments**:

- `component_type` _type_ - The type of Component to retrieve.
  

**Returns**:

  Component or None: The Component object if found, otherwise None.

<a id="phardwareitk.HGame.Component"></a>

## Component Objects

```python
class Component()
```

Base class for components that can be attached to GameObjects.

**Attributes**:

- `game_object` _GameObject or None_ - The GameObject this Component is attached to.

<a id="phardwareitk.HGame.Component.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes a new Component.

<a id="phardwareitk.HGame.Sprite"></a>

## Sprite Objects

```python
class Sprite(Component)
```

Represents a visual sprite for a GameObject.

**Attributes**:

- `image` _str_ - The path to the image file.

<a id="phardwareitk.HGame.Sprite.__init__"></a>

#### \_\_init\_\_

```python
def __init__(image)
```

Initializes a new Sprite.

**Arguments**:

- `image` _str_ - The path to the image file.

<a id="phardwareitk.HGame.Transform"></a>

## Transform Objects

```python
class Transform(Component)
```

Represents the position, rotation, and scale of a GameObject.

**Attributes**:

- `position` _tuple_ - The (x, y) coordinates.
- `rotation` _float_ - The rotation angle in degrees.
- `scale` _tuple_ - The (x, y) scale.

<a id="phardwareitk.HGame.Transform.__init__"></a>

#### \_\_init\_\_

```python
def __init__(position=(0, 0), rotation=0.0, scale=(1.0, 1.0))
```

Initializes a new Transform.

**Arguments**:

- `position` _tuple, optional_ - The (x, y) coordinates. Defaults to (0, 0).
- `rotation` _float, optional_ - The rotation angle. Defaults to 0.0.
- `scale` _tuple, optional_ - The (x, y) scale. Defaults to (1.0, 1.0).

<a id="phardwareitk.HGame.Script"></a>

## Script Objects

```python
class Script(Component)
```

Base class for user-defined scripts attached to GameObjects.

Users should override the Start, Update, and End methods.

<a id="phardwareitk.HGame.Script.start"></a>

#### start

```python
def start()
```

Called when the GameObject is created.

<a id="phardwareitk.HGame.Script.update"></a>

#### update

```python
def update()
```

Called every frame.

<a id="phardwareitk.HGame.Script.end"></a>

#### end

```python
def end()
```

Called when the GameObject is destroyed.

<a id="phardwareitk.HGame.Input"></a>

## Input Objects

```python
class Input()
```

Handles user input.

Class Methods:
get_key(key): Returns True if the specified key is pressed.
get_mouse_position(): Returns the current mouse position.

<a id="phardwareitk.HGame.Input.get_key"></a>

#### get\_key

```python
@staticmethod
def get_key(key)
```

Checks if a key is currently pressed.

**Arguments**:

- `key` _str_ - The key to check (e.g., "W", "SPACE", "LEFT").
  

**Returns**:

- `bool` - True if the key is pressed, False otherwise.

<a id="phardwareitk.HGame.Input.get_mouse_position"></a>

#### get\_mouse\_position

```python
@staticmethod
def get_mouse_position()
```

Returns the current mouse position.

**Returns**:

- `tuple` - The (x, y) coordinates of the mouse.

<a id="phardwareitk.HGame.Scene"></a>

## Scene Objects

```python
class Scene()
```

Represents a game scene containing GameObjects.

**Attributes**:

- `game_objects` _list_ - A list of GameObjects in the scene.

<a id="phardwareitk.HGame.Scene.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes a new Scene.

<a id="phardwareitk.HGame.Scene.add_game_object"></a>

#### add\_game\_object

```python
def add_game_object(game_object)
```

Adds a GameObject to the scene.

**Arguments**:

- `game_object` _GameObject_ - The GameObject to add.

<a id="phardwareitk.HGame.Scene.remove_game_object"></a>

#### remove\_game\_object

```python
def remove_game_object(game_object)
```

Removes a GameObject from the scene.

**Arguments**:

- `game_object` _GameObject_ - The GameObject to remove.

<a id="phardwareitk.GPU._gl_driver"></a>

# phardwareitk.GPU.\_gl\_driver

OpenGL Driver implementation using BaseGPUD class

<a id="phardwareitk.GPU._gl_driver.ctypes"></a>

## ctypes

<a id="phardwareitk.GPU._gl_driver.*"></a>

## \*

<a id="phardwareitk.GPU._gl_driver.sys"></a>

## sys

<a id="phardwareitk.GPU._gl_driver.Any"></a>

## Any

<a id="phardwareitk.GPU._gl_driver.Optional"></a>

## Optional

<a id="phardwareitk.GPU._gl_driver.PIonContext"></a>

## PIonContext

<a id="phardwareitk.GPU._gl_driver.BaseGPUD"></a>

## BaseGPUD

<a id="phardwareitk.GPU._gl_driver.platform"></a>

## platform

<a id="phardwareitk.GPU._gl_driver.GL_COLOR_BUFFER_BIT"></a>

#### GL\_COLOR\_BUFFER\_BIT

<a id="phardwareitk.GPU._gl_driver.GL_COMPILE_STATUS"></a>

#### GL\_COMPILE\_STATUS

<a id="phardwareitk.GPU._gl_driver.GL_LINK_STATUS"></a>

#### GL\_LINK\_STATUS

<a id="phardwareitk.GPU._gl_driver.GL_INFO_LOG_LENGTH"></a>

#### GL\_INFO\_LOG\_LENGTH

<a id="phardwareitk.GPU._gl_driver.GL_ARRAY_BUFFER"></a>

#### GL\_ARRAY\_BUFFER

<a id="phardwareitk.GPU._gl_driver.GL_STATIC_DRAW"></a>

#### GL\_STATIC\_DRAW

<a id="phardwareitk.GPU._gl_driver.GL_TEXTURE_2D"></a>

#### GL\_TEXTURE\_2D

<a id="phardwareitk.GPU._gl_driver.GL_RGBA"></a>

#### GL\_RGBA

<a id="phardwareitk.GPU._gl_driver.GL_UNSIGNED_BYTE"></a>

#### GL\_UNSIGNED\_BYTE

<a id="phardwareitk.GPU._gl_driver.GL_FRAMEBUFFER"></a>

#### GL\_FRAMEBUFFER

<a id="phardwareitk.GPU._gl_driver.GL_VERTEX_SHADER"></a>

#### GL\_VERTEX\_SHADER

<a id="phardwareitk.GPU._gl_driver.GL_FRAGMENT_SHADER"></a>

#### GL\_FRAGMENT\_SHADER

<a id="phardwareitk.GPU._gl_driver.PFD_DRAW_TO_WINDOW"></a>

#### PFD\_DRAW\_TO\_WINDOW

<a id="phardwareitk.GPU._gl_driver.PFD_SUPPORT_OPENGL"></a>

#### PFD\_SUPPORT\_OPENGL

<a id="phardwareitk.GPU._gl_driver.PFD_DOUBLEBUFFER"></a>

#### PFD\_DOUBLEBUFFER

<a id="phardwareitk.GPU._gl_driver.PFD_TYPE_RGBA"></a>

#### PFD\_TYPE\_RGBA

<a id="phardwareitk.GPU._gl_driver.PFD_MAIN_PLANE"></a>

#### PFD\_MAIN\_PLANE

<a id="phardwareitk.GPU._gl_driver.FuncType"></a>

#### FuncType

<a id="phardwareitk.GPU._gl_driver.UnsupportedPlatform"></a>

## UnsupportedPlatform Objects

```python
class UnsupportedPlatform(Exception)
```

<a id="phardwareitk.GPU._gl_driver.UnsupportedPlatform.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message="Unsupported platform for window creation")
```

<a id="phardwareitk.GPU._gl_driver.GLFunctions"></a>

## GLFunctions Objects

```python
class GLFunctions()
```

Wrapper for OpenGL functions — dynamically loads and binds symbols.

<a id="phardwareitk.GPU._gl_driver.GLFunctions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(driver)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver"></a>

## GLDriver Objects

```python
class GLDriver(BaseGPUD)
```

Cross Platform OpenGL Driver

<a id="phardwareitk.GPU._gl_driver.GLDriver.__init__"></a>

#### \_\_init\_\_

```python
def __init__(libGL: Optional[str] = None, screen: Optional[int] = None)
```

Initialization

**Arguments**:

- `libGL` _Optional, str_ - The path to the OpenGL Library, if None this class automatically tries to get it based on OS. Defaults to None
- `screen` _Optional, c_int_ - The screen to use, if None this class tries to get it based on the OS, Defaults to None.

<a id="phardwareitk.GPU._gl_driver.GLDriver.init"></a>

#### init

```python
def init(display: Any, window: Any, create_and_attach_ctx: bool = False)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.clear"></a>

#### clear

```python
def clear(r: int, g: int, b: int, a: int)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.swap"></a>

#### swap

```python
def swap()
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.shutdown"></a>

#### shutdown

```python
def shutdown()
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.load_function"></a>

#### load\_function

```python
def load_function(name: str) -> c_void_p
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.destroy_context"></a>

#### destroy\_context

```python
def destroy_context()
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_context"></a>

#### create\_context

```python
def create_context(display, window)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.check_gl_error"></a>

#### check\_gl\_error

```python
def check_gl_error(func: str = "Unknown")
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.check_error"></a>

#### check\_error

```python
def check_error()
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.viewport"></a>

#### viewport

```python
def viewport(w: int = 800, h: int = 600)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_shader"></a>

#### create\_shader

```python
def create_shader(shader_type: int, source: str) -> int
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_program"></a>

#### create\_program

```python
def create_program(vertex_shader: int, fragment_shader: int) -> int
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.use_program"></a>

#### use\_program

```python
def use_program(program: int)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_buffer"></a>

#### create\_buffer

```python
def create_buffer() -> int
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.bind_array_buffer"></a>

#### bind\_array\_buffer

```python
def bind_array_buffer(buf: int)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.buffer_data"></a>

#### buffer\_data

```python
def buffer_data(data, usage: int = GL_STATIC_DRAW)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_texture"></a>

#### create\_texture

```python
def create_texture() -> int
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.bind_texture"></a>

#### bind\_texture

```python
def bind_texture(texture: int, target: int = GL_TEXTURE_2D)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.tex_image_2d"></a>

#### tex\_image\_2d

```python
def tex_image_2d(width: int,
                 height: int,
                 data: Any = None,
                 target: int = GL_TEXTURE_2D,
                 internal_format: int = 0x1908,
                 format_: int = 0x1908,
                 type_: int = 0x1401)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.create_framebuffer"></a>

#### create\_framebuffer

```python
def create_framebuffer() -> int
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.bind_framebuffer"></a>

#### bind\_framebuffer

```python
def bind_framebuffer(fbo: int, target: int = GL_FRAMEBUFFER)
```

<a id="phardwareitk.GPU._gl_driver.GLDriver.set_uniform_mat4"></a>

#### set\_uniform\_mat4

```python
def set_uniform_mat4(program: int, name: str, mat)
```

<a id="phardwareitk.GPU.SysInfo"></a>

# phardwareitk.GPU.SysInfo

<a id="phardwareitk.GPU.SysInfo.platform"></a>

## platform

<a id="phardwareitk.GPU.SysInfo.os"></a>

## os

<a id="phardwareitk.GPU.SysInfo.platform"></a>

#### platform

<a id="phardwareitk.GPU.SysInfo.Windows"></a>

#### Windows

<a id="phardwareitk.GPU.SysInfo.Linux"></a>

#### Linux

<a id="phardwareitk.GPU.SysInfo.Kali"></a>

#### Kali

<a id="phardwareitk.GPU.SysInfo.MacOs"></a>

#### MacOs

<a id="phardwareitk.GPU.SysInfo.Ubuntu"></a>

#### Ubuntu

<a id="phardwareitk.GPU._base"></a>

# phardwareitk.GPU.\_base

Base Class for GPU drivers

<a id="phardwareitk.GPU._base.Any"></a>

## Any

<a id="phardwareitk.GPU._base.BaseGPUD"></a>

## BaseGPUD Objects

```python
class BaseGPUD()
```

Abstract GPU backend interface

<a id="phardwareitk.GPU._base.BaseGPUD.init"></a>

#### init

```python
def init(display: Any, window: Any, create_and_attach_ctx: bool = False)
```

Initialize GPU context for the specified window

<a id="phardwareitk.GPU._base.BaseGPUD.clear"></a>

#### clear

```python
def clear(r: int, g: int, b: int, a: int)
```

Clear screen to a color.

<a id="phardwareitk.GPU._base.BaseGPUD.swap"></a>

#### swap

```python
def swap()
```

Swap framebuffers / present frame.

<a id="phardwareitk.GPU._base.BaseGPUD.shutdown"></a>

#### shutdown

```python
def shutdown()
```

Release context and resources.

<a id="phardwareitk.GPU._base.BaseGPUD.load_function"></a>

#### load\_function

```python
def load_function(name: str)
```

Get a raw pointer to a GPU function (e.g. glDrawArrays).

<a id="phardwareitk.GPU._base.BaseGPUD.create_context"></a>

#### create\_context

```python
def create_context(display: Any, window: Any)
```

Returns the Created context in form of PIonContext

<a id="phardwareitk.GPU._base.BaseGPUD.destroy_context"></a>

#### destroy\_context

```python
def destroy_context()
```

Destroys the created context

<a id="phardwareitk.GPU._base.BaseGPUD.viewport"></a>

#### viewport

```python
def viewport(w: int = 800, h: int = 600)
```

Changes/Makes the viewport

<a id="phardwareitk.GPU._base.BaseGPUD.create_shader"></a>

#### create\_shader

```python
def create_shader(shader_type: str, source: str)
```

Creates a shader

<a id="phardwareitk.GPU._base.BaseGPUD.create_program"></a>

#### create\_program

```python
def create_program(vertex_shader: Any, fragment_shader: Any)
```

Creates a program based on the shader's provided

<a id="phardwareitk.GPU._base.BaseGPUD.use_program"></a>

#### use\_program

```python
def use_program(program: Any)
```

Uses a creates program

<a id="phardwareitk.GPU._base.BaseGPUD.create_buffer"></a>

#### create\_buffer

```python
def create_buffer()
```

Creates a GPU Buffer

<a id="phardwareitk.GPU._base.BaseGPUD.bind_array_buffer"></a>

#### bind\_array\_buffer

```python
def bind_array_buffer(buf: Any)
```

Binds a Array buffer to the GPU

<a id="phardwareitk.GPU._base.BaseGPUD.buffer_data"></a>

#### buffer\_data

```python
def buffer_data(data: Any, usage: Any)
```

Creats and initializes the buffer's data

<a id="phardwareitk.GPU._base.BaseGPUD.create_texture"></a>

#### create\_texture

```python
def create_texture()
```

Creates a texture

<a id="phardwareitk.GPU._base.BaseGPUD.bind_texture"></a>

#### bind\_texture

```python
def bind_texture(texture: Any, target: Any)
```

Binds the created texture to the GPU

<a id="phardwareitk.GPU._base.BaseGPUD.tex_image_2d"></a>

#### tex\_image\_2d

```python
def tex_image_2d(width: int, height: int, data: Any, target: Any,
                 internal_format: Any, format_: Any, type_: Any)
```

Texture Image 2D

<a id="phardwareitk.GPU._base.BaseGPUD.create_framebuffer"></a>

#### create\_framebuffer

```python
def create_framebuffer()
```

Creates a framebuffer

<a id="phardwareitk.GPU._base.BaseGPUD.bind_framebuffer"></a>

#### bind\_framebuffer

```python
def bind_framebuffer(fbo: Any, target: Any)
```

Binds the created framebuffer to the GPU

<a id="phardwareitk.GPU._base.BaseGPUD.set_uniform_mat4"></a>

#### set\_uniform\_mat4

```python
def set_uniform_mat4(program: Any, name: str, mat: Any)
```

Set the value of a mat4 variable in a shader

<a id="phardwareitk.GPU._base.BaseGPUD.check_error"></a>

#### check\_error

```python
def check_error()
```

Checks for error

<a id="phardwareitk.GPU.StressTester.run"></a>

# phardwareitk.GPU.StressTester.run

<a id="phardwareitk.GPU.StressTester.run.sys"></a>

## sys

<a id="phardwareitk.GPU.StressTester.run.os"></a>

## os

<a id="phardwareitk.GPU.StressTester.run.baseDir"></a>

#### baseDir

<a id="phardwareitk.GPU.StressTester.run.*"></a>

## \*

<a id="phardwareitk.GPU.StressTester.run.*"></a>

## \*

<a id="phardwareitk.GPU.StressTester.run.*"></a>

## \*

<a id="phardwareitk.GPU.StressTester.run.time"></a>

## time

<a id="phardwareitk.GPU.StressTester.run.clinfo"></a>

#### clinfo

<a id="phardwareitk.GPU.StressTester.run.stress_test_torch"></a>

#### stress\_test\_torch

```python
def stress_test_torch(duration=60, tensor_size=3000)
```

Stress test for CUDA or ROCm GPUs using PyTorch.

<a id="phardwareitk.GPU.StressTester.run.stress_test_opencl"></a>

#### stress\_test\_opencl

```python
def stress_test_opencl(duration=60, tensor_size=1024)
```

Stress test for OpenCL-supported GPUs.

<a id="phardwareitk.GPU.StressTester.run.util"></a>

## util

<a id="phardwareitk.GPU.StressTester.run.rq_mod"></a>

#### rq\_mod

<a id="phardwareitk.GPU.StressTester.run.iterations"></a>

#### iterations

<a id="phardwareitk.GPU.StressTester.run.elapsed_time"></a>

#### elapsed\_time

<a id="phardwareitk.GPU.StressTester.run.ranking"></a>

#### ranking

<a id="phardwareitk.GPU.StressTester.run.stress_levels"></a>

#### stress\_levels

<a id="phardwareitk.GPU.StressTester.run.pps"></a>

#### pps

<a id="phardwareitk.GPU.StressTester.run.memAll"></a>

#### memAll

<a id="phardwareitk.GPU.StressTester.run.memPer"></a>

#### memPer

<a id="phardwareitk.GPU.StressTester.run.TotalMem"></a>

#### TotalMem

<a id="phardwareitk.GPU.StressTester.run.type_"></a>

#### type\_

<a id="phardwareitk.GPU.StressTester.run.dur"></a>

#### dur

<a id="phardwareitk.GPU.StressTester.run.dur"></a>

#### dur

<a id="phardwareitk.GPU.StressTester.run.tensor"></a>

#### tensor

<a id="phardwareitk.GPU.StressTester.run.tensor"></a>

#### tensor

<a id="phardwareitk.GPU.OpenGL"></a>

# phardwareitk.GPU.OpenGL

IntelUHD module for handling Intel UHD Graphics operations.

<a id="phardwareitk.GPU.OpenGL.subprocess"></a>

## subprocess

<a id="phardwareitk.GPU.OpenGL.psutil"></a>

## psutil

<a id="phardwareitk.GPU.OpenGL.ctypes"></a>

## ctypes

<a id="phardwareitk.GPU.OpenGL.sys"></a>

## sys

<a id="phardwareitk.GPU.OpenGL.os"></a>

## os

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.*"></a>

## \*

<a id="phardwareitk.GPU.OpenGL.math"></a>

## math

<a id="phardwareitk.GPU.OpenGL.PError"></a>

#### PError

```python
def PError(*values: str) -> None
```

Print the given string (*values) in error format and exit.

**Arguments**:

- `*values` _str_ - The error messages to print.

<a id="phardwareitk.GPU.OpenGL.Basic"></a>

## Basic Objects

```python
class Basic()
```

<a id="phardwareitk.GPU.OpenGL.Basic.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initialize the Basic class.

<a id="phardwareitk.GPU.OpenGL.Basic.initialize_gpu"></a>

#### initialize\_gpu

```python
def initialize_gpu() -> None
```

Initialize the GPU by checking basic compatibility.

<a id="phardwareitk.GPU.OpenGL.Basic.get_gpu_info"></a>

#### get\_gpu\_info

```python
def get_gpu_info() -> dict
```

Retrieve GPU information using system commands.

**Returns**:

- `dict` - A dictionary containing GPU information.

<a id="phardwareitk.GPU.OpenGL.Basic.check_gpu_availability"></a>

#### check\_gpu\_availability

```python
def check_gpu_availability() -> bool
```

Check if the GPU is available.

**Returns**:

- `bool` - True if the GPU is available, False otherwise.

<a id="phardwareitk.GPU.OpenGL.Basic.get_gpu_model"></a>

#### get\_gpu\_model

```python
def get_gpu_model() -> str
```

Extract the GPU model from the GPU information.

**Returns**:

- `str` - The GPU model.

<a id="phardwareitk.GPU.OpenGL.Basic.get_gpu_memory"></a>

#### get\_gpu\_memory

```python
def get_gpu_memory() -> Union[str, None]
```

Retrieve the GPU memory size.

**Returns**:

- `str` - The GPU memory size in MB, or None if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.get_gpu_temperature"></a>

#### get\_gpu\_temperature

```python
def get_gpu_temperature() -> str
```

Get the GPU temperature. ONLY WINDOWS!

**Returns**:

- `str` - The GPU temperature in °C, or an error message if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.get_driver_version"></a>

#### get\_driver\_version

```python
def get_driver_version() -> str
```

Retrieve the GPU driver version.

**Returns**:

- `str` - The GPU driver version, or an error message if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.get_power_modes"></a>

#### get\_power\_modes

```python
def get_power_modes() -> str
```

Retrieve the power modes. In Windows Only, (*) for current power mode.

**Returns**:

- `str` - The power modes, or an error message if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.run_diagnostics"></a>

#### run\_diagnostics

```python
def run_diagnostics() -> str
```

Run diagnostics on the GPU.

**Returns**:

- `str` - The result of the diagnostics.

<a id="phardwareitk.GPU.OpenGL.Basic.test_rendering"></a>

#### test\_rendering

```python
def test_rendering() -> str
```

Test basic rendering capability.

**Returns**:

- `str` - The result of the rendering test.

<a id="phardwareitk.GPU.OpenGL.Basic.enable_overclocking"></a>

#### enable\_overclocking

```python
def enable_overclocking() -> str
```

Enable GPU overclocking.

**Returns**:

- `str` - A message indicating that overclocking is only supported for NVIDIA GPUs.

<a id="phardwareitk.GPU.OpenGL.Basic.disable_overclocking"></a>

#### disable\_overclocking

```python
def disable_overclocking() -> str
```

Disable GPU overclocking.

**Returns**:

- `str` - A message indicating that overclocking is only supported for NVIDIA GPUs.

<a id="phardwareitk.GPU.OpenGL.Basic.reset_gpu"></a>

#### reset\_gpu

```python
def reset_gpu() -> str
```

Reset the GPU settings to default.

**Returns**:

- `str` - A message indicating that resetting is only supported for NVIDIA GPUs.

<a id="phardwareitk.GPU.OpenGL.Basic.get_gpu_resolution"></a>

#### get\_gpu\_resolution

```python
def get_gpu_resolution() -> Union[List[str], str]
```

Get the GPU resolution.

**Returns**:

- `list` - A list of supported resolutions, or an error message if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.get_supported_refresh_rates"></a>

#### get\_supported\_refresh\_rates

```python
def get_supported_refresh_rates() -> Union[List[str], str]
```

Get a list of supported refresh rates.

**Returns**:

- `list` - A list of supported refresh rates, or an error message if not available.

<a id="phardwareitk.GPU.OpenGL.Basic.check_vulkan_support"></a>

#### check\_vulkan\_support

```python
def check_vulkan_support() -> bool
```

Check if Vulkan is supported.

**Returns**:

- `bool` - True if Vulkan is supported, False otherwise.

<a id="phardwareitk.GPU.OpenGL.Basic.check_opencl_support"></a>

#### check\_opencl\_support

```python
def check_opencl_support() -> bool
```

Check if OpenCL is supported.

**Returns**:

- `bool` - True if OpenCL is supported, False otherwise.

<a id="phardwareitk.GPU.OpenGL.Basic.check_directx_support"></a>

#### check\_directx\_support

```python
def check_directx_support() -> bool
```

Check if DirectX is supported.

**Returns**:

- `bool` - True if DirectX is supported, False otherwise.

<a id="phardwareitk.GPU.OpenGL.Basic.get_utilization"></a>

#### get\_utilization

```python
def get_utilization() -> str
```

Get current GPU utilization percentage.

**Returns**:

- `str` - The current GPU utilization percentage.

<a id="phardwareitk.GPU.OpenGL.Creation"></a>

## Creation Objects

```python
class Creation()
```

<a id="phardwareitk.GPU.OpenGL.Creation.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initialize the Creation class.

<a id="phardwareitk.GPU.OpenGL.Creation.create_window"></a>

#### create\_window

```python
def create_window(width: int = 800,
                  height: int = 600,
                  name: str = "PHardwareITK") -> int
```

Create a window using OpenGL.

**Arguments**:

- `width` _int_ - The width of the window.
- `height` _int_ - The height of the window.
- `name` _str_ - The name of the window.
  

**Returns**:

- `int` - The window ID.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_triangle"></a>

#### draw\_triangle

```python
def draw_triangle() -> None
```

Draw a triangle using OpenGL.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_square"></a>

#### draw\_square

```python
def draw_square() -> None
```

Draw a square using OpenGL.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_circle"></a>

#### draw\_circle

```python
def draw_circle(radius: float = 1.0, segments: int = 32) -> None
```

Draw a circle using OpenGL.

**Arguments**:

- `radius` _float_ - The radius of the circle.
- `segments` _int_ - The number of segments to use for the circle.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_line"></a>

#### draw\_line

```python
def draw_line(x1: float, y1: float, x2: float, y2: float) -> None
```

Draw a line using OpenGL.

**Arguments**:

- `x1` _float_ - The x-coordinate of the first point.
- `y1` _float_ - The y-coordinate of the first point.
- `x2` _float_ - The x-coordinate of the second point.
- `y2` _float_ - The y-coordinate of the second point.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_point"></a>

#### draw\_point

```python
def draw_point(x: float, y: float) -> None
```

Draw a point using OpenGL.

**Arguments**:

- `x` _float_ - The x-coordinate of the point.
- `y` _float_ - The y-coordinate of the point.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_polygon"></a>

#### draw\_polygon

```python
def draw_polygon(vertices: List[tuple]) -> None
```

Draw a polygon using OpenGL.

**Arguments**:

- `vertices` _list_ - A list of tuples representing the vertices of the polygon.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_cube"></a>

#### draw\_cube

```python
def draw_cube() -> None
```

Draw a cube using OpenGL.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_sphere"></a>

#### draw\_sphere

```python
def draw_sphere(radius: float = 1.0,
                slices: int = 32,
                stacks: int = 32) -> None
```

Draw a sphere using OpenGL.

**Arguments**:

- `radius` _float_ - The radius of the sphere.
- `slices` _int_ - The number of slices.
- `stacks` _int_ - The number of stacks.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_cone"></a>

#### draw\_cone

```python
def draw_cone(base: float = 1.0,
              height: float = 2.0,
              slices: int = 32,
              stacks: int = 32) -> None
```

Draw a cone using OpenGL.

**Arguments**:

- `base` _float_ - The base radius of the cone.
- `height` _float_ - The height of the cone.
- `slices` _int_ - The number of slices.
- `stacks` _int_ - The number of stacks.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_cylinder"></a>

#### draw\_cylinder

```python
def draw_cylinder(base: float = 1.0,
                  top: float = 1.0,
                  height: float = 2.0,
                  slices: int = 32,
                  stacks: int = 32) -> None
```

Draw a cylinder using OpenGL.

**Arguments**:

- `base` _float_ - The base radius of the cylinder.
- `top` _float_ - The top radius of the cylinder.
- `height` _float_ - The height of the cylinder.
- `slices` _int_ - The number of slices.
- `stacks` _int_ - The number of stacks.

<a id="phardwareitk.GPU.OpenGL.Creation.draw_torus"></a>

#### draw\_torus

```python
def draw_torus(inner_radius: float = 0.5,
               outer_radius: float = 1.0,
               sides: int = 32,
               rings: int = 32) -> None
```

Draw a torus using OpenGL.

**Arguments**:

- `inner_radius` _float_ - The inner radius of the torus.
- `outer_radius` _float_ - The outer radius of the torus.
- `sides` _int_ - The number of sides.
- `rings` _int_ - The number of rings.

<a id="phardwareitk.GPU.OpenGL.Creation.render_scene"></a>

#### render\_scene

```python
def render_scene()
```

Render the scene.

<a id="phardwareitk.GPU.OpenGL.Creation.render_loop"></a>

#### render\_loop

```python
def render_loop()
```

Run the rendering loop.

<a id="phardwareitk.GPU"></a>

# phardwareitk.GPU

GPU level access

<a id="phardwareitk.GPU.subprocess"></a>

## subprocess

<a id="phardwareitk.GPU.platform"></a>

## platform

<a id="phardwareitk.GPU.importlib"></a>

## importlib

<a id="phardwareitk.GPU.get_gpu_type"></a>

#### get\_gpu\_type

```python
def get_gpu_type()
```

<a id="phardwareitk.GPU.gpu_type"></a>

#### gpu\_type

<a id="phardwareitk.GPU.set_gpu_type"></a>

#### set\_gpu\_type

```python
def set_gpu_type()
```

<a id="phardwareitk.GPU._vulkan_driver"></a>

# phardwareitk.GPU.\_vulkan\_driver

Vulkan Driver implementation using BaseGPUD class (incomplete)

<a id="phardwareitk.GPU._vulkan_driver.ctypes"></a>

## ctypes

<a id="phardwareitk.GPU._vulkan_driver.platform"></a>

## platform

<a id="phardwareitk.GPU._vulkan_driver.Any"></a>

## Any

<a id="phardwareitk.GPU._vulkan_driver.BaseGPUD"></a>

## BaseGPUD

<a id="phardwareitk.GPU._vulkan_driver.VK_SUCCESS"></a>

#### VK\_SUCCESS

<a id="phardwareitk.GPU._vulkan_driver.VK_STRUCTURE_TYPE_APPLICATION_INFO"></a>

#### VK\_STRUCTURE\_TYPE\_APPLICATION\_INFO

<a id="phardwareitk.GPU._vulkan_driver.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO"></a>

#### VK\_STRUCTURE\_TYPE\_INSTANCE\_CREATE\_INFO

<a id="phardwareitk.GPU._vulkan_driver.VK_API_VERSION_1_0"></a>

#### VK\_API\_VERSION\_1\_0

Vulkan 1.0

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver"></a>

## VulkanDriver Objects

```python
class VulkanDriver(BaseGPUD)
```

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver.init"></a>

#### init

```python
def init(display: Any, window: Any, create_and_attach_ctx=False)
```

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver.load_function"></a>

#### load\_function

```python
def load_function(name: str)
```

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver.create_context"></a>

#### create\_context

```python
def create_context(display: Any, window: Any)
```

<a id="phardwareitk.GPU._vulkan_driver.VulkanDriver.shutdown"></a>

#### shutdown

```python
def shutdown()
```

<a id="phardwareitk.PLTEC.Linker"></a>

# phardwareitk.PLTEC.Linker

<a id="phardwareitk.PLTEC.Reader"></a>

# phardwareitk.PLTEC.Reader

<a id="phardwareitk.PLTEC.Reader.os"></a>

## os

<a id="phardwareitk.PLTEC.Reader.json"></a>

## json

<a id="phardwareitk.PLTEC.Reader.LangSetPath"></a>

#### LangSetPath

<a id="phardwareitk.PLTEC.Reader.DEF_LANG"></a>

#### DEF\_LANG

<a id="phardwareitk.PLTEC.Reader.AVAIL_types"></a>

#### AVAIL\_types

<a id="phardwareitk.PLTEC.Reader.AVAIL_modes"></a>

#### AVAIL\_modes

<a id="phardwareitk.PLTEC.Reader.CompileLangSET"></a>

#### CompileLangSET

```python
def CompileLangSET() -> dict
```

<a id="phardwareitk.PLTEC.Reader.Compile_LANG"></a>

#### Compile\_LANG

```python
def Compile_LANG(CompiledLangSET: dict,
                 langPath: str = DEF_LANG) -> tuple[dict, dict, list]
```

<a id="phardwareitk.PLTEC.Logger"></a>

# phardwareitk.PLTEC.Logger

<a id="phardwareitk.PLTEC.Logger.os"></a>

## os

<a id="phardwareitk.PLTEC.Logger.sys"></a>

## sys

<a id="phardwareitk.PLTEC.Logger.datetime"></a>

## datetime

<a id="phardwareitk.PLTEC.Logger.*"></a>

## \*

<a id="phardwareitk.PLTEC.Logger.LOG"></a>

## LOG Objects

```python
class LOG()
```

<a id="phardwareitk.PLTEC.Logger.LOG.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    dateTime: bool = True,
    logLevel: int = 1,
    debugLog: bool = True,
    pathInclude: bool = True,
    pathMsgInclude: bool = True,
    MessageInclude: bool = True,
    descriptionInclude: bool = True,
    errorTitleInclude: bool = True,
    titleInclude: bool = True,
    TitleMsg: str = "",
    errorTitle: str = "",
    debugMsg: str = "",
    dateFormat: str = "%d-%m-%y %I:%M:%S %p",
    path: str = "",
    pathMsg: str = "",
    Message: str = "",
    descriptionMsg: str = "",
    ErrorCodeInclude: bool = True,
    ErrorCode: str = "",
    LogFormat:
    str = "\n$dateTime$:%$Title$%<->%$Error->%$errorTitle$:\n$Message$\n\nDescription:%$description$\n\nPath:%$path$:%$pathMsg$\n\nDebug:%$debugLog$\nCode:%$ErrorCode$^PERCENT^ "
) -> None
```

MAIN initialize function


LogFormat % refers to the the sperater string after ^PERCENT^. DEFAULT: SPACE (' ')


VARIABLES IN LogFormat: ['dateTime', 'Title', 'errorTitle', 'Message', 'description', 'path', 'pathMsg', 'debugLog', 'ErrorCode']

<a id="phardwareitk.PLTEC.Logger.LOG.log"></a>

#### log

```python
def log(returnType: Union[str, None] = None) -> Union[str, None]
```

'None' means printing the log and 'str' means, it returns the log.

<a id="phardwareitk.PLTEC.ASM"></a>

# phardwareitk.PLTEC.ASM

<a id="phardwareitk.PLTEC.ASM.x86_Linux"></a>

## x86\_Linux Objects

```python
class x86_Linux()
```

<a id="phardwareitk.PLTEC.ASM.x86_Linux.convert_to_asm"></a>

#### convert\_to\_asm

```python
@staticmethod
def convert_to_asm(data: str, CompiledLangSet: dict,
                   CompiledLang: dict) -> tuple[str, dict, int]
```

<a id="phardwareitk.PLTEC.main"></a>

# phardwareitk.PLTEC.main

<a id="phardwareitk.PLTEC.main.os"></a>

## os

<a id="phardwareitk.PLTEC.main.sys"></a>

## sys

<a id="phardwareitk.PLTEC.main.*"></a>

## \*

<a id="phardwareitk.PLTEC.main.ASM"></a>

## ASM

<a id="phardwareitk.PLTEC.main.Reader"></a>

## Reader

<a id="phardwareitk.PLTEC.main.OBJECT"></a>

## OBJECT

<a id="phardwareitk.PLTEC.main.Linker"></a>

## Linker

<a id="phardwareitk.PLTEC.main.Logger"></a>

## Logger

<a id="phardwareitk.PLTEC.main.Checker"></a>

## Checker

<a id="phardwareitk.PLTEC.main.job"></a>

#### job

```python
def job()
```

<a id="phardwareitk.PLTEC"></a>

# phardwareitk.PLTEC

Pheonix Language To Executable Convertor

<a id="phardwareitk.PLTEC.os"></a>

## os

<a id="phardwareitk.PLTEC.sys"></a>

## sys

<a id="phardwareitk.PLTEC.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.PLTEC.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.PLTEC.Checker"></a>

## Checker

<a id="phardwareitk.PLTEC.Checker"></a>

# phardwareitk.PLTEC.Checker

<a id="phardwareitk.PLTEC.Checker.PLTEC_initCheck"></a>

#### PLTEC\_initCheck

```python
def PLTEC_initCheck() -> None
```

<a id="phardwareitk.PLTEC.OBJECT"></a>

# phardwareitk.PLTEC.OBJECT

<a id="phardwareitk.PLTEC.OBJECT.ELF"></a>

## ELF Objects

```python
class ELF()
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.__init__"></a>

#### \_\_init\_\_

```python
def __init__(labels_addr: dict, current_addr: int) -> None
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.create_header"></a>

#### create\_header

```python
def create_header(section_headers, debug=False)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.add_label"></a>

#### add\_label

```python
def add_label(label)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.advance_addr"></a>

#### advance\_addr

```python
def advance_addr(size: int)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.add_to_text_section"></a>

#### add\_to\_text\_section

```python
def add_to_text_section(code)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.add_to_data_section"></a>

#### add\_to\_data\_section

```python
def add_to_data_section(data)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.add_to_string_table"></a>

#### add\_to\_string\_table

```python
def add_to_string_table(string: str)
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.finalize_elf"></a>

#### finalize\_elf

```python
def finalize_elf()
```

<a id="phardwareitk.PLTEC.OBJECT.ELF.convert_to_o"></a>

#### convert\_to\_o

```python
def convert_to_o(code: str, data_vars: dict)
```

<a id="phardwareitk.Extensions.HyperPython"></a>

# phardwareitk.Extensions.HyperPython

HyperPython is a Extension in PHardwareITK created by (Pheonix Studios (Akshobhya)).
This converts Python code to C/ASM.

Working on -> Compiler

Next Update -> C to Executable without GCC/Clang/....


NOTES:

1. Under Development.

2. Made because I wanted to.

3. Difference between Cython and HyperPython is as follows.

3.a. Hyper Python generates a Pure C file that can't communitcate with python, but cython does.

3.b. Cython generates a .c file from .pyx that needs to be compiled via gcc/clang/.... whereas HyperPython generates a .c file from .py that needs to be compiled via gcc/clang/.... FOR NOW. HyperPython.ToExecutable class under development.

4. You can use this but remember, this is under development.

5. This might give a huge benifit of file size.

<a id="phardwareitk.Extensions.HyperPython.MAXBUFFER"></a>

#### MAXBUFFER

<a id="phardwareitk.Extensions.HyperPython.MAXLINES"></a>

#### MAXLINES

<a id="phardwareitk.Extensions.HyperPython.*"></a>

## \*

<a id="phardwareitk.Extensions.HyperPython.bltin"></a>

## bltin Objects

```python
class bltin()
```

<a id="phardwareitk.Extensions.HyperPython.bltin.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*value)
```

<a id="phardwareitk.Extensions.HyperPython.bltin.buitlin"></a>

#### buitlin

```python
@property
def buitlin()
```

<a id="phardwareitk.Extensions.HyperPython.bltin.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

<a id="phardwareitk.Extensions.HyperPython.HyperList"></a>

## HyperList Objects

```python
class HyperList()
```

<a id="phardwareitk.Extensions.HyperPython.HyperList.__init__"></a>

#### \_\_init\_\_

```python
def __init__(list1: list, list2: list, *args: list) -> None
```

<a id="phardwareitk.Extensions.HyperPython.HyperList.list_"></a>

#### list\_

```python
@property
def list_() -> list[tuple[list]]
```

<a id="phardwareitk.Extensions.HyperPython.HyperList.MHyperList"></a>

#### MHyperList

```python
def MHyperList(list1: list, list2: list, *lists: list) -> list[tuple[list]]
```

<a id="phardwareitk.Extensions.HyperPython.HyperList.append"></a>

#### append

```python
def append(list1: list, list2: list)
```

<a id="phardwareitk.Extensions.HyperPython.buffer"></a>

## buffer Objects

```python
class buffer(bltin)
```

<a id="phardwareitk.Extensions.HyperPython.buffer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*args) -> None
```

<a id="phardwareitk.Extensions.HyperPython.buffer.__list__"></a>

#### \_\_list\_\_

```python
def __list__()
```

<a id="phardwareitk.Extensions.HyperPython.buffer.value"></a>

#### value

```python
@property
def value() -> list
```

<a id="phardwareitk.Extensions.HyperPython.buffer.length"></a>

#### length

```python
@property
def length() -> int
```

<a id="phardwareitk.Extensions.HyperPython.Generator_C"></a>

## Generator\_C Objects

```python
class Generator_C()
```

<a id="phardwareitk.Extensions.HyperPython.Generator_C.__init__"></a>

#### \_\_init\_\_

```python
def __init__(InfTyp: HyperList.list_, includeHeaders: list)
```

<a id="phardwareitk.Extensions.HyperPython.Generator_C.MakeMainFunc"></a>

#### MakeMainFunc

```python
def MakeMainFunc()
```

<a id="phardwareitk.Extensions.HyperPython.Generator_C.Generate"></a>

#### Generate

```python
def Generate()
```

<a id="phardwareitk.Extensions.HyperPython.Tokenizer_C"></a>

## Tokenizer\_C Objects

```python
class Tokenizer_C()
```

<a id="phardwareitk.Extensions.HyperPython.Tokenizer_C.__init__"></a>

#### \_\_init\_\_

```python
def __init__(code: str)
```

<a id="phardwareitk.Extensions.HyperPython.Tokenizer_C.tokenize"></a>

#### tokenize

```python
def tokenize()
```

<a id="phardwareitk.Extensions.HyperPython.Tokenizer_C.infer_types"></a>

#### infer\_types

```python
def infer_types()
```

<a id="phardwareitk.Extensions.HyperPython.Convert"></a>

#### Convert

```python
def Convert(to: int = 0, code: str = "", file: str = "") -> int
```

**Arguments**:

- `to` _int, optional_ - Which type to convert to. Defaults to 0.
  Available Types ->
  # 0 -> C
  # 1 -> ASM
  # 2 -> EXE
  # 3 -> ELF
  # 4 -> AEF
  # 5 -> CAEF
  
- `code` _str, optional_ - If code is in string form, pass here.
- `file` _str, optional_ - If code in inside a file, pass file path here.
  

**Returns**:

- `int` - 0 for success, 1 for failure, -11 for OSError.

<a id="phardwareitk.Extensions.C.stdlib"></a>

# phardwareitk.Extensions.C.stdlib

C-stdlib. Python - C - Standard Library

<a id="phardwareitk.Extensions.C.stdlib.C"></a>

## C

<a id="phardwareitk.Extensions.C.stdlib.Union"></a>

## Union

<a id="phardwareitk.Extensions.C.stdlib.Optional"></a>

## Optional

<a id="phardwareitk.Extensions.C.stdlib.Callable"></a>

## Callable

<a id="phardwareitk.Extensions.C.stdlib.sys"></a>

## sys

<a id="phardwareitk.Extensions.C.stdlib.os"></a>

## os

<a id="phardwareitk.Extensions.C.stdlib.random"></a>

## random

<a id="phardwareitk.Extensions.C.stdlib.malloc"></a>

#### malloc

```python
def malloc(size_: C.size_t) -> Optional[C.pointer[C.void]]
```

Allocate size on heap

<a id="phardwareitk.Extensions.C.stdlib.free"></a>

#### free

```python
def free(ptr: C.pointer) -> None
```

Frees the allocated heap memory for later use

<a id="phardwareitk.Extensions.C.stdlib.realloc"></a>

#### realloc

```python
def realloc(ptr: C.pointer, new_size: C.size_t) -> Optional[C.pointer[C.void]]
```

Reallocate on the heap

<a id="phardwareitk.Extensions.C.stdlib.calloc"></a>

#### calloc

```python
def calloc(nmemb: C.size_t, size: C.size_t) -> Optional[C.pointer[C.void]]
```

Allocate specified number of members of specified size

<a id="phardwareitk.Extensions.C.stdlib.EXIT_SUCCESS"></a>

#### EXIT\_SUCCESS

<a id="phardwareitk.Extensions.C.stdlib.EXIT_FALUIRE"></a>

#### EXIT\_FALUIRE

<a id="phardwareitk.Extensions.C.stdlib.NULL"></a>

#### NULL

((void*)0)

<a id="phardwareitk.Extensions.C.stdlib.abort"></a>

#### abort

```python
def abort() -> None
```

Halts the program directly

<a id="phardwareitk.Extensions.C.stdlib.exit"></a>

#### exit

```python
def exit(status: C.Int) -> None
```

Exits the program

<a id="phardwareitk.Extensions.C.stdlib.atexit"></a>

#### atexit

```python
def atexit(func: Callable) -> None
```

Runs the function provided on exit of program

<a id="phardwareitk.Extensions.C.stdlib.getenv"></a>

#### getenv

```python
def getenv(name: C.pointer[C.char]) -> C.pointer[C.char]
```

Gets Environment Variable

<a id="phardwareitk.Extensions.C.stdlib.system"></a>

#### system

```python
def system(command: C.pointer[C.char]) -> C.Int
```

Runs a system command

<a id="phardwareitk.Extensions.C.stdlib.abs_"></a>

#### abs\_

```python
def abs_(j: C.Int) -> C.Int
```

<a id="phardwareitk.Extensions.C.stdlib.labs"></a>

#### labs

```python
def labs(j: C.Int) -> C.Int
```

<a id="phardwareitk.Extensions.C.stdlib.div_"></a>

#### div\_

```python
def div_(numer: C.Int, denom: C.Int)
```

<a id="phardwareitk.Extensions.C.stdlib.atoi"></a>

#### atoi

```python
def atoi(nptr: C.pointer[C.char]) -> C.Int
```

<a id="phardwareitk.Extensions.C.stdlib.atof"></a>

#### atof

```python
def atof(nptr: C.pointer[C.char]) -> C.double
```

<a id="phardwareitk.Extensions.C.stdlib.atol"></a>

#### atol

```python
def atol(nptr: C.pointer[C.char]) -> C.Int
```

<a id="phardwareitk.Extensions.C.stdlib.srand"></a>

#### srand

```python
def srand(seed: C.Int) -> None
```

<a id="phardwareitk.Extensions.C.stdlib.rand"></a>

#### rand

```python
def rand() -> C.Int
```

<a id="phardwareitk.Extensions.C.stdlib.qsort"></a>

#### qsort

```python
def qsort(base: C.pointer[C.array], nmemb: C.size_t, size: C.size_t,
          compar: Callable)
```

<a id="phardwareitk.Extensions.C.stdlib.bsearch"></a>

#### bsearch

```python
def bsearch(key: C.pointer[C.char], base: C.pointer[C.array], nmemb: C.size_t,
            size: C.size_t, compar: Callable)
```

<a id="phardwareitk.Extensions.C.stdlib.mbstowcs"></a>

#### mbstowcs

```python
def mbstowcs(pwcs, s, n)
```

<a id="phardwareitk.Extensions.C.stdlib.wcstombs"></a>

#### wcstombs

```python
def wcstombs(s, pwcs, n)
```

<a id="phardwareitk.Extensions.C.stdlib.mbtowc"></a>

#### mbtowc

```python
def mbtowc(pwc, s, n)
```

<a id="phardwareitk.Extensions.C.stdlib.wctomb"></a>

#### wctomb

```python
def wctomb(s, wc)
```

<a id="phardwareitk.Extensions.C.stdlib.mblen"></a>

#### mblen

```python
def mblen(s, n)
```

<a id="phardwareitk.Extensions.C"></a>

# phardwareitk.Extensions.C

This is the new and improved C Extension, which allows for easy usage. It allows emulating C in python to do tasks that Cython/C Can do in python by emulating it.

<a id="phardwareitk.Extensions.C.Union"></a>

## Union

<a id="phardwareitk.Extensions.C.Optional"></a>

## Optional

<a id="phardwareitk.Extensions.C.Any"></a>

## Any

<a id="phardwareitk.Extensions.C.__memory__"></a>

## \_\_memory\_\_

<a id="phardwareitk.Extensions.C.align"></a>

#### align

```python
def align(v1: int, v2: int) -> int
```

<a id="phardwareitk.Extensions.C.reset_mem"></a>

#### reset\_mem

```python
def reset_mem(new_size: int) -> None
```

Resets the memory with new size, expanding or shrinking it

<a id="phardwareitk.Extensions.C.initialize"></a>

#### initialize

```python
def initialize(size: int = 64) -> None
```

Initializes the memory, very important to use this before using anything else!

<a id="phardwareitk.Extensions.C.get_memory"></a>

#### get\_memory

```python
def get_memory() -> __memory__
```

Returns the global memory

<a id="phardwareitk.Extensions.C.write_mem"></a>

#### write\_mem

```python
def write_mem(data: bytes, size: int, addr: int) -> None
```

Writes data of specified size at the specified address

<a id="phardwareitk.Extensions.C.read_mem"></a>

#### read\_mem

```python
def read_mem(size: int, addr: int) -> bytes
```

Reads the specified size from the specified address from memory.

<a id="phardwareitk.Extensions.C.delete_mem"></a>

#### delete\_mem

```python
def delete_mem(size: int, addr: int) -> None
```

Deletes/Clears memory at specified address for specified size

<a id="phardwareitk.Extensions.C.stack_push"></a>

#### stack\_push

```python
def stack_push(data: bytes) -> None
```

Pushes data onto the stack

<a id="phardwareitk.Extensions.C.stack_pop"></a>

#### stack\_pop

```python
def stack_pop(count: int) -> bytes
```

Pops 8 bytes off the stack for specifed 'count' times and returns it concatinated

<a id="phardwareitk.Extensions.C.push_frame"></a>

#### push\_frame

```python
def push_frame()
```

Starts a new stack frame

<a id="phardwareitk.Extensions.C.pop_frame"></a>

#### pop\_frame

```python
def pop_frame()
```

Ends a stack frame and restores stack pointer

<a id="phardwareitk.Extensions.C.CBaseType"></a>

## CBaseType Objects

```python
class CBaseType()
```

<a id="phardwareitk.Extensions.C.CBaseType.size"></a>

#### size

<a id="phardwareitk.Extensions.C.CBaseType.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.CBaseType.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int) -> None
```

<a id="phardwareitk.Extensions.C.CBaseType.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C.CBaseType.__sizeof__"></a>

#### \_\_sizeof\_\_

```python
def __sizeof__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__neg__"></a>

#### \_\_neg\_\_

```python
def __neg__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__pos__"></a>

#### \_\_pos\_\_

```python
def __pos__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__abs__"></a>

#### \_\_abs\_\_

```python
def __abs__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__invert__"></a>

#### \_\_invert\_\_

```python
def __invert__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__mul__"></a>

#### \_\_mul\_\_

```python
def __mul__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__truediv__"></a>

#### \_\_truediv\_\_

```python
def __truediv__(other: object) -> float
```

<a id="phardwareitk.Extensions.C.CBaseType.__floordiv__"></a>

#### \_\_floordiv\_\_

```python
def __floordiv__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__mod__"></a>

#### \_\_mod\_\_

```python
def __mod__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__pow__"></a>

#### \_\_pow\_\_

```python
def __pow__(other: object, modulo=None) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__lshift__"></a>

#### \_\_lshift\_\_

```python
def __lshift__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__rshift__"></a>

#### \_\_rshift\_\_

```python
def __rshift__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__and__"></a>

#### \_\_and\_\_

```python
def __and__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__xor__"></a>

#### \_\_xor\_\_

```python
def __xor__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__isub__"></a>

#### \_\_isub\_\_

```python
def __isub__(other: object) -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__index__"></a>

#### \_\_index\_\_

```python
def __index__() -> int
```

<a id="phardwareitk.Extensions.C.CBaseType.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C.char"></a>

## char Objects

```python
class char(CBaseType)
```

A single byte

<a id="phardwareitk.Extensions.C.char.size"></a>

#### size

<a id="phardwareitk.Extensions.C.char.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.char.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: Union[str, int]) -> None
```

<a id="phardwareitk.Extensions.C.char.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C.short"></a>

## short Objects

```python
class short(CBaseType)
```

2 bytes

<a id="phardwareitk.Extensions.C.short.size"></a>

#### size

<a id="phardwareitk.Extensions.C.short.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.int_"></a>

## int\_ Objects

```python
class int_(CBaseType)
```

4 bytes

<a id="phardwareitk.Extensions.C.int_.size"></a>

#### size

<a id="phardwareitk.Extensions.C.int_.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.long"></a>

## long Objects

```python
class long(CBaseType)
```

8 bytes

<a id="phardwareitk.Extensions.C.long.size"></a>

#### size

<a id="phardwareitk.Extensions.C.long.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.unsigned_char"></a>

## unsigned\_char Objects

```python
class unsigned_char(CBaseType)
```

unsigned char

<a id="phardwareitk.Extensions.C.unsigned_char.size"></a>

#### size

<a id="phardwareitk.Extensions.C.unsigned_char.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.unsigned_short"></a>

## unsigned\_short Objects

```python
class unsigned_short(CBaseType)
```

unsigned short

<a id="phardwareitk.Extensions.C.unsigned_short.size"></a>

#### size

<a id="phardwareitk.Extensions.C.unsigned_short.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.unsigned_int"></a>

## unsigned\_int Objects

```python
class unsigned_int(CBaseType)
```

unsigned int

<a id="phardwareitk.Extensions.C.unsigned_int.size"></a>

#### size

<a id="phardwareitk.Extensions.C.unsigned_int.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.unsigned_long"></a>

## unsigned\_long Objects

```python
class unsigned_long(CBaseType)
```

unsigned long

<a id="phardwareitk.Extensions.C.unsigned_long.size"></a>

#### size

<a id="phardwareitk.Extensions.C.unsigned_long.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.double"></a>

## double Objects

```python
class double(CBaseType)
```

64-bit floating point

<a id="phardwareitk.Extensions.C.double.size"></a>

#### size

<a id="phardwareitk.Extensions.C.double.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.double.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: float) -> None
```

<a id="phardwareitk.Extensions.C.double.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.Extensions.C.double.__float__"></a>

#### \_\_float\_\_

```python
def __float__()
```

<a id="phardwareitk.Extensions.C.void"></a>

## void Objects

```python
class void()
```

Just nothing, plain void

<a id="phardwareitk.Extensions.C.void.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="phardwareitk.Extensions.C.pointer"></a>

## pointer Objects

```python
class pointer(CBaseType)
```

A 64-bit Pointer

<a id="phardwareitk.Extensions.C.pointer.size"></a>

#### size

<a id="phardwareitk.Extensions.C.pointer.signed"></a>

#### signed

<a id="phardwareitk.Extensions.C.pointer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(obj: object, typ: type = void) -> None
```

<a id="phardwareitk.Extensions.C.pointer.deref"></a>

#### deref

```python
def deref() -> bytes
```

Dereference the pointer. &pointer

<a id="phardwareitk.Extensions.C.pointer.cast"></a>

#### cast

```python
def cast(newtype: type) -> None
```

Cast the pointer to another type

<a id="phardwareitk.Extensions.C.pointer.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C.pointer.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, *args)
```

<a id="phardwareitk.Extensions.C.ptr"></a>

#### ptr

<a id="phardwareitk.Extensions.C.Pointer"></a>

#### Pointer

<a id="phardwareitk.Extensions.C.Void"></a>

#### Void

<a id="phardwareitk.Extensions.C.Char"></a>

#### Char

<a id="phardwareitk.Extensions.C.Short"></a>

#### Short

<a id="phardwareitk.Extensions.C.Int"></a>

#### Int

<a id="phardwareitk.Extensions.C.Long"></a>

#### Long

<a id="phardwareitk.Extensions.C.UChar"></a>

#### UChar

<a id="phardwareitk.Extensions.C.UShort"></a>

#### UShort

<a id="phardwareitk.Extensions.C.UInt"></a>

#### UInt

<a id="phardwareitk.Extensions.C.ULong"></a>

#### ULong

<a id="phardwareitk.Extensions.C.size_t"></a>

#### size\_t

<a id="phardwareitk.Extensions.C.Size_t"></a>

#### Size\_t

<a id="phardwareitk.Extensions.C.Double"></a>

#### Double

<a id="phardwareitk.Extensions.C.array"></a>

## array Objects

```python
class array()
```

C-Array, Example:
``` c
    char myarray[5] // array of 5 characters/5 bytes
```

<a id="phardwareitk.Extensions.C.array.__init__"></a>

#### \_\_init\_\_

```python
def __init__(typ: type, len: int, address: Optional[int] = None) -> None
```

<a id="phardwareitk.Extensions.C.array.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(index: int) -> CBaseType
```

<a id="phardwareitk.Extensions.C.array.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(index: int, value: Union[int, CBaseType]) -> None
```

<a id="phardwareitk.Extensions.C.array.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

<a id="phardwareitk.Extensions.C.array.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C.array.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, *args)
```

<a id="phardwareitk.Extensions.C.array.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C.Array"></a>

#### Array

<a id="phardwareitk.Extensions.C.struct"></a>

## struct Objects

```python
class struct()
```

A C-Structure, uses format like -
```python
format: dict = {
    "field1": {
        "type": long, # Type of field
        "value": None # Default value
    },
    "field2": {
        "type": pointer,
        "value": None,
        "ptr_type": short, # Pointer-Specific, Type of pointer
        "ptr_val": None # Pointer-Specific, Default Pointer type
    },
    "field3": {
        "type": array,
        "value": None,
        "array_type": char, # Array-Specific, Type of Array
        "array_len": 4 # Array-Specific, Length of Array
    }
}
```

<a id="phardwareitk.Extensions.C.struct.__init__"></a>

#### \_\_init\_\_

```python
def __init__(structure: dict, address: Optional[int] = None) -> None
```

<a id="phardwareitk.Extensions.C.struct.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name: str) -> Any
```

<a id="phardwareitk.Extensions.C.struct.__setattr__"></a>

#### \_\_setattr\_\_

```python
def __setattr__(
        name: str, value: Union[int, CBaseType, array, pointer, bytes,
                                str]) -> None
```

<a id="phardwareitk.Extensions.C.struct.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C.struct.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, *args)
```

<a id="phardwareitk.Extensions.C.struct.from_address"></a>

#### from\_address

```python
@classmethod
def from_address(cls, structure: dict, address: int)
```

Cast an existing memory address to a struct.

<a id="phardwareitk.Extensions.C.struct.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C.Struct"></a>

#### Struct

<a id="phardwareitk.Extensions.C.enum"></a>

## enum Objects

```python
class enum()
```

C-style enum

<a id="phardwareitk.Extensions.C.enum.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str, fields: dict[str, int])
```

<a id="phardwareitk.Extensions.C.enum.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(key)
```

<a id="phardwareitk.Extensions.C.enum.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

<a id="phardwareitk.Extensions.C.enum.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, *args)
```

<a id="phardwareitk.Extensions.C.cstring"></a>

#### cstring

```python
def cstring(py_str: str) -> pointer
```

Allocates a null-terminated C string on the heap and returns a pointer to it.

<a id="phardwareitk.Extensions.C.stdio"></a>

# phardwareitk.Extensions.C.stdio

<a id="phardwareitk.Extensions.C.stdio.*"></a>

## \*

<a id="phardwareitk.Extensions.C.stdio.os"></a>

## os

<a id="phardwareitk.Extensions.C.stdio.sys"></a>

## sys

<a id="phardwareitk.Extensions.C.stdio.C"></a>

## C

<a id="phardwareitk.Extensions.C.stdio.stdlib"></a>

## stdlib

<a id="phardwareitk.Extensions.C.stdio.do_print_exception"></a>

#### do\_print\_exception

<a id="phardwareitk.Extensions.C.stdio.set_exception_print"></a>

#### set\_exception\_print

```python
def set_exception_print(val: bool) -> None
```

True for printing exception, False for otherwise

<a id="phardwareitk.Extensions.C.stdio.print_exception"></a>

#### print\_exception

```python
def print_exception(exception) -> None
```

Prints exception provided based on the do_print_exception, whose value is setted by set_exception_print function

<a id="phardwareitk.Extensions.C.stdio.SEEK_SET"></a>

#### SEEK\_SET

<a id="phardwareitk.Extensions.C.stdio.SEEK_CUR"></a>

#### SEEK\_CUR

<a id="phardwareitk.Extensions.C.stdio.SEEK_END"></a>

#### SEEK\_END

<a id="phardwareitk.Extensions.C.stdio.FILE"></a>

#### FILE

<a id="phardwareitk.Extensions.C.stdio.fopen"></a>

#### fopen

```python
def fopen(
        path: Union[C.pointer[C.char], str],
        mode: Union[C.pointer[C.char], str]) -> Union[C.pointer[FILE], C.Int]
```

fopen - Open a file and return a FILE struct pointer

**Arguments**:

  path (char*):
  Path to the file
  mode (char*):
  Mode to open the file with (e.g. 'r', 'w', 'rb', ...)
  
- `Returns` - Pointer to FILE (_IO_FILE) struct or -1 on failure, -2 on file not found, -3 on permission error

<a id="phardwareitk.Extensions.C.stdio.fclose"></a>

#### fclose

```python
def fclose(file_: C.pointer[FILE]) -> C.Int
```

fclose - Close a file and free its memory

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C.stdio.ftell"></a>

#### ftell

```python
def ftell(file: C.pointer[FILE]) -> C.size_t
```

ftell - Get the current position in the file

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - Current position in the file or -1 on failure

<a id="phardwareitk.Extensions.C.stdio.fflush"></a>

#### fflush

```python
def fflush(file: C.pointer[FILE]) -> C.Int
```

fflush - Flush the output buffer of a file

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C.stdio.fseek"></a>

#### fseek

```python
def fseek(file: C.pointer[FILE], offset: C.Int, whence: C.Int) -> C.Int
```

fseek - Set the file position indicator for the stream

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  offset (int):
  Offset to set the position to
  whence (int):
  Position from which to set the offset (e.g. SEEK_SET, SEEK_CUR, SEEK_END)
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C.stdio.fread"></a>

#### fread

```python
def fread(dest: C.pointer[C.void], size: C.size_t, nmemb: C.size_t,
          file_ptr: C.pointer[FILE]) -> C.Int
```

fread - Read data from a file

**Arguments**:

- `dest` _void*_ - The destination pointer where data will be stored
- `size` _size_t_ - size of each element to read
- `nmemb` _size_t_ - number of elements to read
- `file_ptr` _FILE*_ - Pointer to the FILE struct
  

**Returns**:

- `int` - Number of elements successfully read, or -1 on failure

<a id="phardwareitk.Extensions.C.stdio.fwrite"></a>

#### fwrite

```python
def fwrite(src: Union[C.pointer[C.void], str, bytes],
           size: C.size_t,
           nmemb: C.size_t,
           file_ptr: C.pointer[FILE],
           chunk_size: Optional[C.Int] = None) -> C.Int
```

fwrite - Write data to a file

**Arguments**:

- `src` _void*_ - The source pointer containing data to write
- `size` _size_t_ - size of each element to write
- `nmemb` _size_t_ - number of elements to write
- `file_ptr` _FILE*_ - Pointer to the FILE struct
- `chunk_size` _int_ - Writing files in chunk to prevent overuse of memory. Defaults to 4096 bytes / 4KB
  

**Returns**:

- `int` - Number of elements successfully written, or -1 on failure

<a id="phardwareitk.Extensions.C.stdio.remove"></a>

#### remove

```python
def remove(filename: Union[C.pointer[C.char], str]) -> C.Int
```

remove - Remove a file

**Arguments**:

  filename (char*):
  Path to the file to remove
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C.stdio.rename"></a>

#### rename

```python
def rename(old_filename: Union[C.pointer[C.char], str],
           new_filename: Union[C.pointer[C.char], str]) -> C.Int
```

rename - Rename a file

**Arguments**:

  old_filename (char*):
  Path to the file to rename
  new_filename (char*):
  New path for the file
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C.stdint"></a>

# phardwareitk.Extensions.C.stdint

C Standard Int

<a id="phardwareitk.Extensions.C.stdint.*"></a>

## \*

<a id="phardwareitk.Extensions.C.stdint.int8_t"></a>

#### int8\_t

<a id="phardwareitk.Extensions.C.stdint.int16_t"></a>

#### int16\_t

<a id="phardwareitk.Extensions.C.stdint.int32_t"></a>

#### int32\_t

<a id="phardwareitk.Extensions.C.stdint.int64_t"></a>

#### int64\_t

<a id="phardwareitk.Extensions.C.stdint.uint8_t"></a>

#### uint8\_t

<a id="phardwareitk.Extensions.C.stdint.uint16_t"></a>

#### uint16\_t

<a id="phardwareitk.Extensions.C.stdint.uint32_t"></a>

#### uint32\_t

<a id="phardwareitk.Extensions.C.stdint.uint64_t"></a>

#### uint64\_t

<a id="phardwareitk.Extensions.C.stdint.Int8_t"></a>

#### Int8\_t

<a id="phardwareitk.Extensions.C.stdint.Int16_t"></a>

#### Int16\_t

<a id="phardwareitk.Extensions.C.stdint.Int32_t"></a>

#### Int32\_t

<a id="phardwareitk.Extensions.C.stdint.Int64_t"></a>

#### Int64\_t

<a id="phardwareitk.Extensions.C.stdint.Uint8_t"></a>

#### Uint8\_t

<a id="phardwareitk.Extensions.C.stdint.Uint16_t"></a>

#### Uint16\_t

<a id="phardwareitk.Extensions.C.stdint.Uint32_t"></a>

#### Uint32\_t

<a id="phardwareitk.Extensions.C.stdint.Uint64_t"></a>

#### Uint64\_t

<a id="phardwareitk.Extensions.C_IO_Old"></a>

# phardwareitk.Extensions.C\_IO\_Old

<a id="phardwareitk.Extensions.C_IO_Old.*"></a>

## \*

<a id="phardwareitk.Extensions.C_IO_Old.os"></a>

## os

<a id="phardwareitk.Extensions.C_IO_Old.sys"></a>

## sys

<a id="phardwareitk.Extensions.C_IO_Old.time"></a>

## time

<a id="phardwareitk.Extensions.C_IO_Old.*"></a>

## \*

<a id="phardwareitk.Extensions.C_IO_Old.do_print_exception"></a>

#### do\_print\_exception

<a id="phardwareitk.Extensions.C_IO_Old.set_exception_print"></a>

#### set\_exception\_print

```python
def set_exception_print(val: bool) -> None
```

True for printing exception, False for otherwise

<a id="phardwareitk.Extensions.C_IO_Old.print_exception"></a>

#### print\_exception

```python
def print_exception(exception) -> None
```

Prints exception provided based on the do_print_exception, whose value is setted by set_exception_print function

<a id="phardwareitk.Extensions.C_IO_Old.SEEK_SET"></a>

#### SEEK\_SET

<a id="phardwareitk.Extensions.C_IO_Old.SEEK_CUR"></a>

#### SEEK\_CUR

<a id="phardwareitk.Extensions.C_IO_Old.SEEK_END"></a>

#### SEEK\_END

<a id="phardwareitk.Extensions.C_IO_Old.FILE"></a>

#### FILE

<a id="phardwareitk.Extensions.C_IO_Old.fopen"></a>

#### fopen

```python
def fopen(path: Union[Pointer[Char], str],
          mode: str) -> Union[Pointer[FILE], int]
```

fopen - Open a file and return a FILE struct pointer

**Arguments**:

  path (char*):
  Path to the file
  mode (char*):
  Mode to open the file with (e.g. 'r', 'w', 'rb', ...)
  
- `Returns` - Pointer to FILE (_IO_FILE) struct or -1 on failure, -2 on file not found, -3 on permission error

<a id="phardwareitk.Extensions.C_IO_Old.fclose"></a>

#### fclose

```python
def fclose(file_: Pointer[FILE]) -> int
```

fclose - Close a file and free its memory

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.ftell"></a>

#### ftell

```python
def ftell(file: Pointer[FILE]) -> int
```

ftell - Get the current position in the file

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - Current position in the file or -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.fflush"></a>

#### fflush

```python
def fflush(file: Pointer[FILE]) -> int
```

fflush - Flush the output buffer of a file

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.fseek"></a>

#### fseek

```python
def fseek(file: Pointer[FILE], offset: int, whence: int) -> int
```

fseek - Set the file position indicator for the stream

**Arguments**:

  file (FILE*):
  Pointer to the FILE struct
  offset (int):
  Offset to set the position to
  whence (int):
  Position from which to set the offset (e.g. SEEK_SET, SEEK_CUR, SEEK_END)
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.fread"></a>

#### fread

```python
def fread(dest: Pointer[Void], size: Union[int, Size_t],
          nmemb: Union[int, Size_t], file_ptr: Pointer[FILE]) -> int
```

fread - Read data from a file

**Arguments**:

- `dest` _Pointer[Void]_ - The destination pointer where data will be stored
- `size` _int_ - size of each element to read
- `nmemb` _int_ - number of elements to read
- `file_ptr` _Pointer[FILE]_ - Pointer to the FILE struct
  

**Returns**:

- `int` - Number of elements successfully read, or -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.fwrite"></a>

#### fwrite

```python
def fwrite(src: Union[Pointer[Void], str, bytes],
           size: Union[int, Size_t],
           nmemb: Union[int, Size_t],
           file_ptr: Pointer[FILE],
           chunk_size: int = 4096) -> int
```

fwrite - Write data to a file

**Arguments**:

- `src` _Pointer[Void]_ - The source pointer containing data to write
- `size` _int_ - size of each element to write
- `nmemb` _int_ - number of elements to write
- `file_ptr` _Pointer[FILE]_ - Pointer to the FILE struct
- `chunk_size` _int_ - Writing files in chunk to prevent overuse of memory. Defaults to 4096 bytes / 4KB
  

**Returns**:

- `int` - Number of elements successfully written, or -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.remove"></a>

#### remove

```python
def remove(filename: Union[Pointer[Char], str]) -> int
```

remove - Remove a file

**Arguments**:

  filename (char*):
  Path to the file to remove
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.C_IO_Old.rename"></a>

#### rename

```python
def rename(old_filename: Union[Pointer[Char], str],
           new_filename: Union[Pointer[Char], str]) -> int
```

rename - Rename a file

**Arguments**:

  old_filename (char*):
  Path to the file to rename
  new_filename (char*):
  New path for the file
  
- `Returns` - 0 on success, -1 on failure

<a id="phardwareitk.Extensions.Windows"></a>

# phardwareitk.Extensions.Windows

This file includes everything for windows platform

<a id="phardwareitk.Extensions.Windows.sys"></a>

## sys

<a id="phardwareitk.Extensions.Windows.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows.ctypes"></a>

## ctypes

<a id="phardwareitk.Extensions.Windows.CS_BYTEALIGNCLIENT"></a>

#### CS\_BYTEALIGNCLIENT

<a id="phardwareitk.Extensions.Windows.CS_BYTEALIGNWINDOW"></a>

#### CS\_BYTEALIGNWINDOW

<a id="phardwareitk.Extensions.Windows.CS_CLASSDC"></a>

#### CS\_CLASSDC

<a id="phardwareitk.Extensions.Windows.CS_DBLCLKS"></a>

#### CS\_DBLCLKS

<a id="phardwareitk.Extensions.Windows.CS_DROPSHADOW"></a>

#### CS\_DROPSHADOW

<a id="phardwareitk.Extensions.Windows.CS_GLOBALCLASS"></a>

#### CS\_GLOBALCLASS

<a id="phardwareitk.Extensions.Windows.CS_HREDRAW"></a>

#### CS\_HREDRAW

<a id="phardwareitk.Extensions.Windows.CS_NOCLOSE"></a>

#### CS\_NOCLOSE

<a id="phardwareitk.Extensions.Windows.CS_OWNDC"></a>

#### CS\_OWNDC

<a id="phardwareitk.Extensions.Windows.CS_PARENTDC"></a>

#### CS\_PARENTDC

<a id="phardwareitk.Extensions.Windows.CS_SAVEBITS"></a>

#### CS\_SAVEBITS

<a id="phardwareitk.Extensions.Windows.CS_VREDRAW"></a>

#### CS\_VREDRAW

<a id="phardwareitk.Extensions.Windows.IDI_APPLICATION"></a>

#### IDI\_APPLICATION

<a id="phardwareitk.Extensions.Windows.IDI_ERROR"></a>

#### IDI\_ERROR

<a id="phardwareitk.Extensions.Windows.IDI_QUESTION"></a>

#### IDI\_QUESTION

<a id="phardwareitk.Extensions.Windows.IDI_WARNING"></a>

#### IDI\_WARNING

<a id="phardwareitk.Extensions.Windows.IDI_INFORMATION"></a>

#### IDI\_INFORMATION

<a id="phardwareitk.Extensions.Windows.IDI_WINLOGO"></a>

#### IDI\_WINLOGO

<a id="phardwareitk.Extensions.Windows.IDI_SHIELD"></a>

#### IDI\_SHIELD

<a id="phardwareitk.Extensions.Windows.IDC_ARROW"></a>

#### IDC\_ARROW

<a id="phardwareitk.Extensions.Windows.IDC_IBEAM"></a>

#### IDC\_IBEAM

<a id="phardwareitk.Extensions.Windows.IDC_WAIT"></a>

#### IDC\_WAIT

<a id="phardwareitk.Extensions.Windows.IDC_CROSS"></a>

#### IDC\_CROSS

<a id="phardwareitk.Extensions.Windows.IDC_UPARROW"></a>

#### IDC\_UPARROW

<a id="phardwareitk.Extensions.Windows.IDC_SIZENWSE"></a>

#### IDC\_SIZENWSE

<a id="phardwareitk.Extensions.Windows.IDC_SIZENESW"></a>

#### IDC\_SIZENESW

<a id="phardwareitk.Extensions.Windows.IDC_SIZEWE"></a>

#### IDC\_SIZEWE

<a id="phardwareitk.Extensions.Windows.IDC_SIZENS"></a>

#### IDC\_SIZENS

<a id="phardwareitk.Extensions.Windows.IDC_SIZEALL"></a>

#### IDC\_SIZEALL

<a id="phardwareitk.Extensions.Windows.IDC_NO"></a>

#### IDC\_NO

<a id="phardwareitk.Extensions.Windows.IDC_HAND"></a>

#### IDC\_HAND

<a id="phardwareitk.Extensions.Windows.IDC_APPSTARTING"></a>

#### IDC\_APPSTARTING

<a id="phardwareitk.Extensions.Windows.IDC_HELP"></a>

#### IDC\_HELP

<a id="phardwareitk.Extensions.Windows.IDC_PIN"></a>

#### IDC\_PIN

<a id="phardwareitk.Extensions.Windows.IDC_PERSON"></a>

#### IDC\_PERSON

<a id="phardwareitk.Extensions.Windows.WHITE_BRUSH"></a>

#### WHITE\_BRUSH

<a id="phardwareitk.Extensions.Windows.LTGRAY_BRUSH"></a>

#### LTGRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows.GRAY_BRUSH"></a>

#### GRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows.DKGRAY_BRUSH"></a>

#### DKGRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows.BLACK_BRUSH"></a>

#### BLACK\_BRUSH

<a id="phardwareitk.Extensions.Windows.NULL_BRUSH"></a>

#### NULL\_BRUSH

<a id="phardwareitk.Extensions.Windows.HOLLOW_BRUSH"></a>

#### HOLLOW\_BRUSH

<a id="phardwareitk.Extensions.Windows.WHITE_PEN"></a>

#### WHITE\_PEN

<a id="phardwareitk.Extensions.Windows.BLACK_PEN"></a>

#### BLACK\_PEN

<a id="phardwareitk.Extensions.Windows.NULL_PEN"></a>

#### NULL\_PEN

<a id="phardwareitk.Extensions.Windows.OEM_FIXED_FONT"></a>

#### OEM\_FIXED\_FONT

<a id="phardwareitk.Extensions.Windows.ANSI_FIXED_FONT"></a>

#### ANSI\_FIXED\_FONT

<a id="phardwareitk.Extensions.Windows.ANSI_VAR_FONT"></a>

#### ANSI\_VAR\_FONT

<a id="phardwareitk.Extensions.Windows.SYSTEM_FONT"></a>

#### SYSTEM\_FONT

<a id="phardwareitk.Extensions.Windows.DEVICE_DEFAULT_FONT"></a>

#### DEVICE\_DEFAULT\_FONT

<a id="phardwareitk.Extensions.Windows.DEFAULT_PALETTE"></a>

#### DEFAULT\_PALETTE

<a id="phardwareitk.Extensions.Windows.CW_USEDEFAULT"></a>

#### CW\_USEDEFAULT

<a id="phardwareitk.Extensions.Windows.SW_HIDE"></a>

#### SW\_HIDE

<a id="phardwareitk.Extensions.Windows.SW_SHOWNORMAL"></a>

#### SW\_SHOWNORMAL

<a id="phardwareitk.Extensions.Windows.SW_NORMAL"></a>

#### SW\_NORMAL

<a id="phardwareitk.Extensions.Windows.SW_SHOWMINIMIZED"></a>

#### SW\_SHOWMINIMIZED

<a id="phardwareitk.Extensions.Windows.SW_SHOWMAXIMIZED"></a>

#### SW\_SHOWMAXIMIZED

<a id="phardwareitk.Extensions.Windows.SW_MAXIMIZED"></a>

#### SW\_MAXIMIZED

<a id="phardwareitk.Extensions.Windows.SW_SHOWNOACTIVATE"></a>

#### SW\_SHOWNOACTIVATE

<a id="phardwareitk.Extensions.Windows.SW_SHOW"></a>

#### SW\_SHOW

<a id="phardwareitk.Extensions.Windows.SW_MINIMIZE"></a>

#### SW\_MINIMIZE

<a id="phardwareitk.Extensions.Windows.SW_SHOWMINNOACTIVE"></a>

#### SW\_SHOWMINNOACTIVE

<a id="phardwareitk.Extensions.Windows.SW_SHOWNA"></a>

#### SW\_SHOWNA

<a id="phardwareitk.Extensions.Windows.SW_RESTORE"></a>

#### SW\_RESTORE

<a id="phardwareitk.Extensions.Windows.SW_SHOWDEFAULT"></a>

#### SW\_SHOWDEFAULT

<a id="phardwareitk.Extensions.Windows.SW_FORCEMINIMIZE"></a>

#### SW\_FORCEMINIMIZE

<a id="phardwareitk.Extensions.Windows.WM_DISPLAYCHANGE"></a>

#### WM\_DISPLAYCHANGE

<a id="phardwareitk.Extensions.Windows.WM_ERASEBKGND"></a>

#### WM\_ERASEBKGND

<a id="phardwareitk.Extensions.Windows.WM_NCPAINT"></a>

#### WM\_NCPAINT

<a id="phardwareitk.Extensions.Windows.WM_PAINT"></a>

#### WM\_PAINT

<a id="phardwareitk.Extensions.Windows.WM_PRINT"></a>

#### WM\_PRINT

<a id="phardwareitk.Extensions.Windows.WM_PRINTCLIENT"></a>

#### WM\_PRINTCLIENT

<a id="phardwareitk.Extensions.Windows.WM_SETREDRAW"></a>

#### WM\_SETREDRAW

<a id="phardwareitk.Extensions.Windows.WM_SYNCPAINT"></a>

#### WM\_SYNCPAINT

<a id="phardwareitk.Extensions.Windows.WM_CREATE"></a>

#### WM\_CREATE

<a id="phardwareitk.Extensions.Windows.WM_DESTROY"></a>

#### WM\_DESTROY

<a id="phardwareitk.Extensions.Windows.WM_CLOSE"></a>

#### WM\_CLOSE

<a id="phardwareitk.Extensions.Windows.WM_SHOWWINDOW"></a>

#### WM\_SHOWWINDOW

<a id="phardwareitk.Extensions.Windows.WM_SIZE"></a>

#### WM\_SIZE

<a id="phardwareitk.Extensions.Windows.WM_MOVE"></a>

#### WM\_MOVE

<a id="phardwareitk.Extensions.Windows.WM_MOUSEMOVE"></a>

#### WM\_MOUSEMOVE

<a id="phardwareitk.Extensions.Windows.WM_LBUTTONDOWN"></a>

#### WM\_LBUTTONDOWN

<a id="phardwareitk.Extensions.Windows.WM_LBUTTONUP"></a>

#### WM\_LBUTTONUP

<a id="phardwareitk.Extensions.Windows.WM_RBUTTONDOWN"></a>

#### WM\_RBUTTONDOWN

<a id="phardwareitk.Extensions.Windows.WM_RBUTTONUP"></a>

#### WM\_RBUTTONUP

<a id="phardwareitk.Extensions.Windows.WM_MBUTTONDOWN"></a>

#### WM\_MBUTTONDOWN

<a id="phardwareitk.Extensions.Windows.WM_MBUTTONUP"></a>

#### WM\_MBUTTONUP

<a id="phardwareitk.Extensions.Windows.WM_MOUSEWHEEL"></a>

#### WM\_MOUSEWHEEL

<a id="phardwareitk.Extensions.Windows.WM_MOUSELEAVE"></a>

#### WM\_MOUSELEAVE

<a id="phardwareitk.Extensions.Windows.WM_MOUSEHOVER"></a>

#### WM\_MOUSEHOVER

<a id="phardwareitk.Extensions.Windows.WM_KEYDOWN"></a>

#### WM\_KEYDOWN

<a id="phardwareitk.Extensions.Windows.WM_KEYUP"></a>

#### WM\_KEYUP

<a id="phardwareitk.Extensions.Windows.WM_CHAR"></a>

#### WM\_CHAR

<a id="phardwareitk.Extensions.Windows.WM_IME_COMPOSITION"></a>

#### WM\_IME\_COMPOSITION

<a id="phardwareitk.Extensions.Windows.WM_IME_ENDCOMPOSITION"></a>

#### WM\_IME\_ENDCOMPOSITION

<a id="phardwareitk.Extensions.Windows.WM_DISPLAYCHANGE"></a>

#### WM\_DISPLAYCHANGE

<a id="phardwareitk.Extensions.Windows.WM_POWERBROADCAST"></a>

#### WM\_POWERBROADCAST

<a id="phardwareitk.Extensions.Windows.WM_TIMER"></a>

#### WM\_TIMER

<a id="phardwareitk.Extensions.Windows.PM_NOREMOVE"></a>

#### PM\_NOREMOVE

<a id="phardwareitk.Extensions.Windows.PM_REMOVE"></a>

#### PM\_REMOVE

<a id="phardwareitk.Extensions.Windows.PM_NOYIELD"></a>

#### PM\_NOYIELD

<a id="phardwareitk.Extensions.Windows.WS_BORDER"></a>

#### WS\_BORDER

<a id="phardwareitk.Extensions.Windows.WS_CAPTION"></a>

#### WS\_CAPTION

<a id="phardwareitk.Extensions.Windows.WS_CHILD"></a>

#### WS\_CHILD

<a id="phardwareitk.Extensions.Windows.WS_CHILDWINDOW"></a>

#### WS\_CHILDWINDOW

<a id="phardwareitk.Extensions.Windows.WS_CLIPCHILDREN"></a>

#### WS\_CLIPCHILDREN

<a id="phardwareitk.Extensions.Windows.WS_CLIPSIBLINGS"></a>

#### WS\_CLIPSIBLINGS

<a id="phardwareitk.Extensions.Windows.WS_DISABLED"></a>

#### WS\_DISABLED

<a id="phardwareitk.Extensions.Windows.WS_DLGFRAME"></a>

#### WS\_DLGFRAME

<a id="phardwareitk.Extensions.Windows.WS_GROUP"></a>

#### WS\_GROUP

<a id="phardwareitk.Extensions.Windows.WS_HSCROLL"></a>

#### WS\_HSCROLL

<a id="phardwareitk.Extensions.Windows.WS_ICONIC"></a>

#### WS\_ICONIC

<a id="phardwareitk.Extensions.Windows.WS_MAXIMIZE"></a>

#### WS\_MAXIMIZE

<a id="phardwareitk.Extensions.Windows.WS_MAXIMIZEBOX"></a>

#### WS\_MAXIMIZEBOX

<a id="phardwareitk.Extensions.Windows.WS_MINIMIZE"></a>

#### WS\_MINIMIZE

<a id="phardwareitk.Extensions.Windows.WS_MINIMIZEBOX"></a>

#### WS\_MINIMIZEBOX

<a id="phardwareitk.Extensions.Windows.WS_OVERLAPPED"></a>

#### WS\_OVERLAPPED

<a id="phardwareitk.Extensions.Windows.WS_SYSMENU"></a>

#### WS\_SYSMENU

<a id="phardwareitk.Extensions.Windows.WS_THICKFRAME"></a>

#### WS\_THICKFRAME

<a id="phardwareitk.Extensions.Windows.WS_OVERLAPPEDWINDOW"></a>

#### WS\_OVERLAPPEDWINDOW

<a id="phardwareitk.Extensions.Windows.WS_POPUP"></a>

#### WS\_POPUP

<a id="phardwareitk.Extensions.Windows.WS_POPUPWINDOW"></a>

#### WS\_POPUPWINDOW

<a id="phardwareitk.Extensions.Windows.WS_SIZEBOX"></a>

#### WS\_SIZEBOX

<a id="phardwareitk.Extensions.Windows.WS_TABSTOP"></a>

#### WS\_TABSTOP

<a id="phardwareitk.Extensions.Windows.WS_TILED"></a>

#### WS\_TILED

<a id="phardwareitk.Extensions.Windows.WS_TILEDWINDOW"></a>

#### WS\_TILEDWINDOW

<a id="phardwareitk.Extensions.Windows.WS_VISIBLE"></a>

#### WS\_VISIBLE

<a id="phardwareitk.Extensions.Windows.WS_VSCROLL"></a>

#### WS\_VSCROLL

<a id="phardwareitk.Extensions.Windows.HANDLE"></a>

#### HANDLE

<a id="phardwareitk.Extensions.Windows.HACCEL"></a>

#### HACCEL

<a id="phardwareitk.Extensions.Windows.HBITMAP"></a>

#### HBITMAP

<a id="phardwareitk.Extensions.Windows.HBRUSH"></a>

#### HBRUSH

<a id="phardwareitk.Extensions.Windows.HCOLORSPACE"></a>

#### HCOLORSPACE

<a id="phardwareitk.Extensions.Windows.HDC"></a>

#### HDC

<a id="phardwareitk.Extensions.Windows.HDESK"></a>

#### HDESK

<a id="phardwareitk.Extensions.Windows.HDWP"></a>

#### HDWP

<a id="phardwareitk.Extensions.Windows.HENHMETAFILE"></a>

#### HENHMETAFILE

<a id="phardwareitk.Extensions.Windows.HFONT"></a>

#### HFONT

<a id="phardwareitk.Extensions.Windows.HGDIOBJ"></a>

#### HGDIOBJ

<a id="phardwareitk.Extensions.Windows.HGLOBAL"></a>

#### HGLOBAL

<a id="phardwareitk.Extensions.Windows.HHOOK"></a>

#### HHOOK

<a id="phardwareitk.Extensions.Windows.HICON"></a>

#### HICON

<a id="phardwareitk.Extensions.Windows.HCURSOR"></a>

#### HCURSOR

<a id="phardwareitk.Extensions.Windows.HINSTANCE"></a>

#### HINSTANCE

<a id="phardwareitk.Extensions.Windows.HKEY"></a>

#### HKEY

<a id="phardwareitk.Extensions.Windows.HKL"></a>

#### HKL

<a id="phardwareitk.Extensions.Windows.HLOCAL"></a>

#### HLOCAL

<a id="phardwareitk.Extensions.Windows.HMENU"></a>

#### HMENU

<a id="phardwareitk.Extensions.Windows.HMETAFILE"></a>

#### HMETAFILE

<a id="phardwareitk.Extensions.Windows.HMODULE"></a>

#### HMODULE

<a id="phardwareitk.Extensions.Windows.HMONITOR"></a>

#### HMONITOR

<a id="phardwareitk.Extensions.Windows.HPALETTE"></a>

#### HPALETTE

<a id="phardwareitk.Extensions.Windows.HPEN"></a>

#### HPEN

<a id="phardwareitk.Extensions.Windows.HRGN"></a>

#### HRGN

<a id="phardwareitk.Extensions.Windows.HRSRC"></a>

#### HRSRC

<a id="phardwareitk.Extensions.Windows.HSTR"></a>

#### HSTR

<a id="phardwareitk.Extensions.Windows.HTASK"></a>

#### HTASK

<a id="phardwareitk.Extensions.Windows.HWINSTA"></a>

#### HWINSTA

<a id="phardwareitk.Extensions.Windows.HWND"></a>

#### HWND

<a id="phardwareitk.Extensions.Windows.SC_HANDLE"></a>

#### SC\_HANDLE

<a id="phardwareitk.Extensions.Windows.SERVICE_STATUS_HANDLE"></a>

#### SERVICE\_STATUS\_HANDLE

<a id="phardwareitk.Extensions.Windows.LPCOLESTR"></a>

#### LPCOLESTR

<a id="phardwareitk.Extensions.Windows.LPCWSTR"></a>

#### LPCWSTR

<a id="phardwareitk.Extensions.Windows.LPCSTR"></a>

#### LPCSTR

<a id="phardwareitk.Extensions.Windows.LPCVOID"></a>

#### LPCVOID

<a id="phardwareitk.Extensions.Windows.BYTE"></a>

#### BYTE

<a id="phardwareitk.Extensions.Windows.WORD"></a>

#### WORD

<a id="phardwareitk.Extensions.Windows.DWORD"></a>

#### DWORD

<a id="phardwareitk.Extensions.Windows.CHAR"></a>

#### CHAR

<a id="phardwareitk.Extensions.Windows.WCHAR"></a>

#### WCHAR

<a id="phardwareitk.Extensions.Windows.UINT"></a>

#### UINT

<a id="phardwareitk.Extensions.Windows.INT"></a>

#### INT

<a id="phardwareitk.Extensions.Windows.DOUBLE"></a>

#### DOUBLE

<a id="phardwareitk.Extensions.Windows.FLOAT"></a>

#### FLOAT

<a id="phardwareitk.Extensions.Windows.BOOLEAN"></a>

#### BOOLEAN

<a id="phardwareitk.Extensions.Windows.BOOL"></a>

#### BOOL

<a id="phardwareitk.Extensions.Windows.ULONG"></a>

#### ULONG

<a id="phardwareitk.Extensions.Windows.LONG"></a>

#### LONG

<a id="phardwareitk.Extensions.Windows.USHORT"></a>

#### USHORT

<a id="phardwareitk.Extensions.Windows.SHORT"></a>

#### SHORT

<a id="phardwareitk.Extensions.Windows.WPARAM"></a>

#### WPARAM

<a id="phardwareitk.Extensions.Windows.LPARAM"></a>

#### LPARAM

<a id="phardwareitk.Extensions.Windows.LRESULT"></a>

#### LRESULT

<a id="phardwareitk.Extensions.Windows.WNDPROC"></a>

#### WNDPROC

<a id="phardwareitk.Extensions.Windows.POINT"></a>

## POINT Objects

```python
class POINT(ctypes.Structure)
```

<a id="phardwareitk.Extensions.Windows.POINT._fields_"></a>

#### \_fields\_

<a id="phardwareitk.Extensions.Windows.MSG"></a>

## MSG Objects

```python
class MSG(ctypes.Structure)
```

<a id="phardwareitk.Extensions.Windows.MSG._fields_"></a>

#### \_fields\_

<a id="phardwareitk.Extensions.Windows.WNDCLASS"></a>

## WNDCLASS Objects

```python
class WNDCLASS(ctypes.Structure)
```

<a id="phardwareitk.Extensions.Windows.WNDCLASS._fields_"></a>

#### \_fields\_

<a id="phardwareitk.Extensions.C_Old"></a>

# phardwareitk.Extensions.C\_Old

This file includes all classes to write Basic 'C' Code inside Python without the need of Cython. (OLD VERSION)

<a id="phardwareitk.Extensions.C_Old.*"></a>

## \*

<a id="phardwareitk.Extensions.C_Old.sys"></a>

## sys

<a id="phardwareitk.Extensions.C_Old.errno"></a>

## errno

<a id="phardwareitk.Extensions.C_Old.os"></a>

## os

<a id="phardwareitk.Extensions.C_Old.MODULE_DIR"></a>

#### MODULE\_DIR

<a id="phardwareitk.Extensions.C_Old.mem"></a>

## mem

<a id="phardwareitk.Extensions.C_Old.NULL"></a>

#### NULL

<a id="phardwareitk.Extensions.C_Old.UNINITIALIZED"></a>

#### UNINITIALIZED

<a id="phardwareitk.Extensions.C_Old.FALSE"></a>

#### FALSE

<a id="phardwareitk.Extensions.C_Old.TRUE"></a>

#### TRUE

<a id="phardwareitk.Extensions.C_Old.EXIT_SUCCESS"></a>

#### EXIT\_SUCCESS

<a id="phardwareitk.Extensions.C_Old.EXIT_FALUIRE"></a>

#### EXIT\_FALUIRE

<a id="phardwareitk.Extensions.C_Old.METADATA_MAGIC"></a>

#### METADATA\_MAGIC

<a id="phardwareitk.Extensions.C_Old.base"></a>

#### base

<a id="phardwareitk.Extensions.C_Old.heap_base"></a>

#### heap\_base

<a id="phardwareitk.Extensions.C_Old.heap_ptr"></a>

#### heap\_ptr

<a id="phardwareitk.Extensions.C_Old.next_alloc"></a>

#### next\_alloc

<a id="phardwareitk.Extensions.C_Old.size"></a>

#### size

<a id="phardwareitk.Extensions.C_Old.stack_base"></a>

#### stack\_base

<a id="phardwareitk.Extensions.C_Old.stack_ptr"></a>

#### stack\_ptr

<a id="phardwareitk.Extensions.C_Old.memory"></a>

#### memory

Defaults to 64 bytes as size

<a id="phardwareitk.Extensions.C_Old.FREE_ADDR"></a>

#### FREE\_ADDR

<a id="phardwareitk.Extensions.C_Old.reset_mem"></a>

#### reset\_mem

```python
def reset_mem(size_: int, base_: int = 0x0, debug: bool = False) -> None
```

Resets the memory but updates its size

<a id="phardwareitk.Extensions.C_Old.get_next_alloc"></a>

#### get\_next\_alloc

```python
def get_next_alloc() -> int
```

<a id="phardwareitk.Extensions.C_Old.set_next_alloc"></a>

#### set\_next\_alloc

```python
def set_next_alloc(value: int) -> None
```

<a id="phardwareitk.Extensions.C_Old.append_next_alloc"></a>

#### append\_next\_alloc

```python
def append_next_alloc(value: int) -> None
```

<a id="phardwareitk.Extensions.C_Old.align"></a>

#### align

```python
def align(address: int, alignment: int) -> int
```

<a id="phardwareitk.Extensions.C_Old.full_delete"></a>

#### full\_delete

```python
def full_delete() -> None
```

Deletes everything from memory

<a id="phardwareitk.Extensions.C_Old.del_mem"></a>

#### del\_mem

```python
def del_mem(addr: int, size_: int, stack: bool = True) -> None
```

NULLS/frees the specified memory block for the specified size

<a id="phardwareitk.Extensions.C_Old.get_memory"></a>

#### get\_memory

```python
def get_memory() -> mem.Memory
```

<a id="phardwareitk.Extensions.C_Old.set_mem"></a>

#### set\_mem

```python
def set_mem(addr: int, size_: int, data: bytes) -> None
```

Sets memory to specfied data

<a id="phardwareitk.Extensions.C_Old.write_mem"></a>

#### write\_mem

```python
def write_mem(addr: int, size_: int, data: bytes) -> None
```

Writes data to specified address, unlike set_mem, this doesnt create metadata

<a id="phardwareitk.Extensions.C_Old.get_mem"></a>

#### get\_mem

```python
def get_mem(addr: int, size_: int) -> bytes
```

Gets memory

<a id="phardwareitk.Extensions.C_Old.push_stack"></a>

#### push\_stack

```python
def push_stack(data: bytes, size: int) -> None
```

Pushes data onto stack

<a id="phardwareitk.Extensions.C_Old.pop_stack"></a>

#### pop\_stack

```python
def pop_stack(size: int) -> bytes
```

Pops data from the stack and returns it

<a id="phardwareitk.Extensions.C_Old.get_mem_size"></a>

#### get\_mem\_size

```python
def get_mem_size() -> int
```

<a id="phardwareitk.Extensions.C_Old.metadata_verify"></a>

#### metadata\_verify

```python
def metadata_verify(data: bytes) -> int
```

<a id="phardwareitk.Extensions.C_Old.get_size_metadata"></a>

#### get\_size\_metadata

```python
def get_size_metadata(addr: int) -> int
```

<a id="phardwareitk.Extensions.C_Old.Size_t"></a>

## Size\_t Objects

```python
class Size_t()
```

size_t

<a id="phardwareitk.Extensions.C_Old.Size_t.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int) -> None
```

<a id="phardwareitk.Extensions.C_Old.Size_t.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Uint8_t"></a>

## Uint8\_t Objects

```python
class Uint8_t()
```

<a id="phardwareitk.Extensions.C_Old.Uint8_t.size"></a>

#### size

uint8_t

<a id="phardwareitk.Extensions.C_Old.Uint8_t.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint8_t.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Uint8_t.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint16_t"></a>

## Uint16\_t Objects

```python
class Uint16_t()
```

<a id="phardwareitk.Extensions.C_Old.Uint16_t.size"></a>

#### size

uint16_t

<a id="phardwareitk.Extensions.C_Old.Uint16_t.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint16_t.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Uint16_t.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint32_t"></a>

## Uint32\_t Objects

```python
class Uint32_t()
```

<a id="phardwareitk.Extensions.C_Old.Uint32_t.size"></a>

#### size

uint32_t

<a id="phardwareitk.Extensions.C_Old.Uint32_t.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint32_t.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Uint32_t.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint64_t"></a>

## Uint64\_t Objects

```python
class Uint64_t()
```

<a id="phardwareitk.Extensions.C_Old.Uint64_t.size"></a>

#### size

uint64_t

<a id="phardwareitk.Extensions.C_Old.Uint64_t.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Uint64_t.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Uint64_t.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Int8"></a>

## Int8 Objects

```python
class Int8()
```

int8

<a id="phardwareitk.Extensions.C_Old.Int8.size"></a>

#### size

<a id="phardwareitk.Extensions.C_Old.Int8.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Int8.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Int8.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Int16"></a>

## Int16 Objects

```python
class Int16()
```

int16

<a id="phardwareitk.Extensions.C_Old.Int16.size"></a>

#### size

<a id="phardwareitk.Extensions.C_Old.Int16.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Int16.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Int16.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Int32"></a>

## Int32 Objects

```python
class Int32()
```

int32

<a id="phardwareitk.Extensions.C_Old.Int32.size"></a>

#### size

<a id="phardwareitk.Extensions.C_Old.Int32.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Int32.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Int32.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Int64"></a>

## Int64 Objects

```python
class Int64()
```

int64

<a id="phardwareitk.Extensions.C_Old.Int64.size"></a>

#### size

<a id="phardwareitk.Extensions.C_Old.Int64.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Int64.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Int64.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Short"></a>

## Short Objects

```python
class Short(Int16)
```

short

<a id="phardwareitk.Extensions.C_Old.Short.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Short.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Short.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Long"></a>

## Long Objects

```python
class Long(Int32)
```

long

<a id="phardwareitk.Extensions.C_Old.Long.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Long.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Long.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Int"></a>

## Int Objects

```python
class Int(Int32)
```

int

<a id="phardwareitk.Extensions.C_Old.Int.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="phardwareitk.Extensions.C_Old.Int.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Int.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Char"></a>

## Char Objects

```python
class Char(Int8)
```

char

<a id="phardwareitk.Extensions.C_Old.Char.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: Union[str, int, bytes] = "\0") -> None
```

<a id="phardwareitk.Extensions.C_Old.Char.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Char.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Void"></a>

## Void Objects

```python
class Void()
```

void

<a id="phardwareitk.Extensions.C_Old.Void.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Void.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Pointer"></a>

## Pointer Objects

```python
class Pointer(Uint64_t)
```

*<value>

<a id="phardwareitk.Extensions.C_Old.Pointer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type_: object = Void,
             object_: object = Void(),
             save: bool = False) -> None
```

<a id="phardwareitk.Extensions.C_Old.Pointer.dereference"></a>

#### dereference

```python
def dereference() -> object
```

<a id="phardwareitk.Extensions.C_Old.Pointer.cast"></a>

#### cast

```python
def cast(type_: object, object_: object = None) -> None
```

Casts a pointer to another type

<a id="phardwareitk.Extensions.C_Old.Pointer.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Pointer.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Pointer.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, type_: object)
```

<a id="phardwareitk.Extensions.C_Old.get_string"></a>

#### get\_string

```python
def get_string(ptr: Union[Pointer[Char], str, bytes]) -> str
```

Returns a string from an	memory address

<a id="phardwareitk.Extensions.C_Old.CHAR_PTR"></a>

#### CHAR\_PTR

<a id="phardwareitk.Extensions.C_Old.Array"></a>

## Array Objects

```python
class Array()
```

<type>[<size>]

<a id="phardwareitk.Extensions.C_Old.Array.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: object, size: int) -> None
```

<a id="phardwareitk.Extensions.C_Old.Array.fill"></a>

#### fill

```python
def fill(data: bytes) -> None
```

<a id="phardwareitk.Extensions.C_Old.Array.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="phardwareitk.Extensions.C_Old.Array.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Array.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, type_: object = None, size_: int = 0)
```

<a id="phardwareitk.Extensions.C_Old.sizeof"></a>

#### sizeof

```python
def sizeof(value: object) -> Size_t
```

<a id="phardwareitk.Extensions.C_Old.malloc"></a>

#### malloc

```python
def malloc(size: Union[int, Size_t]) -> Pointer[Void]
```

Allocate memory

<a id="phardwareitk.Extensions.C_Old.free"></a>

#### free

```python
def free(ptr: Pointer, chunk_size: int = 1024 * 16) -> int
```

Free memory (doesn't delete pointer). This frees memory in chunks to be memory safe and default chunk size if 16KB

<a id="phardwareitk.Extensions.C_Old.calloc"></a>

#### calloc

```python
def calloc(nmemb: Union[int, Size_t], size: Union[int,
                                                  Size_t]) -> Pointer[Void]
```

Allocate memory and set all values to 0

<a id="phardwareitk.Extensions.C_Old.realloc"></a>

#### realloc

```python
def realloc(ptr: Pointer[Void], size: Union[int, Size_t]) -> Pointer[Void]
```

Reallocate memory with new size

<a id="phardwareitk.Extensions.C_Old.memcpy"></a>

#### memcpy

```python
def memcpy(dest: Pointer[Void], src: Pointer[Void],
           size: Union[int, Size_t]) -> Pointer[Void]
```

Copies [size] bytes from src to dest

<a id="phardwareitk.Extensions.C_Old.memmove"></a>

#### memmove

```python
def memmove(dest: Pointer[Void], src: Pointer[Void],
            size: Union[int, Size_t]) -> Pointer[Void]
```

Moves [size] bytes from src to dest

<a id="phardwareitk.Extensions.C_Old.memset"></a>

#### memset

```python
def memset(ptr: Pointer[Void], value: int,
           size: Union[int, Size_t]) -> Pointer[Void]
```

Sets [size] number of bytes of memory pointed to by [ptr] to the byte value [value]

<a id="phardwareitk.Extensions.C_Old.memchr"></a>

#### memchr

```python
def memchr(ptr: Pointer[Void], value: int,
           size: Union[int, Size_t]) -> Pointer[Void]
```

Finds the needed byte in memory

<a id="phardwareitk.Extensions.C_Old.memcmp"></a>

#### memcmp

```python
def memcmp(ptr1: Pointer[Void], ptr2: Pointer[Void],
           size: Union[int, Size_t]) -> int
```

Compares two data in memory

<a id="phardwareitk.Extensions.C_Old.write"></a>

#### write

```python
def write(ptr: Pointer[Void],
          data: bytes,
          size: Union[int, Size_t],
          no_meta: bool = False) -> int
```

Writes data to memory

<a id="phardwareitk.Extensions.C_Old.read"></a>

#### read

```python
def read(ptr: Pointer[Void], size: Union[int, Size_t]) -> bytes
```

Reads data from memory

<a id="phardwareitk.Extensions.C_Old.make_string"></a>

#### make\_string

```python
def make_string(value: str) -> Pointer[Char]
```

Makes a char*

<a id="phardwareitk.Extensions.C_Old.Struct"></a>

## Struct Objects

```python
class Struct()
```

struct {...}

<a id="phardwareitk.Extensions.C_Old.Struct.__init__"></a>

#### \_\_init\_\_

```python
def __init__(structure: dict) -> None
```

Format:
{
        '<Name>': {
                'type': <type in form of one of the class here>,
                'value': <value>,
                'ptr_type': <type of pointer. NOTE: Only if your 'type' is a Pointer and this is Optional, it will default to Void>,
                'array_type': <type of array. NOTE: Only if your 'type' is a Array>,
                'array_size': <size of array. NOTE: Only if your 'type' is a Array>
        }
}

<a id="phardwareitk.Extensions.C_Old.Struct.access"></a>

#### access

```python
def access(name: str) -> Any
```

Returns the value of the object

<a id="phardwareitk.Extensions.C_Old.Struct.get_offset"></a>

#### get\_offset

```python
def get_offset(name: str) -> int
```

Returns the offset of the object

<a id="phardwareitk.Extensions.C_Old.Struct.set"></a>

#### set

```python
def set(name: str, value: object) -> int
```

Sets the new value of a part of the struct. NOTE: The new value must be of the old defined type

<a id="phardwareitk.Extensions.C_Old.Struct.get_size"></a>

#### get\_size

```python
def get_size() -> int
```

Gets the size of the struct

<a id="phardwareitk.Extensions.C_Old.Struct.fill_b"></a>

#### fill\_b

```python
def fill_b(data: bytes, byteorder: str = "big") -> int
```

Fills the entire struct by the provided value (bytes)

<a id="phardwareitk.Extensions.C_Old.Struct.fill_f"></a>

#### fill\_f

```python
def fill_f(file: TextIO, byteorder: str = "big") -> int
```

Fills the struct from a file

<a id="phardwareitk.Extensions.C_Old.Struct.write_b"></a>

#### write\_b

```python
def write_b(buffer_: Pointer[Void],
            max_memory_usage: int = 1024 * 1024 * 64) -> int
```

Writes the filled structure to any point in memory.

**Arguments**:

- `buffer_` _Pointer[Void]_ - The address in memory to write to
- `max_memory_usage` _int_ - The maximum memory usage by this function to prevent crashes to Python/Terminal/Environment. Default is 64 MB / 1024*1024*64 bytes.
  

**Returns**:

- `int` - Return Code. 0 Means success.

<a id="phardwareitk.Extensions.C_Old.Struct.dereference"></a>

#### dereference

```python
def dereference(ptr: Pointer[Void]) -> None
```

Dereferences a pointer to the struct and returns the struct object.

<a id="phardwareitk.Extensions.C_Old.Struct.__del__"></a>

#### \_\_del\_\_

```python
def __del__() -> None
```

<a id="phardwareitk.Extensions.C_Old.Struct.__class_getitem__"></a>

#### \_\_class\_getitem\_\_

```python
@classmethod
def __class_getitem__(cls, struct: dict = {}, size_: int = 0)
```

<a id="phardwareitk.Extensions.C_Old.dereference_struct"></a>

#### dereference\_struct

```python
def dereference_struct(ptr: Pointer[Struct], structure: dict) -> Struct
```

Dereferences a pointer to a struct and returns the struct object.

**Arguments**:

- `ptr` _Pointer[Struct]_ - Pointer to the struct object
- `structure` _dict_ - The struct definition
  

**Returns**:

- `Struct` - The struct object

<a id="phardwareitk.Extensions"></a>

# phardwareitk.Extensions

Provides many extensions

<a id="phardwareitk.Extensions.*"></a>

## \*

<a id="phardwareitk.Extensions.os"></a>

## os

<a id="phardwareitk.Extensions.sys"></a>

## sys

<a id="phardwareitk.Extensions.PHardwareITK"></a>

#### PHardwareITK

<a id="phardwareitk.Extensions.PHardwareITK_P"></a>

#### PHardwareITK\_P

<a id="phardwareitk.Extensions.Color"></a>

## Color Objects

```python
class Color()
```

Color Class for defining color.

<a id="phardwareitk.Extensions.Color.__init__"></a>

#### \_\_init\_\_

```python
def __init__(color: str = "white", alpha: int = 255) -> None
```

Init of color class.

**Arguments**:

- `color` _str, optional_ - The color, leave and chose a function if, want to use RGB. Defaults to "white".

<a id="phardwareitk.Extensions.Color.RGB"></a>

#### RGB

```python
def RGB(r: int, g: int, b: int) -> tuple
```

Sets the color to the specified RGB values

**Arguments**:

- `r` _int_ - Red.
- `g` _int_ - Green.
- `b` _int_ - Blue.
  

**Returns**:

- `tuple` - Just a copy of the entered data in the form of a tuple.

<a id="phardwareitk.Extensions.Color.ColorToRGB"></a>

#### ColorToRGB

```python
def ColorToRGB(color: str) -> tuple
```

Converts the specified color into its specified RGB values IF IT IS PRESENT IN THE DICTIONARY.

**Arguments**:

- `color` _str_ - The color name.
  

**Returns**:

- `tuple` - The RGB values.

<a id="phardwareitk.Extensions.Color.HexToRGB"></a>

#### HexToRGB

```python
def HexToRGB(hex_code: str) -> tuple
```

Converts Hex code to RGB values IF IT IS PRESENT IN THE DICTIONARY.

**Arguments**:

- `hex_code` _str_ - The hexadecimal code.
  

**Returns**:

- `tuple` - The RGB values.

<a id="phardwareitk.Extensions.Color.ColorToHex"></a>

#### ColorToHex

```python
def ColorToHex(color: str) -> tuple
```

Converts a color name to a hexadecimal code IF IT IS PRESENT IN THE DICTIONARY.

**Arguments**:

- `color` _str_ - The color name.
  

**Returns**:

- `tuple` - The Hexadecimal value.

<a id="phardwareitk.Extensions.Color.to_rgb_code"></a>

#### to\_rgb\_code

```python
def to_rgb_code()
```

Converts the RGB tuple to an ANSI escape code.

<a id="phardwareitk.Extensions.Color.to_background_code"></a>

#### to\_background\_code

```python
def to_background_code()
```

Converts the RGB tuple to an ANSI background escape code.

<a id="phardwareitk.Extensions.PHeader"></a>

## PHeader Objects

```python
class PHeader()
```

Generates a PHardware Header.

**Arguments**:

- `version` _int, optional_ - The version of the program/File. Defaults to 1.
- `flags` _int, optional_ - The flags.. Defaults to 0.
- `magicCode` _Union[str, bytes], optional_ - The magic code in ASCII or string. Defaults to "PHardwareITK".

<a id="phardwareitk.Extensions.PHeader.__init__"></a>

#### \_\_init\_\_

```python
def __init__(version: int = 1,
             flags: int = 0,
             magicCode: Union[str, bytes] = "PHardwareITK") -> None
```

Initialize the PHeader.

**Arguments**:

- `version` _int, optional_ - The version of the program/File. Defaults to 1.
- `flags` _int, optional_ - The flags.. Defaults to 0.
- `magicCode` _Union[str, bytes], optional_ - The magic code in ASCII or string. Defaults to "PHardwareITK".

<a id="phardwareitk.Extensions.PHeader.calculateChecksum"></a>

#### calculateChecksum

```python
def calculateChecksum(Header: bytes) -> str
```

Calculate checksum of Header.

**Arguments**:

- `Header` _bytes_ - The header.
  

**Returns**:

- `str` - The checksum.

<a id="phardwareitk.Extensions.PHeader.Pack"></a>

#### Pack

```python
def Pack() -> Any
```

Packs the specified data into a single PHeader.


The structure includes:


- Magic number (4 bytes)

- Version (4 bytes)

- Flags (4 bytes)

- Placeholder for checksum (32 bytes as hexadecimal string)


**Returns**:

- `Any` - The header.

<a id="phardwareitk.Extensions.PHeader.UnPack"></a>

#### UnPack

```python
def UnPack(data: str) -> Any
```

Upacks the binary header into header fields.

<a id="phardwareitk.Extensions.PHeader.WriteToFile"></a>

#### WriteToFile

```python
def WriteToFile(filename)
```

Write the packed header data to a binary file.

<a id="phardwareitk.Extensions.PHeader.ReadFromFile"></a>

#### ReadFromFile

```python
def ReadFromFile(filename)
```

Read the header from a binary file and unpack the fields.

<a id="phardwareitk.Extensions.PBin"></a>

## PBin Objects

```python
class PBin()
```

PBin (PHardware Binary) is a custom binary serialization format designed to serialize various data types into a
compact binary representation. The format includes strings, integers, floats, and custom flags.

**Attributes**:

- `data` _bytes_ - The binary data representing the serialized object.

<a id="phardwareitk.Extensions.PBin.__init__"></a>

#### \_\_init\_\_

```python
def __init__(header: Optional[PHeader]) -> None
```

Initializes the PBin object with an empty data field.

<a id="phardwareitk.Extensions.PBin.Serialize"></a>

#### Serialize

```python
def Serialize(data: Union[str, bytes, int, dict, float, list, bool],
              CB_flag: Optional[bool] = None) -> bytes
```

Serializes a string, integer, float, and a custom flag into a binary format.

**Arguments**:

  data (Union[str, bytes (UTF-8), int, dict (CONVERTED TO STR), float, list, bool]): The data to serialize, in UTF-8 format.
- `CB_flag` _Optional[bool], optional_ - A flag indicating whether a custom byte follows. Defaults to None
  

**Returns**:

- `bytes` - The serialized binary data.

<a id="phardwareitk.Extensions.PBin.Deserialize"></a>

#### Deserialize

```python
def Deserialize(binary_data: bytes) -> tuple[str, bool, Optional[int]]
```

Deserializes the provided binary data into its original components.

**Arguments**:

- `binary_data` _bytes_ - The binary data to deserialize.
  

**Returns**:

- `tuple` - A tuple containing the deserialized values in the following order:
  - string_data (str): The deserialized string.
  - CB_flag (bool): Flag indicating whether custom data exists.
  - CB_data (Optional[int]): Custom data byte if present.

<a id="phardwareitk.Extensions.PBin.BinaryData"></a>

#### BinaryData

```python
@property
def BinaryData()
```

<a id="phardwareitk.Extensions.ToBytes"></a>

#### ToBytes

```python
def ToBytes(data: Optional[Union[str, dict, int, bool]]) -> Optional[bytes]
```

Encode the given data.

**Arguments**:

- `data` _Optional[Union[str, dict, int, bool]]_ - The data.
  

**Returns**:

- `Optional[bytes]` - Encoded data.

<a id="phardwareitk.Extensions.FromBytes"></a>

#### FromBytes

```python
def FromBytes(data: Optional[bytes]) -> Optional[str]
```

Decode the given data.

**Arguments**:

- `data` _Optional[bytes]_ - The data.
  

**Returns**:

- `Optional[str]` - Decoded data.

<a id="phardwareitk.Extensions.TextFont"></a>

## TextFont Objects

```python
class TextFont()
```

Just a Class for Font.

<a id="phardwareitk.Extensions.TextFont.__init__"></a>

#### \_\_init\_\_

```python
def __init__(font: str = "Arial",
             font_size: int = 11,
             font_color: Color = Color(),
             font_background_color: Color = Color("black"),
             Italic: bool = False,
             Underline: bool = False,
             Bold: bool = False,
             XtraBold: bool = False,
             StrikeThrough: bool = False) -> None
```

Initialize for TextFont class.

**Arguments**:

- `font` _str, optional_ - Font. Defaults to "Arial".
- `font_size` _int, optional_ - The size of the font. Defaults to 11.
- `font_color` _Color, optional_ - The color of the font. Defaults to Color().
- `font_background_color` _Color, optional_ - The bg color of the font. Defaults to Color("black").
- `Italic` _bool, optional_ - Font Italic. Defaults to False.
- `Underline` _bool, optional_ - Underlined Font. Defaults to False.
- `Bold` _bool, optional_ - Bold Font. Defaults to False.
- `XtraBold` _bool, optional_ - More Bolder Font. Defaults to False.
- `StrikeThrough` _bool, optional_ - StikeThrough Font. Defaults to False.

<a id="phardwareitk.Extensions.TextFont.to_font_code"></a>

#### to\_font\_code

```python
def to_font_code()
```

Generate the font style escape codes.

<a id="phardwareitk.Extensions.TextFont.to_reset_code"></a>

#### to\_reset\_code

```python
def to_reset_code()
```

Reset the font styles.

<a id="phardwareitk.Extensions.TextFont.to_font_size_code"></a>

#### to\_font\_size\_code

```python
def to_font_size_code()
```

Returns the Escape codes for Font Size. NOTE: Does't work with all OS/Terminals. Due to Font size not being supported universally.
OS like -> MacOS, XTerm Based, GNOME (Not via Escape codes), Windows (By changing data in a windows file), etc do support it.

Supported Platforms for this function -> MacOS (ITerm2), Xterm Based (Includes Konsole).

<a id="phardwareitk.Extensions.PWidget"></a>

## PWidget Objects

```python
class PWidget()
```

<a id="phardwareitk.Extensions.PWidget.__init__"></a>

#### \_\_init\_\_

```python
def __init__(x: int = 0,
             y: int = 0,
             width: int = 5,
             height: int = 5,
             radius: int = 0,
             bgColor: Color = Color(),
             textWrap: bool = False,
             textFont: TextFont = TextFont(),
             text: str = "") -> None
```

Initialize function for PWidget class.

**Arguments**:

- `x` _int, optional_ - X coordinate. Defaults to 0.
- `y` _int, optional_ - Y coordinate. Defaults to 0.
- `width` _int, optional_ - Width of widget. Defaults to 5.
- `height` _int, optional_ - Height of widget. Defaults to 5.
- `radius` _int, optional_ - Radius of widget (If required). Defaults to 0.
- `bgColor` _Color, optional_ - Background color of widget. Defaults to Color().
- `textWrap` _bool, optional_ - Text In Widget?. Defaults to False.
- `textFont` _TextFont, optional_ - The Text Font (if required). Defaults to TextFont().
- `text` _str, optional_ - The text. (if required). Defaults to "".

<a id="phardwareitk.Extensions.PWidget.Contains"></a>

#### Contains

```python
def Contains(x: int, y: int) -> bool
```

Check if a point (x, y) is within the widget's boundaries.

<a id="phardwareitk.Extensions.PWidget.Draw"></a>

#### Draw

```python
def Draw(window: Any)
```

Draw the widget onto the window. Should be overridden by subclasses.

<a id="phardwareitk.Extensions.PWidget.Change"></a>

#### Change

```python
def Change(x: Optional[int] = None,
           y: Optional[int] = None,
           width: Optional[int] = None,
           height: Optional[int] = None,
           radius: Optional[int] = None,
           bgColor: Optional[Color] = None,
           textWrap: Optional[bool] = None,
           textFont: Optional[TextFont] = None,
           text: Optional[str] = None) -> None
```

Change the details.

**Arguments**:

- `x` _Optional[int], optional_ - X. Defaults to None.
- `y` _Optional[int], optional_ - Y. Defaults to None.
- `width` _Optional[int], optional_ - Width. Defaults to None.
- `height` _Optional[int], optional_ - Height. Defaults to None.
- `radius` _Optional[int], optional_ - Radius. Defaults to None.
- `bgColor` _Optional[Color], optional_ - Background Color. Defaults to None.
- `textWrap` _Optional[bool], optional_ - Text Wrap?. Defaults to None.
- `textFont` _TextFont, optional_ - Text Font. Defaults to None.
- `text` _Optional[str], optional_ - Text. Defaults to None.

<a id="phardwareitk.Extensions.PIcon"></a>

## PIcon Objects

```python
class PIcon()
```

PIcon (PHardware Icon) class.

<a id="phardwareitk.Extensions.PIcon.__init__"></a>

#### \_\_init\_\_

```python
def __init__(iconPath: Optional[str] = "",
             x: Optional[int] = None,
             y: Optional[int] = None,
             width: Optional[int] = None,
             height: Optional[int] = None) -> None
```

The INIT function of the PIcon class.

**Arguments**:

- `iconPath` _Optional[str], optional_ - The path to the icon file. Defaults to "".
- `x` _Optional[int], optional_ - The X coordinate of the icon. Defaults to None.
- `y` _Optional[int], optional_ - The Y coordinate of the icon. Defaults to None.
- `width` _Optional[int], optional_ - The Width of the icon. Defaults to None.
- `height` _Optional[int], optional_ - The Height of the icon. Defaults to None.

<a id="phardwareitk.Extensions.PIcon.LoadImageSDL2"></a>

#### LoadImageSDL2

```python
def LoadImageSDL2() -> Any
```

Loads the image for SDL2.

**Returns**:

- `Any` - Loaded image.

<a id="phardwareitk.Extensions.PIcon.SetIconSDL2"></a>

#### SetIconSDL2

```python
def SetIconSDL2(window: Any) -> None
```

Changes the icon in the specified window. SDL2.

**Arguments**:

- `window` _Any_ - The window.

<a id="phardwareitk.Extensions.PIcon.Free"></a>

#### Free

```python
def Free() -> None
```

Frees the image.

<a id="phardwareitk.Extensions.PIcon.ToBytes"></a>

#### ToBytes

```python
def ToBytes(data: Optional[Union[str, dict, int, bool]]) -> Optional[bytes]
```

Encode the given data.

**Arguments**:

- `data` _Optional[Union[str, dict, int, bool]]_ - The data.
  

**Returns**:

- `Optional[bytes]` - Encoded data.

<a id="phardwareitk.Extensions.PIcon.FromBytes"></a>

#### FromBytes

```python
def FromBytes(data: Optional[bytes]) -> Optional[str]
```

Decode the given data.

**Arguments**:

- `data` _Optional[bytes]_ - The data.
  

**Returns**:

- `Optional[str]` - Decoded data.

<a id="phardwareitk.Extensions.HyperIn"></a>

# phardwareitk.Extensions.HyperIn

<a id="phardwareitk.Extensions.HyperIn.*"></a>

## \*

<a id="phardwareitk.Extensions.HyperIn.*"></a>

## \*

<a id="phardwareitk.Extensions.HyperIn.time"></a>

## time

<a id="phardwareitk.Extensions.HyperIn.inputH"></a>

#### inputH

```python
def inputH(*values: object,
           seperator: Union[str, None] = " ",
           endl: Union[str, None] = None,
           backgroundColorEnabled: bool = False,
           FontEnabled: bool = False,
           Font: TextFont = TextFont(),
           mask: bool = False,
           maskCharacter: str = "*",
           History: Optional[list] = None,
           Regex_ReEntry: Optional[str] = None,
           Regex_Msg: Optional[str] = None,
           Regex_Time: Optional[float] = None,
           DefaultVal: Optional[str] = None,
           cpuHoggin: float = 0.005) -> str
```

Hyper version of Python's input function.


NOTE: This function uses custom key input detection and, if any bug occurs, please post in [https://github.com/AkshuDev/PHardwareITK/issues]


**Arguments**:

- `seperator` _Union[str, None], optional_ - The seperator between [*values]. Defaults to " ".
- `endl` _Union[str, None], optional_ - The string to add at the end of [*values]. None if don't want. Defaults to None.
- `backgroundColorEnabled` _bool, optional_ - Wether to enable background-color. Defaults to False.
- `FontEnabled` _bool, optional_ - Wether to enable the custom font. Defaults to False.
- `Font` _TextFont, optional_ - The font. Defaults to TextFont().
- `mask` _bool, optional_ - Whether to mask the input text. Defaults to False.
- `maskCharacter` _str, optional_ - The character used to mask the input text. Defaults to '*'.
- `History` _Optional[list], optional_ - If not None, Upon receiving arrow keys, The old prompts/History will appear (User choice to enter history or not). Defaults to None.
- `Regex_ReEntry` _Optional[str], optional_ - If not None, The input will be going through a validation via the given regex. Defaults to None.
- `Regex_Msg` _Optional[str], optional_ - If not None and if the Regex_ReEntry is not None, then if match fails, then this msg will be printed, without newline. Please add newline before if you want. Defaults to None.
- `Regex_Time` _Optional[float], optional_ - If not None and if the Regex_ReEntry is not None, then if match fails, then this specifies the time, the message will be shown for. Defaults to None.
- `DefaultVal` _Optional[str], optional_ - If not None, If the input is empty, the provided Value will be returned.
- `cpuHoggin` _float, optional_ - Cpu Hogging is very much required for programs like this. This is a complex input function, so unlike python's input function, it cannot avoid CPU usage. To prevent it a small delay is added at the end of the loop. IT CANNOT BE 0 as it can harm the CPU. Defaults to 0.005 seconds or 5 milliseconds.
  

**Returns**:

- `str` - The user provided input

<a id="phardwareitk.Extensions.HyperOut"></a>

# phardwareitk.Extensions.HyperOut

<a id="phardwareitk.Extensions.HyperOut.*"></a>

## \*

<a id="phardwareitk.Extensions.HyperOut.*"></a>

## \*

<a id="phardwareitk.Extensions.HyperOut.sys"></a>

## sys

<a id="phardwareitk.Extensions.HyperOut.os"></a>

## os

<a id="phardwareitk.Extensions.HyperOut.printH"></a>

#### printH

```python
def printH(*values: object,
           seperator: Union[str, None] = " ",
           endl: Union[str, None] = "\n",
           File: Union[str, None] = None,
           Flush: bool = False,
           backgroundColorEnabled: bool = False,
           FontEnabled: bool = False,
           Font: TextFont = TextFont()) -> None
```

A Hyper version of Python's print function.

**Arguments**:

- `seperator` _Union[str, None], optional_ - Seperator between values in [*values]. Defaults to " ".
- `endl` _Union[str, None], optional_ - The ending string to include at the end of the values. None is don't want. Defaults to "
  ".
- `File` _Union[str, None], optional_ - Wether to save the print contents in a file before printing in console. Defaults to None.
- `Flush` _bool, optional_ - Wether to use Flush during printing. Defaults to False.
- `backgroundColorEnabled` _bool, optional_ - Wether to enable background-color. Defaults to False.
- `FontEnabled` _bool, optional_ - Wether to enable custom font. Defaults to False.
- `Font` _TextFont, optional_ - The font. Defaults to TextFont().
  
- `NOTE` - The font-size is not universally supported in all Terminals. Terminals like -> Xterm, ITerm2 (MacOS), etc do support it, but please check.

<a id="phardwareitk.Extensions.HyperOut.exitH"></a>

#### exitH

```python
def exitH(ExitCode: Optional[int],
          *ExitMsg: Optional[object],
          seperator: Optional[str] = " ",
          endl: Optional[str] = "\n",
          File: Optional[str] = None,
          Flush: bool = False,
          backgroundColorEnabled: bool = False,
          FontEnabled: bool = False,
          Font: TextFont = TextFont()) -> None
```

A hyper version of Python's exit function.

**Arguments**:

- `ExitCode` _Optional[int]_ - The ExitCode.
- `seperator` _Union[str, None], optional_ - Seperator between values in [*ExitMsg]. Defaults to " ".
- `endl` _Union[str, None], optional_ - The ending string to include at the end of the ExitMsg. None is don't want. Defaults to "
  ".
- `File` _Union[str, None], optional_ - Wether to save the print contents in a file before printing in console. Defaults to None.
- `Flush` _bool, optional_ - Wether to use Flush during printing. Defaults to False.
- `backgroundColorEnabled` _bool, optional_ - Wether to enable background-color. Defaults to False.
- `FontEnabled` _bool, optional_ - Wether to enable custom font. Defaults to False.
- `Font` _TextFont, optional_ - The font. Defaults to TextFont().

<a id="phardwareitk.Extensions.HyperOut.evalH"></a>

#### evalH

```python
def evalH(source: Union[str, Any],
          globals: Optional[dict[str, Any]] = None,
          locals: Optional[Mapping[str, object]] = None,
          Log: bool = False) -> Any
```

A Hyper version of Python's eval.

Enhancements:
Security: Restrics specific functions that can cause harm to OS/Files/etc. ONLY FOR STRING LITERALS.
Log: Logging functionality.

**Arguments**:

- `source` _Union[str, Any]_ - The source string/ReadableBuffer/CodeType object.
- `globals` _Optional[dict[str, Any]], optional_ - The globals in eval. Defaults to None.
- `locals` _Optional[Mapping[str, object]], optional_ - The locals in eval. Defaults to None.
- `Log` _bool, optional_ - Log evaluate. Defaults to False.
  

**Returns**:

- `Any` - Compiled expr.

<a id="phardwareitk.Extensions.HyperOut.progressH"></a>

#### progressH

```python
def progressH(update: bool = False,
              basePos: tuple[Union[str, int]] = (0, "CPos+1"),
              cvalue: int = 0,
              maxValue: int = 100,
              useP: str = "#",
              useNP: str = "-",
              Pcolor: Color = Color("green"),
              msgColor: Color = Color("white"),
              NPcolor: Color = Color("red"),
              onMaxMsg: Optional[str] = None,
              defMsg: Optional[str] = None,
              First: bool = True,
              HideCursor: bool = True) -> Union[str, None]
```

Progress Indicator Hyper.

**Arguments**:

- `update` _bool, optional_ - Wether to update a single value, give the value to update in cvalue. Defaults to False.
- `basePos` _tuple[Union[str, int]], optional_ - The base position for the progressbar. (x, y). Use CPos to define Current Pos and you can add +/- after it to define the lines/chars. Defaults to (0, "CPos+1").
- `cvalue` _int, optional_ - The current value. Defaults to 0.
- `maxValue` _int, optional_ - The max value. Defaults to 100.
- `useP` _str, optional_ - The character to use for the parts which is already progressed. Defaults to "#".
- `useNP` _str, optional_ - The character to use for the parts which are not progressed. Defaults to "-".
- `Ncolor` _Color, optional_ - The color of the Progressed Section of the Bar. Defaults to Color("green").
- `NPcolor` _Color, optional_ - The color of the Unprogressed Section of the Bar. Defaults to Color("red").
- `MsgColor` _Color, optional_ - The color of the message. Defaults to Color("white").
- `onMaxMsg` _Optional[str], optional_ - The message to include if fully progressed. NOTE: Include ' ' before the message. Defaults to None.
- `defMsg` _Optional[str], optional_ - The default message to include after the progress Bar. Defaults to None.
- `First` _bool, optional_ - If first time called, then set to True, otherwise set to False. Defaults to True.
- `HideCursor` _bool, optional_ - If True, the cursor is hidden. Defaults to True.
  

**Returns**:

  Union[str, None]: Str if an error occurred, otherwise None. STR 'MAX' is returned if current Value == max Value.

<a id="phardwareitk.Extensions.HyperOut.cacheH"></a>

#### cacheH

```python
def cacheH(path: str,
           callable: Optional[object] = None,
           expiration: Optional[int] = None) -> Union[Optional[str], Any]
```

Cache Hyper function.

Generates Cache files, Incase file already exists, returns the function output.


Useful For:

1. Large Functions that cannot be run easily.

2. Cache functions.

3. Large Data.

4. Easy Loading and Unloading.

**Arguments**:

- `path` _str_ - The Path to the Cache file.
- `callable` _Optional[object], optional_ - The function to cache. Defaults to None.
- `expiration` _Optional[int], optional_ - If not None, The expiration time, in hours. Defaults to None.
  

**Returns**:

  None | str | Any: string, for success, if string includes '$Error$' at the start there is a Error. In case file already exists, the result of the callable function will be returned.

<a id="phardwareitk.Extensions.Windows_emu"></a>

# phardwareitk.Extensions.Windows\_emu

This file includes everything you can think of for making C/Python/Asm/C++/C#/etc code for windows, which will run on any OS that python runs on.

<a id="phardwareitk.Extensions.Windows_emu.sys"></a>

## sys

<a id="phardwareitk.Extensions.Windows_emu.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows_emu.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows_emu.*"></a>

## \*

<a id="phardwareitk.Extensions.Windows_emu.CS_BYTEALIGNCLIENT"></a>

#### CS\_BYTEALIGNCLIENT

<a id="phardwareitk.Extensions.Windows_emu.CS_BYTEALIGNWINDOW"></a>

#### CS\_BYTEALIGNWINDOW

<a id="phardwareitk.Extensions.Windows_emu.CS_CLASSDC"></a>

#### CS\_CLASSDC

<a id="phardwareitk.Extensions.Windows_emu.CS_DBLCLKS"></a>

#### CS\_DBLCLKS

<a id="phardwareitk.Extensions.Windows_emu.CS_DROPSHADOW"></a>

#### CS\_DROPSHADOW

<a id="phardwareitk.Extensions.Windows_emu.CS_GLOBALCLASS"></a>

#### CS\_GLOBALCLASS

<a id="phardwareitk.Extensions.Windows_emu.CS_HREDRAW"></a>

#### CS\_HREDRAW

<a id="phardwareitk.Extensions.Windows_emu.CS_NOCLOSE"></a>

#### CS\_NOCLOSE

<a id="phardwareitk.Extensions.Windows_emu.CS_OWNDC"></a>

#### CS\_OWNDC

<a id="phardwareitk.Extensions.Windows_emu.CS_PARENTDC"></a>

#### CS\_PARENTDC

<a id="phardwareitk.Extensions.Windows_emu.CS_SAVEBITS"></a>

#### CS\_SAVEBITS

<a id="phardwareitk.Extensions.Windows_emu.CS_VREDRAW"></a>

#### CS\_VREDRAW

<a id="phardwareitk.Extensions.Windows_emu.IDI_APPLICATION"></a>

#### IDI\_APPLICATION

<a id="phardwareitk.Extensions.Windows_emu.IDI_ERROR"></a>

#### IDI\_ERROR

<a id="phardwareitk.Extensions.Windows_emu.IDI_QUESTION"></a>

#### IDI\_QUESTION

<a id="phardwareitk.Extensions.Windows_emu.IDI_WARNING"></a>

#### IDI\_WARNING

<a id="phardwareitk.Extensions.Windows_emu.IDI_INFORMATION"></a>

#### IDI\_INFORMATION

<a id="phardwareitk.Extensions.Windows_emu.IDI_WINLOGO"></a>

#### IDI\_WINLOGO

<a id="phardwareitk.Extensions.Windows_emu.IDI_SHIELD"></a>

#### IDI\_SHIELD

<a id="phardwareitk.Extensions.Windows_emu.IDC_ARROW"></a>

#### IDC\_ARROW

<a id="phardwareitk.Extensions.Windows_emu.IDC_IBEAM"></a>

#### IDC\_IBEAM

<a id="phardwareitk.Extensions.Windows_emu.IDC_WAIT"></a>

#### IDC\_WAIT

<a id="phardwareitk.Extensions.Windows_emu.IDC_CROSS"></a>

#### IDC\_CROSS

<a id="phardwareitk.Extensions.Windows_emu.IDC_UPARROW"></a>

#### IDC\_UPARROW

<a id="phardwareitk.Extensions.Windows_emu.IDC_SIZENWSE"></a>

#### IDC\_SIZENWSE

<a id="phardwareitk.Extensions.Windows_emu.IDC_SIZENESW"></a>

#### IDC\_SIZENESW

<a id="phardwareitk.Extensions.Windows_emu.IDC_SIZEWE"></a>

#### IDC\_SIZEWE

<a id="phardwareitk.Extensions.Windows_emu.IDC_SIZENS"></a>

#### IDC\_SIZENS

<a id="phardwareitk.Extensions.Windows_emu.IDC_SIZEALL"></a>

#### IDC\_SIZEALL

<a id="phardwareitk.Extensions.Windows_emu.IDC_NO"></a>

#### IDC\_NO

<a id="phardwareitk.Extensions.Windows_emu.IDC_HAND"></a>

#### IDC\_HAND

<a id="phardwareitk.Extensions.Windows_emu.IDC_APPSTARTING"></a>

#### IDC\_APPSTARTING

<a id="phardwareitk.Extensions.Windows_emu.IDC_HELP"></a>

#### IDC\_HELP

<a id="phardwareitk.Extensions.Windows_emu.IDC_PIN"></a>

#### IDC\_PIN

<a id="phardwareitk.Extensions.Windows_emu.IDC_PERSON"></a>

#### IDC\_PERSON

<a id="phardwareitk.Extensions.Windows_emu.WHITE_BRUSH"></a>

#### WHITE\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.LTGRAY_BRUSH"></a>

#### LTGRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.GRAY_BRUSH"></a>

#### GRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.DKGRAY_BRUSH"></a>

#### DKGRAY\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.BLACK_BRUSH"></a>

#### BLACK\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.NULL_BRUSH"></a>

#### NULL\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.HOLLOW_BRUSH"></a>

#### HOLLOW\_BRUSH

<a id="phardwareitk.Extensions.Windows_emu.WHITE_PEN"></a>

#### WHITE\_PEN

<a id="phardwareitk.Extensions.Windows_emu.BLACK_PEN"></a>

#### BLACK\_PEN

<a id="phardwareitk.Extensions.Windows_emu.NULL_PEN"></a>

#### NULL\_PEN

<a id="phardwareitk.Extensions.Windows_emu.OEM_FIXED_FONT"></a>

#### OEM\_FIXED\_FONT

<a id="phardwareitk.Extensions.Windows_emu.ANSI_FIXED_FONT"></a>

#### ANSI\_FIXED\_FONT

<a id="phardwareitk.Extensions.Windows_emu.ANSI_VAR_FONT"></a>

#### ANSI\_VAR\_FONT

<a id="phardwareitk.Extensions.Windows_emu.SYSTEM_FONT"></a>

#### SYSTEM\_FONT

<a id="phardwareitk.Extensions.Windows_emu.DEVICE_DEFAULT_FONT"></a>

#### DEVICE\_DEFAULT\_FONT

<a id="phardwareitk.Extensions.Windows_emu.DEFAULT_PALETTE"></a>

#### DEFAULT\_PALETTE

<a id="phardwareitk.Extensions.Windows_emu.CW_USEDEFAULT"></a>

#### CW\_USEDEFAULT

<a id="phardwareitk.Extensions.Windows_emu.SW_HIDE"></a>

#### SW\_HIDE

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWNORMAL"></a>

#### SW\_SHOWNORMAL

<a id="phardwareitk.Extensions.Windows_emu.SW_NORMAL"></a>

#### SW\_NORMAL

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWMINIMIZED"></a>

#### SW\_SHOWMINIMIZED

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWMAXIMIZED"></a>

#### SW\_SHOWMAXIMIZED

<a id="phardwareitk.Extensions.Windows_emu.SW_MAXIMIZED"></a>

#### SW\_MAXIMIZED

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWNOACTIVATE"></a>

#### SW\_SHOWNOACTIVATE

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOW"></a>

#### SW\_SHOW

<a id="phardwareitk.Extensions.Windows_emu.SW_MINIMIZE"></a>

#### SW\_MINIMIZE

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWMINNOACTIVE"></a>

#### SW\_SHOWMINNOACTIVE

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWNA"></a>

#### SW\_SHOWNA

<a id="phardwareitk.Extensions.Windows_emu.SW_RESTORE"></a>

#### SW\_RESTORE

<a id="phardwareitk.Extensions.Windows_emu.SW_SHOWDEFAULT"></a>

#### SW\_SHOWDEFAULT

<a id="phardwareitk.Extensions.Windows_emu.SW_FORCEMINIMIZE"></a>

#### SW\_FORCEMINIMIZE

<a id="phardwareitk.Extensions.Windows_emu.WM_DISPLAYCHANGE"></a>

#### WM\_DISPLAYCHANGE

<a id="phardwareitk.Extensions.Windows_emu.WM_ERASEBKGND"></a>

#### WM\_ERASEBKGND

<a id="phardwareitk.Extensions.Windows_emu.WM_NCPAINT"></a>

#### WM\_NCPAINT

<a id="phardwareitk.Extensions.Windows_emu.WM_PAINT"></a>

#### WM\_PAINT

<a id="phardwareitk.Extensions.Windows_emu.WM_PRINT"></a>

#### WM\_PRINT

<a id="phardwareitk.Extensions.Windows_emu.WM_PRINTCLIENT"></a>

#### WM\_PRINTCLIENT

<a id="phardwareitk.Extensions.Windows_emu.WM_SETREDRAW"></a>

#### WM\_SETREDRAW

<a id="phardwareitk.Extensions.Windows_emu.WM_SYNCPAINT"></a>

#### WM\_SYNCPAINT

<a id="phardwareitk.Extensions.Windows_emu.WM_DESTROY"></a>

#### WM\_DESTROY

<a id="phardwareitk.Extensions.Windows_emu.WM_CLOSE"></a>

#### WM\_CLOSE

<a id="phardwareitk.Extensions.Windows_emu.PM_NOREMOVE"></a>

#### PM\_NOREMOVE

<a id="phardwareitk.Extensions.Windows_emu.PM_REMOVE"></a>

#### PM\_REMOVE

<a id="phardwareitk.Extensions.Windows_emu.PM_NOYIELD"></a>

#### PM\_NOYIELD

<a id="phardwareitk.Extensions.Windows_emu.LPCWSTR"></a>

## LPCWSTR Objects

```python
class LPCWSTR(str)
```

Represents a pointer to a wide-character string (Unicode).

<a id="phardwareitk.Extensions.Windows_emu.DWORD"></a>

## DWORD Objects

```python
class DWORD(int)
```

Represents a 32-bit unsigned integer.

<a id="phardwareitk.Extensions.Windows_emu.HANDLE"></a>

## HANDLE Objects

```python
class HANDLE(int)
```

Represents a handle to an object (file, process, etc.).

<a id="phardwareitk.Extensions.Windows_emu.HANDLE.INVALID_HANDLE_VALUE"></a>

#### INVALID\_HANDLE\_VALUE

Represents a failure case

<a id="phardwareitk.Extensions.Windows_emu.BOOL"></a>

## BOOL Objects

```python
class BOOL(int)
```

Represents a bool.

<a id="phardwareitk.Extensions.Windows_emu.BYTE"></a>

## BYTE Objects

```python
class BYTE(int)
```

Represents a byte.

<a id="phardwareitk.Extensions.Windows_emu.WORD"></a>

## WORD Objects

```python
class WORD(int)
```

Represents a word (16-bit unsigned integer)

<a id="phardwareitk.Extensions.Windows_emu.LONG"></a>

## LONG Objects

```python
class LONG(int)
```

Represents a LONG (32-bit signed integer).

<a id="phardwareitk.Extensions.Windows_emu.PLONG"></a>

## PLONG Objects

```python
class PLONG(Pointer)
```

Represents a pointer to a LONG (32-bit signed integer).

<a id="phardwareitk.Extensions.Windows_emu.PLONG.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.Extensions.Windows_emu.LPVOID"></a>

## LPVOID Objects

```python
class LPVOID(Pointer)
```

A Pointer to a void type.

<a id="phardwareitk.Extensions.Windows_emu.LPVOID.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: bytearray)
```

<a id="phardwareitk.Extensions.Windows_emu.LPCVOID"></a>

## LPCVOID Objects

```python
class LPCVOID(Pointer)
```

A Pointer to a constant void type (immutable raw bytes).

<a id="phardwareitk.Extensions.Windows_emu.LPCVOID.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: bytes)
```

<a id="phardwareitk.Extensions.Windows_emu.LPDWORD"></a>

## LPDWORD Objects

```python
class LPDWORD(Pointer)
```

A Pointer to a DWORD (32-bit unsigned integer).

<a id="phardwareitk.Extensions.Windows_emu.LPDWORD.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.Extensions.Windows_emu.LPLONG"></a>

## LPLONG Objects

```python
class LPLONG(Pointer)
```

A Pointer to a LONG (32-bit signed integer).

<a id="phardwareitk.Extensions.Windows_emu.LPLONG.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int)
```

<a id="phardwareitk.Extensions.Windows_emu.LPOVERLAPPED"></a>

## LPOVERLAPPED Objects

```python
class LPOVERLAPPED(Pointer)
```

A Pointer to an OVERLAPPED structure.

<a id="phardwareitk.Extensions.Windows_emu.LPOVERLAPPED.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: dict)
```

<a id="phardwareitk.Extensions.Windows_emu.LPSECURITY_ATTRIBUTES"></a>

## LPSECURITY\_ATTRIBUTES Objects

```python
class LPSECURITY_ATTRIBUTES(Pointer)
```

A Pointer to security attributes.

<a id="phardwareitk.Extensions.Windows_emu.LPSECURITY_ATTRIBUTES.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: dict)
```

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode"></a>

## FileAccessMode Objects

```python
class FileAccessMode()
```

A class for all the File Access modes, example -> read, write, etc

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode.GENERIC_READ"></a>

#### GENERIC\_READ

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode.GENERIC_WRITE"></a>

#### GENERIC\_WRITE

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode.GENERIC_EXECUTE"></a>

#### GENERIC\_EXECUTE

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode.ALL"></a>

#### ALL

<a id="phardwareitk.Extensions.Windows_emu.FileAccessMode.convert_to_python"></a>

#### convert\_to\_python

```python
@staticmethod
def convert_to_python(value: Union[int, DWORD]) -> str
```

Converts a DWORD value to a Python file mode string (e.g., "r", "w", "w+", "a+").

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition"></a>

## FileDisposition Objects

```python
class FileDisposition()
```

Defines Windows file creation/opening behaviors.

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition.CREATE_NEW"></a>

#### CREATE\_NEW

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition.CREATE_ALWAYS"></a>

#### CREATE\_ALWAYS

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition.OPEN_EXISTING"></a>

#### OPEN\_EXISTING

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition.OPEN_ALWAYS"></a>

#### OPEN\_ALWAYS

<a id="phardwareitk.Extensions.Windows_emu.FileDisposition.TRUNCATE_EXISTING"></a>

#### TRUNCATE\_EXISTING

<a id="phardwareitk.Extensions.Windows_emu.FilePointerMoveMethod"></a>

## FilePointerMoveMethod Objects

```python
class FilePointerMoveMethod()
```

Defines how file pointers are moved.

<a id="phardwareitk.Extensions.Windows_emu.FilePointerMoveMethod.FILE_BEGIN"></a>

#### FILE\_BEGIN

<a id="phardwareitk.Extensions.Windows_emu.FilePointerMoveMethod.FILE_CURRENT"></a>

#### FILE\_CURRENT

<a id="phardwareitk.Extensions.Windows_emu.FilePointerMoveMethod.FILE_END"></a>

#### FILE\_END

<a id="phardwareitk.Extensions.Windows_emu.FileHandleManager"></a>

## FileHandleManager Objects

```python
class FileHandleManager()
```

Manages file handles.

<a id="phardwareitk.Extensions.Windows_emu.FileHandleManager.create_handle"></a>

#### create\_handle

```python
@classmethod
def create_handle(cls, file_path: str, mode: str) -> HANDLE
```

Creates and registers a file handle.

<a id="phardwareitk.Extensions.Windows_emu.FileHandleManager.get_file"></a>

#### get\_file

```python
@classmethod
def get_file(cls, handle: HANDLE) -> Optional[IO]
```

Retrieves a file object from a handle.

<a id="phardwareitk.Extensions.Windows_emu.FileHandleManager.close_handle"></a>

#### close\_handle

```python
@classmethod
def close_handle(cls, handle: HANDLE) -> BOOL
```

Closes a handle and removes it from tracking.

<a id="phardwareitk.Extensions.Windows_emu.FILE_TYPE"></a>

## FILE\_TYPE Objects

```python
class FILE_TYPE()
```

File types returned by GetFileType

<a id="phardwareitk.Extensions.Windows_emu.FILE_TYPE.UNKNOWN"></a>

#### UNKNOWN

<a id="phardwareitk.Extensions.Windows_emu.FILE_TYPE.DISK"></a>

#### DISK

<a id="phardwareitk.Extensions.Windows_emu.FILE_TYPE.CHAR"></a>

#### CHAR

<a id="phardwareitk.Extensions.Windows_emu.FILE_TYPE.PIPE"></a>

#### PIPE

<a id="phardwareitk.Extensions.Windows_emu.FILE_INFO"></a>

## FILE\_INFO Objects

```python
class FILE_INFO()
```

Represents file information returned by GetFileInformationByHandle.

<a id="phardwareitk.Extensions.Windows_emu.FILE_INFO.__init__"></a>

#### \_\_init\_\_

```python
def __init__(file_size: DWORD, creation_time: DWORD, last_access_time: DWORD,
             last_write_time: DWORD)
```

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes"></a>

## FileAttributes Objects

```python
class FileAttributes()
```

Represents file attribute flags used in Windows API.

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.READONLY"></a>

#### READONLY

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.HIDDEN"></a>

#### HIDDEN

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.SYSTEM"></a>

#### SYSTEM

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.DIRECTORY"></a>

#### DIRECTORY

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.ARCHIVE"></a>

#### ARCHIVE

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.DEVICE"></a>

#### DEVICE

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.NORMAL"></a>

#### NORMAL

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.TEMPORARY"></a>

#### TEMPORARY

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.SPARSE_FILE"></a>

#### SPARSE\_FILE

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.REPARSE_POINT"></a>

#### REPARSE\_POINT

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.COMPRESSED"></a>

#### COMPRESSED

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.OFFLINE"></a>

#### OFFLINE

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.NOT_CONTENT_INDEXED"></a>

#### NOT\_CONTENT\_INDEXED

<a id="phardwareitk.Extensions.Windows_emu.FileAttributes.ENCRYPTED"></a>

#### ENCRYPTED

<a id="phardwareitk.Extensions.Windows_emu.FileAPI"></a>

## FileAPI Objects

```python
class FileAPI()
```

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.CreateFileW"></a>

#### CreateFileW

```python
@staticmethod
def CreateFileW(lpFileName: LPCWSTR, dwDesiredAccess: Union[FileAccessMode,
                                                            DWORD],
                dwShareMode: DWORD,
                lpSecurityAttributes: LPSECURITY_ATTRIBUTES,
                dwCreationDisposition: DWORD, dwFlagsAndAttributes: DWORD,
                hTemplateFile: HANDLE) -> HANDLE
```

Opens or creates a file, device, pipe, or other system object.

**Arguments**:

- `lpFileName` _LPCWSTR_ - The name of the file or device to be created/opened.
- `dwDesiredAccess` _FileAccessMode | DWORD_ - The requested access (read, write, execute).
- `dwShareMode` _DWORD_ - The sharing mode (e.g., read/write sharing).
- `lpSecurityAttributes` _Optional[LPSECURITY_ATTRIBUTES]_ - Security attributes for the file.
- `dwCreationDisposition` _DWORD_ - Action to take if the file exists or not (CREATE_NEW, OPEN_EXISTING, etc.).
- `dwFlagsAndAttributes` _DWORD_ - File attributes and flags (e.g., FILE_ATTRIBUTE_NORMAL).
- `hTemplateFile` _HANDLE_ - Handle to a template file (if applicable).
  

**Returns**:

- `HANDLE` - A handle to the created or opened file. INVALID_HANDLE_VALUE (-1) on failure.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.CloseHandle"></a>

#### CloseHandle

```python
@staticmethod
def CloseHandle(hObject: HANDLE) -> BOOL
```

Closes a handle.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.ReadFile"></a>

#### ReadFile

```python
@staticmethod
def ReadFile(hFile: HANDLE, lpBuffer: LPVOID, nNumberOfBytesToRead: DWORD,
             lpNumberOfBytesRead: LPDWORD, lpOverlapped: LPOVERLAPPED) -> BOOL
```

Reads data from the specified file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `lpBuffer` _LPVOID_ - Buffer to receive data.
- `nNumberOfBytesToRead` _DWORD_ - Maximum number of bytes to read.
- `lpNumberOfBytesRead` _LPDWORD_ - Pointer to variable that receives the number of bytes read.
- `lpOverlapped` _LPOVERLAPPED_ - Pointer to an OVERLAPPED structure (for async I/O, not implemented).
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.WriteFile"></a>

#### WriteFile

```python
@staticmethod
def WriteFile(hFile: HANDLE, lpBuffer: LPCVOID, nNumberOfBytesToWrite: DWORD,
              lpNumberOfBytesWritten: LPDWORD,
              lpOverlapped: LPOVERLAPPED) -> BOOL
```

Writes data to the specified file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `lpBuffer` _LPCVOID_ - The data to write.
- `nNumberOfBytesToWrite` _DWORD_ - Number of bytes to write.
- `lpNumberOfBytesWritten` _LPDWORD_ - Pointer to variable that receives the number of bytes written.
- `lpOverlapped` _LPOVERLAPPED_ - Pointer to an OVERLAPPED structure (for async I/O, not implemented).
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.SetFilePointer"></a>

#### SetFilePointer

```python
@staticmethod
def SetFilePointer(hFile: HANDLE, lDistanceToMove: LONG,
                   lpDistanceToMoveHigh: PLONG, dwMoveMethod: DWORD) -> DWORD
```

Moves the file pointer of an open file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `lDistanceToMove` _LONG_ - Number of bytes to move.
- `lpDistanceToMoveHigh` _PLONG_ - Pointer to high-order bytes of move distance (not used in this implementation).
- `dwMoveMethod` _DWORD_ - Move method (beginning, current, or end).
  

**Returns**:

- `DWORD` - The new file pointer position, or -1 on failure.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.GetFileSize"></a>

#### GetFileSize

```python
@staticmethod
def GetFileSize(hFile: HANDLE, lpFileSizeHigh: LPDWORD) -> DWORD
```

Retrieves the size of a specified file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file whose size is being queried.
- `lpFileSizeHigh` _LPDWORD_ - Pointer to a variable that receives the high-order DWORD of the file size.
  

**Returns**:

- `DWORD` - The low-order part of the file size. Returns INVALID_FILE_SIZE (-1) on failure.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.FlushFileBuffers"></a>

#### FlushFileBuffers

```python
@staticmethod
def FlushFileBuffers(hFile: HANDLE) -> BOOL
```

Flushes buffers of the specified file, ensuring data is written to disk.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.SetEndOfFile"></a>

#### SetEndOfFile

```python
@staticmethod
def SetEndOfFile(hFile: HANDLE) -> BOOL
```

Truncates or extends a file to the current file pointer position.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.GetFileInformationByHandle"></a>

#### GetFileInformationByHandle

```python
@staticmethod
def GetFileInformationByHandle(hFile: HANDLE) -> Optional[FILE_INFO]
```

Retrieves file metadata.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
  

**Returns**:

- `Optional[FILE_INFO]` - File metadata if successful, otherwise None.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.GetFileType"></a>

#### GetFileType

```python
@staticmethod
def GetFileType(hFile: HANDLE) -> DWORD
```

Retrieves the type of file (disk, char, or pipe).

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
  

**Returns**:

- `DWORD` - File type.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.DuplicateHandle"></a>

#### DuplicateHandle

```python
@staticmethod
def DuplicateHandle(hSourceHandle: HANDLE) -> HANDLE
```

Duplicates an existing handle.

**Arguments**:

- `hSourceHandle` _HANDLE_ - Handle to duplicate.
  

**Returns**:

- `HANDLE` - A new handle if successful, INVALID_HANDLE_VALUE (-1) otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.LockFile"></a>

#### LockFile

```python
@staticmethod
def LockFile(hFile: HANDLE, dwFileOffsetLow: DWORD, dwFileOffsetHigh: DWORD,
             nNumberOfBytesToLock: DWORD) -> BOOL
```

Locks a region of a file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `dwFileOffsetLow` _DWORD_ - Low-order part of the starting byte offset.
- `dwFileOffsetHigh` _DWORD_ - High-order part of the starting byte offset.
- `nNumberOfBytesToLock` _DWORD_ - Number of bytes to lock.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.UnlockFile"></a>

#### UnlockFile

```python
@staticmethod
def UnlockFile(hFile: HANDLE, dwFileOffsetLow: DWORD, dwFileOffsetHigh: DWORD,
               nNumberOfBytesToUnlock: DWORD) -> BOOL
```

Unlocks a previously locked region.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `dwFileOffsetLow` _DWORD_ - Low-order part of the starting byte offset.
- `dwFileOffsetHigh` _DWORD_ - High-order part of the starting byte offset.
- `nNumberOfBytesToUnlock` _DWORD_ - Number of bytes to unlock.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.LockFileEx"></a>

#### LockFileEx

```python
@staticmethod
def LockFileEx(hFile: HANDLE, dwFlags: DWORD, dwReserved: DWORD,
               nNumberOfBytesToLockLow: DWORD, nNumberOfBytesToLockHigh: DWORD,
               lpOverlapped: LPOVERLAPPED) -> BOOL
```

Locks a region of a file with additional options.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `dwFlags` _DWORD_ - Locking flags.
- `dwReserved` _DWORD_ - Reserved, must be zero.
- `nNumberOfBytesToLockLow` _DWORD_ - Low-order part of the lock range.
- `nNumberOfBytesToLockHigh` _DWORD_ - High-order part of the lock range.
- `lpOverlapped` _LPOVERLAPPED_ - Overlapped structure.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.UnlockFileEx"></a>

#### UnlockFileEx

```python
@staticmethod
def UnlockFileEx(hFile: HANDLE, dwReserved: DWORD,
                 nNumberOfBytesToUnlockLow: DWORD,
                 nNumberOfBytesToUnlockHigh: DWORD,
                 lpOverlapped: LPOVERLAPPED) -> BOOL
```

Unlocks a previously locked region (extended).

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `dwReserved` _DWORD_ - Reserved, must be zero.
- `nNumberOfBytesToUnlockLow` _DWORD_ - Low-order part of the unlock range.
- `nNumberOfBytesToUnlockHigh` _DWORD_ - High-order part of the unlock range.
- `lpOverlapped` _LPOVERLAPPED_ - Overlapped structure.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.DeleteFileW"></a>

#### DeleteFileW

```python
@staticmethod
def DeleteFileW(lpFileName: LPCWSTR) -> BOOL
```

Deletes a File.

**Arguments**:

- `lpFileName` _LPCWSTR_ - The name of the file to be deleted.
  

**Returns**:

- `BOOL` - True if successfull, else False

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.GetFileAttributesW"></a>

#### GetFileAttributesW

```python
@staticmethod
def GetFileAttributesW(lpFileName: LPCWSTR) -> DWORD
```

Gets the file Attributes

**Arguments**:

- `lpFileName` _LPCWSTR_ - The name of the file or directory.
  

**Returns**:

- `DWORD` - If the function succeeds, the return value contains the attributes of the specified file or directory, If the function fails, the return value is **INVALID_FILE_ATTRIBUTES**.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.SetFileAttributesW"></a>

#### SetFileAttributesW

```python
@staticmethod
def SetFileAttributesW(lpFileName: LPCWSTR, dwFileAttributes: DWORD) -> BOOL
```

Sets attributes for the specified file.

**Arguments**:

- `lpFileName` _LPCWSTR_ - The name of the file.
- `dwFileAttributes` _DWORD_ - The new file attributes to be set.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.GetFileTime"></a>

#### GetFileTime

```python
@staticmethod
def GetFileTime(hFile: HANDLE, lpCreationTime: LPDWORD,
                lpLastAccessTime: LPDWORD, lpLastWriteTime: LPDWORD) -> BOOL
```

Retrieves the creation, last access, and last write times of a file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `lpCreationTime` _LPDWORD_ - Pointer to store creation time.
- `lpLastAccessTime` _LPDWORD_ - Pointer to store last access time.
- `lpLastWriteTime` _LPDWORD_ - Pointer to store last write time.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

<a id="phardwareitk.Extensions.Windows_emu.FileAPI.SetFileTime"></a>

#### SetFileTime

```python
@staticmethod
def SetFileTime(hFile: HANDLE, lpCreationTime: LPDWORD,
                lpLastAccessTime: LPDWORD, lpLastWriteTime: LPDWORD) -> BOOL
```

Sets the creation, last access, and last write times of a file.

**Arguments**:

- `hFile` _HANDLE_ - Handle to the file.
- `lpCreationTime` _LPDWORD_ - Pointer to new creation time.
- `lpLastAccessTime` _LPDWORD_ - Pointer to new last access time.
- `lpLastWriteTime` _LPDWORD_ - Pointer to new last write time.
  

**Returns**:

- `BOOL` - True if successful, False otherwise.

