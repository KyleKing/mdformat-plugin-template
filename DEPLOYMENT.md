# Hetzner Deployment Guide

Automated deployment setup for mdformat-plugin-template using Hetzner Cloud and cloud-init.

## Prerequisites

- Hetzner Cloud account
- SSH key pair
- GitHub repository access

## Quick Start

### 1. Prepare Cloud-Config

Edit `cloud-config.yaml` and replace:

- `YOUR_USERNAME` - Your preferred username (e.g., `deploy`)
- `YOUR_SSH_PUBLIC_KEY_HERE` - Your SSH public key (`~/.ssh/id_rsa.pub`)
- `YOUR_GITHUB_USERNAME` - Your GitHub username

### 2. Create Hetzner Server

**Via Hetzner Cloud Console:**

1. Create new server
2. Choose Ubuntu 22.04 LTS
3. Select server size (CX11 minimum)
4. Under "Cloud config", paste contents of `cloud-config.yaml`
5. Add SSH key
6. Create server

**Via CLI (`hcloud`):**

```bash
# Install hcloud CLI
brew install hcloud  # macOS
# or: apt install hcloud  # Linux

# Authenticate
hcloud context create mdformat-project

# Create server with cloud-config
hcloud server create \
  --name mdformat-server \
  --type cx11 \
  --image ubuntu-22.04 \
  --ssh-key YOUR_KEY_NAME \
  --user-data-from-file cloud-config.yaml
```

### 3. Verify Deployment

Wait 2-3 minutes for cloud-init to complete, then SSH:

```bash
ssh YOUR_USERNAME@SERVER_IP

# Check auto-deploy status
systemctl status auto-deploy.timer
journalctl -u auto-deploy.service -f

# Check Syncthing
systemctl status syncthing@YOUR_USERNAME
curl http://localhost:8384  # Web UI

# Verify mise installation
mise --version
mise list
```

## What Gets Configured

### Automatic Setup

- **SSH**: Password auth disabled, pubkey auth enabled
- **mise**: Installed for Python version management
- **Git repository**: Cloned to `/opt/mdformat-plugin-template`
- **Auto-deploy**: Pulls from `main` every 5 minutes via systemd timer
- **Syncthing**: File sync service running on port 8384
- **Security**: Firewall rules, automatic security updates

### Services

All services auto-start on reboot:

- `auto-deploy.timer` - Auto-deploy from GitHub
- `syncthing@YOUR_USERNAME` - File synchronization

## Manual Operations

### Trigger Deployment

```bash
sudo systemctl start auto-deploy.service
journalctl -u auto-deploy.service -n 50
```

### Check Logs

```bash
# Auto-deploy logs
tail -f /var/log/auto-deploy.log

# Service logs
journalctl -u auto-deploy.service -f
journalctl -u syncthing@YOUR_USERNAME -f
```

### Update Dependencies

```bash
cd /opt/mdformat-plugin-template
mise install
mise prune  # Remove unused versions
```

### Syncthing Configuration

Access Syncthing UI to configure folders:

```bash
# Create SSH tunnel
ssh -L 8384:localhost:8384 YOUR_USERNAME@SERVER_IP

# Visit http://localhost:8384 in browser
```

Configure folders and devices in the web UI.

## Troubleshooting

### Cloud-init Status

```bash
# Check cloud-init completion
cloud-init status

# View cloud-init logs
tail -f /var/log/cloud-init-output.log
```

### Auto-deploy Not Running

```bash
# Check timer
systemctl status auto-deploy.timer
systemctl list-timers

# Restart timer
sudo systemctl restart auto-deploy.timer
```

### mise Issues

```bash
# Ensure mise is in PATH
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
source ~/.bashrc

# Reinstall mise
curl https://mise.run | sh
```

## Customization

### Change Update Interval

Edit `/etc/systemd/system/auto-deploy.timer`:

```ini
[Timer]
OnUnitActiveSec=15min  # Change from 5min
```

Then reload:

```bash
sudo systemctl daemon-reload
sudo systemctl restart auto-deploy.timer
```

### Add Environment Variables

Edit `/etc/systemd/system/auto-deploy.service`:

```ini
[Service]
Environment="KEY=value"
```

### Modify Deploy Script

Edit `/usr/local/bin/auto-deploy.sh` to add custom commands after git pull.

## Security Hardening

Additional recommended steps:

```bash
# Enable UFW firewall
sudo ufw allow OpenSSH
sudo ufw allow 22000/tcp  # Syncthing transfer
sudo ufw allow 21027/udp  # Syncthing discovery
sudo ufw enable

# Enable automatic security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

## Backup Strategy

Syncthing provides real-time sync. For additional backups:

```bash
# Snapshot via Hetzner (use hcloud or web UI)
hcloud server create-image --description "Backup-$(date +%Y%m%d)" SERVER_NAME

# Manual backup
tar -czf backup-$(date +%Y%m%d).tar.gz /opt/mdformat-plugin-template
```
