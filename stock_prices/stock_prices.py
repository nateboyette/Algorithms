#!/usr/bin/python

import argparse


def find_max_profit(prices):

    profits = []
    maxProfit = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] == prices[i]:
                continue
            else:
                profit = prices[j] - prices[i]
                profits.append(profit)

    maxProfit = max(profits)
    return maxProfit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
