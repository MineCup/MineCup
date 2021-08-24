from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


def table():
    services = {"rating": None}
    credentials = ServiceAccountCredentials._from_parsed_json_keyfile({
        "type": "service_account",
        "project_id": "calm-mariner-304222",
        "private_key_id": "d646789cdd016b0c4c4176c07345dccf1f1a6866",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDSzhhcXqeTR2zT\nh1tjz4U9dN4DliwyUGwaz83DtSKFJQZz910fs+sEBjUnv9zTDSlHucA5nc2xs7qs\nd0mMtyAo4vOXuXdLMPon12iFQDQB/8va2Sd5+F3E8yuyycXGySIs5ugkvQ0BKzQR\nGOjG/bEcsgiGV8dQMg9SFLPFs+LEZ/kQWeTtAMrHgaygUzJZqL/ebhQ3QGmJ3N1z\n691f28gqva3QM3pDYhrq4NfYxBK9L28XKa1OlfqZyKSwUvyfj29C6UDPZcM9Toed\njy7ICujd9CCzEGR7NKBBlP4GaVl46Y4DZhlmavI3xBnLpUzu566vDx2qAs7GUUhi\nuSTe1IpdAgMBAAECggEABwYyhhtqUoxB+k9rkmkXC7vx7OUrXlbTL1aGyPNnbc/U\nxfbzXavRVC4/xa4NNeQdoMP1/YV+VeJDAV2tL/jnI62iR8c4jCMa5sp082G3Ce0D\n1iw/tj76IuamaVvzUOMhViUwjY7WGNifcMVndj/8T5Q4F//jRo8Qdx/0+Iy8rOYp\nhjuw1jlm3KapggrsH3u/kF6SZICYJUbqct7THtl14/5jz0PHnDHjZXciVbwQhHzh\ntUCb8eT8346OY7Pod58in+10ot5cQ/Qmt7LOVFOtX16EkVb3TZHyBGj5PAVpctAP\njlJvc6/fi+UXL9dlqVtQm7NlxTkKAv0IZApDtCwGGQKBgQDxyMfnMWIroX+Y8FpN\nnQpo7Z+s4ER0/kScKaT9Kdwyoiu1lyqIgxR0d2EjyJlVn3KfgKHzYGwFb3c1gjuz\nxiz4BnMuvp3p3rrwmoYh//2ymuqN4atvgDh1JAzGCnmz9YCvcHefxo77gOX+3Mys\nyjlGwEBj7K6HYNiK23lIxowMiQKBgQDfMwem7zOyv7j3NLarMCnO0seS2kDl750X\n9mV5StOQyoIbqqYxcGldQivC2XY7+1AsvY9LNOP4NUIN4OPFhPAjWeBcaOEJqRXt\n1oPBtazTbpJbxB05nTOblbGGcMv7ppPR9Mo4FCvjDATPiHc1HL3iaBSvhsf8e8T0\nJhPIO13iNQKBgQDp/hdArrFEanJzT8EFNgM6EyYiB5UY6G779u2euKFLO1kzz40x\nOjJUmKghGmUS0VH7/WA+ikVgaUSkO1qOHC+vBYb5aS6ohI7EhbdkNjuPW4++KfVg\n3mVFMNNP4hlwSRr2LtEGhwIfctqjcYp/euI9j5eBXTB3AgnvMIJLJSOqiQKBgHjt\n+RNlPql2XwzxLpeJvN0mLqNORSNPs9mr0kbpV793OQ8sYmce9LdmhrdHg1v0Sfgz\nrFOfEHUGxgcm9cGqyUEeDQWEfYjyZ8M5GqH1gPH9UqcNlpgEqFV/wXOJ4bszAZwb\n+QRxSWX2uRSIZ64LKIZmxe5kJC6UEJ4Hk2hFYhSRAoGALbF7KG6GQe0PdRN13FsP\nmX007O8o/sDV6srFaifA1ff2F4syVl6VU9NfeHSDuyq6sG0Th/3pLPunpIfHVw1A\n7n2YyEkiCdrWcikgwYjLXBf8JAuVRTIka5Mo/h/7mIhAlehL1hs41vVR/2v6MpKt\nEiTZBMmusFhHbDB7lvYOsIE=\n-----END PRIVATE KEY-----\n",
        "client_email": "sxa-666@calm-mariner-304222.iam.gserviceaccount.com",
        "client_id": "104872701392314037045",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sxa-666%40calm-mariner-304222.iam.gserviceaccount.com"
    },
        ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(Http())
    services["rating"] = discovery.build('sheets', 'v4', http=httpAuth)
    return services
