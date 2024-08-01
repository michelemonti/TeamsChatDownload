English Version

# TeamsChatDownload v1.0

TeamsChatAnalyzer is a utility for downloading and analyzing Microsoft Teams chat data using Microsoft Graph API. This project allows users to authenticate, download chat data, and utilize it to generate summaries and useful documentation for business purposes.

## Prerequisites
- Python 3.6 or higher
- Azure AD account with necessary permissions
- Azure AD registered application with permissions to access Microsoft Graph API

## Setup

Clone this repository to your local machine using the following command:

git clone https://github.com/michelemonti/TeamsChatDownload.git


#### Install Dependencies
Use pip to install the required dependencies:

pip install -r requirements.txt


#### Configuration
Create a .env file in the project root and add the following variables:

CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
TENANT_ID=your-tenant-id
REDIRECT_URI=http://localhost:5500/get_token
Replace your-client-id, your-client-secret, and your-tenant-id with the correct values from your Azure AD registered application.

## Usage
Start the Server

Run the server to start the application:
python src/get_chats.py
Fetching Chat Messages

To fetch chat messages, you can run:
python src/fetch_chat_messages.py
The messages will be saved in chat_messages.txt.

###### Contributing
Contributions are welcome! I started this project because I didn't find anything useful on this process here on github. I'll share public this first version, and I'll fork to continue my idea with my team at https://github.com/3FESTO

###### License 
This project is licensed under the MIT License. See the LICENSE file for more details.

##### Contact
For questions or assistance, contact me, I', Michele Miky Monti and I'm here on GitHub
