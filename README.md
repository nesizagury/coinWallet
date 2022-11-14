# coinWallet
Flask python app, a bitcoin wallet

Data saved in postgress

## Api calls:

- add address
{server_url}:5000/api/v1/{address}

- remove address
{server_url}:5000/api/v1/{address}/remove

- sync data
{server_url}:5000/api/v1/sync


## how to run:
run: docker-compose up -d in root folder

## open issue
- needs to add some kind of ip change in case of 429 errors
- maybe make a bitcoin node so we don't need to use external api
