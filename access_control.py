from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# Whitelist: Allowed communication pairs
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

    # ✅ ALLOW TRAFFIC
    if (src, dst) in whitelist:
        log.info(f"✅ ALLOWED: {src} -> {dst}")

        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

    # ❌ BLOCK TRAFFIC (install drop rule)
    else:
        log.info(f"❌ BLOCKED: {src} -> {dst}")

        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match(
            dl_type=0x800,     # IPv4
            nw_src=src,
            nw_dst=dst
        )
        msg.actions = []  # No action = DROP
        event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    
