import unittest

from deptools.register import packages_from_files, Package, is_linux_resource, get_category


class TestRegister(unittest.TestCase):
    def test_packages_from_file(self):
        packages = packages_from_files(
            ['path/to/installer/ats-sdk-rpm_v7.5.0.zip', '/path/to/installer/ATS-SDK-ReleaseNotes.html'])
        self.assertEqual(packages, [
            Package(os='Linux (.rpm)',
                    product_id='1018',
                    installer='ats-sdk-rpm_v7.5.0.zip',
                    readme='ATS-SDK-ReleaseNotes.html',
                    name='ATS-SDK',
                    arch='x86_64',
                    category='software')
        ])
        packages = packages_from_files(
            ['/path/to/installer/drivers-ats9352-dkms_7.3.1_arm64.deb', '/path/to/installer/ATS9352_Driver_V7.3.1_Readme.html'])
        self.assertEqual(packages, [
            Package(os='Linux (.deb)',
                    product_id='1036',
                    installer='drivers-ats9352-dkms_7.3.1_arm64.deb',
                    readme='ATS9352_Driver_V7.3.1_Readme.html',
                    name='ATS9352 arm64 driver for Linux',
                    arch='arm64',
                    category='driver')
        ])
        package = Package(os='Linux (.deb)',
                        product_id='-1',
                        installer='',
                        readme='',
                        name='libats',
                        arch='x86_64',
                        category='')
        self.assertEqual(is_linux_resource(package), 1)
        package = Package(os='Windows',
                        product_id='',
                        installer='',
                        readme='',
                        name='libats',
                        arch='',
                        category='')
        self.assertEqual(is_linux_resource(package), 0)
        self.assertEqual(get_category('ATS9352'), 'driver')
        self.assertEqual(get_category('libats'), 'software')
        self.assertEqual(get_category('Firmware Update Utility (CLI)'), 'utility')
        


if __name__ == "__main__":
    unittest.main()
