"""Smoke tests of the note scripts in lab/notes.

Each entry runs one quick script (under 30 s, standard library only) with python3 -I and checks that its output has the expected lines. The expected lines are those of the README.md of the folder and of the note.
"""

import os
import subprocess
import sys
import unittest

NOTES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (folder, arguments, expected substrings of stdout, forbidden substrings)
CASES = [
    ("50", ["ex.py"], ["children [('y', 0, 0)"], []),
    ("50", ["ex2.py"], ["7 two-step continuations ['yy', 'zz']"], []),
    ("50", ["follow.py"], ["max further depth 0"], []),
    ("50", ["walk.py", "3", "1", "line", "300", "16", "7"], ["'deep_nz': 185, 'tail_rank2': 0, 'h1fail': 0, 'lfail': 0"], []),
    ("50", ["lincheck.py", "3", "1", "300", "18", "5"], ["'deep_lin': 159, 'inG_xd': 159", "'surf_ge_rho': 159"], []),
    ("50", ["tcheck.py", "5", "1", "40", "24", "1"], ["ok 40 bad 0"], []),
    ("50", ["tcheck.py", "3", "2", "40", "24", "1"], ["ok 40 bad 0"], []),
    ("51", ["loop51b.py"], ["RECUR step 10 = step 3", "RECUR step 16 = step 5", "RECUR step 22 = step 7"], []),
    ("51", ["loop51.py"], ["p=3 MONO=True iota=((1, Fraction(0, 1)), 1) centre S=(1,) drop", "p=3 DIV=True iota=(1, Fraction(1, 1)) regime=1 centre S=(0,) drop"], []),
    ("51", ["ex51.py", "40"], ["== ex45 p=3 ()"], []),
    ("51", ["run51.py", "rule", "pow", "3", "20", "30", "3"], ["rule pow 3 [] {", "'nu_nonzero': 0", "'omega_fixed_up': 0"], []),
    ("52", ["sanity.py"], ["7 ex3.17.22 rho 3 d 4 surf_y 1 curve 4 fixed True True"], []),
    ("52", ["lem21.py"], ["cases 1468 min exponent < 5 after 150 steps 0 latest first level with both exponents >= 0 15"], []),
    ("52", ["linwalk.py", "3", "1", "400", "18", "1"], ["'fail': 0"], []),
    ("52", ["tie.py"], ["7 2 {'deep': 54, 'fail': 15"], []),
    ("52", ["tie2.py"], ["7 1 fail lastnz: [14, 16, 17]  pass lastnz: [-1]"], []),
    ("53", ["t_examples.py"], ["same data: True", "state at step 7 recurs at step 22", "R3 p=7: regime=R3"], []),
    ("53", ["t_ex45.py"], ["p=7 origin R1 iota=(1, Fraction(29, 14))", "chart x0 lam={1: 0} nu=0: R3 iota=(1, Fraction(13, 14))"], []),
    ("53", ["t_random.py", "3", "200", "pow", "120"], ["'pts': 870", "'nu_bad': 0", "'hyp_up': 0", "'readapt_up': 0", "'class_up': 0"], []),
    ("54", ["hahn54.py", "5", "3", "300", "1"], ["trials 300 failures 0"], []),
    ("54", ["dom54.py", "5", "3", "80", "1"], ["dominance results {'ok': 159} Theorem 5 step {'divisible': 80}"], []),
    ("55", ["summ.py"] + [f"run_{s}.jsonl" for s in ["p2", "p3", "p5n2", "p5n3_w1", "p5n3_w2", "p5n3_w3", "p5n3_old", "p5n3"]], ["| (2,3,(1,1,1),2) | 12 | 12 | 12 | 0 | 0 | 0 |", "| (3,3,(1,1,1),3) | 12 | 8 | 10 | 0 | 2 | 2 |", "| (5,3,(1,1,1),5) | 7 | 7 | 0 | 0 | 7 | 7 |"], []),
    ("56", ["fam3.py"], ["41 r = 14 deg f = 28 [(1, 5, 2, 'pass'), (2, 4, 41, 'FAIL"], []),
    ("56", ["run.py", "fam"], ["43 deg f = 42 ord f = 2 [(1, 5, 2, 'pass'), (2, 4, 43, 'FAIL"], []),
    ("56", ["run.py", "fam2"], ["43 deg f = 42 [(1, 5, 2, 'pass'), (2, 4, 43, 'FAIL"], []),
    ("56", ["run.py", "rand", "13", "2", "30", "4"], ["9 ((2, 'pass'), (2, 'pass'), ('>T', 'stop'))", "8 ((2, 'pass'), (2, 'pass'), (2, 'pass'))"], ["FAIL"]),
    ("57", ["ca_family.py"], ["p=2: 12 polynomials, leading term of h equals that of h0 in all cases", "p=3: 12 polynomials, leading term of h equals that of h0 in all cases"], []),
    ("57", ["dist_tests.py"], ["sup = 0-, the idempotent cut: independent defect", "('1/2', '1/2'), value 1.2071", "('1/3', '2/3'), value 1.2761", "distance <= -7/15"], []),
    ("59", ["checks.py"], ["nu(theta - (-x1 x3)) = 4.000 (expected 2p-2 = 4)", "nu(theta - (-x1 x3)) = 8.000 (expected 2p-2 = 8)", "transcendence test p=3: 35 products X^j s^k (j<=6, k<=4) have rank 35 mod X^200"], []),
    ("61", ["ex61_jumps.py"], ["prepared True omega 1/12", "prepared True omega 1/3"], []),
    ("61", ["ex_jump.py"], ["omega* = 5/3"], []),
    ("61", ["min_jump.py"], ["intrinsic 1/3", "vertex at xi' solvable"], []),
    ("61", ["loop54b.py", "3", "3"], ["CYCLE of length 7 after 0 steps"], []),
    ("61", ["loop54b.py", "5", "5", "plain", "12"], ["CYCLE of length 11 after 0 steps"], []),
    ("61", ["loop54b.py", "3", "3", "om"], ["depth 9 frontier 0"], []),
    ("61", ["walk61.py", "3", "300", "30", "gen", "11", "om"], ['"steps_main": 274', '"steps_div": 113', '"drops": 299'], []),
    ("61", ["t_single.py", "3", "300", "gen", "1"], ["'T1_bad': 0", "'T2_bad': 0", "'T3_bad': 0", "'T4_delta_bad': 0"], []),
    ("61", ["t_W.py", "3", "30", "10", "ex54", "5"], ["'R3': 46", "'lemma_fail': 0", "'persist': 30", "'persist_fail': 0"], []),
    ("62", ["fam3_rerun.py"], ["5 z^2-x^p [(1, 5, 2, 'pass'), (2, 4, 5, 'FAIL", "23 11 deg 22 [(1, 5, 2, 'pass'), (2, 4, 23, 'FAIL"], []),
    ("62", ["hermitian.py", "3", "1", "6"], ["q=3 field F_3^6 rational orders along R_P: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]"], []),
    ("62", ["hermitian.py", "5", "1", "4"], ["q=5 field F_5^4 rational orders along R_P: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]", "general orders along R_P: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]"], []),
    ("63", ["selftest63.py"], ["mismatches 0 of 54", "mismatches 0 of 1200"], []),
    ("63", ["hahn63.py", "5", "3", "200", "14", "planar", "1"], ["'exact': 170, 'failA': 0, 'failB': 0, 'failC': 0, 'dom_checked': 504, 'dom_fail': 0"], []),
    ("63", ["control63.py", "2", "1", "pcls", "2", "10", "15", "2", "100000"], ["criterion-2 hits without rho condition 8"], []),
    ("63", ["runs63.py", "3", "1", "bin", "2", "3", "9", "15", "107", "20000", "30"], ["'rank2_1': 0", "'rank2_2': 0"], []),
]


class NoteScriptTest(unittest.TestCase):
    def test_scripts(self):
        for folder, args, want, avoid in CASES:
            with self.subTest(note=folder, args=" ".join(args)):
                d = os.path.join(NOTES, folder)
                script = os.path.join(d, args[0])
                rest = [os.path.join(d, a) if a.endswith(".jsonl") else a for a in args[1:]]
                run = subprocess.run([sys.executable, "-I", script] + rest, cwd=os.sep, capture_output=True, text=True, timeout=120)
                self.assertEqual(run.returncode, 0, run.stderr[-2000:])
                for s in want:
                    self.assertIn(s, run.stdout)
                for s in avoid:
                    self.assertNotIn(s, run.stdout)


if __name__ == "__main__":
    unittest.main()
