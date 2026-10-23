import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "analytics.py"
SPEC = importlib.util.spec_from_file_location("inventory_analytics", MODULE_PATH)
analytics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analytics)


class InventoryAnalyticsTests(unittest.TestCase):
    def write_csv(self, frame):
        temp = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
        temp.close()
        frame.to_csv(temp.name, index=False)
        self.addCleanup(Path(temp.name).unlink, missing_ok=True)
        return Path(temp.name)

    def sample_frame(self):
        rows = [
            {"sku": "A1", "product": "High value", "unit_cost": 10, "on_hand": 1,
             "lead_time_days": 10, "safety_stock": 2, **{f"m{i:02d}": 10 for i in range(1, 13)}},
            {"sku": "B1", "product": "Low value", "unit_cost": 1, "on_hand": 500,
             "lead_time_days": 5, "safety_stock": 1, **{f"m{i:02d}": 2 for i in range(1, 13)}},
        ]
        return pd.DataFrame(rows)

    def test_calculates_segments_and_reorder_review(self):
        result = analytics.analyse(self.write_csv(self.sample_frame())).set_index("sku")
        self.assertEqual(result.loc["A1", "annual_demand"], 120)
        self.assertEqual(result.loc["A1", "reorder_point"], 6)
        self.assertTrue(bool(result.loc["A1", "replenishment_review"]))
        self.assertEqual(result.loc["B1", "reorder_point"], 2)
        self.assertFalse(bool(result.loc["B1", "replenishment_review"]))
        self.assertIn(result.loc["A1", "abc_xyz_segment"], {"AX", "AY", "AZ"})

    def test_missing_columns_raise_clear_error(self):
        path = self.write_csv(pd.DataFrame([{"sku": "A1"}]))
        with self.assertRaisesRegex(ValueError, "Missing required columns"):
            analytics.analyse(path)

    def test_negative_monthly_demand_is_rejected(self):
        frame = self.sample_frame()
        frame.loc[0, "m01"] = -1
        with self.assertRaisesRegex(ValueError, "non-negative"):
            analytics.analyse(self.write_csv(frame))

    def test_zero_demand_has_zero_reorder_point(self):
        frame = self.sample_frame()
        for month in analytics.MONTHS:
            frame[month] = 0
        result = analytics.analyse(self.write_csv(frame))
        self.assertTrue((result["annual_demand"] == 0).all())
        self.assertTrue((result["reorder_point"] == result["safety_stock"]).all())


if __name__ == "__main__":
    unittest.main()
