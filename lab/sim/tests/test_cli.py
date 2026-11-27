"""The command line and the stored certificates."""

import contextlib
import io
import pathlib
import unittest

from labsim.__main__ import main

HERE = pathlib.Path(__file__).resolve().parent.parent


def run(args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = main(args)
    return code, out.getvalue()


class CliTest(unittest.TestCase):
    def test_step(self):
        code, out = run(["step", "-p", "2", "-q", "4", "-vars", "x,y,w", "-f", "x^2*y^2*w^3*(w*(x+y)^4+x^13)", "-divisor", "x,y,w", "-chart", "x", "-t", "y=1"])
        self.assertEqual(code, 0)
        self.assertIn("d = 5", out)
        self.assertIn("d = 7", out)

    def test_certificates(self):
        for path in sorted((HERE / "certificates").glob("*.json")):
            code, out = run(["check", str(path)])
            self.assertEqual((code, out.strip()), (0, "ok"), path)

    def test_walk(self):
        code, out = run(["walk", "-p", "3", "-walks", "20"])
        self.assertEqual(code, 0)
        self.assertIn("rho_up=0", out)


if __name__ == "__main__":
    unittest.main()
