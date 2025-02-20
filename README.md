# Webullpay OpenAPI Python SDK

Webullpay OpenAPI aims to provide quantitative trading investors with convenient, fast and secure services. Webullpay aims to help every quant traders achieve flexible and changeable trading or market strategies.

The main function:

Trading management: create, modify, cancel orders, etc.

Market information: You can query crypto market information through the HTTP interface.

Account Information: Query account balance and position information.

Subscription to real-time information: Subscribe to order status changes.

## Requirements

- Please first generate the app key and app secret on the Webullpay official website.

| Market | Link                      |
|--------|---------------------------|
| US     | https://www.webullpay.com |

- Requires Python 3.7 and above.

## Interface Protocol

The bottom layer of Webullpay OpenAPI provides three protocols, HTTP / GRPC, to support functions and features like trading, subscriptions for changes of order status.

| Protocol    | Description                                       |
|-------|------------------------------------------|
| HTTP  | It mainly provides interface services for data such as tradings, accounts, candlestick charts, snapshots, etc.              |
| GRPC	 | 1. Provide real-time push messages for order status changes.<br/>2. Provide data query support for the market interface. |

## Developer documentation

| Market | Link                                     |
|--------|------------------------------------------|
| US     | https://www.webullpay.com/api-doc/ |
