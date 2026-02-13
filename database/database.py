# database/database.py - Modified to work WITHOUT MongoDB

import os

# Dummy database functions that do nothing
# This allows the bot to run without MongoDB

def present_user(user_id: int):
    """Check if user exists - always return False (no database)"""
    return False

async def add_user(user_id: int):
    """Add user to database - do nothing (no database)"""
    return True

async def full_userbase():
    """Get all users - return empty list (no database)"""
    return []

async def del_user(user_id: int):
    """Delete user - do nothing (no database)"""
    return True

# Database is disabled - all functions return dummy values
print("INFO: Running in NO-DATABASE mode")
