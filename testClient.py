import sys
import json
import dbus
import dbus.service
import dbus.mainloop.glib
from Atomic import util
from slip.dbus import polkit

class TestDBus (object):
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.dbus_object = self.bus.get_object("org.test", "/org/test/object")

    @polkit.enable_proxy
    def output(self):
        ret = self.dbus_object.getMessage(dbus_interface="org.test")
        return ret

if __name__ == "__main__":
    try:
        dbus_proxy = TestDBus()
        dbus_proxy.output()
    except dbus.DBusException as e:
        print e
