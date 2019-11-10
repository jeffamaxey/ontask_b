# -*- coding: utf-8 -*-

"""Module containing the forms for manipulating actions and conditions."""

from ontask.action.forms.crud import (
    FIELD_PREFIX, SUFFIX_LENGTH, ActionDescriptionForm, ActionForm,
    ActionImportForm, ActionUpdateForm, ConditionForm, FilterForm,
    RubricCellForm, RubricLOAForm,
)
from ontask.action.forms.edit import (
    EditActionOutForm, EnterActionIn, column_to_field,
)
from ontask.action.forms.run import (
    EmailActionForm, EmailActionFormRun,
    JSONActionForm, JSONActionFormRun,
    JSONListActionForm, JSONListActionFormRun,
    SendListActionForm, SendListActionFormRun,
    CanvasEmailActionForm, CanvasEmailActionFormRun,
    ZipActionForm, ValueExcludeForm, EnableURLForm)
