import requests

class AccessTokenError(Exception):
    pass

def access_token(tenentID, clientID, clientSecrate):
    '''
    This function will help user to generate access_token to use azure rest api's.
    Access tokens play a crucial role in securing those APIs. 
    The tokens carry information about the client's identity and the granted permissions, 
    enabling the API to make access control decisions.

    Args:
        tenentID (string): tenant ID, also known as a directory ID, is a unique identifier assigned 
                           to each Azure AD instance. It represents a single and distinct organization 
                           or entity that uses Azure AD to manage and secure its identities, 
                           applications, and services.

        clientID (string): client ID, also known as an application ID, is a unique identifier assigned 
                           to an application when it is registered in Azure AD.
                           
        clientSecrate (string): client secret is a piece of information that is used by a registered 
                                application to prove its identity when authenticating with Azure AD.

    Returns: 
        string: It will return a access token in datatype string.
    '''
# url endpoint to generate access token 
    token_endpoint = f'https://login.microsoftonline.com/{tenentID}/oauth2/token'
#    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
# request payload with service pricipal
    data = {
      'grant_type': 'client_credentials',
      'client_id': clientID,
      'client_secret': clientSecrate,
      'resource': 'https://management.azure.com'
    }
# requesting the response with post method 
    try:
        response = requests.post(token_endpoint, headers=headers, data=data)
        response.raise_for_status()
        access_token = response.json()['access_token']

        if access_token:
            return access_token
        else:
            raise AccessTokenError("Access token not found in response.")
        
    except requests.exceptions.RequestException as e:
        raise AccessTokenError(f"Error during request: {e}")
    
    except Exception as e:
        raise AccessTokenError(f"Unexpected error: {e}")
    