#!/usr/bin/python -Es

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib # pylint: disable=no-name-in-module
import slip.dbus.service
from slip.dbus import polkit
import testHello

class testDBus(slip.dbus.service.Object):
    default_polkit_auth_required = "org.test.readwrite"

    """
    The storage_import method imports all containers and their associated contents from a filesystem directory.
    """
    @slip.dbus.polkit.require_auth("org.test.read")
    @dbus.service.method("org.test", in_signature='', out_signature='s')
    def getMessage(self):
        return testHello.hello_world()

if __name__ == "__main__":
        mainloop = GLib.MainLoop()
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        system_bus = dbus.SystemBus()
        name = dbus.service.BusName("org.test", system_bus)
        object = testDBus(system_bus, "/org/test/object")
        slip.dbus.service.set_mainloop(mainloop)
        mainloop.run()
