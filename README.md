# MCP Server for Google Calendar
This is a simple Model Context Protocol ([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)) server for Google Calendar in Python. It includes the following functionalities:
- List calendars
- Create calendars
- List events
- Create events
- Update events
- Delete events

## Setup
1. **System requirements**
- Python 3.10 or higher installed
- Git installed
2. **Clone repository**
- Run `git clone https://github.com/stefania-vasileiadou/gcal-mcp.git`
3. **Google Cloud Setup**
- TBA  

**Note**: If your project is configured for an external user type and a publishing status of "Testing", every OAuth2 token will [expire after 7 days](https://developers.google.com/identity/protocols/oauth2#expiration). For this reason, you may encouter errors such as:
```
google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})
```
For a quick fix, delete your `token.json` file and rerun. Otherwise, consider upgrading to a Workspace account.