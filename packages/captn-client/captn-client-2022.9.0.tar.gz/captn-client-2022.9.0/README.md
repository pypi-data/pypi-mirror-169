# Capt’n python client 2022.9.0

## Docs

Full documentation can be found at the following link:

- <a href="https://docs.captn.ai" target="_blank">https://docs.captn.ai/</a>


## How to install

If you don't have the captn library already installed, please install it using pip.


```console
pip install captn-client
```

## How to use

To access the captn service, you must create a developer account. Please fill out the signup form below to get one:

- [https://bit.ly/3I4cNuv](https://bit.ly/3I4cNuv)

Upon successful verification, you will receive the username/password for the developer account in an email. 

Finally, you need an application token to access all the APIs in captn service. Please call the `Client.get_token` method with the username/password to get one. 

You can either pass the username, password, and server address as parameters to the `Client.get_token` method or store the same in the **CAPTN_SERVICE_USERNAME**, **CAPTN_SERVICE_PASSWORD**, and **CAPTN_SERVER_URL** environment variables.

After successful authentication, the captn services will be available to access.

As an additional layer of security, we also support Multi-Factor Authentication (MFA) and Single sign-on (SSO) for generating tokens.

Multi-Factor Authentication (MFA) can be used to help protect your account from unauthorized access by requiring you to enter an additional code when you request a new token. 

Once authenticated successfully, activating MFA for your account is a simple two step process:

1. Enable MFA for your account by calling `User.enable_mfa` method which will generate a QR code. You can then use an authenticator app, such as Google Authenticator to scan the QR code.

2. Activate the MFA by calling `User.activate_mfa` method and passing the dynamically generated six-digit verification code from the authenticator app.

Once MFA is successfully activated, you need to pass the dynamically generated six-digit verification code along with the username/password to `Client.get_token` method for generating new tokens.

You can also disable MFA for you account anytime by calling `User.disable_mfa` method.

Once authenticated successfully, you can also enable Single sign-on (SSO) for your account. Currently, we support only Google and Github as the external authentication providers (SSO). More authentication providers will be supported in the upcoming releases.

Authenticating using Single sign-on (SSO) is a simple three-step process:

1. Enable the SSO provider by calling the `User.enable_sso` method with a valid SSO provider and an email address.

2. To get the token, you must have to complete the SSO authentication with the provider. Calling the `Client.get_token` method with a valid SSO provider will give you an authorization URL. Please copy and paste it into your preferred browser and initiate the authentication and authorization process with the SSO provider.

3. Once the authentication is successful, calling the `Client.set_sso_token` method gets a new developer token and will implicitly use in all the interactions with the captn server.

For more information, please check:

- [Tutorial](https://docs.captn.ai/Tutorial/) with more elaborate example, and

- [API](https://docs.captn.ai/API/client/Client/) with reference documentation.


Below is a minimal example explaining how to load the data, train a model and make predictions using captn services. 


In the below example, the username, password, and server address are stored in **CAPTN_SERVICE_USERNAME**, **CAPTN_SERVICE_PASSWORD**, and **CAPTN_SERVER_URL** environment variables.


### 0. Get token


```
from captn.client import Client, DataBlob, DataSource

Client.get_token()
```

### 1. Connect and preprocess data

In our example, we will be using the captn APIs to load and preprocess a sample CSV file stored in an AWS S3 bucket. 


```
data_blob = DataBlob.from_s3(
    uri="s3://test-airt-service/sample_gaming_130k/"
)
data_blob.progress_bar()

```

    100%|██████████| 1/1 [00:30<00:00, 30.36s/it]


The sample data we used in this example doesn't have the header rows and their data types defined. 

The following code creates the necessary headers along with their data types and reads only a subset of columns that are required for modeling:



```
prefix = ["revenue", "ad_revenue", "conversion", "retention"]
days = list(range(30)) + list(range(30, 361, 30))
dtype = {
    "date": "str",
    "game_name": "str",
    "platform": "str",
    "user_type": "str",
    "network": "str",
    "campaign": "str",
    "adgroup": "str",
    "installs": "int32",
    "spend": "float32",
}
dtype.update({f"{p}_{d}": "float32" for p in prefix for d in days})
names = list(dtype.keys())

kwargs = {"delimiter": "|", "names": names, "parse_dates": ["date"], "usecols": names[:42], "dtype": dtype}
```

Finally, the above variables are passed to the `DataBlob.to_datasource` method which preprocesses the data and stores it in captn server.


```
data_source = data_blob.to_datasource(
    file_type="csv",
    index_column="game_name",
    sort_by="date",
    **kwargs
)

data_source.progress_bar()
```

    100%|██████████| 1/1 [01:00<00:00, 60.68s/it]



```
print(data_source.head())
```

                      date platform          user_type            network  \
    game_name                                                               
    game_name_0 2021-03-15      ios      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15      ios      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15      ios      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15      ios      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15      ios      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15  android  googleadwords_int  googleadwords_int   
    game_name_0 2021-03-15  android  googleadwords_int  googleadwords_int   
    game_name_0 2021-03-15  android         moloco_int         moloco_int   
    game_name_0 2021-03-15  android      jetfuelit_int      jetfuelit_int   
    game_name_0 2021-03-15  android      jetfuelit_int      jetfuelit_int   
    
                     campaign       adgroup  installs       spend  revenue_0  \
    game_name                                                                  
    game_name_0    campaign_0   adgroup_541         1    0.600000   0.000000   
    game_name_0    campaign_0  adgroup_2351         2    4.900000   0.000000   
    game_name_0    campaign_0   adgroup_636         3    7.350000   0.000000   
    game_name_0    campaign_0   adgroup_569         1    0.750000   0.000000   
    game_name_0    campaign_0   adgroup_243         2    3.440000   0.000000   
    game_name_0  campaign_283  adgroup_1685        11    0.000000   0.000000   
    game_name_0    campaign_2    adgroup_56        32   30.090000   0.000000   
    game_name_0  campaign_191          None       291  503.480011  34.701553   
    game_name_0    campaign_0   adgroup_190         4    2.740000   0.000000   
    game_name_0    campaign_0   adgroup_755         8   11.300000  13.976003   
    
                 revenue_1  ...  revenue_23  revenue_24  revenue_25  revenue_26  \
    game_name               ...                                                   
    game_name_0   0.018173  ...    0.018173    0.018173    0.018173    0.018173   
    game_name_0   0.034000  ...    0.034000    6.034000    6.034000    6.034000   
    game_name_0   0.000000  ...   12.112897   12.112897   12.112897   12.112897   
    game_name_0   0.029673  ...    0.029673    0.029673    0.029673    0.029673   
    game_name_0   0.027981  ...    0.042155    0.042155    0.042155    0.042155   
    game_name_0   0.097342  ...    0.139581    0.139581    0.139581    0.139581   
    game_name_0   0.802349  ...    2.548253    2.548253    2.771138    2.805776   
    game_name_0  63.618111  ...  116.508331  117.334709  117.387489  117.509506   
    game_name_0   0.000000  ...    0.000000    0.000000    0.000000    0.000000   
    game_name_0  14.358793  ...   14.338905   14.338905   14.338905   14.338905   
    
                 revenue_27  revenue_28  revenue_29  revenue_30  revenue_60  \
    game_name                                                                 
    game_name_0    0.018173    0.018173    0.018173    0.018173    0.018173   
    game_name_0    6.034000    6.034000    6.034000    6.034000    6.034000   
    game_name_0   12.112897   12.112897   12.112897   12.112897   12.112897   
    game_name_0    0.029673    0.029673    0.029673    0.029673    0.029673   
    game_name_0    0.042155    0.042155    0.042155    0.042155    0.042155   
    game_name_0    0.139581    0.139581    0.139581    0.139581    0.139581   
    game_name_0    2.805776    2.805776    2.805776    2.805776    2.805776   
    game_name_0  118.811417  118.760765  119.151291  119.350220  139.069443   
    game_name_0    0.000000    0.000000    0.000000    0.000000    0.000000   
    game_name_0   14.338905   14.338905   14.338905   14.338905   14.338905   
    
                 revenue_90  
    game_name                
    game_name_0    0.018173  
    game_name_0   13.030497  
    game_name_0   12.112897  
    game_name_0    0.029673  
    game_name_0    0.042155  
    game_name_0    0.139581  
    game_name_0    2.805776  
    game_name_0  147.528793  
    game_name_0    0.000000  
    game_name_0   14.338905  
    
    [10 rows x 41 columns]


### 2. Training


```
# Todo
```
