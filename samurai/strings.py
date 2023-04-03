scan_request_string = """
$SCAN
Cymatic Scan request!
**CASE ID**: {}
**User scanned:** [{}](tg://openmessage?user_id={})
**Reason:** `{}`
**Proof:** `{}`
**Bancode:** {}
**Inspector:** `{}`
"""

scan_string = """
$SCAN
Cymatic Scan!
**CASE ID**: {}
**User scanned:** [{}](tg://openmessage?user_id={})
**Reason:** `{}`
**Proof:** `{}`
**Bancode:** {}
**Enforcer:** `{}`
"""

forced_scan_string = """
$FORCED
**CASE ID**: {}
**Target:** [{}](tg://openmessage?user_id={})
**Reason:** `{}`
**Proof:** `{}`
**Bancode:** {}
**Enforcer:** `{}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`
Not a target for enforcement action. 
The trigger of Dominator will be locked.
"""

scan_approved_string = """
{}
**Target User:** [{}](tg://openmessage?user_id={})
**Crime Coefficient:** `Over 300`
**Reason:** `{}`
**Enforcer:** `{}`
"""