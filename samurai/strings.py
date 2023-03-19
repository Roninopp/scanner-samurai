scan_request_string = """
$SCAN
Cymatic Scan request!
**CASE ID**: `{}`
**Inspector:** {} 
**User scanned:** [{}](tg://openmessage?user_id={})
**Reason:** {}
**Proof:** `{}`
**Bancode:** {}
"""

forced_scan_string = """
$FORCED
**CASE ID**: `{}`
**Enforcer:** {}
**Target:** [{}](tg://openmessage?user_id={})
**Reason:** `{}`
**Proof:** {}
**Bancode:** `{}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`
Not a target for enforcement action. 
The trigger of Dominator will be locked.
"""

scan_approved_string = """
#LethalEliminator
**Target User:** [{}](tg://openmessage?user_id={})
**Crime Coefficient:** `Over 300`
**Reason:** `{}`
**Enforcer:** `{}`
"""