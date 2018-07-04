import xbmcaddon
import oeWindows

__scriptid__ = 'virtual.test'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
__cwd__ = __addon__.getAddonInfo('path')

winOeMain = oeWindows.mainWindow('mainWindow.xml', __cwd__, 'Default')
winOeMain.doModal()
