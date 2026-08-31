# Practical Example: Delete Old Copilot Sessions

## EXAMPLE of Situation
- 19 total sessions
- 7 sessions older than 60 days (60-80 days old)
- Want to clean up old sessions from Test_Task project

## Three Simple Options

### Option 1: File Explorer (Safest & Most Visual) ⭐

1. Press `Win + R`
2. Type: `%USERPROFILE%\.copilot\session-state`
3. Press Enter
4. Sort by "Date Modified" (oldest first)
5. Select sessions from 60+ days ago
6. Press Delete
7. Confirm

**Example**
**Sessions to delete:**
- e8fc2c04-ef90-421d-ab4a-88233966d0cb (80 days)
- 5a486a79-fc20-42ef-9970-365c096f659e (73 days)
- 84da4c35-5679-4549-98a2-f99d9081f38a (69 days)
- a0b76e33-873d-4a27-b181-d05f83c9391b (67 days)
- e691ded9-6701-4a18-9bed-6625cc554946 (64 days)
- c6ef5a5b-4f7f-47de-b1eb-370883ccb861 (63 days)
- dcef1168-108a-4598-8bb8-8f40f5f51c27 (62 days)

### Option 2: PowerShell (Delete All Old Sessions at Once)

Open PowerShell and run:

```powershell
$sessionPath = "$env:USERPROFILE\.copilot\session-state"
Get-ChildItem -Path $sessionPath -Directory | 
  Where-Object { $_.CreationTime -lt (Get-Date).AddDays(-60) } | 
  Remove-Item -Recurse -Force

Write-Host "Cleanup complete!"
```

**What happens:**
- Finds all session folders created before 60 days ago
- Deletes them automatically
- Done in ~2 seconds

### Option 3: Delete One Specific Session

```powershell
rmdir "$env:USERPROFILE\.copilot\session-state\e8fc2c04-ef90-421d-ab4a-88233966d0cb" /s /q
```

Replace `e8fc2c04-ef90-421d-ab4a-88233966d0cb` with the session ID you want to delete.

## Before & After

**Before Cleanup:**
```
Session Count: 19
  • 3 sessions from today
  • 2 sessions from 34 days ago
  • 5 sessions from 42-55 days ago
  • 7 sessions from 62-80 days ago ← REMOVE THESE
Disk Space Used: ~450 MB
```

**After Cleanup:**
```
Session Count: 12
  • 3 sessions from today
  • 2 sessions from 34 days ago
  • 5 sessions from 42-55 days ago
Disk Space Used: ~250 MB
Freed: ~200 MB
```

## Safety Checklist

Before deleting, ask yourself:

- [ ] Is the session older than 60 days?
- [ ] Have I saved important work from this session elsewhere?
- [ ] Do I still need the session history?
- [ ] Is this a one-off exploration or completed project?

If YES to all: **Safe to delete**

## Quick Facts

| Aspect | Details                                      |
|--------|----------------------------------------------|
| **Location** | `C:\Users\user_name\.copilot\session-state\` |
| **What to delete** | Session folders (directories)                |
| **Can I undo?** | ❌ NO - Permanent deletion                    |
| **Space freed** | ~20-30 MB per session                        |
| **Time to cleanup** | < 5 seconds                                  |
| **Cloud sync** | ❌ Local only, not synced                     |

## Recommended Action

1. Open File Explorer
2. Navigate to `C:\Users\user_name\.copilot\session-state`
3. Sort by Date Modified (oldest first)
4. Select all sessions older than 60+ days
5. Press Delete
6. Confirm

**Result:** ~200 MB freed, only active sessions remain!

## After Cleanup Maintenance

To prevent accumulation:
- Delete sessions older than 60 days monthly
- Archive important work before deleting
- Use descriptive session names for future sessions

---

**That's it! Sessions are just folders. Delete = Close.**
