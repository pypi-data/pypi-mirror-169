import asyncio
import base58
from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
from .enums import AccountTypes, SolanaNetwork
from .aver_client import AverClient
from .constants import AVER_HOST_ACCOUNT, AVER_PROGRAM_IDS, get_solana_endpoint
from solana.rpc.types import TxOpts
from .utils import fetch_with_version
from .errors import get_idl_errors
from solana.rpc.commitment import Confirmed
import base58 
from .enums import Side, SizeFormat
from .refresh import refresh_multiple_user_markets, refresh_user_market
from solana.publickey import PublicKey
from .market import AverMarket
from .user_market import UserMarket
from requests import get, post

#DEVNET EXAMPLE

async def main():
    #Decoding the secret key from base58 to bytes
    secret_key = base58.b58decode('3onYh3TSCg92X3kD9gD7RCZF1N8JFVSDp39eSkRswsQb5YwWuyMnzuCN2wuPb52XEnPzjVrCtkYe5Xo8Czd3CDyV')
    owner = Keypair.from_secret_key(secret_key)

    #Default Transaction Options
    opts = TxOpts(preflight_commitment=Confirmed)
    connection = AsyncClient(
            get_solana_endpoint(SolanaNetwork.DEVNET),
            'confirmed',
            timeout=30
    )
    client = await AverClient.load(
        connection=connection, 
        owner=owner, 
        opts=opts, 
        network=SolanaNetwork.DEVNET, 
        program_ids=[PublicKey('DfMQPAuAeECP7iSCwTKjbpzyx6X1HZT6rz872iYWA8St')]
        #program_ids=AVER_PROGRAM_IDS
        )
    
    print(get_idl_errors(client.programs[0]))

    # all_markets = get(get_aver_api_endpoint(SolanaNetwork.DEVNET) + '/v2/markets')
    # #Just pick the first active market
    # chosen_market = ''
    # for m in all_markets.json():
    #     if m['internal_status'] != 'test':
    #         chosen_market = m
    #         break
    # market_pubkey = PublicKey(chosen_market['pubkey'])
    ###
    #Example warning
    #Sometimes, the markets loaded above may have already been resolved
    #Therefore, I've copied and pasted a market public key from https://dev.app.aver.exchange/
    ###
    # market_pubkey = PublicKey('55JcicbzvoxktKbZ6fgWqUWZHXi7guDCRYv7C2a3MstK')
    # v = (await client.program.account['MarketV0'].fetch(market_pubkey)).version
    # print(v)
    #a = await fetch_with_version(connection, client.program, AccountTypes.MARKET, market_pubkey)
    #print(a)

    market_pubkey = PublicKey('2xvvvKMoFXCbafqyXQ3hEZHiv1mcvokscziBbUYst7M3')

    #Load market
    market = await AverMarket.load(client, market_pubkey)


    # #Obtain orderbook
    # outcome_1_orderbook = market.orderbooks[0]
    # #Print orderbook data
    # print('Best Ask Price', outcome_1_orderbook.get_best_ask_price(True))
    # print('Best Bid Price', outcome_1_orderbook.get_best_bid_price(True))

    #Gets Solana Airdrop and USDC Token Airdrop
    #Only available on devnet
    # await client.request_lamport_airdrop(1_000_000, owner.public_key)
    # print('New Balance: ', await client.request_lamport_balance(owner.public_key))
    # #Creates Associated Token Account where tokens will be stored
    # ata = await client.get_or_create_associated_token_account(
    #     owner.public_key,
    #     owner,
    # )
    # signature = request_token_airdrop(client.aver_api_endpoint, client.quote_token,owner.public_key, 1_000_000_000)['signature']
    # #Wait to ensure transaction has been confirmed before moving on
    # await client.provider.connection.confirm_transaction(signature, Confirmed) 
    # token_balance = await client.request_token_balance(client.quote_token, owner.public_key)
    # print('New token balance: ', token_balance)

    #Create User Market Account
    #This function also automatically gets_or_creates a UserHostLifetime account
    owner = Keypair.from_secret_key(base58.b58decode('2S1DDiUZuqFNPHx2uzX9pphxynV1CgpLXnT9QrwPoWwXaGrqAP88XNEh9NK7JbFByJFDsER7PQgsNyacJyCGsH8S'))
    host, bump = PublicKey.find_program_address([b"host", bytes(owner.public_key)], PublicKey('DfMQPAuAeECP7iSCwTKjbpzyx6X1HZT6rz872iYWA8St'))

    uma = await UserMarket.get_or_create_user_market_account(
        client,
        market,
        owner,
        host=host
    )


#     # Place order
#     # This order a BUY side on outcome 1 at a price of 0.5 and size 10
#     # This means it will cost 5 tokens and we will win 10 (once the bet is matched and if we win)
#     signature = await uma.place_order(
#         owner,
#         0, #Outcome 1
#         Side.SELL,
#         limit_price=0.5,
#         size=3,
#         size_format=SizeFormat.PAYOUT
#     )
#     #Wait to ensure transaction has been confirmed before moving on
#     print(signature['result'])
#     await client.provider.connection.confirm_transaction(signature['result'], Confirmed)

#     # print(await market.crank_market(payer=owner))

#     #Refresh market information efficiently
#     #Refreshing a User Market also automatically refreshes the market
#     uma = (await refresh_multiple_user_markets(client, [uma, uma]))[0]
#     market = uma.market
#     print('UHL')
#     print(uma.user_host_lifetime.user_host_lifetime_state)
#     print('UMA')
#     print(uma.user_market_state)
    
#     #Cancel order
#     #We should only have 1 order, so we'll cancel the first in the array
#     # my_order_id = uma.user_market_state.orders[0].order_id
#     # signature = await uma.cancel_order(
#     #     owner,
#     #     my_order_id,
#     #     0, #We placed an order on outcome 1
#     #     active_pre_flight_check=True
#     # )
#     # signature = await uma.cancel_all_orders([0], owner)
#     # #Wait to ensure transaction has been confirmed before moving on
#     # await client.provider.connection.confirm_transaction(signature[0]['result'], Confirmed) 

#     #Finally close the client
#     await client.close()
# def request_token_airdrop(
#     aver_api_endpoint: str,
#     quote_token: PublicKey,
#     owner: PublicKey, 
#     amount: int = 1_000_000_000,
#     ):

#     url = aver_api_endpoint + '/airdrop'

#     body = {
#         'wallet': owner.to_base58(),
#         'mint': quote_token.__str__(),
#         'amount': amount
#     }

#     response = post(url, body)
#     return response.json()
    

asyncio.run(main())