#!/usr/bin/env python3
"""
⚠️ DELIBERATELY INSECURE — FOR DEMONSTRATION ONLY
This file triggers all 9 engines. Do not use in production.
"""

import os
import subprocess
import hashlib
import sqlite3
import pickle
import yaml
import tempfile
import xml.etree.ElementTree as ET
from flask import Flask, request, render_template_string
import requests

# ============================================================
# 1. HARDCODED SECRETS (Gitleaks + TruffleHog)
# ============================================================

# These will trigger Gitleaks immediately
AWS_ACCESS_KEY = "AKIA1234567890ABCDEF"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuv"
STRIPE_SECRET = "sk_live_1234567890abcdefghijklmnop"
DATABASE_PASSWORD = "admin123"
OPENAI_API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyz"

# ============================================================
# 2. COMMAND INJECTION (Bandit — subprocess with shell=True)
# ============================================================

def run_user_command(user_input):
    """This will trigger Bandit B602: subprocess_popen_with_shell_equals_true"""
    subprocess.call(f"ping -c 1 {user_input}", shell=True)
    subprocess.Popen(user_input, shell=True)
    os.system(f"echo {user_input}")

# ============================================================
# 3. SQL INJECTION (Bandit + Semgrep)
# ============================================================

def get_user(username):
    """This will trigger Bandit B608: hardcoded_sql_expressions"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Direct string formatting in SQL — classic injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def insert_user(name, email):
    """Another SQL injection vector"""
    conn = sqlite3.connect("users.db")
    query = "INSERT INTO users (name, email) VALUES ('%s', '%s')" % (name, email)
    conn.execute(query)
    conn.commit()

# ============================================================
# 4. INSECURE DESERIALIZATION (Bandit B301: pickle)
# ============================================================

def load_user_data(data):
    """This will trigger Bandit B301: pickle"""
    return pickle.loads(data)

# ============================================================
# 5. UNSAFE YAML LOADING (Bandit B506: yaml_load)
# ============================================================

def parse_config(config_file):
    """This will trigger Bandit B506: yaml_load"""
    with open(config_file, 'r') as f:
        return yaml.load(f)  # Should be yaml.safe_load()

# ============================================================
# 6. WEAK CRYPTOGRAPHY (Semgrep — MD5, SHA1)
# ============================================================

def hash_password(password):
    """This will trigger Semgrep: insecure hashing"""
    return hashlib.md5(password.encode()).hexdigest()

def generate_token(data):
    """Another weak hash"""
    return hashlib.sha1(data.encode()).hexdigest()

# ============================================================
# 7. XML PARSING VULNERABILITIES (Bandit B314, B409, B410)
# ============================================================

def parse_xml(xml_string):
    """This will trigger Bandit: xml.etree vulnerabilities"""
    root = ET.fromstring(xml_string)  # Vulnerable to XXE
    return root

# ============================================================
# 8. INSECURE TEMP FILES (Bandit B108)
# ============================================================

def create_temp_config():
    """This will trigger Bandit B108: hardcoded_tmp_directory"""
    path = "/tmp/config.ini"
    with open(path, 'w') as f:
        f.write("debug=true")
    return path

# ============================================================
# 9. OPEN REDIRECT (Semgrep)
# ============================================================

app = Flask(__name__)

@app.route('/redirect')
def unsafe_redirect():
    """This will trigger Semgrep: open redirect"""
    target = request.args.get('url')
    return f'<meta http-equiv="refresh" content="0;url={target}">'

# ============================================================
# 10. XSS VULNERABILITY (Semgrep — ESAPI checks)
# ============================================================

@app.route('/greet')
def xss_vulnerable():
    """This will trigger Semgrep: reflected XSS"""
    name = request.args.get('name', 'Guest')
    return render_template_string(f"<h1>Hello {name}!</h1>")

# ============================================================
# 11. HARDCODED SECRET IN ENV (Gitleaks)
# ============================================================

os.environ["DATABASE_URL"] = "postgresql://admin:SuperSecret123@localhost:5432/mydb"

# ============================================================
# 12. UNSAFE REQUESTS WITHOUT TIMEOUT (Bandit B113)
# ============================================================

def fetch_data(url):
    """This will trigger Bandit B113: request_without_timeout"""
    return requests.get(url)  # No timeout parameter

# ============================================================
# 13. BINDING TO ALL INTERFACES (Bandit B104)
# ============================================================

def start_server():
    """This will trigger Bandit B104: hardcoded_bind_all_interfaces"""
    app.run(host='0.0.0.0', port=5000)

# ============================================================
# 14. ASSERT USED FOR VALIDATION (Bandit B101)
# ============================================================

def validate_admin(user):
    """This will trigger Bandit B101: assert_used"""
    assert user.is_admin, "User is not admin"
    return True

# ============================================================
# 15. DEBUG FLAG ENABLED (Semgrep)
# ============================================================

DEBUG = True  # Flask debug mode in production

# ============================================================
# 16. UNSAFE PERMISSIONS (Bandit B103)
# ============================================================

def set_permissions():
    """This will trigger Bandit B103: set_bad_file_permissions"""
    os.chmod("/etc/shadow", 0o777)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("⚠️  This script is deliberately insecure for demo purposes")
    print("   It will trigger: Gitleaks, TruffleHog, Bandit, Semgrep, ESLint")
    print("   Do NOT deploy this anywhere real.")
    start_server()
