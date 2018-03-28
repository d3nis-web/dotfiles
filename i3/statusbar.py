from i3pystatus import Status
status = Status()

status.register("clock",
    format="%a %-d %b %X",)

status.register("load")

status.register("temp",
    format="{temp:.0f}°C",)

status.register("disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

status.register("pulseaudio",
    format="♪{volume}",)

status.run()
