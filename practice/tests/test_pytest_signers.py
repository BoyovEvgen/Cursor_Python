import os
import sys
import pytest
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from signers import Signer

PAYLOAD = [{'username': 'name'}, {'first_name': 'first_name'}, {'last_name': 'last_name'}, {'password': 'very_strong_password'}]

OUTPUT_JWT_ENCODE = ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im5hbWUifQ.SK2nfl8iYJfWhgVhvlyTHQOMwysTWlHD2HdYC-2IC0Y",
                     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdF9uYW1lIjoiZmlyc3RfbmFtZSJ9.eq-9NOmDqupsNPPVuv41FZYfeOxc_E2akyr3OOcNPoM",
                     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsYXN0X25hbWUiOiJsYXN0X25hbWUifQ.EL9LqeNpCxAJpmUfhk1arhDivpQjgUIgWcPE7B_8qgA",
                     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InZlcnlfc3Ryb25nX3Bhc3N3b3JkIn0.R-WNqqj42Yq8RJxuR6bUmL9a7T6kZpSbLv7XjjkHIFE"
                     ]

OUTPUT_ITSDANGEROUS_ENCODE = ["eyJ1c2VybmFtZSI6Im5hbWUifQ.PihNnBKX75phXftAhNS_nO0JphA",
                              ".eJyrVkrLLCouic9LzE1VskLm1AIAjPMKCw.1xyYgxTZqlvgS2RW9yWrtjDlUPQ",
                              "eyJsYXN0X25hbWUiOiJsYXN0X25hbWUifQ.jvb2GfqMFyg7o9A0_ObsI-MgCwU",
                              "eyJwYXNzd29yZCI6InZlcnlfc3Ryb25nX3Bhc3N3b3JkIn0.ufK4Deb9abK4aFj-iZiiKtuQ37M"
                              ]

signer = Signer(secret='123', salt='123')


@pytest.mark.parametrize('input_data, output_data', zip(PAYLOAD, OUTPUT_JWT_ENCODE))
def test_jwt_encode(input_data, output_data):
    assert signer.jwt_encode(input_data) == output_data


@pytest.mark.parametrize('input_data, output_data', zip(PAYLOAD, OUTPUT_ITSDANGEROUS_ENCODE))
def test_itsdangerous_encode(input_data, output_data):
    assert signer.itsdangerous_encode(input_data) == output_data


@pytest.mark.parametrize('input_data, output_data', zip(OUTPUT_JWT_ENCODE, PAYLOAD))
def test_jwt_decode(input_data, output_data):
    assert signer.jwt_decode(input_data) == output_data


@pytest.mark.parametrize('input_data, output_data', zip(OUTPUT_ITSDANGEROUS_ENCODE, PAYLOAD))
def test_itsdangerous_decode(input_data, output_data):
    assert signer.itsdangerous_decode(input_data) == output_data


def test_jwt_encode_no_valid_input():
    with pytest.raises(TypeError):
        signer.jwt_encode('name')

