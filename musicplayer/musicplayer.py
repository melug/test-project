# coding: utf-8
import pygst
pygst.require("0.10")
import gst

def on_tag(bus, msg):
    taglist = msg.parse_tag()
    print 'on_tag:'
    for key in taglist.keys():
        print '\t%s = %s' % (key, taglist[key])

#тоглуулах гэж байгаа стриим
music_stream_uri = 'http://mp3channels.webradio.antenne.de/alternative'

player = gst.element_factory_make("playbin", "player")

#uri-г тохируулах
player.set_property('uri', music_stream_uri)

#тоглуулж эхлэх
player.set_state(gst.STATE_PLAYING)

bus = player.get_bus()
bus.enable_sync_message_emission()
bus.add_signal_watch()
bus.connect('message::tag', on_tag)

raw_input('enter дарж тоглуулагчаас гарна уу')