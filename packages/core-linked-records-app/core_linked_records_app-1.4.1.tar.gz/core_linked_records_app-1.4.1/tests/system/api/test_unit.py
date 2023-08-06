""" Unit tests for core_linked_records_app.system.api
"""
from unittest import TestCase
from unittest.mock import patch, Mock

from core_linked_records_app.components.pid_xpath.models import PidXpath
from core_linked_records_app.system.api import (
    delete_pid_for_data,
    get_pid_xpath_by_template,
)
from core_linked_records_app.utils.providers import AbstractIdProvider
from core_main_app.components.data.models import Data
from tests import test_settings
from tests.mocks import MockResponse
from core_main_app.components.template.models import Template


class TestIsPidDefinedForDocument(TestCase):
    def test_wrong_document_id_raise_error(self):
        pass

    def test_undefined_pid_returns_false(self):
        pass

    def test_duplicate_pid_returns_false(self):
        pass

    def test_defined_pid_for_other_document_returns_false(self):
        pass

    def test_defined_pid_for_current_document_returns_true(self):
        pass


class TestIsPidDefined(TestCase):
    def test_get_data_by_pid_fails_with_unexpected_error_raises_error(self):
        pass

    def test_get_data_by_pid_fails_with_expected_error_returns_false(self):
        pass

    def test_get_data_by_pid_succeeds_return_true(self):
        pass


class TestGetDataByPid(TestCase):
    def test_query_returns_no_results_raises_error(self):
        pass

    def test_query_returns_several_results_raises_error(self):
        pass

    def test_query_returns_single_result_returns_result(self):
        pass


class TestGetPidForData(TestCase):
    def test_not_existing_pid_returns_none(self):
        pass

    def test_existing_pid_returns_pid(self):
        pass


class TestDeletePidForData(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_data = Mock(spec=Data)
        cls.mock_data.pk = "mock_pk"

        cls.mock_provider = Mock(spec=AbstractIdProvider)

    @patch("core_linked_records_app.utils.providers.ProviderManager.get")
    @patch("core_linked_records_app.system.api.get_pid_for_data")
    def test_empty_pid_is_not_deleted(
        self, mock_get_pid_for_data, mock_provider_manager_get
    ):
        mock_get_pid_for_data.return_value = None
        mock_provider_manager_get.return_value = self.mock_provider

        delete_pid_for_data(self.mock_data)
        self.mock_provider.delete.assert_not_called()

    @patch("core_linked_records_app.utils.providers.ProviderManager.get")
    @patch("core_linked_records_app.system.api.get_pid_for_data")
    def test_provider_delete_called(
        self, mock_get_pid_for_data, mock_provider_manager_get
    ):
        mock_pid = "mock_pid"
        mock_get_pid_for_data.return_value = mock_pid
        mock_provider_manager_get.return_value = self.mock_provider

        delete_pid_for_data(self.mock_data)
        self.mock_provider.delete.assert_called_with(mock_pid)

    @patch("core_linked_records_app.utils.providers.ProviderManager.get")
    @patch("core_linked_records_app.system.api.get_pid_for_data")
    def test_pid_delete_failure_exits(
        self, mock_get_pid_for_data, mock_provider_manager_get
    ):
        mock_pid = "mock_pid"
        mock_get_pid_for_data.return_value = mock_pid
        mock_provider_manager_get.return_value = self.mock_provider

        self.mock_provider.delete.return_value = MockResponse(status_code=500)

        delete_pid_for_data(self.mock_data)

    @patch("core_linked_records_app.utils.providers.ProviderManager.get")
    @patch("core_linked_records_app.system.api.get_pid_for_data")
    def test_pid_delete_success_works(
        self, mock_get_pid_for_data, mock_provider_manager_get
    ):
        mock_pid = "mock_pid"
        mock_get_pid_for_data.return_value = mock_pid
        mock_provider_manager_get.return_value = self.mock_provider

        self.mock_provider.delete.return_value = MockResponse(status_code=200)

        delete_pid_for_data(self.mock_data)
