"""核对交换资料的字段和数值关系。"""
import json
from pathlib import Path
import unittest

import numpy as np


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "data" / "exchange.json"
        self.data = json.loads(source.read_text(encoding="utf-8"))

    def test_exchange_data(self):
        a=np.float32(1.)
        self.assertNotEqual(float(np.nextafter(a,np.float32(2)))-float(a),float(a)-float(np.nextafter(a,np.float32(0))))
        self.assertEqual(self.data['logical_k'],len(self.data['b'])-1)
        receipts = self.data['receipts']
        self.assertEqual([r['kind'] for r in receipts[:3]],['rounded32','rounded32','terms_binary64'])
        a=np.array(self.data['a'],dtype=np.float32).astype(np.float64)
        b=np.array(self.data['b'],dtype=np.float32).astype(np.float64)
        for r in receipts[2:]:
            lo,hi=r['k']
            np.testing.assert_array_equal(a[r['batch'],r['row'],lo:hi,None]*b[lo:hi],r['terms'])
