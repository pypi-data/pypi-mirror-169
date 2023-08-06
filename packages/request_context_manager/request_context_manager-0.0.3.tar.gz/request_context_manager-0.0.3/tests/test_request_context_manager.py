import uuid
import pytest

from request_context_manager import Errors, RequestContextAttr, RequestContextManager


class DummyException(Exception):
    pass


class TestRequestContext:

    @pytest.fixture(autouse=True)
    def _init(self) -> None:
        self.dummy_rc = RequestContextManager('dummy_rc', allow_nested=False)
        self.dummy_rc_attr = RequestContextAttr('attr', self.dummy_rc)

    def test_attr__set_then_get(self):
        value = f'value_{uuid.uuid4()}'
        with self.dummy_rc.under_request_context():
            self.dummy_rc_attr.set(value)
            assert self.dummy_rc_attr.get() == value

    def test_attr__set_then_get__nested_context(self):
        dummy_rc = RequestContextManager('dummy_rc', allow_nested=True)
        dummy_rc_attr = RequestContextAttr('dummy_rc_attr', dummy_rc)
        rc_1_value = f"value_1_{uuid.uuid4()}"
        rc_2_value = f"value_2_{uuid.uuid4()}"
        with dummy_rc.under_request_context():
            dummy_rc_attr.set(rc_1_value)
            with dummy_rc.under_request_context():
                dummy_rc_attr.set(rc_2_value)
                assert dummy_rc_attr.get() == rc_2_value
            assert dummy_rc_attr.get() == rc_1_value

    def test_attr__set__outside_context(self):
        value = f'value_{uuid.uuid4()}'
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.set(value)

    def test_attr__setdefault_then_get__attr_exists(self):
        existed_task_id = f"value_{uuid.uuid4()}"
        with self.dummy_rc.under_request_context():
            self.dummy_rc_attr.set(existed_task_id)
            assert self.dummy_rc_attr.get() == existed_task_id

            task_id_returned = self.dummy_rc_attr.setdefault("value_not_set")
            assert task_id_returned == existed_task_id
            assert self.dummy_rc_attr.get() == existed_task_id

    def test_attr__setdefault_then_get__attr_not_exists(self):
        value = f"value_{uuid.uuid4()}"
        with self.dummy_rc.under_request_context():
            assert self.dummy_rc_attr.get(default=None) != value

            value_returned = self.dummy_rc_attr.setdefault(value)
            assert value_returned == value
            assert self.dummy_rc_attr.get() == value

    def test_attr__setdefault_then_get__nested_context(self):
        dummy_rc = RequestContextManager('dummy_rc', allow_nested=True)
        dummy_rc_attr = RequestContextAttr('dummy_rc_attr', dummy_rc)
        rc_1_value = f"value_1_{uuid.uuid4()}"
        rc_2_value = f"value_2_{uuid.uuid4()}"
        with dummy_rc.under_request_context():
            dummy_rc_attr.set(rc_1_value)
            with dummy_rc.under_request_context():
                value_returned = dummy_rc_attr.setdefault(rc_2_value)
                assert value_returned == rc_2_value
                assert dummy_rc_attr.get() == rc_2_value
            assert dummy_rc_attr.get() == rc_1_value

    def test_attr__setdefault__outside_context(self):
        value = f'value_{uuid.uuid4()}'
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.setdefault(value)

    def test_attr__get__has_no_default_value(self):
        with self.dummy_rc.under_request_context():
            with pytest.raises(Errors.AttrNotFound):
                self.dummy_rc_attr.get()

    def test_attr__get__has_default_value(self):
        default_value = str(uuid.uuid4())
        with self.dummy_rc.under_request_context():
            assert self.dummy_rc_attr.get(default_value) == default_value

    def test_attr__get__not_allow_outside_context(self):
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.get()

    def test_attr__get__allow_outside_context(self):
        default_value = str(uuid.uuid4())
        assert self.dummy_rc_attr.get(default_value, allow_outside_context=True) == default_value

    def test_attr__delete_then_get__attr_exists(self):
        value = f"value_{uuid.uuid4()}"
        with self.dummy_rc.under_request_context():
            self.dummy_rc_attr.set(value)
            assert self.dummy_rc_attr.get() == value

            self.dummy_rc_attr.delete()
            with pytest.raises(Errors.AttrNotFound):
                self.dummy_rc_attr.get()

    def test_attr__delete_then_get__attr_not_exists(self):
        with self.dummy_rc.under_request_context():
            self.dummy_rc_attr.delete()
            with pytest.raises(Errors.AttrNotFound):
                self.dummy_rc_attr.get()

    def test_attr__delete__nested_context(self):
        dummy_rc = RequestContextManager('dummy_rc', allow_nested=True)
        dummy_rc_attr = RequestContextAttr('dummy_rc_attr', dummy_rc)
        rc_1_value = f"value_1_{uuid.uuid4()}"
        with dummy_rc.under_request_context():
            dummy_rc_attr.set(rc_1_value)
            with dummy_rc.under_request_context():
                with pytest.raises(Errors.AttrNotFound):
                    dummy_rc_attr.get()

    def test_attr__delete__outside_context(self):
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.delete()

    def test_under_request_context__not_allow_nested(self):
        with self.dummy_rc.under_request_context():
            with pytest.raises(Errors.AlreadyUnderContext):
                with self.dummy_rc.under_request_context():
                    pass

    def test_under_request_context__allow_nested(self):
        allow_nested_dummy_rc = RequestContextManager('nested_dummy_rc', allow_nested=True)
        with allow_nested_dummy_rc.under_request_context():
            with allow_nested_dummy_rc.under_request_context():
                pass

    def test_is_under_request_context(self):
        assert not self.dummy_rc.is_under_request_context()
        with self.dummy_rc.under_request_context():
            assert self.dummy_rc.is_under_request_context()
        assert not self.dummy_rc.is_under_request_context()

    def test_always_clear_context__normal_exit(self):
        value = f"value_{uuid.uuid4()}"
        with self.dummy_rc.under_request_context():
            self.dummy_rc_attr.set(value)
            assert self.dummy_rc_attr.get() == value

        assert not self.dummy_rc.is_under_request_context()
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.get()

    def test_always_clear_context__exception(self):
        value = f"value_{uuid.uuid4()}"
        try:
            with self.dummy_rc.under_request_context():
                self.dummy_rc_attr.set(value)
                raise DummyException
        except DummyException:
            pass
        assert not self.dummy_rc.is_under_request_context()
        with pytest.raises(Errors.OutsideContext):
            self.dummy_rc_attr.get()
