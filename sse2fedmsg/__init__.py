# -*- coding: utf-8 -*-
# Copyright (C) 2017 Jeremy Cline
#
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
"""
sse2fedmsg is a simple wrapper around `sseclient`_ that publishes messages to a
ZeroMQ messaging infrastructure via `fedmsg`_.

.. _fedmsg: http://www.fedmsg.com
.. _sseclient: https://pypi.python.org/pypi/sseclient/
"""
from __future__ import absolute_import, unicode_literals, print_function

import argparse
import logging
import json

from sseclient import SSEClient
import fedmsg


_log = logging.getLogger(__name__)


__version__ = '0.1.0'
__author__ = 'The Fedora Infrastructure Team'


class Sse2Fedmsg(object):
    """
    This class connects to the Server-Sent Events feed provided and publishes
    fedmsgs to the given topic.

    Attributes:
        feed (str): The Server-Sent events feed URL.
        topic (str): The topic suffix fedmsg should append to published messages.
    """

    def __init__(self, topic, feed):
        self.feed = feed
        self.topic = topic

    def run(self):
        """
        Start the SSE client.

        This call is blocking and will continue until the underlying TCP
        connection is closed.
        """
        _log.info('Starting Server-Sent Events client for ', self.feed)
        sse_stream = SSEClient(self.feed)
        for sse_message in sse_stream:
            # If the server sends too many newlines the client can generate
            # messages that are completely empty, so we filter those here.
            if sse_message.data:
                msg = self.process_message(sse_message)
                _log.debug('Received message from SSE: %s', msg)
                try:
                    fedmsg.publish(self.topic, msg)
                except Exception as err:
                    _log.exception('Fatal error publishing %s to %s: %s', msg,
                                   self.topic, err)

    @staticmethod
    def process_message(sse_message):
        """
        This provides an opportunity to manipulate the incoming SSE message.

        Args:
            sse_message(sseclient.Event): an object representing a message. An SSE
            message has four object attributes of interest: `data`, `event`,
            `id`, and `retry`. Some or all may be `None`.

        Returns:
            A message that is handed directly to the ``fedmsg.publish`` function.
        """
        # The SSE spec requires all data to be UTF-8 encoded
        msg = {
            'data': json.loads(sse_message.data, encoding='utf-8'),
            'event': sse_message.event,
            'id': sse_message.id,
            'retry': sse_message.retry,
        }
        return msg


def main():
    """
    CLI entry point for sse2fedmsg.
    """
    desc = ('sse2fedmsg translates a Server-Sent Event feed into ZeroMQ messages using fedmsg.')
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('topic', help='The ØMQ topic suffix to use')
    parser.add_argument('feed', help='The SSE feed URL (e.g. http://firehose.libraries.io/events)')

    args = parser.parse_args()
    client = Sse2Fedmsg(args.topic, args.feed)
    client.run()
