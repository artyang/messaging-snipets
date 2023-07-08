#!/bin/bash

# Update package repositories
sudo apt update

# Install Sendmail and related utilities
sudo apt install sendmail mailutils

# Backup original Sendmail configuration file
sudo cp /etc/mail/sendmail.cf /etc/mail/sendmail.cf.bak

# Generate a new Sendmail configuration file
sudo sendmailconfig

# Prompt for the hostname
read -p "Enter the fully qualified domain name (FQDN) of your mail server: " hostname

# Update the Sendmail configuration file with the provided hostname
sudo sed -i "s/Dj.*/Dj${hostname}/" /etc/mail/sendmail.cf

# Restart Sendmail service
sudo systemctl restart sendmail

echo "Sendmail setup complete!"
