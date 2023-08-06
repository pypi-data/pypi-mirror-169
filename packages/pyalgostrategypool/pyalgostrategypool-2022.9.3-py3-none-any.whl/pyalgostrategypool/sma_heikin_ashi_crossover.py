from pyalgotrading.constants import *
from pyalgotrading.strategy import StrategyBase


class SMAHeikinAshiCrossover(StrategyBase):

    def __init__(self, *args, **kwargs):
        """
        Accept and sanitize all your parameters here.
        Setup the variables ou will need here.
        If you are running the strategy for multiple days, then this method will be called only once at the start of the strategy.
        """

        super().__init__(*args, **kwargs)

        # SMA Heikin Ashi parameters
        self.profit_booking_buy_points = self.strategy_parameters['PROFIT_BOOKING_BUY_POINTS']
        self.profit_booking_sell_points = self.strategy_parameters['PROFIT_BOOKING_SELL_POINTS']
        self.sma_period = self.strategy_parameters['SMA_PERIOD']

        # Sanity
        assert (0 < self.profit_booking_buy_points == int(self.profit_booking_buy_points)), f"Strategy parameter PROFIT_BOOKING_BUY_POINTS should be a positive integer. Received: {self.profit_booking_buy_points}"
        assert (0 < self.profit_booking_sell_points == int(self.profit_booking_sell_points)), f"Strategy parameter PROFIT_BOOKING_SELL_POINTS should be a positive integer. Received: {self.profit_booking_sell_points}"
        assert (0 < self.sma_period == int(self.sma_period)), f"Strategy parameter SMA_PERIOD should be a positive integer. Received: {self.sma_period}"

        # Variables
        self.main_order = None
        self.profit_order = None

    def initialize(self):
        """
        If you are running the strategy for multiple days, then this method will be called only once at the start of every day.
        Use this to initialize and re-initialize your variables.
        """

        self.main_order = {}
        self.profit_order = {}

    @staticmethod
    def name():
        """
        Name of your strategy.
        """
        return 'SMA Heikin Ashi Crossover'

    @staticmethod
    def versions_supported():
        """
        Strategy should always support the latest engine version.
        Current version is 3.3.0
        """

        return AlgoBullsEngineVersion.VERSION_3_3_0

    def get_decision(self, instrument, decision):
        """
        This method calculates the crossover using the hist data of the instrument along with the required indicator.
        """

        # Get OHLC historical data for the instrument
        hist_data = self.get_historical_data(instrument)

        # Calculate the Heikin Ashi and SMA values
        hist_data_heikinashi = HeikinAshi(hist_data)
        sma_value = talib.SMA(hist_data_heikinashi['HA_close'], timeperiod=self.sma_period)

        # Get the crossover value
        crossover_value = self.utils.crossover(hist_data_heikinashi['HA_close'], sma_value)

        # Return action as BUY if crossover is Upwards and decision is Entry, else SELL if decision is EXIT
        if crossover_value == 1:
            action = ActionConstants.ENTRY_BUY if decision is DecisionConstants.ENTRY_POSITION else ActionConstants.EXIT_SELL

        # Return action as SELL if crossover is Downwards and decision is Entry, else BUY if decision is EXIT
        elif crossover_value == -1:
            action = ActionConstants.ENTRY_SELL if decision is DecisionConstants.ENTRY_POSITION else ActionConstants.EXIT_BUY

        # Return action as NO_ACTION if there is no crossover
        else:
            action = ActionConstants.NO_ACTION

        return action

    def get_exit_action(self, action):
        action_map = {ActionConstants.ENTRY_BUY: ActionConstants.EXIT_BUY, ActionConstants.ENTRY_SELL: ActionConstants.EXIT_SELL}
        return action_map[action]

    def strategy_select_instruments_for_entry(self, candle, instruments_bucket):
        """
        This method is called once every candle time.
        If you set the candle at 5 minutes, then this method will be called every 5 minutes (09:15, 09:20, 09:25 and so on).
        In a candle, the exit method is called first, then the entry method is called.
        So once a candle starts, strategy_select_instruments_for_exit gets called first
        and then this method strategy_select_instruments_for_entry gets called.
        """

        # Add instrument in this bucket if you want to place an order for it
        # We decide whether to place an instrument in this bucket or not based on the decision making process given below in the loop
        selected_instruments_bucket = []

        # Add accompanying info in this bucket for that particular instrument in the bucket above
        sideband_info_bucket = []

        # Looping over all instruments given by you in the bucket (we can give multiple instruments in the configuration)
        for instrument in instruments_bucket:

            # Compute various things and get the decision to place an order only if no current order is going on (main order is empty / none)
            if self.main_order.get(instrument) is None:

                # Get entry decision
                action = self.get_decision(instrument, DecisionConstants.ENTRY_POSITION)

                if action is ActionConstants.ENTRY_BUY or (action is ActionConstants.ENTRY_SELL and self.strategy_mode is StrategyMode.INTRADAY):
                    # Add instrument to the bucket and its additional info for main order
                    selected_instruments_bucket.append(instrument)
                    sideband_info_bucket.append({'action': action})

                    # Add instrument to the bucket and its additional info for profit order
                    selected_instruments_bucket.append(instrument)
                    sideband_info_bucket.append({'action': self.get_exit_action(action)})

        # Return the buckets to the core engine
        # Engine will now call strategy_enter_position with each instrument and its additional info one by one
        return selected_instruments_bucket, sideband_info_bucket

    def strategy_enter_position(self, candle, instrument, sideband_info):
        """
        This method is called once for each instrument from the bucket in this candle.
        Place an order here and return it to the core.
        """

        # Quantity formula (number of lots comes from the config)
        qty = self.number_of_lots * instrument.lot_size

        action = sideband_info['action']

        # Place buy order
        if action is ActionConstants.ENTRY_BUY:
            _order = self.broker.BuyOrderRegular(instrument=instrument, order_code=BrokerOrderCodeConstants.INTRADAY, order_variety=BrokerOrderVarietyConstants.MARKET, quantity=qty)

        elif action is ActionConstants.EXIT_BUY:
            _order = self.broker.SellOrderRegular(instrument=instrument, order_code=BrokerOrderCodeConstants.INTRADAY, order_variety=BrokerOrderVarietyConstants.LIMIT, quantity=qty,
                                                  price=self.main_order[instrument].entry_price + self.profit_booking_buy_points, position=BrokerExistingOrderPositionConstants.EXIT,
                                                  related_order=self.main_order[instrument])
        # Place sell order
        elif action is ActionConstants.ENTRY_SELL:
            _order = self.broker.SellOrderRegular(instrument=instrument, order_code=BrokerOrderCodeConstants.INTRADAY, order_variety=BrokerOrderVarietyConstants.MARKET, quantity=qty)

        elif action is ActionConstants.EXIT_SELL:
            _order = self.broker.BuyOrderRegular(instrument=instrument, order_code=BrokerOrderCodeConstants.INTRADAY, order_variety=BrokerOrderVarietyConstants.LIMIT, quantity=qty,
                                                 price=self.main_order[instrument].entry_price - self.profit_booking_sell_points, position=BrokerExistingOrderPositionConstants.EXIT,
                                                 related_order=self.main_order[instrument])

        # Sanity
        else:
            raise SystemExit(f'Got invalid sideband_info value: {sideband_info}')

        if action in [ActionConstants.ENTRY_BUY, ActionConstants.ENTRY_SELL]:
            self.main_order[instrument] = _order
        else:
            self.profit_order[instrument] = _order

        # Return the order to the core engine for management
        return _order

    def strategy_select_instruments_for_exit(self, candle, instruments_bucket):
        """
        This method is called once every candle time.
        If you set the candle at 5 minutes, then this method will be called every 5 minutes (09:15, 09:20, 09:25 and so on).
        In a candle, the exit method is called first, then the entry method is called.
        So once a candle starts, this method strategy_select_instruments_for_exit gets called first
        and then strategy_select_instruments_for_entry gets called.
        """

        # Add instrument in this bucket if you want to place an (exit) order for it
        # We decide whether to place an instrument in this bucket or not based on the decision making process given below in the loop
        selected_instruments_bucket = []

        # Add accompanying info in this bucket for that particular instrument in the bucket above
        sideband_info_bucket = []

        for instrument in instruments_bucket:
            main_order = self.main_order.get(instrument)

            # Compute various things and get the decision to place an (exit) order only if there is a current order is going on (main order is not empty / none)
            # Also check if order status is complete
            if main_order is not None and main_order.get_order_status() is BrokerOrderStatusConstants.COMPLETE:

                # Check for action (decision making process)
                action = self.get_decision(instrument, DecisionConstants.EXIT_POSITION)

                # For this strategy, we take the decision as:
                # If order transaction type is buy and current action is sell or order transaction type is sell and current action is buy, then exit the order
                if (action is ActionConstants.EXIT_SELL and main_order.order_transaction_type is BrokerOrderTransactionTypeConstants.SELL) or \
                        (action is ActionConstants.EXIT_BUY and main_order.order_transaction_type is BrokerOrderTransactionTypeConstants.BUY):
                    # Add instrument to the bucket
                    selected_instruments_bucket.append(instrument)

                    # Add additional info for the instrument
                    sideband_info_bucket.append({'action': action})

        # Return the buckets to the core engine
        # Engine will now call strategy_exit_position with each instrument and its additional info one by one
        return selected_instruments_bucket, sideband_info_bucket

    def strategy_exit_position(self, candle, instrument, sideband_info):
        """
        This method is called once for each instrument from the bucket in this candle.
        Exit an order here and return the instrument status to the core.
        """

        if sideband_info['action'] in [ActionConstants.EXIT_BUY, ActionConstants.EXIT_SELL]:

            main_order_position_closed = False
            main_order, profit_order = self.main_order.get(instrument), self.profit_order.get(instrument)
            if profit_order is not None:

                # If complete, main order position is closed
                if profit_order.get_order_status() is BrokerOrderStatusConstants.COMPLETE:
                    main_order_position_closed = True

                # If not complete, main order position is not closed, and cancel profit order
                else:
                    profit_order.cancel_order()

            if main_order is not None:

                # Main order is complete
                if main_order.get_order_status() is BrokerOrderStatusConstants.COMPLETE:

                    # If not squared off with target/stoploss, exit position now
                    if not main_order_position_closed:
                        main_order.exit_position()

                # Main order is not complete, cancel it
                else:
                    main_order.cancel_order()

            # Set the variables to none so that entry decision can be taken properly
            self.main_order[instrument] = None
            self.profit_order[instrument] = None

            # Return true so that the core engine knows that this instrument has exited completely
            return True

        # Return false in all other cases
        return False
