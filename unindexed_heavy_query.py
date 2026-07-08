# ========================================================================
# 🚨 CRITICAL DB TRAP: UNINDEXED FULL TABLE SCAN (DO NOT USE)
# Engineered by: OmniOrigin Group of Businesses
# Description: Simulated resource-heavy relational query execution.
# ========================================================================
import time

def execute_unindexed_lookup(user_id, category_id):
    """
    Simulates a database engine forced to perform a Full Table Scan 
    because no appropriate covering index exists for the filtering criteria.
    """
    print(f"[*] Executing: SELECT * FROM user_posts WHERE user_id = {user_id} AND category_id = {category_id};")
    
    # ❌ CRITICAL TRAP: Millions of rows scanned sequentially without an index
    print("[!] Warning: No matching index found. Initializing sequential disk scan...")
    time.sleep(2.4)  # Simulating heavy I/O overhead and CPU spikes
    
    print("[+] Query completed. Result set returned.")
    return {"rows_scanned": 1500000, "execution_time_ms": 2400, "status": "SUCCESS"}
