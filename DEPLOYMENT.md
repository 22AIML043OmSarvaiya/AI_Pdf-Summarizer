# 🚀 PDF Summarizer - Deployment Guide

This guide will help you deploy the PDF Summarizer application in production environments.

## 📋 Prerequisites

### System Requirements
- **OS**: Windows 10/11, Linux (Ubuntu 18.04+), macOS 10.15+
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: 5GB free space for models and dependencies
- **GPU**: Optional but recommended for faster processing

### Software Requirements
- Python 3.8+
- pip (Python package manager)
- Git (for version control)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd PdF_Summarizer
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Windows
set ENCRYPTION_KEY=your-32-byte-encryption-key
set SECRET_KEY=your-secret-key

# Linux/macOS
export ENCRYPTION_KEY=your-32-byte-encryption-key
export SECRET_KEY=your-secret-key
```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
python run.py
```

### Production Mode
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 🌐 Web Server Deployment

### Using Nginx (Recommended)

1. **Install Nginx**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install nginx
```

2. **Configure Nginx**
```bash
sudo nano /etc/nginx/sites-available/pdf-summarizer
```

Add this configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

3. **Enable the Site**
```bash
sudo ln -s /etc/nginx/sites-available/pdf-summarizer /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Using Apache

1. **Install Apache**
```bash
sudo apt install apache2
```

2. **Configure Proxy**
```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_wstunnel
```

3. **Create Virtual Host**
```apache
<VirtualHost *:80>
    ServerName your-domain.com
    
    ProxyPreserveHost On
    ProxyPass / http://localhost:8501/
    ProxyPassReverse / http://localhost:8501/
    
    ErrorLog ${APACHE_LOG_DIR}/pdf-summarizer_error.log
    CustomLog ${APACHE_LOG_DIR}/pdf-summarizer_access.log combined
</VirtualHost>
```

## 🔧 Systemd Service (Linux)

### Create Service File
```bash
sudo nano /etc/systemd/system/pdf-summarizer.service
```

Add this content:
```ini
[Unit]
Description=PDF Summarizer Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/your/PdF_Summarizer
Environment=PATH=/path/to/your/venv/bin
ExecStart=/path/to/your/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Enable and Start Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable pdf-summarizer
sudo systemctl start pdf-summarizer
sudo systemctl status pdf-summarizer
```

## 🔒 Security Configuration

### SSL/HTTPS Setup

1. **Install Certbot**
```bash
sudo apt install certbot python3-certbot-nginx
```

2. **Obtain SSL Certificate**
```bash
sudo certbot --nginx -d your-domain.com
```

3. **Auto-renewal**
```bash
sudo crontab -e
# Add this line:
0 12 * * * /usr/bin/certbot renew --quiet
```

### Firewall Configuration
```bash
# Ubuntu/Debian
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 22
sudo ufw enable

# CentOS/RHEL
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

## 📊 Monitoring and Logging

### Application Logs
```bash
# View application logs
sudo journalctl -u pdf-summarizer -f

# View nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Performance Monitoring
```bash
# Monitor system resources
htop
iotop
nethogs
```

## 🔄 Backup and Maintenance

### Backup Strategy
```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/pdf-summarizer"
APP_DIR="/path/to/your/PdF_Summarizer"

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/pdf-summarizer_$DATE.tar.gz $APP_DIR
```

### Automated Maintenance
```bash
# Add to crontab
0 2 * * 0 /path/to/backup.sh
0 3 * * 0 systemctl restart pdf-summarizer
```

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
```bash
sudo netstat -tulpn | grep :8501
sudo kill -9 <PID>
```

2. **Permission Issues**
```bash
sudo chown -R www-data:www-data /path/to/your/PdF_Summarizer
sudo chmod -R 755 /path/to/your/PdF_Summarizer
```

3. **Model Loading Issues**
```bash
# Clear model cache
rm -rf ~/.cache/huggingface/
```

4. **Memory Issues**
```bash
# Monitor memory usage
free -h
# Increase swap if needed
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## 📈 Performance Optimization

### GPU Acceleration
```bash
# Install CUDA drivers
sudo apt install nvidia-driver-470

# Install PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Memory Optimization
```bash
# Add to /etc/sysctl.conf
vm.swappiness=10
vm.vfs_cache_pressure=50
```

## 🔄 Updates and Maintenance

### Application Updates
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart service
sudo systemctl restart pdf-summarizer
```

### System Updates
```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade

# CentOS/RHEL
sudo yum update
```

## 📞 Support

For deployment issues:
1. Check the logs: `sudo journalctl -u pdf-summarizer -f`
2. Verify configuration: `nginx -t`
3. Test connectivity: `curl http://localhost:8501`
4. Check system resources: `htop`

---

**Happy Deploying! 🚀** 