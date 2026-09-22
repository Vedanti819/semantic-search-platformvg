# Example Queries

After running ingestion and starting the API, try:

### Query 1
`How many annual leave days do employees receive?`

Expected top result: `leave_policy.txt`

### Query 2
`When do I need to submit an expense claim?`

Expected top result: `expense_policy.txt`

### Query 3
`Which systems require multi-factor authentication?`

Expected top result: `it_security.txt`

### Query 4
`Can employees work remotely?`

Expected top result: `hr_policy.txt`

## API example

### PowerShell

```powershell
$body = @{ query = "How many annual leave days do employees receive?"; top_k = 3 } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/search -ContentType "application/json" -Body $body
```
