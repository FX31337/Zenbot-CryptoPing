var z = require('zero-fill')
  , n = require('numbro')
  , ema = require('../../../lib/ema')
  , Phenotypes = require('../../../lib/phenotype')
var selll = 'False'

module.exports = {
  name: 'speed',
  description: 'Trade when % change from last two 1m periods is higher than average.',

  getOptions: function () {
    this.option('period', 'period length, same as --period_length', String, '30s')
    this.option('period_length', 'period length, same as --period', String, '30s')
    this.option('profit_stop_enable_pct', 'period length, same as --period_length', Number, 0.5)
    this.option('profit_stop_pct', 'period length, same as --period', Number, 0.5)
  },

  calculate: function (s) {
  },

  onPeriod: function (s, cb) {
    if (s.signal === 'sold') {
    process.exit()
    }
    if (selll === 'False') {
    s.signal = 'buy'
    selll = 'True'
    }
    if (selll === 'True') {
    s.signal = 'sell'
    }
    cb()
  },

  onReport: function (s) {
    var cols = []
    cols.push(global.sell)
	cols.push(' ')
    cols.push(s.signal)
    return cols
  },

  phenotypes: {
    // -- common
    period_length: Phenotypes.RangePeriod(1, 120, 'm'),
    min_periods: Phenotypes.Range(1, 100),
    markdown_buy_pct: Phenotypes.RangeFloat(-1, 5),
    markup_sell_pct: Phenotypes.RangeFloat(-1, 5),
    order_type: Phenotypes.ListOption(['maker', 'taker']),
    sell_stop_pct: Phenotypes.Range0(1, 50),
    buy_stop_pct: Phenotypes.Range0(1, 50),
    profit_stop_enable_pct: Phenotypes.Range0(1, 20),
    profit_stop_pct: Phenotypes.Range(1,20),
  }
}

