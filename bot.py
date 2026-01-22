import base64
import os
import sys

# --- RANKIFY NEURAL GATEWAY LOADER ---
# Encapsulated Core v2.1
# Pulls credentials from os.environ: TELEGRAM_TOKEN, FIREBASE_JSON

_NEURAL_STREAM = (
    "aW1wb3J0IG9zLCBqc29uLCByYW5kb20sIHRlbGVib3QsIGZpcmViYXNlX2FkbWluCmZyb20gZmly"
    "ZWJhc2VfYWRtaW4gaW1wb3J0IGNyZWRlbnRpYWxzLCBmaXJlc3RvcmUKCiMgRmlyZWJhc2UgU2V0"
    "dXAKZmlyZWJhc2VfaW5mbyA9IGpzb24ubG9hZHMob3MuZW52aXJvblsnRklSRUJBU0VfSlNPTidd"
    "KQpjcmVkID0gY3JlZGVudGlhbHMuQ2VydGlmaWNhdGUoZmlyZWJhc2VfaW5mbykKZmlyZWJhc2Vf"
    "YWRtaW4uaW5pdGlhbGl6ZV9hcHAoY3JlZCkKZGIgPSBmaXJlc3RvcmUuY2xpZW50KCkKCiMgQm90"
    "IFNldHVwCmJvdCA9IHRlbGVib3QuVGVsZUJvdChvcy5lbnZpcm9uWydURUxFR1JBTV9UT0tFTidd"
    "CgpAYm90Lm1lc3NhZ2VfaGFuZGxlcihjb21tYW5kcz1bJ3N0YXJ0J10pCmRlZiB3ZWxjb21lKG1l"
    "c3NhZ2UpOgogICAgbWFya3VwID0gdGVsZWJvdC50eXBlcy5SZXBseUtleWJvYXJkTWFya3VwKG9u"
    "ZV90aW1lX2tleWJvYXJkPVRydWUsIHJlc2l6ZV9rZXlib2FyZD1UcnVlKQogICAgaXRlbSA9IHRl"
    "bGVib3QudHlwZXMuS2V5Ym9hcmRCdXR0b24oIvCfk7YgU2hhcmUgTnVtYmVyICYgR2V0IFBJTiIs"
    "IHJlcXVlc3RfY29udGFjdD1UcnVlKQogICAgbWFya3VwLmFkZChpdGVtKQogICAgYm90LnNlbmRf"
    "bWVzc2FnZShtZXNzYWdlLmNoYXQuaWQsICJ3ZWxjb21lIGFzcGlyYW50ICEgUmFua2lmeSBDb250"
    "cm9sIFJvb20gbWVpbiBBcGthIHN3YWdhdCBoYWkuXG5cbk5pY2hlIGJ1dHRvbiBkYWJha2FyIG51"
    "bWJlciBzaGFyZWluIGthcmVpbiwgUElOIHR1cmFudCBtaWwgamF5ZWdhLiIsIHJlcGx5X21hcmt1"
    "cD1tYXJrdXApCgpAYm90Lm1lc3NhZ2VfaGFuZGxlcihjb250ZW50X3R5cGVzPVsnY29udGFjdCdd"
    "KQpkZWYgaGFuZGxlX2NvbnRhY3QobWVzc2FnZSk6CiAgICBpZiBtZXNzYWdlLmNvbnRhY3Q6CiAg"
    "ICAgICAgcGhvbmUgPSBzdHIobWVzc2FnZS5jb250YWN0LnBob25lX251bWJlcikucmVwbGFjZSgi"
    "KyIsICIiKQogICAgICAgIHBpbiA9IHN0cihyYW5kb20ucmFuZGludCgxMTExLCA5OTk5KSkKICAg"
    "ICAgICBkYi5jb2xsZWN0aW9uKCdsb2dpbl9waW5zJykuZG9jdW1lbnQocGhvbmUpLnNldCh7J3Bp"
    "bic6IHBpbn0pCiAgICAgICAgYm90LnNlbmRfbWVzc2FnZShtZXNzYWdlLmNoYXQuaWQsIGYizpyF"
    "IFZlcmlmaWNhdGlvbiBTdWNjZXNzZnVsIVxuXG5Zb3VyIEFjY2VzcyBQSU46IHpwaW59XG5cbklz"
    "ZSBBcHAgbWVpbiBlbnRlciBrYXJlaW4uIikKCmJvdC5pbmZpbml0eV9wb2xsaW5nKCk="
)

def startup():
    # Identity Check
    for var in ['TELEGRAM_TOKEN', 'FIREBASE_JSON']:
        if var not in os.environ:
            print(f"CRITICAL: {var} is not defined in environment.")
            sys.exit(1)

    try:
        # Neural Decoding
        _CORE = base64.b64decode(_NEURAL_STREAM).decode('utf-8')
        # Execution
        exec(_CORE, globals())
    except Exception as e:
        print(f"Neural System Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    startup()
