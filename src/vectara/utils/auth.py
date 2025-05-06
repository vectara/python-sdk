import os
from typing import Tuple, Optional
import httpx
from ..core.oauth_token_provider import OAuthTokenProvider
from ..core.client_wrapper import SyncClientWrapper
from ..environment import VectaraEnvironment

def get_oauth2_credentials_from_env() -> Tuple[Optional[str], Optional[str]]:
    """
    Get OAuth2 credentials from environment variables.
    
    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple containing (client_id, client_secret) if both are present,
        otherwise (None, None)
    """
    client_id = os.getenv("VECTARA_CLIENT_ID")
    client_secret = os.getenv("VECTARA_CLIENT_SECRET")
    
    if client_id is not None and client_secret is not None:
        return client_id, client_secret
    return None, None

def create_oauth2_client_wrapper(
    environment: VectaraEnvironment,
    client_id: str,
    client_secret: str,
    timeout: Optional[float],
    follow_redirects: Optional[bool],
    httpx_client: Optional[httpx.Client],
    token_getter_override: Optional[callable] = None
) -> SyncClientWrapper:
    """
    Create a client wrapper with OAuth2 authentication.
    
    Args:
        environment: The Vectara environment to use
        client_id: OAuth2 client ID
        client_secret: OAuth2 client secret
        timeout: Request timeout in seconds
        follow_redirects: Whether to follow redirects
        httpx_client: Custom httpx client to use
        token_getter_override: Optional token getter override
        
    Returns:
        A configured client wrapper
    """
    defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
    
    # Create base client for OAuth token provider
    base_client = SyncClientWrapper(
        environment=environment,
        api_key=None,
        httpx_client=httpx.Client(timeout=defaulted_timeout, follow_redirects=follow_redirects)
        if follow_redirects is not None
        else httpx.Client(timeout=defaulted_timeout),
        timeout=defaulted_timeout,
    )
    
    # Create OAuth token provider
    oauth_token_provider = OAuthTokenProvider(
        client_id=client_id,
        client_secret=client_secret,
        client_wrapper=base_client,
    )
    
    # Create client wrapper
    return SyncClientWrapper(
        environment=environment,
        api_key=None,
        token=token_getter_override if token_getter_override is not None else oauth_token_provider.get_token,
        httpx_client=httpx_client
        if httpx_client is not None
        else httpx.Client(timeout=defaulted_timeout, follow_redirects=follow_redirects)
        if follow_redirects is not None
        else httpx.Client(timeout=defaulted_timeout),
        timeout=defaulted_timeout,
    )

def create_api_key_client_wrapper(
    environment: VectaraEnvironment,
    api_key: str,
    timeout: Optional[float],
    follow_redirects: Optional[bool],
    httpx_client: Optional[httpx.Client]
) -> SyncClientWrapper:
    """
    Create a client wrapper with API key authentication.
    
    Args:
        environment: The Vectara environment to use
        api_key: API key to use
        timeout: Request timeout in seconds
        follow_redirects: Whether to follow redirects
        httpx_client: Custom httpx client to use
        
    Returns:
        A configured client wrapper
    """
    defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
    
    return SyncClientWrapper(
        environment=environment,
        api_key=api_key,
        httpx_client=httpx_client
        if httpx_client is not None
        else httpx.Client(timeout=defaulted_timeout, follow_redirects=follow_redirects)
        if follow_redirects is not None
        else httpx.Client(timeout=defaulted_timeout),
        timeout=defaulted_timeout,
    ) 