#!/usr/bin/env python3

import sys
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from subprocess import getstatusoutput

"""
method QDBusRawType::a{s(bgav)} org.gtk.Actions.DescribeAll()
method QDBusRawType::a(uuaa{sv}) org.gtk.Menus.Start(QDBusRawType::au groups)
method QDBusRawType::(bgav) org.gtk.Actions.Describe(QString action_name)
method QDBusVariant org.freedesktop.DBus.Properties.Get(QString interface_name, QString property_name)
method QStringList org.gtk.Actions.List()
method QString org.freedesktop.DBus.Introspectable.Introspect()
method QString org.freedesktop.DBus.Peer.GetMachineId()
method QVariantMap org.freedesktop.DBus.Properties.GetAll(QString interface_name)
method void org.freedesktop.DBus.Peer.Ping()
method void org.freedesktop.DBus.Properties.Set(QString interface_name, QString property_name, QDBusVariant value)
method void org.gtk.Actions.Activate(QString action_name, QVariantList parameter, QVariantMap platform_data)
method void org.gtk.Actions.SetState(QString action_name, QDBusVariant value, QVariantMap platform_data)
method void org.gtk.Menus.End(QDBusRawType::au groups)
signal void org.freedesktop.DBus.Properties.PropertiesChanged(QString interface_name, QVariantMap changed_properties, QStringList invalidated_properties)
signal void org.gtk.Actions.Changed(QStringList removals, QDBusRawType::a{sb} enable_changes, QVariantMap state_changes, QDBusRawType::a{s(bgav additions)
signal void org.gtk.Menus.Changed()
"""

DBusGMainLoop(set_as_default=True)

try:
    profile = int(sys.argv[1])
except Exception:
    profile = 0

num_tab_counts_to_change = 10
action_change_profile = "TerminalSetProfile%s" % profile
action_change_next_tab = "TabsNext"
action_change_prev_tab = "TabsPrevious"
try:
    window = int(sys.argv[2])
except Exception:
    window = 0

service_name = 'org.gnome.Terminal'
path_prefix = '/com/canonical/unity/gtk/window/'

bus = dbus.SessionBus()
retcode, output = getstatusoutput('qdbus org.gnome.Terminal')
prefix_lenth = len(path_prefix)
for path in output.splitlines():
    if not (path.startswith(path_prefix) and len(path) > prefix_lenth):
        continue
    obj = bus.get_object(service_name, path)
    actions = dbus.Interface(obj, "org.gtk.Actions")
    for c in range(num_tab_counts_to_change):
        actions.Activate(dbus.String(action_change_profile), dbus.Array([dbus.String(action_change_profile, variant_level=1)]), dbus.Array([]))
        actions.Activate(dbus.String(action_change_next_tab), dbus.Array([]), dbus.Array([]))

    for c in range(num_tab_counts_to_change):
        actions.Activate(dbus.String(action_change_prev_tab), dbus.Array([]), dbus.Array([]))
