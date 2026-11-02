# Google Drive: Basic API Usage

## Contents

1. Reading a .csv stored on Google Drive
2. Creating a fallback "dummy" API for demo purposes when a user does not have / want to obtain API credentials.

## Getting an API Key and File ID:

For this example, your `.env` file should be located in the same directory as the `example.py` file and contain:
```
GOOGLE_DRIVE_API_KEY=
GOOGLE_DRIVE_FILE_ID=
# Optional: copy resourcekey from the sharing link if present.
GOOGLE_DRIVE_RESOURCE_KEY=
```
The file id can be found from the link you use to share your document. It is the part between `d/` and `/view?` below:

https://drive.google.com/file/d/1L_JhsrAXBc7qVsUFCrx7mn1sIcL4gF3K/view?usp=drive_link

To create your API key:

1. Go to:
https://console.cloud.google.com/apis/library/browse?filter=category:gsuite

2. Find the option for "Google Drive API"

3. Click "Enable" (or "Manage", if already enabled)

4. On the left, select "Credentials"

5. Click "Create Credentials" -> "API key"

6. Give the API key a name (unique to the project it will be used for)

7. Under "Select API Restrictions", select "Google Drive API"

8. Click "Create".

"Keep it secret, keep it safe." -Gandalf the Grey