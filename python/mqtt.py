#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import pmt
import paho.mqtt.client as pmqtt

class mqtt(gr.sync_block):
    """
    docstring for block manchester_pdu_decoder
    """
    def __init__(self, hostname = "127.0.0.1", port = 1883, channel = "/gnuradio"):
        gr.sync_block.__init__(self,
            name="mqtt",
            in_sig=None,
            out_sig=None)
        self.channel = channel
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.client = pmqtt.Client()
        print("Connecting to hostname: " + hostname)
        self.client.connect(hostname, port, 60)
        self.client.loop_start()


    def handle_msg(self, msg):
        msg = pmt.to_python(msg)[1]
        msg_str = ''.join(chr(c) for c in msg)
        self.client.publish(self.channel, msg_str)
