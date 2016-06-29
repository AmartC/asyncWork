#!/usr/bin/python -Es

import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import dbus.mainloop.glib

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class testDBus(dbus.service.Object):
    #default_polkit_auth_required = "org.test.readwrite"
    def __init__(self):
        bus_name = dbus.service.BusName('org.test.dbus', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/test/dbus')
    """
    The storage_import method imports all containers and their associated contents from a filesystem directory.
    """

    @dbus.service.method("org.test.dbus", in_signature='', out_signature='s')
    def hello(self):
        return "Hello"

DBusGMainLoop(set_as_default=True)
myservice = testDBus()
Gtk.main()