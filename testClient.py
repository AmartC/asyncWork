import dbus
import dbus.service
import dbus.mainloop.glib

class TestDBus (object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        self.dbus_object = self.bus.get_object("org.test.dbus", "/org/test/dbus")
        self.the_interface = dbus.Interface(self.dbus_object, "org.test.dbus")

    def output(self):
        print(self.the_interface.hello())
if __name__ == "__main__":
    try:
        dbus_proxy = TestDBus()
        dbus_proxy.output()
    except dbus.DBusException as e:
        print(e)
