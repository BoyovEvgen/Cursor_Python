import os
import sys
import unittest
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from signers import Signer


class Singer_test(unittest.TestCase):
    PAYLOAD = [{'username': 'name'}, {'first_name': 'first_name'}, {'last_name': 'last_name'},
               {'password': 'very_strong_password'}]

    OUTPUT_JWT_ENCODE = [
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ.SK2nfl8iYJfWhgVhvlyTHQOMwysTWlHD2HdYC-2IC0Y",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdF9uYW1lIjoiZmlyc3RfbmFtZSJ9.eq-9NOmDqupsNPPVuv41FZYfeOxc_E2akyr3OOcNPoM",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsYXN0X25hbWUiOiJsYXN0X25hbWUifQ.EL9LqeNpCxAJpmUfhk1arhDivpQjgUIgWcPE7B_8qgA",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InZlcnlfc3Ryb25nX3Bhc3N3b3JkIn0.R-WNqqj42Yq8RJxuR6bUmL9a7T6kZpSbLv7XjjkHIFE"
        ]

    OUTPUT_ITSDANGEROUS_ENCODE = ["eyJ1c2VybmFtZSI6Im5hbWUifQ.PihNnBKX75phXftAhNS_nO0JphA",
                                  ".eJyrVkrLLCouic9LzE1VskLm1AIAjPMKCw.1xyYgxTZqlvgS2RW9yWrtjDlUPQ",
                                  "eyJsYXN0X25hbWUiOiJsYXN0X25hbWUifQ.jvb2GfqMFyg7o9A0_ObsI-MgCwU",
                                  "eyJwYXNzd29yZCI6InZlcnlfc3Ryb25nX3Bhc3N3b3JkIn0.ufK4Deb9abK4aFj-iZiiKtuQ37M"
                                  ]

    def setUp(self) -> None:
        self.signer = Signer(secret='123', salt='123')
        self.jwt_encode = [self.signer.jwt_encode(data) for data in Singer_test.PAYLOAD]
        self.jwt_decode = [self.signer.jwt_decode(data) for data in Singer_test.OUTPUT_JWT_ENCODE]
        self.itsdangerous_encode = [self.signer.itsdangerous_encode(data) for data in Singer_test.PAYLOAD]
        self.itsdangerous_decode = [self.signer.itsdangerous_decode(data) for data in Singer_test.OUTPUT_ITSDANGEROUS_ENCODE]

    def test_singer_obj(self):
        self.assertIsInstance(self.signer, Signer)

    def test_jwt_encode(self):
        self.assertEqual(self.jwt_encode, Singer_test.OUTPUT_JWT_ENCODE)

    def test_jwt_decode(self):
        self.assertEqual(self.jwt_decode, Singer_test.PAYLOAD)

    def test_itsdangerous_encode(self):
        self.assertEqual(self.itsdangerous_encode, Singer_test.OUTPUT_ITSDANGEROUS_ENCODE)

    def test_itsdangerous_decode(self):
        self.assertEqual(self.itsdangerous_decode, Singer_test.PAYLOAD)

    def test_jwt_encode_arg(self):
        self.assertRaises(TypeError, self.signer.jwt_encode, 'string')
