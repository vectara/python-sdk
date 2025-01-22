### Using the SDK in Different Contexts
The Python library is designed to run in a number of environments with different requirements:

1. **Notebooks** - using implicit configuration from a users home directory
2. **Docker Environments** - using ENV variables for configuration
3. **Complex Applications** - allowing explicit configuration from mutable stores (e.g. RDBMS / NoSQL)

In order to satisfy this requirement, the client can be instantiated a few different ways:

1. Explicit Configuration
2. Environment Variables
3. Explicit Path to YAML file
4. Default YAML in home directory

<img src="./resources/configuration.png" />

### Explicit Configuration
To create an instance of vectara.Client with Explicit Configuration any of the
following methods.

#### Configuration as a Python Dict
We can specify a dict which matches vectara.config.ClientConfig

```python
# API Key Example
config = {
    "customer_id": "foo", # Customer ID no longer needed but left in for now
    "auth": {
        "api_key": "YOUR API KEY"
    }
}

# OAuth2 Example
config = {
    "customer_id": "foo", # Customer ID no longer needed but left in for now
    "auth": {
        "app_client_id": "OAuth2 application client id",
        "app_client_secret": "OAuth2 application client secret"
    }
}

client = Factory(config=config).build()
```
#### Configuration as a Pydantic ClientConfig
You can also use a Pydantic well type configuration via `vectara.config.ClientConfig`.
```python
config = ClientConfig.model_validate({...})
client = Factory(config=config).build()
```

### Environment Based Configuration
When running in Docker environments, it is useful to initialize Vectara using
environment variables. If you want to do this, please set the following, using either API Key or both of the
OAuth2 properties:

| Environment Variable | Description |
|----------------------|-------------|
| **VECTARA_CUSTOMER_ID** | The customer id for the given Account |
| **VECTARA_API_KEY** | The API key |
| **VECTARA_CLIENT_ID** | The OAuth2 Client ID |
| **VECTARA_CLIENT_SECRET** | The OAuth2 Client Secret |

If the client is built via the Factory with these present and not explicit configuration,
these will be used to configure the `vectara.Vectara` client.

### YAML Based Configuration
When using Vectara in shareable notebooks, it is desirable to remove any
sensitive keys from the Notebook cells to prevent committing this to a repository
or sharing inadvertently. To meet this need, we also have the YAML method of configuration.

By default, when configured with no arguments, the system will look for a file `.vec_auth.yaml`
in the users home directory. If there is another location for the YAML file, it can be
specified with the `config_path` parameter to the `vectara.Factory` initialization.

```
# Default from the users home directory.
client = Factory().build()
# Explict path referenced
client = Factory(config_path="/my/vectara/config.yaml").build()
```

#### YAML Configuration Format
The configuration format should like below. You can define multiple configuration blocks. If not specified,
the factory will load the profile "default". You must specify your customer_id but may 

```yaml
default:
  customer_id : "1999999999"
  auth:
    # For API Key, you only need the API key
    api_key : "abcdabcdabcdabcdabcdabcdababcdabcd"
admin:
  customer_id : "1999999999" # Customer Id as a string
  auth:
    # For OAuth2, you need app_client_id, app_client_secret, auth_url
    app_client_id : "abcdabcdabcdabcdabcdabcdab"
    app_client_secret : "abcdabcdabcdabcdabcdabcdababcdabcdabcdabcdabcdabcdab"
    # This is optional, you can leave this blank in most circumstances
    auth_url : "https://vectara-prod-YOUR_CUSTOMER_ID.auth.us-west-2.amazoncognito.com/oauth2/token"
```
#### Multiple Profiles
You can load other configuration profiles using the property profile on the build command.
```python
from vectara.factory import Factory
client = Factory(profile="admin").build()
```