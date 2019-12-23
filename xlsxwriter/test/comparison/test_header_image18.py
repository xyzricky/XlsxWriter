###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2019, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('header_image18.xlsx')
        self.ignore_elements = {'xl/worksheets/sheet1.xml': ['<pageMargins', '<pageSetup']}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with image(s)."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.insert_image('E9', self.image_dir + 'red.png')

        worksheet.set_header('&L&G&C&G&R&G',
                             {'image_left': self.image_dir + 'red.jpg',
                              'image_center': self.image_dir + 'blue.jpg',
                              'image_right': self.image_dir + 'red.jpg'})

        worksheet.set_footer('&L&G&C&G&R&G',
                             {'image_left': self.image_dir + 'blue.jpg',
                              'image_center': self.image_dir + 'red.jpg',
                              'image_right': self.image_dir + 'blue.jpg'})

        workbook.close()

        self.assertExcelEqual()