# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.api_role import ApiRole
from ..types.app_client import AppClient
from .raw_client import AsyncRawAppClientsClient, RawAppClientsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AppClientsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppClientsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[AppClient]:
        """
        Retrieve a list of application clients configured for the customer account.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of App Clients to return at one time.

        filter : typing.Optional[str]
            Regular expression to filter the names of the App Clients.

        page_key : typing.Optional[str]
            Used to retrieve the next page of App Clients after the limit has been reached.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[AppClient]
            An array of App Clients.

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        response = client.app_clients.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        response = self._raw_client.list(
            limit=limit,
            filter=filter,
            page_key=page_key,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    def create(
        self,
        *,
        name: str,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        description: typing.Optional[str] = OMIT,
        api_roles: typing.Optional[typing.Sequence[ApiRole]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        An App Client is used for OAuth 2.0 authentication when calling Vectara APIs.

        Parameters
        ----------
        name : str
            Name of the client credentials.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        description : typing.Optional[str]
            Description of the client credentials.

        api_roles : typing.Optional[typing.Sequence[ApiRole]]
            API roles that the client credentials will have.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            An App Client object, used to query the Vectara API with the assigned roles.

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.app_clients.create(name='name', )
        """
        response = self._raw_client.create(
            name=name,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            description=description,
            api_roles=api_roles,
            request_options=request_options,
        )
        return response.data

    def get(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        Retrieve details of a specific application client by its ID.

        Parameters
        ----------
        app_client_id : str
            The ID of the App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            The App Client.

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.app_clients.get(app_client_id='app_client_id', )
        """
        response = self._raw_client.get(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    def delete(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove an application client configuration from the customer account.

        Parameters
        ----------
        app_client_id : str
            The ID of App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.app_clients.delete(app_client_id='app_client_id', )
        """
        response = self._raw_client.delete(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    def update(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        description: typing.Optional[str] = OMIT,
        api_roles: typing.Optional[typing.Sequence[ApiRole]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        Update the configuration or settings of an existing application client.

        Parameters
        ----------
        app_client_id : str
            The name of App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        description : typing.Optional[str]
            The new App Client description.

        api_roles : typing.Optional[typing.Sequence[ApiRole]]
            The new roles attached to the App Client. These roles will replace the current roles.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            The App Client.

        Examples
        --------
        from vectara import Vectara
        client = Vectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.app_clients.update(app_client_id='app_client_id', )
        """
        response = self._raw_client.update(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            description=description,
            api_roles=api_roles,
            request_options=request_options,
        )
        return response.data


class AsyncAppClientsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppClientsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppClientsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppClientsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        page_key: typing.Optional[str] = None,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[AppClient]:
        """
        Retrieve a list of application clients configured for the customer account.

        Parameters
        ----------
        limit : typing.Optional[int]
            The maximum number of App Clients to return at one time.

        filter : typing.Optional[str]
            Regular expression to filter the names of the App Clients.

        page_key : typing.Optional[str]
            Used to retrieve the next page of App Clients after the limit has been reached.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[AppClient]
            An array of App Clients.

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            response = await client.app_clients.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page
        asyncio.run(main())
        """
        response = await self._raw_client.list(
            limit=limit,
            filter=filter,
            page_key=page_key,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    async def create(
        self,
        *,
        name: str,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        description: typing.Optional[str] = OMIT,
        api_roles: typing.Optional[typing.Sequence[ApiRole]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        An App Client is used for OAuth 2.0 authentication when calling Vectara APIs.

        Parameters
        ----------
        name : str
            Name of the client credentials.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        description : typing.Optional[str]
            Description of the client credentials.

        api_roles : typing.Optional[typing.Sequence[ApiRole]]
            API roles that the client credentials will have.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            An App Client object, used to query the Vectara API with the assigned roles.

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.app_clients.create(name='name', )
        asyncio.run(main())
        """
        response = await self._raw_client.create(
            name=name,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            description=description,
            api_roles=api_roles,
            request_options=request_options,
        )
        return response.data

    async def get(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        Retrieve details of a specific application client by its ID.

        Parameters
        ----------
        app_client_id : str
            The ID of the App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            The App Client.

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.app_clients.get(app_client_id='app_client_id', )
        asyncio.run(main())
        """
        response = await self._raw_client.get(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    async def delete(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove an application client configuration from the customer account.

        Parameters
        ----------
        app_client_id : str
            The ID of App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.app_clients.delete(app_client_id='app_client_id', )
        asyncio.run(main())
        """
        response = await self._raw_client.delete(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            request_options=request_options,
        )
        return response.data

    async def update(
        self,
        app_client_id: str,
        *,
        request_timeout: typing.Optional[int] = None,
        request_timeout_millis: typing.Optional[int] = None,
        description: typing.Optional[str] = OMIT,
        api_roles: typing.Optional[typing.Sequence[ApiRole]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppClient:
        """
        Update the configuration or settings of an existing application client.

        Parameters
        ----------
        app_client_id : str
            The name of App Client.

        request_timeout : typing.Optional[int]
            The API will make a best effort to complete the request in the specified seconds or time out.

        request_timeout_millis : typing.Optional[int]
            The API will make a best effort to complete the request in the specified milliseconds or time out.

        description : typing.Optional[str]
            The new App Client description.

        api_roles : typing.Optional[typing.Sequence[ApiRole]]
            The new roles attached to the App Client. These roles will replace the current roles.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppClient
            The App Client.

        Examples
        --------
        from vectara import AsyncVectara
        import asyncio
        client = AsyncVectara(api_key="YOUR_API_KEY", client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.app_clients.update(app_client_id='app_client_id', )
        asyncio.run(main())
        """
        response = await self._raw_client.update(
            app_client_id,
            request_timeout=request_timeout,
            request_timeout_millis=request_timeout_millis,
            description=description,
            api_roles=api_roles,
            request_options=request_options,
        )
        return response.data
