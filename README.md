# sse2fedmsg

sse2fedmsg translates [Server-Sent Events](https://www.w3.org/TR/eventsource/)
to [fedmsgs](http://fedmsg.com/).

## Usage

First, install the Python package:
```
$ pip install sse2fedmsg
```

Next, run the following:
```
$ sse2fedmsg <topic> <feed>
```

For example:
```
$ sse2fedmsg librariesio http://firehose.libraries.io/events
```

## Development

To observe the messages being published, start a fedmsg-relay and optionally
run it in the background:
```
$ fedmsg-relay --config-filename fedmsg.d/fedmsg-config.py &
```

Messages are published by the relay using TCP on port 9940 via all interfaces.

Next, tail fedmsg:
```
$ fedmsg-tail --config fedmsg.d/fedmsg-config.py --no-validate --really-pretty
```
