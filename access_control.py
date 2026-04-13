from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

whitelist = [
    ("10.0.0.1", "10.0.0.2"),
    ("10.0.0.2", "10.0.0.1")
]

def _handle_PacketIn(event):
    packet = event.parsed

    ip = packet.find('ipv4')
    if not ip:
        return

    src = str(ip.srcip)
    dst = str(ip.dstip)

    if (src, dst) in whitelist:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        log.info(f"ALLOWED: {src} -> {dst}")
    else:
        log.info(f"BLOCKED: {src} -> {dst}")

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)