import unittest
from datetime import datetime
from pytz import timezone
from unittest import TestCase

from app.api.helpers.exceptions import UnprocessableEntity
from app.api.schema.tickets import TicketSchema


class TestTicketValidation(TestCase):

    def test_date_pass(self):
        """
        Tickets Validate Date - Tests if the function runs without an exception
        :return:
        """
        schema = TicketSchema()
        original_data = {
            'data': {}
        }
        data = {
            'sales_starts_at': datetime(2003, 8, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
            'sales_ends_at': datetime(2003, 9, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
            'event_ends_at': datetime(2003, 9, 10, 12, 30, 45).replace(tzinfo=timezone('UTC'))
        }
        TicketSchema.validate_date(schema, data, original_data)

    def test_date_start_gt_end(self):
        """
        Tickets Validate Date - Tests if exception is raised when sales_ends_at is before sales_starts_at
        :return:
        """
        schema = TicketSchema()
        original_data = {
            'data': {}
        }
        data = {
            'sales_starts_at': datetime(2003, 9, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
            'sales_ends_at': datetime(2003, 8, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
            'event_ends_at': datetime(2003, 8, 10, 12, 30, 45).replace(tzinfo=timezone('UTC'))
        }
        with self.assertRaises(UnprocessableEntity):
            TicketSchema.validate_date(schema, data, original_data)

    # def test_date_start_gt_event_end(self):
    #     """
    #     Tickets Validate Date-Tests if exception is raised when sales_starts_at is after event ends_at
    #     :return:
    #     """
    #     schema = TicketSchema()
    #     original_data = {
    #         'data': {}
    #     }
    #     data = {
    #         'sales_starts_at': datetime(2003, 8, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
    #         'sales_ends_at': datetime(2003, 9, 4, 12, 30, 45).replace(tzinfo=timezone('UTC')),
    #         'event_ends_at': datetime(2003, 8, 2, 12, 30, 45).replace(tzinfo=timezone('UTC'))
    #     }
    #     with self.assertRaises(UnprocessableEntity):
    #         TicketSchema.validate_date(schema, data, original_data)

    # def test_date_end_gt_event_end(self):
    #     """
    #     Tickets Validate Date-Tests if exception is raised when sales_ends_at is after event ends_at
    #     :return:
    #     """
    #     schema = TicketSchema()
    #     original_data = {
    #         'data': {}
    #     }
    #     data = {
    #         'sales_starts_at': datetime(2003, 8, 1, 12, 30, 45).replace(tzinfo=timezone('UTC')),
    #         'sales_ends_at': datetime(2003, 8, 10, 12, 30, 45).replace(tzinfo=timezone('UTC')),
    #         'event_ends_at': datetime(2003, 8, 2, 12, 30, 45).replace(tzinfo=timezone('UTC'))
    #     }
    #     with self.assertRaises(UnprocessableEntity):
    #         TicketSchema.validate_date(schema, data, original_data)

    def test_quantity_pass(self):
        """
        Tickets Validate Quantity - Tests if the function runs without an exception
        :return:
        """
        schema = TicketSchema()
        data = {
            'min_order': 10,
            'max_order': 20,
            'quantity': 30
        }
        TicketSchema.validate_quantity(schema, data)

    def test_quantity_min_gt_max(self):
        """
        Tickets Validate Quantity - Tests if exception is raised when min_order greater than max
        :return:
        """
        schema = TicketSchema()
        data = {
            'min_order': 20,
            'max_order': 10,
            'quantity': 30
        }
        with self.assertRaises(UnprocessableEntity):
            TicketSchema.validate_quantity(schema, data)

    def test_quantity_quantity_gt_min(self):
        """
        Tickets Validate Quantity - Tests if exception is raised when quantity less than max_order
        :return:
        """
        schema = TicketSchema()
        data = {
            'min_order': 10,
            'max_order': 20,
            'quantity': 5
        }
        with self.assertRaises(UnprocessableEntity):
            TicketSchema.validate_quantity(schema, data)


if __name__ == '__main__':
    unittest.main()
