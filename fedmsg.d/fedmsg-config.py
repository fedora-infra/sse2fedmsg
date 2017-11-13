# -*- coding: utf-8 -*-
# Copyright (C) 2017 Red Hat, Inc.
# This file is part of sse2fedmsg.

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.

config = dict(
    zmq_enabled=True,
    active=True,
    environment="dev",
    high_water_mark=0,
    io_threads=1,
    post_init_sleep=0.5,
    zmq_linger=1000,
    zmq_tcp_keepalive=1,
    zmq_tcp_keepalive_cnt=3,
    zmq_tcp_keepalive_idle=60,
    zmq_tcp_keepalive_intvl=5,
    zmq_reconnect_ivl=100,
    zmq_reconnect_ivl_max=1000,
    endpoints={
        "relay_outbound": [
            "tcp://*:9940",
        ],
    },
    relay_inbound=[
        "tcp://127.0.0.1:4001",
    ],
    sign_messages=False,
    validate_signatures=False,
)
