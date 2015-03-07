__author__ = 'lewuahte'

import unittest
import numpy as np
import hash.image

class TestImageHash(unittest.TestCase):

    def test_md5_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.md5_for_vec(vec, 'hex')
        self.assertEqual(ret, 'aa341a15f5ade44faafbe190f98c2587')

    def test_sha1_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.sha1_for_vec(vec, 'hex')
        self.assertEqual(ret, 'e2d1839ed1706f7d470d87f8c48a5584cafa5a12')

    def test_sha224_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.sha224_for_vec(vec, 'hex')
        self.assertEqual(ret, '9836ae031a73c8b11b0d5e2490382d0c94cf57de85971f4f282fa6fa')

    def test_sha256_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.sha256_for_vec(vec, 'hex')
        self.assertEqual(ret, 'e2e2033ae7e19d680599d4eb0a1359a2b48ec5baac75066c317fbf85159c54ef')

    def test_sha384_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.sha384_for_vec(vec, 'hex')
        self.assertEqual(ret, '2898e7a634c3d8a76ad9fd3bcc8eac8129f0bed6f9f1d40e26c822d0677420f65e59fc729e7c5959f181e1502e4aca49')

    def test_sha512_for_vec(self):
        vec = np.array([1, 2, 3])
        ret = hash.image.sha512_for_vec(vec, 'hex')
        self.assertEqual(ret, 'f1d3a02078c2bf707afd3d022e3406626bc7487ea35e1de428be70702f350a9b890865e4b981cb372d39e595579e066ec022ed0bc605fe83abd8e70938f7491c')



if __name__ == '__main__':
    unittest.main()
