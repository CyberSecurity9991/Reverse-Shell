# Lab Setup Guide

## Requirements

- VirtualBox or VMware Workstation Player
- Kali Linux VM (attacker)
- Windows or Linux VM (target)
- Host-Only network adapter on both VMs

## Network Configuration

1. Set both VMs to **Host-Only** adapter.
2. Assign static IPs:
   - Kali: `192.168.56.101`
   - Target: `192.168.56.102`
3. Verify connectivity:
   ```bash
   ping 192.168.56.102   # From Kali
   ping 192.168.56.101   # From Target