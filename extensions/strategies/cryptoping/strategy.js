var z = require('zero-fill')
  , n = require('numbro')
  , ema = require('../../../lib/ema')
  , Phenotypes = require('../../../lib/phenotype')
global.selll = 'True'

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
    if (s.action === 'sold') {
    return process.exit(0)
    }
  },

  onPeriod: function (s, cb) {
    console.log(s.signal)
    if (s.action === 'sold') {
    return process.exit(0)
    }
    if (global.selll === 'True') {
    s.signal = 'buy'
    global.selll = 'False'
    }

    cb()
  },

  onReport: function (s) {
    var cols = []
    cols.push(global.selll)
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

